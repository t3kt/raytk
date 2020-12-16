from pathlib import Path
from typing import Callable
from raytkUtil import detachTox, CategoryInfo, ROPInfo, getToolkit, stripFirstMarkdownHeader
from raytkDocs import CategoryHelp, ROPHelp

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List, Optional, Union

class BuildContext:
	def __init__(self, log: Callable[[str], None]):
		self.log = log

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
			self.log(f'Locking {o}')
			o.lock = True

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
	def __init__(self, context: 'BuildContext', outputFolder: 'Union[str, Path]'):
		self.context = context
		self.outputFolder = Path(outputFolder)
		self.toolkit = getToolkit()

	def processOp(self, rop: 'COMP'):
		self.context.log(f'Processing docs for op {rop}')
		ropInfo = ROPInfo(rop)
		if not ropInfo or not ropInfo.isMaster:
			self.context.log(f'Invalid rop for docs {rop}')
			return
		ropHelp = ROPHelp.extractFromROP(rop)
		dat = ropInfo.helpDAT
		if not dat:
			dat = ropInfo.rop.create(textDAT, 'help')
			ropInfo.helpDAT = dat
		docText = ropHelp.formatAsMarkdown()
		dat.clear()
		dat.write(docText)
		docText = ropHelp.formatAsFullPage(ropInfo)
		self._writeDocs(
			Path(self.toolkit.relativePath(rop).replace('./', '') + '.md'),
			docText)

	@staticmethod
	def _generateDefaultOpDoc(ropInfo: 'ROPInfo'):
		parts = [
			f'# {ropInfo.shortName}',
			f'Category: {ropInfo.categoryName}',
			f'OP Type: `{ropInfo.opType}`',
			f'## Parameters',
			'\n'.join([
				f'* `{parTuplet[0].label}` - '
				for parTuplet in ropInfo.rop.customTuplets
				if not parTuplet[0].isPulse and not parTuplet[0].readOnly
			])
		]
		return '\n\n'.join(parts)

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

