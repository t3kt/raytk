import asyncio
from datetime import datetime
from pathlib import Path
from raytkBuild import BuildContext, BuildTaskContext, DocProcessor, chunked_iterable
from raytkTools import RaytkTools
from raytkUtil import RaytkContext, CategoryInfo, IconColors, RaytkTags, focusFirstCustomParameterPage, navigateTo
from typing import TextIO

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from devel.thirdParty.TDAsyncIO import TDAsyncIO
	op.TDAsyncIO = TDAsyncIO(COMP())

class BuildManagerAsync:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp
		self.logTable = ownerComp.op('log')
		self.context = None  # type: BuildContext | None
		self.docProcessor = None  # type: DocProcessor | None
		self.experimentalMode = False
		self.logFile = None  # type: TextIO | None
		self.enableVerboseLogging = False

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
		self.closeLogFile()

	def closeLogFile(self):
		if not self.logFile:
			return
		self.logFile.close()
		self.logFile = None

	def startNewLogFile(self):
		stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
		fileName = f'build/log/build-{stamp}.txt'
		filePath = Path(fileName)
		filePath.parent.mkdir(parents=True, exist_ok=True)
		self.logFile = filePath.open('a')

	def ReloadToolkit(self):
		self.logTable.clear()
		self.log('Reloading toolkit')
		builder = ToolkitBuilderAsync(self.context)
		op.TDAsyncIO.Run([builder.reloadToolkit()])

	def prepareForBuild(self):
		self.experimentalMode = bool(self.ownerComp.op('experimental_toggle').par.Value0)
		self.enableVerboseLogging = bool(self.ownerComp.op('verboseLogging_toggle').par.Value0)
		self.logTable.clear()
		self.closeLogFile()
		if self.ownerComp.op('useLogFile_toggle').par.Value0:
			self.startNewLogFile()
		self.context = BuildContext(self.log, self.experimentalMode)

	def runToolkitBuildOnly(self):
		self.prepareForBuild()
		builder = ToolkitBuilderAsync(self.context)

		async def _build():
			await builder.runBuild()
			self.log('Finished toolkit build process')
			self.closeLogFile()

		op.TDAsyncIO.Cancel()
		op.TDAsyncIO.Run([_build()])

	def log(self, message: str, verbose=False):
		if verbose and not self.enableVerboseLogging:
			return
		print(message, flush=True)
		if self.logFile:
			stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
			print(stamp, message, file=self.logFile, flush=True)
		self.logTable.appendRow([message])


