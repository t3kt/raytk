from develCommon import *
from raytkUtil import RaytkTags
from raytkBuild import BuildContext
from typing import List, Optional

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
		self.context = None  # type: Optional[BuildContext]

	@staticmethod
	def GetToolkitVersion():
		return getToolkitVersion()

	def ReloadToolkit(self):
		self.logTable.clear()
		self.reloadToolkit(getToolkit())

	def RunBuild(self):
		self.logTable.clear()
		self.log('Starting build')
		self.context = BuildContext(self.log)
		self.queueMethodCall('runBuild_stage', 0)

	def runBuild_stage(self, stage: int):
		toolkit = getToolkit()
		if stage == 0:
			self.reloadToolkit(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 1:
			self.detachAllFileSyncDats(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 2:
			self.updateLibraryInfo(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 3:
			components = toolkit.op('components')
			self.processComponents(components, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 4:
			operators = toolkit.op('operators')
			self.processOperators(operators, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 5:
			self.processTools(toolkit.op('tools'), thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 6:
			self.lockBuildLockOps(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 7:
			self.removeBuildExcludeOps(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 8:
			self.finalizeToolkitPars(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 9:
			version = getToolkitVersion()
			toxFile = f'build/RayTK-{version}.tox'
			self.log('Exporting TOX to ' + toxFile)
			toolkit.op('buildLog').copy(self.logTable)
			toolkit.save(toxFile)
			self.log('Build completed!')
			self.log(f'Exported tox file: {toxFile}')

	def reloadToolkit(self, toolkit: 'COMP'):
		self.log('Reloading toolkit')
		toolkit.par.externaltox = 'src/raytk.tox'
		toolkit.par.reinitnet.pulse()

	def finalizeToolkitPars(self, toolkit: 'COMP'):
		self.log('Finalizing toolkit parameters')
		# toolkit.par.Devel = False
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

	def processComponents(self, components: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing components {components}')
		self.context.detachTox(components)
		comps = components.findChildren(type=COMP, maxDepth=1)
		self.queueMethodCall('processComponents_stage', comps, thenRun, runArgs)

	def processComponents_stage(self, components: List['COMP'], thenRun: str = None, runArgs: list = None):
		if components:
			comp = components.pop()
			self.context.detachTox(comp)
			if components:
				self.queueMethodCall('processComponents_stage', components, thenRun, runArgs)
				return
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperators(self, comp: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing operators {comp}')
		self.context.detachTox(comp)
		categories = comp.findChildren(type=baseCOMP, maxDepth=1)
		self.queueMethodCall('processOperatorCategories_stage', categories, thenRun, runArgs)

	def processOperatorCategories_stage(self, categories: List['COMP'], thenRun: str = None, runArgs: list = None):
		if categories:
			category = categories.pop()
			self.processOperatorCategory(category, thenRun='processOperatorCategories_stage', runArgs=[categories, thenRun, runArgs])
		elif thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperatorCategory(self, category: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing operator category {category.name}')
		self.context.detachTox(category)
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
		self.context.disableCloning(comp)
		self.context.detachTox(comp)
		for child in comp.findChildren(type=COMP):
			if 'raytkOP' in child.tags:
				self.processOperator(child)
			else:
				self.processOperatorSubComp(child)
		updateROPMetadata(comp)

	def processOperatorSubComp(self, comp: 'COMP'):
		self.context.disableCloning(comp)
		self.context.detachTox(comp)

	def detachAllFileSyncDats(self, toolkit: 'COMP'):
		self.log('Detaching all fileSync DATs')
		for o in toolkit.findChildren(tags=[RaytkTags.fileSync.name], type=DAT):
			self.context.detachDat(o)

	def processTools(self, comp: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing tools {comp}')
		self.context.reloadTox(comp)
		self.context.detachTox(comp)
		self.context.runBuildScript(
			comp.op('BUILD'),
			thenRun=lambda: self.queueMethodCall(thenRun, *(runArgs or [])),
			runArgs=[])

	def removeBuildExcludeOps(self, comp: 'COMP'):
		self.log(f'Removing build excluded ops from {comp}')
		toRemove = list(comp.findChildren(tags=['buildExclude']))
		for o in toRemove:
			self.log(f'Removing {o}')
			o.destroy()

	def lockBuildLockOps(self, comp: 'COMP'):
		self.log(f'Locking build locked ops in {comp}')
		toLock = comp.findChildren(tags=['buildLock'])
		for o in toLock:
			self.log(f'Locking {o}')
			o.lock = True

	def log(self, message: str):
		print(message)
		self.logTable.appendRow([message])

	def queueMethodCall(self, method: str, *args):
		if '.' in method:
			run(method, *args, delayFrames=5, delayRef=root)
		else:
			run(f'args[0].{method}(*(args[1:]))', self, *args, delayFrames=5, delayRef=root)
