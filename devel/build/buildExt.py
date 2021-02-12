from pathlib import Path
from raytkTools import RaytkTools
from raytkUtil import RaytkTags, navigateTo, focusCustomParameterPage, CategoryInfo, RaytkContext
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
		field = self.ownerComp.op('docSiteFolder_field')
		field.par.Value0 = self.GetDefaultDocSitePath() or ''
		self.ClearLog()

	@staticmethod
	def GetToolkitVersion():
		return RaytkContext().toolkitVersion()

	@staticmethod
	def GetDefaultDocSitePath():
		folder = Path('docs')
		if folder.exists():
			return folder.as_posix()
		return ''

	def getDocSitePath(self):
		field = self.ownerComp.op('docSiteFolder_field')
		if not field.par.Value0:
			return None
		folder = Path(field.par.Value0.eval())
		if not folder.exists():
			return None
		return folder

	@staticmethod
	def OpenToolkitNetwork():
		navigateTo(RaytkContext().toolkit(), name='toolkit', popup=True, goInto=True)

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
		docFolder = self.getDocSitePath()
		if docFolder:
			self.docProcessor = DocProcessor(self.context, docFolder / '_reference')
		else:
			self.docProcessor = None
		self.queueMethodCall(self.runBuild_stage, 0)

	def runBuild_stage(self, stage: int):
		toolkit = RaytkContext().toolkit()
		self.log('Reloading toolkit')
		if stage == 0:
			self.reloadToolkit(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 1:
			self.detachAllFileSyncDats(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 2:
			self.updateLibraryInfo(toolkit, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 3:
			self.processOperators(toolkit.op('operators'), thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 4:
			self.context.lockBuildLockOps(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 5:
			self.processTools(toolkit.op('tools'), thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 6:
			self.processComponents(toolkit.op('components'), thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 7:
			self.removeBuildExcludeOps(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 8:
			self.finalizeToolkitPars(toolkit)
			self.queueMethodCall(self.runBuild_stage, stage + 1)
		elif stage == 9:
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
		# toolkit.par.Devel = False
		toolkit.par.Devel.readOnly = True
		toolkit.par.externaltox = ''
		toolkit.par.enablecloning = False
		toolkit.par.savebackup = True
		toolkit.par.reloadtoxonstart = True
		toolkit.par.reloadcustom = True
		toolkit.par.reloadbuiltin = True
		image = toolkit.op('./libraryImage')
		if image:
			toolkit.par.opviewer.val = image
			toolkit.par.opviewer.readOnly = True
			toolkit.viewer = True
		else:
			toolkit.par.opviewer.val = ''
			toolkit.viewer = False
		focusCustomParameterPage(toolkit, 'RayTK')

	def updateLibraryInfo(self, toolkit: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log('Updating library info')
		toolkit.op('libraryInfo').par.Forcebuild.pulse()
		libraryInfo = toolkit.op('libraryInfo')
		self.context.runBuildScript(
			libraryInfo.op('BUILD'),
			thenRun=lambda: self.queueMethodCall(thenRun, *(runArgs or [])),
			runArgs=[])

	def processComponents(self, components: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing components {components}')
		self.context.runBuildScript(
			components.op('BUILD'),
			thenRun=lambda: self.queueMethodCall(thenRun, *(runArgs or [])),
			runArgs=[])

	def processOperators(self, comp: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing operators {comp}')
		self.context.detachTox(comp)
		categories = comp.findChildren(type=baseCOMP, maxDepth=1)
		if self.docProcessor:
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
		self.context.detachTox(category)
		template = category.op('__template')
		if template:
			template.destroy()
		comps = categoryInfo.operators
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
		self.context.disableCloning(comp)
		self.context.detachTox(comp)
		comp.showCustomOnly = True
		for child in comp.findChildren(type=COMP):
			self.processOperatorSubComp(child)
		tools = RaytkTools()
		tools.updateROPMetadata(comp)
		tools.updateROPParams(comp)
		self.log(f'Updating OP image for {comp}')
		img = tools.updateOPImage(comp)
		if img:
			self.context.disableCloning(img)
			self.context.detachTox(img)
			self.context.lockBuildLockOps(img)
		comp.color = 0.0477209, 0.111349, 0.114
		if self.docProcessor:
			self.docProcessor.processOp(comp)

	def processOperatorSubComp(self, comp: 'COMP'):
		self.context.disableCloning(comp)
		self.context.detachTox(comp)

	def detachAllFileSyncDats(self, toolkit: 'COMP'):
		self.log('Detaching all fileSync DATs')
		for o in toolkit.findChildren(tags=[RaytkTags.fileSync.name], type=DAT):
			self.context.detachDat(o, reloadFirst=True)

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
		toRemove = list(comp.findChildren(tags=[RaytkTags.buildExclude.name]))
		self.context.safeDestroyOps(toRemove)

	def lockBuildLockOps(self, comp: 'COMP'):
		self.log(f'Locking build locked ops in {comp}')
		toLock = comp.findChildren(tags=[RaytkTags.buildLock.name])
		self.context.lockOps(toLock)

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
