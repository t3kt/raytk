"""
Utilities used within the build process.

This should only be used in the build tool, and component BUILD scripts.
"""

from pathlib import Path
import shutil
from typing import Callable
from raytkUtil import detachTox, CategoryInfo, ROPInfo, RaytkTags, RaytkContext
from raytkDocs import CategoryHelp, OpDocManager

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List, Optional, Union
	from tools.updater.updater import Updater

class BuildContext:
	"""
	Utility that is passed through parts of the build process to provide common tools.
	"""

	def __init__(self, log: Callable[[str], None]):
		self.log = log
		self.pane = None  # type: Optional[NetworkEditor]

	def _findExistingPane(self):
		for pane in ui.panes:
			if pane.name == 'raytkBuildNetwork':
				self.pane = pane
				return

	def openNetworkPane(self):
		self._findExistingPane()
		if not self.pane:
			self.pane = ui.panes.createFloating(type=PaneType.NETWORKEDITOR, name='raytkBuildNetwork')
		self.moveNetworkPane(self._toolkit())

	def closeNetworkPane(self):
		if self.pane:
			self.pane.close()
			self.pane = None

	def moveNetworkPane(self, comp: 'COMP'):
		if self.pane:
			self.pane.owner = comp

	def focusInNetworkPane(self, o: 'OP'):
		if o and self.pane:
			self.pane.owner = o.parent()
			self.pane.home(zoom=True, op=o)
			o.current = True

	@staticmethod
	def _toolkit() -> 'COMP':
		return RaytkContext().toolkit()

	def detachTox(self, comp: 'COMP'):
		if not comp or comp.par['externaltox'] is None:
			return
		if not comp.par.externaltox and comp.par.externaltox.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching tox from {comp}')
		detachTox(comp)

	def reclone(self, comp: 'COMP'):
		if not comp or not comp.par['enablecloningpulse'] or not comp.par['clone']:
			return
		self.log(f'Recloning {comp}')
		comp.par.enablecloningpulse.pulse()

	def updateOrReclone(self, comp: 'COMP'):
		if not comp:
			return
		if comp.par['Updateop'] is not None:
			comp.par.Updateop.pulse()
		else:
			self.reclone(comp)

	def disableCloning(self, comp: 'COMP'):
		if not comp or comp.par['enablecloning'] is None:
			return
		self.log(f'Disabling cloning on {comp}')
		comp.par.enablecloning.expr = ''
		comp.par.enablecloning = False

	def detachDat(self, dat: 'DAT', reloadFirst=False):
		if not dat or dat.par['file'] is None:
			return
		if not dat.par.file and dat.par.file.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching DAT {dat}')
		for par in dat.pars('syncfile', 'loadonstart', 'loadonstartpulse', 'write', 'writepulse'):
			par.expr = ''
			par.val = False
		if reloadFirst and dat.par['loadonstartpulse'] is not None:
			dat.par.loadonstartpulse.pulse()
		dat.par.file.expr = ''
		dat.par.file.val = ''

	def resetCustomPars(self, o: 'OP'):
		if not o:
			return
		self.log(f'Resetting pars on {o}')
		for par in o.customPars:
			if par.readOnly or not par.enable:
				continue
			par.val = par.default

	def lockROPPars(self, comp: 'COMP'):
		info = ROPInfo(comp)
		if not info:
			return
		names = tdu.expand(info.opDefPar.Lockpars.eval().strip())
		if not names:
			return
		pars = comp.pars(*[pn.strip() for pn in names])
		self.log(f'Locking pars on {comp}: {[p.name for p in pars]}')
		for p in pars:
			p.val = p.default
		processedTuplets = set()
		for p in pars:
			if p.tupletName in processedTuplets:
				continue
			p.enableExpr = ''
			p.enable = False
			processedTuplets.add(p.tupletName)

	def reloadTox(self, comp: 'COMP'):
		if not comp or not comp.par['reinitnet'] or not comp.par['externaltox']:
			return
		self.log(f'Reloading {comp.par.externaltox} for {comp}')
		comp.par.reinitnet.pulse()

	def safeDestroyOp(self, o: 'OP'):
		if not o or not o.valid:
			return
		self.log(f'Removing {o}')
		try:
			o.destroy()
		except Exception as e:
			self.log(f'Ignoring error removing {o}: {e}')

	def safeDestroyOps(self, os: 'List[OP]'):
		for o in os:
			self.safeDestroyOp(o)

	def lockOps(self, os: 'List[OP]'):
		for o in os:
			if o.lock:
				continue
			self.log(f'Locking {o}')
			o.lock = True

	def lockBuildLockOps(self, comp: 'COMP'):
		self.log(f'Locking build locked ops in {comp}')
		toLock = comp.findChildren(tags=[RaytkTags.buildLock.name])
		self.lockOps(toLock)

	def removeBuildExcludeOps(self, comp: 'COMP'):
		self.log(f'Removing build excluded ops from {comp}')
		toRemove = list(comp.findChildren(tags=[RaytkTags.buildExclude.name]))
		self.safeDestroyOps(toRemove)

	@staticmethod
	def queueAction(action: Callable, *args):
		run(f'args[0](*(args[1:]))', action, *args, delayFrames=5, delayRef=root)

	def runBuildScript(self, dat: 'DAT', thenRun: Callable, runArgs: list):
		self.log(f'Running build script: {dat}')

		def finishTask():
			self.log(f'Finished running build script: {dat}')
			self.queueAction(thenRun, *runArgs)
		subContext = BuildTaskContext(finishTask, self.log)
		dat.run(subContext)

	def updateROPInstance(self, comp: 'COMP'):
		self.log(f'Updating OP instance: {comp}')
		# noinspection PyTypeChecker
		updater = self._toolkit().op('tools/updater')  # type: Updater
		updater.UpdateOP(comp)
		self.log(f'Finished updating OP instance {comp}')

