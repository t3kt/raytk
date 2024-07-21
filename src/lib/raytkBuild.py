"""
Utilities used within the build process.

This should only be used in the build tool, and component BUILD scripts.
"""

import itertools
from typing import Callable
from raytkUtil import detachTox, CategoryInfo, ROPInfo, RaytkTags, RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List, Optional, Union
	from tools.updater.updater import Updater
	from devel.thirdParty.TDAsyncIO import TDAsyncIO
	op.TDAsyncIO = TDAsyncIO(COMP())

class BuildContext:
	"""
	Utility that is passed through parts of the build process to provide common tools.
	"""

	def __init__(
			self,
			log: Callable,
			experimental=False,
			includeModules=False,
	):
		self._log = log
		self.pane = None  # type: Optional[NetworkEditor]
		self.experimental = experimental
		self.includeModules = includeModules

	def log(self, msg, verbose=False):
		self._log(msg, verbose=verbose)

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

	def moveNetworkPane(self, comp: COMP):
		if self.pane:
			self.pane.owner = comp

	def focusInNetworkPane(self, o: OP):
		if o and self.pane:
			self.pane.owner = o.parent()
			self.pane.home(zoom=True, op=o)
			o.current = True

	@staticmethod
	def _toolkit() -> COMP:
		return RaytkContext().toolkit()

	def detachTox(self, comp: COMP):
		if not comp or comp.par['externaltox'] is None:
			return
		if not comp.par.externaltox and comp.par.externaltox.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching tox from {comp}')
		detachTox(comp)

	def reclone(self, comp: COMP, verbose=True):
		if not comp or not comp.par['enablecloningpulse'] or not comp.par['clone']:
			return
		self.log(f'Recloning {comp}', verbose)
		comp.par.enablecloningpulse.pulse()

	def updateOrReclone(self, comp: COMP):
		if not comp:
			return
		if comp.par['Updateop'] is not None:
			comp.par.Updateop.pulse()
		else:
			self.reclone(comp)

	def disableCloning(self, comp: COMP, verbose=True):
		if not comp or comp.par['enablecloning'] is None:
			return
		self.log(f'Disabling cloning on {comp}', verbose)
		comp.par.enablecloning.expr = ''
		comp.par.enablecloning = False

	def detachDat(self, dat: DAT, reloadFirst=False, verbose=True):
		if not dat or dat.par['file'] is None:
			return
		if not dat.par.file and dat.par.file.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching DAT {dat}', verbose)
		for par in dat.pars('syncfile', 'loadonstart', 'loadonstartpulse', 'write', 'writepulse'):
			par.expr = ''
			par.val = False
		if reloadFirst and dat.par['loadonstartpulse'] is not None:
			dat.par.loadonstartpulse.pulse()
		dat.par.file.expr = ''
		dat.par.file.val = ''

	def detachAllFileSyncDatsIn(self, scope: COMP, reloadFirst=False, verbose=True):
		if not scope:
			return
		self.log(f'Detaching all fileSync DATs in {scope}')
		for o in scope.findChildren(tags=[RaytkTags.fileSync.name], type=DAT):
			self.detachDat(o, reloadFirst=reloadFirst, verbose=verbose)

	def resetCustomPars(self, o: OP):
		if not o:
			return
		self.log(f'Resetting pars on {o}')
		for par in o.customPars:
			if par.readOnly or not par.enable:
				continue
			par.val = par.default

	def lockROPPars(self, comp: COMP):
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

	def reloadTox(self, comp: COMP):
		if not comp or not comp.par['enableexternaltoxpulse'] or not comp.par['enableexternaltox']:
			self.log(f'No tox to reload for {comp}')
			return
		self.log(f'Reloading {comp.par.externaltox} for {comp}')
		comp.par.enableexternaltoxpulse.pulse()

	def removeAlphaOps(self, category: COMP):
		catInfo = CategoryInfo(category)
		alphaOps = [
			o
			for o in catInfo.operators
			if ROPInfo(o).isAlpha
		]
		if alphaOps:
			self.log(f'Removing {len(alphaOps)} alpha operators from {category.name}')
			self.safeDestroyOps(alphaOps)

	def safeDestroyOp(self, o: OP, verbose=True):
		if not o or not o.valid:
			return
		self.log(f'Removing {o}', verbose)
		try:
			o.destroy()
		except Exception as e:
			self.log(f'Ignoring error removing {o}: {e}', verbose=False)

	def safeDestroyOps(self, os: 'List[OP]', verbose=True):
		for o in os:
			self.safeDestroyOp(o, verbose)

	def lockOps(self, os: 'List[OP]'):
		for o in os:
			if o.lock:
				continue
			self.log(f'Locking {o}')
			o.lock = True

	def lockBuildLockOps(self, comp: COMP):
		self.log(f'Locking build locked ops in {comp}')
		toLock = comp.findChildren(tags=[RaytkTags.buildLock.name])
		self.lockOps(toLock)

	def removeBuildExcludeOps(self, comp: COMP, verbose=True):
		toRemove = list(comp.findChildren(tags=[RaytkTags.buildExclude.name]))
		if not toRemove:
			return
		self.log(f'Removing build excluded ops from {comp}', verbose)
		self.safeDestroyOps(toRemove)

	def cleanOpImage(self, img: COMP):
		self.log(f'Cleaning opImage {img}')
		overlaySwitch = img.op('useOverlaySwitch')
		if overlaySwitch:
			overlaySwitch.outputs[0].inputConnectors[0].connect(overlaySwitch.inputs[int(overlaySwitch.par.index)])
		toRemove = img.ops('compImage/componentMeta') + [overlaySwitch]
		if overlaySwitch and overlaySwitch.par.index == 0:
			toRemove += img.ops('sel__*')
		self.safeDestroyOps(toRemove)

	def removeOpHelp(self, comp: COMP):
		ropInfo = ROPInfo(comp)
		self.safeDestroyOp(ropInfo.helpDAT)
		ropInfo.helpDAT = ''

	def removeCatHelp(self, comp: COMP):
		self.safeDestroyOp(CategoryInfo(comp).helpDAT)

	def applyParamUpdatersIn(self, comp: COMP):
		for child in comp.children:
			self._applyParamUpdater(child)

	def _applyParamUpdater(self, comp: COMP):
		if not comp or not comp.isCOMP:
			return
		if comp.name.startswith('parMenuUpdater') and comp.par['Autoupdate'] and comp.par['Update'] is not None:
			self.log(f'Applying parameter updater {comp}')
			comp.par.Update.pulse()
		elif comp.name.startswith('codeSwitcher') and comp.par['Autoupdateparams'] and comp.par['Updateparams'] is not None:
			self.log(f'Applying parameter updater {comp}')
			comp.par.Updateparams.pulse()
		elif comp.name.startswith('expressionSwitcher'):
			self._applyParamUpdater(comp.op('parMenuUpdater'))

	@staticmethod
	def queueAction(action: Callable, *args):
		run(f'args[0](*(args[1:]))', action, *args, delayFrames=5, delayRef=root)

	async def runBuildScript(self, dat: DAT):
		self.log(f'Running build script: {dat}')
		m = dat.module
		buildFunc = getattr(m, 'build', None)
		if buildFunc is None:
			self.log('No build function found in build script')
			raise Exception('No build function found in build script')
		await buildFunc(self)
		self.log(f'Finished build script: {dat}')

	async def yieldAsync(self):
		# do nothing!
		pass

	async def waitFrames(self, frames: int):
		from asyncio import Future
		future = Future()
		run('args[0].set_result(None)', future, delayFrames=frames, delayRef=root)
		await future

	def updateROPInstance(self, comp: COMP):
		self.log(f'Updating OP instance: {comp}')
		# noinspection PyTypeChecker
		updater = self._toolkit().op('tools/updater')  # type: Updater
		updater.UpdateOP(comp)
		self.log(f'Finished updating OP instance {comp}')

	def removeRedundantPythonModules(self, scopeRoot: COMP, scopeChildren: list[COMP]):
		if not scopeRoot:
			return
		loc = scopeRoot.op('local')
		if not loc:
			return
		self.detachTox(loc)
		mods = loc.op('modules')
		if not mods:
			return
		self.detachTox(mods)
		if not scopeChildren:
			return
		modNames = [m.name for m in mods.children if _isPythonLibrary(m)]
		opsToDelete = []
		for modName in modNames:
			for scopeChild in scopeChildren:
				if not scopeChild:
					continue
				for m in scopeChild.findChildren(type=textDAT, path='*/' + modName):
					if _isPythonLibrary(m, modName):
						opsToDelete.append(m)
		if not opsToDelete:
			return
		self.log(f'Deleting {len(opsToDelete)} redundant python libraries')
		self.safeDestroyOps(opsToDelete)

	def consolidateOperatorPythonModules(self, rop: COMP):
		info = ROPInfo(rop)
		if not info or not info.isROP:
			return
		inputHandlers = info.inputHandlers
		if not inputHandlers:
			return
		self.log(f'Consolidating python modules for {rop}, {len(inputHandlers)} input handlers')
		localComp = rop.op('local')
		if not localComp:
			localComp = rop.create(baseCOMP, 'local')
			localComp.nodeX = -900
			localComp.nodeY = 500
		modulesComp = localComp.op('modules')
		if not modulesComp:
			modulesComp = localComp.create(baseCOMP, 'modules')
		modulesComp.copy(info.opDef.op('typeTable'))
		modulesComp.copy(info.opDef.op('typeSpec'))
		self.safeDestroyOp(info.opDef.op('typeSpec'))
		self.safeDestroyOp(info.opDef.op('typeTable'))
		for handler in inputHandlers:
			self.safeDestroyOp(handler.op('typeSpec'))
			self.safeDestroyOp(handler.op('typeTable'))
		modulesComp.copy(inputHandlers[0].op('inputHandler'))
		for handler in inputHandlers:
			self.safeDestroyOp(handler.op('inputHandler'))

	def cleanOperatorTypeSpecs(self, rop: COMP):
		info = ROPInfo(rop)
		if not info or not info.isROP:
			return
		self.cleanTypeSpec(info.typeSpec)
		inputHandlers = info.inputHandlers
		if not inputHandlers:
			return
		self.log(f'Cleaning input handlers for {rop}, {len(inputHandlers)} input handlers')
		for handler in inputHandlers:
			self.cleanTypeSpec(handler)

	def cleanTypeSpec(self, comp: COMP):
		self.log(f'Cleaning type spec {comp}')
		self._removeUnusedPars(comp.pars('Coordtype*', 'Contexttype*', 'Returntype*'))

	def cleanOperatorDefPars(self, rop: COMP):
		info = ROPInfo(rop)
		if not info.isROP:
			return
		self.log(f'Cleaning operator def pars for {rop}')
		opDef = info.opDef
		self._removeUnusedPars(opDef.pars(
			'Tagtable', 'Callbacks',
			'Librarynames',
			'Disableinspect',
			'Shortcuts', 'Keywords', 'Displaycategory', 'Flags',
			# 'Help',
		))

	def _removeUnusedPars(self, pars: list[Par]):
		if not pars:
			return
		removePars = []
		for par in pars:
			if par.mode == ParMode.CONSTANT and not par:
				removePars.append(par)
		if not removePars:
			return
		self.log(f'Removing {len(removePars)} unnecessary pars from {pars[0].owner}')
		for par in removePars:
			par.destroy()

	# def stripComments(self, comp: COMP):
	# 	if not comp:
	# 		return
	# 	comp.comment = ''
	# 	for child in comp.children:
	# 		self.stripComments(child)

def _isPythonLibrary(m: OP, modName: 'str | None' = None):
	if not isinstance(m, textDAT) or not RaytkTags.fileSync.isOn(m):
		return False
	return modName is None or m.name == modName

def chunked_iterable(iterable, size):
	it = iter(iterable)
	while True:
		chunk = tuple(itertools.islice(it, size))
		if not chunk:
			break
		yield chunk