class ToolkitBuilderAsync:
	def __init__(
			self,
			context: BuildContext,
	):
		self.context = context
		self.docProcessor = None
		if not self.context.experimental:
			self.docProcessor = DocProcessor(
				context,
				dataFolder='docs/_data',
				referenceFolder='docs/reference',
				imagesFolder='docs/assets/images',
			)
		self.toolkit = None  # type: COMP | None

	async def runBuild(self):
		self.log('Starting build')
		await self.reloadToolkit()
		version = RaytkContext().toolkitVersion()
		self.log(f'Version: {version}' + (' (experimental)' if self.context.experimental else ''))
		# NO SNIPPETS RELOAD
		self.context.openNetworkPane()

		await self._detachFileSyncOps()

		if self.docProcessor:
			self.logStageStart('Clearing old docs')
			await _asyncYield()
			self.docProcessor.clearPreviousDocs()

		self.logStageStart('Process thumbnails')
		await self._runBuildScript(self.toolkit.op('libraryThumbs/BUILD'))

		self.logStageStart('Update library info')
		await self._updateLibraryInfo()

		self.logStageStart('Update library image')
		await self._updateLibraryImage()

		self.logStageStart('Pre-process components')
		await self._preProcessComponents()

		self.logStageStart('Process operators')
		await self._processAllOperators()

		self.logStageStart('Process nested operators')
		await self._processAllNestedOperators()

		self.logStageStart('Generate operator docs')
		await self._generateAllOperatorDocs()

		self.logStageStart('Generate category docs')
		await self._generateAllCategoryDocs()

		self.logStageStart('Lock library info')
		await self._lockLibraryInfo()

		self.logStageStart('Process tools')
		await self._processTools()

		self.logStageStart('Lock build lock ops')
		await self._lockAllBuildLockOps()

		self.logStageStart('Destroy components')
		await self._destroyComponents()

		self.logStageStart('Clean operators')
		await self._cleanAllOperators()

		self.logStageStart('Clear operator categories')
		await self._cleanAllCategories()

		self.logStageStart('Consolidate shared python mods')
		await self._consolidateSharedPythonMods()

		self.logStageStart('Remove build exclude ops')
		await self._removeAllBuildExcludeOps(self.toolkit)

		self.logStageStart('Finalize toolkit pars')
		await self._finalizeToolkitPars()

		self.logStageStart('Generate toolkit docs')
		await self._generateToolkitDocs()

		self.logStageStart('Finish build')
		await self._finishBuild()

	async def reloadToolkit(self):
		self.toolkit = RaytkContext().toolkit()
		self.toolkit.par.externaltox = 'src/raytk.tox'
		self.toolkit.par.reinitnet.pulse()
		# Do this early since it switches off things like automatically writing to the opList.txt file.
		# See https://github.com/t3kt/raytk/issues/95
		self.toolkit.par.Devel = False

	async def _detachFileSyncOps(self):
		self.context.detachAllFileSyncDatsIn(self.toolkit, reloadFirst=True)

	async def _updateLibraryInfo(self):
		if self.toolkit.par['Experimentalbuild'] is not None:
			self.toolkit.par.Experimentalbuild.val = self.context.experimental
			self.toolkit.par.Experimentalbuild.readOnly = True
		libraryInfo = self.toolkit.op('libraryInfo')
		libraryInfo.par.Forcebuild.pulse()
		self.context.moveNetworkPane(libraryInfo)
		await self._runBuildScript(libraryInfo.op('BUILD'))

	async def _updateLibraryImage(self):
		image = RaytkContext().libraryImage()
		if image:
			self.context.detachTox(image)
			self.context.lockBuildLockOps(image)
			image.par.Showshortcut = True
			self.toolkit.par.opviewer.val = image
			self.toolkit.par.opviewer.readOnly = True
			self.toolkit.viewer = True
		else:
			self.toolkit.par.opviewer.val = ''
			self.toolkit.par.opviewer.readOnly = False
			self.toolkit.viewer = False

	async def _preProcessComponents(self):
		components = self.toolkit.op('components')
		shared = components.op('shared')
		self.context.lockBuildLockOps(shared)
		# this one has a buildLock typeTable that isn't instance-specific,
		# so we lock it first then delete the stuff that built it
		typeSpec = components.op('typeSpec')
		self.context.lockBuildLockOps(typeSpec)
		opDef = components.op('opDefinition')
		self.context.lockBuildLockOps(opDef)
		opDef.op('buildOpState').par.Pretty = False
		comps = components.ops(
			'typeSpec', 'typeResolver', 'typeRestrictor',
			# 'opImage',  # this has some instance-dependent stuff
			'opDefinition', 'compDefinition',
			# 'inputHandler',  # don't process inputHandler since it uses buildExclude for the config tables, which
			# won't have been locked yet when this stage runs
			'shaderBuilder',
			'opElement', 'transformCodeGenerator', 'timeProvider',
			'supportDetector', 'expresssionSwitcher', 'parMenuUpdater',
			# 'codeSwitcher',
			'aggregateCodeGenerator',
			# 'combiner',  # don't process combiner since it has instance-specific buildLock things depending
			# on buildExclude
			'waveFunction',
		)
		for comp in comps:
			self.context.removeBuildExcludeOps(comp)
			await _asyncYield()

	async def _processAllOperators(self):
		operatorsComp = self.toolkit.op('operators')
		self.context.moveNetworkPane(operatorsComp)
		self.context.detachTox(operatorsComp)
		categories = RaytkContext().allCategories()
		if self.docProcessor:
			self.docProcessor.writeCategoryListPage(categories)
		for category in categories:
			await self._processOperatorCategory(category)

	async def _processOperatorCategory(self, category: COMP):
		self.log('Processing category: ' + category.path)
		categoryInfo = CategoryInfo(category)
		self.context.moveNetworkPane(category)
		self.context.detachTox(category)
		template = category.op('__template')
		self.context.safeDestroyOp(template)
		if not self.context.experimental:
			self.context.removeAlphaOps(category)
		for comp in categoryInfo.operators:
			await self._processOperator(comp)

	async def _processOperator(self, comp: COMP):
		self.log('Processing operator: ' + comp.path)
		self.context.focusInNetworkPane(comp)
		self.context.disableCloning(comp)
		self.context.detachTox(comp)
		tools = RaytkTools()
		tools.updateROPMetadata(comp)
		tools.updateROPParams(comp)
		self.context.applyParamUpdatersIn(comp)
		self.context.resetCustomPars(comp)
		self.context.lockROPPars(comp)
		await self._processOperatorSubCompChildren(comp)
		if not comp.isPanel:
			comp.showCustomOnly = True
			self.log('Updating OP image for ' + comp.path)
			img = tools.updateOPImage(comp)
			if img:
				self.context.disableCloning(img)
				self.context.detachTox(img)
				self.context.lockBuildLockOps(img)
				self.context.cleanOpImage(img)
		comp.color = IconColors.defaultBgColor

	async def _processOperatorSubCompChildren(self, comp: COMP):
		subComps = comp.findChildren(type=COMP)
		if not subComps:
			return
		self.log(f'Processing {len(subComps)} sub-comps of {comp.path}', verbose=True)
		for child in subComps:
			self.log('Processing sub-comp: ' + child.path, verbose=True)
			self.context.detachTox(child)
			self.context.reclone(child)
			self.context.disableCloning(child)
			await self._processOperatorSubCompChildren(child)

	async def _processAllNestedOperators(self):
		operatorsComp = self.toolkit.op('operators')
		subOps = operatorsComp.findChildren(tags=[RaytkTags.raytkOP.name], depth=3)
		self.log(f'Found {len(subOps)} nested operators')
		for subOp in subOps:
			self.log('Processing sub-operator: ' + subOp.path)
			self.context.updateOrReclone(subOp)
			self.context.detachTox(subOp)
			self.context.disableCloning(subOp)

	async def _generateAllOperatorDocs(self):
		if not self.docProcessor:
			return
		self.log('Generate operator docs')
		for comp in RaytkContext().allMasterOperators():
			self.docProcessor.processOp(comp)

	async def _generateAllCategoryDocs(self):
		if not self.docProcessor:
			return
		self.log('Generate category docs')
		for comp in RaytkContext().allCategories():
			self.docProcessor.processOpCategory(comp)

	async def _lockLibraryInfo(self):
		self.context.lockOps(self.toolkit.ops(
			'info', 'opTable', 'opCategoryTable', 'opHelpTable', 'buildInfo'))

	async def _processTools(self):
		tools = self.toolkit.op('tools')
		self.context.moveNetworkPane(tools)
		self.context.reloadTox(tools)
		self.context.detachTox(tools)
		await self._runBuildScript(tools.op('BUILD'))

	async def _lockAllBuildLockOps(self):
		self.context.lockBuildLockOps(self.toolkit)

	async def _destroyComponents(self):
		comp = self.toolkit.op('components')
		self.context.focusInNetworkPane(comp)
		self.context.safeDestroyOp(comp)

	async def _cleanAllOperators(self):
		for comp in RaytkContext().allMasterOperators():
			self.log('Clean operator ' + comp.path)
			self.context.removeOpHelp(comp)
			self.context.cleanOperatorTypeSpecs(comp)
			self.context.cleanOperatorDefPars(comp)

	async def _cleanAllCategories(self):
		for comp in RaytkContext().allCategories():
			self.log('Clean category ' + comp.path)
			self.context.removeCatHelp(comp)

	async def _consolidateSharedPythonMods(self):
		self.context.removeRedundantPythonModules(self.toolkit, self.toolkit.ops('tools', 'libraryInfo'))

	async def _removeAllBuildExcludeOps(self, scope: COMP):
		self.log(f'Removing buildExclude ops in {scope}')
		toRemove = scope.findChildren(tags=[RaytkTags.buildExclude.name], includeUtility=True)
		chunks = [list(chunk) for chunk in chunked_iterable(toRemove, 30)]
		self.log(f'Found {len(toRemove)} ops to remove in {len(chunks)} chunks')
		total = len(chunks)
		for i in range(total):
			chunk = chunks[i]
			self.log(f'Processing chunk {total - i} of {total}')
			self.context.safeDestroyOps(chunk, verbose=True)
			await _asyncYield()

	async def _finalizeToolkitPars(self):
		comp = self.toolkit
		self.context.moveNetworkPane(comp)
		comp.par.Devel.readOnly = True
		comp.par.externaltox = ''
		comp.par.enablecloning = False
		comp.par.savebackup = True
		if comp.par['reloadtoxonstart'] is not None:
			comp.par.reloadtoxonstart = True
		else:
			comp.par.enableexternaltox = True
		comp.par.reloadcustom = True
		comp.par.reloadbuiltin = True
		focusFirstCustomParameterPage(comp)

	async def _generateToolkitDocs(self):
		if self.docProcessor:
			self.docProcessor.writeToolkitDocData()

	async def _finishBuild(self):
		comp = self.toolkit
		self.context.focusInNetworkPane(comp)
		toxFile = self._getOutputToxPath('RayTK')
		self.log(f'Saving toolkit to {toxFile}')
		comp.save(toxFile)
		self.log('Finished build')

	async def _runBuildScript(self, dat: DAT):
		self.log(f'Running build script: {dat}')
		result = asyncio.Future()

		def finishTask():
			self.log(f'Finished build script: {dat}')
			result.set_result(None)

		subContext = BuildTaskContext(finishTask, self.log, self.context.experimental)
		dat.run(subContext)

		await result

	def _getOutputToxPath(self, baseName: str):
		return self._getOutputFilePath(baseName, 'tox')

	def _getOutputFilePath(self, baseName: str, extension: str):
		version = RaytkContext().toolkitVersion()
		if self.context.experimental:
			suffix = '-exp'
		else:
			suffix = ''
		return f'build/{baseName}-{version}{suffix}.{extension}'

	def log(self, message: str, verbose=False):
		self.context.log(message, verbose)

	def logStageStart(self, desc: str):
		self.log(f'===[{desc}]===')

async def _asyncYield():
	pass