class BuildTaskContext(BuildContext):
	"""
	Context passed to build scripts, in order to provide common tools, and to support asynchronously triggering the rest
	of the build process to continue.

	`
	context = args[0]  # type: BuildTaskContext
	doStuff()
	context.detachTox(foo)
	# This part is required:
	context.finishTask()
	`
	"""
	def __init__(
			self,
			finish: Callable[[], None],
			log: Callable[[str], None]):
		self.finish = finish
		super().__init__(log)

	def finishTask(self):
		self.finish()

class DocProcessor:
	"""
	Tool used to extract and process documentation for ROPs.
	"""
	def __init__(self, context: 'BuildContext', outputFolder: 'Union[str, Path]'):
		self.context = context
		self.outputFolder = Path(outputFolder)
		self.toolkit = RaytkContext().toolkit()

	def clearPreviousDocs(self):
		if not self.outputFolder.exists():
			self.context.log(f'No previous docs to clear in {self.outputFolder}')
			return
		self.context.log(f'Clearing docs from {self.outputFolder}')
		paths = list(sorted(self.outputFolder.iterdir()))
		for path in paths:
			self.context.log(f'Clearing {path}')
			shutil.rmtree(path)

	def processOp(self, rop: 'COMP'):
		self.context.log(f'Processing docs for op {rop}')
		ropInfo = ROPInfo(rop)
		if not ropInfo or not ropInfo.isMaster:
			self.context.log(f'Invalid rop for docs {rop}')
			return
		docManager = OpDocManager(ropInfo)
		docManager.setUpMissingParts()
		docManager.pushToParamsAndInputs()
		docText = docManager.formatForBuild()
		self._writeDocs(
			Path(self.toolkit.relativePath(rop).replace('./', '') + '.md'),
			docText)

	def _writeDocs(self, relativePath: 'Path', docText: str):
		outFile = self.outputFolder / relativePath
		outFile.parent.mkdir(parents=True, exist_ok=True)
		self.context.log(f'Writing docs to {outFile}')
		with outFile.open('w') as f:
			f.write(docText)

	def processOpCategory(self, categoryOp: 'COMP'):
		self.context.log(f'Processing docs for category {categoryOp}')
		categoryInfo = CategoryInfo(categoryOp)
		catHelp = CategoryHelp.extractFromComp(categoryOp)
		dat = categoryInfo.helpDAT
		docText = catHelp.formatAsList()
		if not dat:
			dat = categoryOp.create(textDAT, 'help')
		dat.text = docText
		docText = catHelp.formatAsListPage()
		self._writeDocs(
			Path(self.toolkit.relativePath(categoryOp).replace('./', '') + '/index.md'),
			docText)

	def writeCategoryListPage(self, categories: 'List[COMP]'):
		self.context.log('Writing category list page')
		docText = '''---
layout: page
title: Operators
nav_order: 3
has_children: true
has_toc: false
permalink: /reference/operators/
---

# Operator Categories
'''
		categoryInfos = [
			CategoryInfo(o)
			for o in sorted(categories, key=lambda o: o.name)
		]
		docText += '\n'.join([
			f'* [{categoryInfo.categoryName.capitalize()}]({categoryInfo.categoryName}/) - {_extractSummary(categoryInfo.helpDAT)}'
			for categoryInfo in categoryInfos
		])
		self._writeDocs(Path('operators/index.md'), docText)

def _extractSummary(dat: 'Optional[DAT]'):
	if not dat or not dat.text:
		return ''
	for block in dat.text.split('\n\n'):
		if block and not block.startswith('#'):
			return block
	return ''

