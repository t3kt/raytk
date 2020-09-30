from develCommon import *
from typing import List

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from tools.createMenu.createMenuExt import CreateMenu
	from tools.inspector.inspectorExt import Inspector

class BuildManager:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.logTable = ownerComp.op('log')

	@staticmethod
	def GetToolkitVersion():
		return getToolkitVersion()

	def RunBuild(self):
		self.logTable.clear()
		self.log('Starting build')
		self.queueMethodCall('runBuild_stage', 0)

	def runBuild_stage(self, stage: int):
		toolkit = getToolkit()
		if stage == 0:
			self.reloadToolkit(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 1:
			components = toolkit.op('components')
			self.processComponents(components, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 2:
			operators = toolkit.op('operators')
			self.processOperators(operators, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 3:
			self.freezeOperatorTable(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 4:
			self.processTools(toolkit.op('tools'))
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 5:
			self.finalizeToolkitPars(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 6:
			self.updateLibraryInfo(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 7:
			self.removeBuildExcludeOps(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 8:
			version = getToolkitVersion()
			toxFile = f'build/RayTK-{version}.tox'
			self.log('Exporting TOX to ' + toxFile)
			toolkit.op('buildLog').copy(self.logTable)
			toolkit.save(toxFile)
			self.log('Build completed!')
			ui.messageBox('Build completed!', f'Exported tox file: {toxFile}!')

	def reloadToolkit(self, toolkit: 'COMP'):
		self.log('Reloading toolkit')
		toolkit.par.externaltox = 'src/raytk.tox'
		toolkit.par.reinitnet.pulse()

	def finalizeToolkitPars(self, toolkit: 'COMP'):
		self.log('Finalizing toolkit parameters')
		toolkit.par.Devel = False
		toolkit.par.Devel.readOnly = True
		toolkit.par.externaltox = ''
		toolkit.par.enablecloning = False
		toolkit.par.savebackup = True
		toolkit.par.reloadtoxonstart = True
		toolkit.par.reloadcustom = True
		toolkit.par.reloadbuiltin = True

	def updateLibraryInfo(self, toolkit: 'COMP'):
		self.log('Updating library info')
		toolkit.op('libraryInfo').par.Forcebuild.pulse()
		self.lockBuildLockOps(toolkit)

	def processComponents(self, components: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing components {components}')
		self.detachTox(components)
		comps = getChildComps(components)
		self.queueMethodCall('processComponents_stage', comps, thenRun, runArgs)

	def processComponents_stage(self, components: List['COMP'], thenRun: str = None, runArgs: list = None):
		if components:
			comp = components.pop()
			self.detachTox(comp)
			self.detachDats(comp, recursive=True)
			if components:
				self.queueMethodCall('processComponents_stage', components, thenRun, runArgs)
				return
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperators(self, comp: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing operators {comp}')
		self.detachTox(comp)
		categories = comp.findChildren(type=baseCOMP, maxDepth=1)
		self.queueMethodCall('processOperatorCategories_stage', categories, thenRun, runArgs)

	def freezeOperatorTable(self, toolkit: 'COMP'):
		self.log('Freezing operator table')
		for table in toolkit.ops('opTable', 'opCategoryTable'):
			table.lock = True

	def processOperatorCategories_stage(self, categories: List['COMP'], thenRun: str = None, runArgs: list = None):
		if categories:
			category = categories.pop()
			self.processOperatorCategory(category, thenRun='processOperatorCategories_stage', runArgs=[categories, thenRun, runArgs])
		elif thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperatorCategory(self, category: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing operator category {category.name}')
		self.detachTox(category)
		template = category.op('__template')
		if template:
			template.destroy()
		comps = category.findChildren(type=baseCOMP, tags=['raytkOP'], maxDepth=1)
		self.queueMethodCall('processOperatorCategory_stage', comps, thenRun, runArgs)

	def processOperatorCategory_stage(self, components: List['COMP'], thenRun: str = None, runArgs: list = None):
		if components:
			comp = components.pop()
			self.processOperator(comp)
			if components:
				self.queueMethodCall('processOperatorCategory_stage', components, thenRun, runArgs)
				return
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperator(self, comp: 'COMP'):
		self.log(f'Processing operator {comp}')
		comp.par.enablecloning = False
		self.detachTox(comp)
		self.detachDats(comp, recursive=True)
		for child in comp.findChildren(type=COMP):
			if 'raytkOP' in child.tags:
				self.processOperator(child)
			else:
				self.processOperatorSubComp(child)
		updateROPMetadata(comp)

	def processOperatorSubComp(self, comp: 'COMP'):
		comp.par.enablecloning = False
		self.detachTox(comp)

	def detachTox(self, comp: 'COMP'):
		if not comp.par.externaltox and comp.par.externaltox.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching tox from {comp}')
		comp.par.reloadtoxonstart.expr = ''
		comp.par.reloadtoxonstart.val = False
		comp.par.externaltox.expr = ''
		comp.par.externaltox.val = ''

	def detachDats(self, comp: 'COMP', recursive=False):
		self.log(f'Detaching DATs in {comp}')
		for dat in comp.findChildren(type=textDAT, maxDepth=None if recursive else 1):
			self.detachDat(dat)
		for dat in comp.findChildren(type=tableDAT, maxDepth=None if recursive else 1):
			self.detachDat(dat)

	def detachDat(self, dat: 'DAT'):
		if not dat.par.file and dat.par.file.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching DAT {dat}')
		for par in dat.pars('syncfile', 'loadonstart', 'loadonstartpulse', 'write', 'writepulse'):
			par.expr = ''
			par.val = False
		dat.par.file.expr = ''
		dat.par.file.val = ''

	def processRopCategory(self, comp: 'COMP'):
		self.log(f'Processing ROP category {comp}')
		self.removeTestingOps(comp)

	def processTools(self, comp: 'COMP'):
		self.log(f'Processing tools {comp}')
		self.detachTox(comp)
		self.detachDats(comp, recursive=True)
		createMenu = comp.op('createMenu')  # type: Union[COMP, CreateMenu]
		createMenu.ClearFilter()
		par = createMenu.par['Devel']
		if par is not None:
			par.expr = ''
			par.val = False
		self.detachTox(createMenu)
		inspector = comp.op('inspector')  # type: Union[COMP, Inspector]
		inspector.Reset()
		self.detachTox(inspector)

	def removeTestingOps(self, comp: 'COMP'):
		self.log(f'Removing testing ops from {comp}')
		toRemove = list(comp.ops('__test_*'))
		for o in toRemove:
			o.destroy()

	def removeBuildExcludeOps(self, comp: 'COMP'):
		self.log(f'Removing build excluded ops from {comp}')
		toRemove = list(comp.findChildren(tags=['buildExclude'], maxDepth=1))
		for o in toRemove:
			o.destroy()

	def lockBuildLockOps(self, comp: 'COMP'):
		self.log(f'Locking build locked ops in {comp}')
		toLock = list(comp.findChildren(tags=['buildLock'], maxDepth=1))
		for o in toLock:
			o.lock = True

	def log(self, message: str):
		print(message)
		self.logTable.appendRow([message])

	def queueMethodCall(self, method: str, *args):
		if '.' in method:
			run(method, *args, delayFrames=5, delayRef=root)
		else:
			run(f'args[0].{method}(*(args[1:]))', self, *args, delayFrames=5, delayRef=root)

def getChildComps(comp: 'COMP'):
	return comp.findChildren(type=COMP, maxDepth=1) if comp else []
