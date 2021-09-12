from raytkTools import RaytkTools
from raytkUtil import RaytkTags, navigateTo, focusFirstCustomParameterPage, CategoryInfo, RaytkContext, IconColors, isROP
from raytkBuild import BuildContext, DocProcessor
from typing import Callable, List, Optional, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class BuildManager:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.logTable = ownerComp.op('log')
		self.context = None  # type: Optional[BuildContext]
		self.docProcessor = None  # type: Optional[DocProcessor]

	def OnInit(self):
		self.ClearLog()

	@staticmethod
	def GetToolkitVersion():
		return RaytkContext().toolkitVersion()

	@staticmethod
	def OpenToolkitNetwork():
		navigateTo(RaytkContext().toolkit(), name='raytkBuildNetwork', popup=True, goInto=True)

	def OpenLog(self):
		dat = self.ownerComp.op('full_log_text')
		dat.openViewer()

	def ClearLog(self):
		self.logTable.clear()

	def ReloadToolkit(self):
		self.logTable.clear()
		self.log('Reloading toolkit')
		toolkit = RaytkContext().toolkit()
		self.queueMethodCall(self.reloadToolkit, toolkit)

	def RunBuild(self):
		self.logTable.clear()
		self.log('Starting build')
		self.context = BuildContext(self.log)
		self.docProcessor = DocProcessor(
			self.context,
			outputFolder='docs/_reference',
			imagesFolder='docs/assets/images',
		)
		self.queueMethodCall(self.runBuild_stage, 0)

	def runBuild_stage(self, stage: int):
		toolkit = RaytkContext().toolkit()
		if stage == 0:
			self.log('Reloading toolkit')
			self.reloadToolkit(toolkit)
			self.context.openNetworkPane()
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 1:
			self.detachAllFileSyncDats(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 2:
			self.docProcessor.clearPreviousDocs()
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 3:
			self.updateLibraryInfo(toolkit, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 4:
			self.updateLibraryImage(toolkit, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 5:
			self.processOperators(toolkit.op('operators'), thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 6:
			self.processNestedOperators(toolkit.op('operators'), thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 7:
			self.processTools(toolkit.op('tools'), thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 8:
			self.context.lockBuildLockOps(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 9:
			self.processComponents(toolkit.op('components'), thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 10:
			self.context.removeBuildExcludeOps(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 11:
			self.finalizeToolkitPars(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 12:
			self.context.focusInNetworkPane(toolkit)
			version = RaytkContext().toolkitVersion()
			toxFile = f'build/RayTK-{version}.tox'
			self.log('Exporting TOX to ' + toxFile)
			toolkit.save(toxFile)
			self.log('Build completed!')
			self.log(f'Exported tox file: {toxFile}')

	@staticmethod
	def reloadToolkit(toolkit: 'COMP'):
		toolkit.par.externaltox = 'src/raytk.tox'
		toolkit.par.reinitnet.pulse()
		# Do this early since it switches off things like automatically writing to the opList.txt file.
		# See https://github.com/t3kt/raytk/issues/95
		toolkit.par.Devel = False

	def finalizeToolkitPars(self, toolkit: 'COMP'):
		self.log('Finalizing toolkit parameters')
		self.context.moveNetworkPane(toolkit)
		# toolkit.par.Devel = False
		toolkit.par.Devel.readOnly = True
		toolkit.par.externaltox = ''
		toolkit.par.enablecloning = False
		toolkit.par.savebackup = True
		toolkit.par.reloadtoxonstart = True
		toolkit.par.reloadcustom = True
		toolkit.par.reloadbuiltin = True
		focusFirstCustomParameterPage(toolkit)

	def updateLibraryImage(self, toolkit: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log('Updating library image')
		image = RaytkContext().libraryImage()
		if image:
			# self.context.moveNetworkPane(image)
			self.context.detachTox(image)
			self.context.lockBuildLockOps(image)
			image.par.Showshortcut = True
			toolkit.par.opviewer.val = image
			toolkit.par.opviewer.readOnly = True
			toolkit.viewer = True
		else:
			toolkit.par.opviewer.val = ''
			toolkit.viewer = False
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def updateLibraryInfo(self, toolkit: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log('Updating library info')
		libraryInfo = toolkit.op('libraryInfo')
		libraryInfo.par.Forcebuild.pulse()
		self.context.moveNetworkPane(libraryInfo)
		self.context.runBuildScript(
			libraryInfo.op('BUILD'),
			thenRun=lambda: self.queueMethodCall(thenRun, *(runArgs or [])),
			runArgs=[])

	def processComponents(self, components: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing components {components}')
		self.context.focusInNetworkPane(components)
		try:
			components.destroy()
		except:
			pass
		self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperators(self, comp: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing operators {comp}')
		self.context.moveNetworkPane(comp)
		self.context.detachTox(comp)
		categories = RaytkContext().allCategories()
		# categories.sort(key=lambda c: c.name)
		self.docProcessor.writeCategoryListPage(categories)
		self.queueMethodCall('processOperatorCategories_stage', categories, thenRun, runArgs)

	def processOperatorCategories_stage(self, categories: List['COMP'], thenRun: str = None, runArgs: list = None):
		if categories:
			category = categories.pop()
			self.processOperatorCategory(
				category, thenRun='processOperatorCategories_stage', runArgs=[categories, thenRun, runArgs])
		elif thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperatorCategory(self, category: 'COMP', thenRun: str = None, runArgs: list = None):
		categoryInfo = CategoryInfo(category)
		self.log(f'Processing operator category {category.name}')
		self.context.moveNetworkPane(category)
		self.context.detachTox(category)
		template = category.op('__template')
		if template:
			template.destroy()
		comps = categoryInfo.operators
		# comps.sort(key=lambda c: c.name)
		for o in comps:
			if RaytkTags.alpha.isOn(o):
				self.context.safeDestroyOp(o)
		comps = categoryInfo.operators
		if self.docProcessor:
			self.docProcessor.processOpCategory(category)
		self.queueMethodCall(self.processOperatorCategory_stage, comps, thenRun, runArgs)

	def processOperatorCategory_stage(self, components: List['COMP'], thenRun: str = None, runArgs: list = None):
		if components:
			comp = components.pop()
			self.processOperator(comp)
			if components:
				self.queueMethodCall(self.processOperatorCategory_stage, components, thenRun, runArgs)
				return
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperator(self, comp: 'COMP'):
		self.log(f'Processing operator {comp}')
		self.context.focusInNetworkPane(comp)
		self.context.disableCloning(comp)
		self.context.detachTox(comp)
		comp.showCustomOnly = True
		tools = RaytkTools()
		tools.updateROPMetadata(comp)
		tools.updateROPParams(comp)
		self.context.applyParamUpdatersIn(comp)
		self.context.resetCustomPars(comp)
		self.context.lockROPPars(comp)

		# This really shouldn't be necessary but there's something strange with old cloned components...
		self.context.safeDestroyOp(comp.op('opDefinition/paramHelpEditor'))

		# self.context.moveNetworkPane(comp)
		self.processOperatorSubCompChildrenOf(comp)
		# self.context.moveNetworkPane(comp)
		if not comp.isPanel:
			self.log(f'Updating OP image for {comp}')
			img = tools.updateOPImage(comp)
			if img:
				# self.context.focusInNetworkPane(img)
				self.context.disableCloning(img)
				self.context.detachTox(img)
				self.context.lockBuildLockOps(img)
		comp.color = IconColors.defaultBgColor
		if self.docProcessor:
			self.docProcessor.processOp(comp)

	def processOperatorSubCompChildrenOf(self, comp: 'COMP'):
		subComps = comp.findChildren(type=COMP)
		if not subComps:
			return
		self.context.log(f'Processing {len(subComps)} sub-comps in {comp}')
		for child in subComps:
			self.processOperatorSubComp_2(child)

	def processOperatorSubComp_2(self, comp: 'COMP'):
		self.context.log(f'Processing {comp}')
		self.context.detachTox(comp)
		self.context.reclone(comp)
		self.context.disableCloning(comp)
		self.processOperatorSubCompChildrenOf(comp)

	def processNestedOperators(self, comp: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log('Processing nested operators')
		subOps = comp.findChildren(tags=[RaytkTags.raytkOP.name], depth=4)
		self.log(f'found {len(subOps)} nested operators')
		self.queueMethodCall('processNestedOperators_stage', subOps, thenRun, runArgs)

	def processNestedOperators_stage(self, comps: List['COMP'], thenRun: str = None, runArgs: list = None):
		if comps:
			comp = comps.pop()
			self.processNestedOperator(comp)
			if comps:
				self.queueMethodCall(self.processNestedOperators_stage, comps, thenRun, runArgs)
				return
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processNestedOperator(self, rop: 'COMP'):
		self.log(f'Processing sub-operator {rop.path}')
		self.context.updateOrReclone(rop)
		self.context.detachTox(rop)
		self.context.disableCloning(rop)

	def detachAllFileSyncDats(self, toolkit: 'COMP'):
		self.log('Detaching all fileSync DATs')
		for o in toolkit.findChildren(tags=[RaytkTags.fileSync.name], type=DAT):
			self.context.detachDat(o, reloadFirst=True)

	def processTools(self, comp: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing tools {comp}')
		self.context.moveNetworkPane(comp)
		self.context.reloadTox(comp)
		self.context.detachTox(comp)
		self.context.runBuildScript(
			comp.op('BUILD'),
			thenRun=lambda: self.queueMethodCall(thenRun, *(runArgs or [])),
			runArgs=[])

	def log(self, message: str):
		print(message)
		self.logTable.appendRow([message])

	def queueMethodCall(self, method: Union[str, Callable], *args):
		if callable(method):
			run('args[0](*(args[1:]))', method, *args, delayFrames=5, delayRef=root)
		elif '.' in method:
			run(method, *args, delayFrames=5, delayRef=root)
		else:
			run(f'args[0].{method}(*(args[1:]))', self, *args, delayFrames=5, delayRef=root)
