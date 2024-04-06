import zipfile

import shutil

from datetime import datetime
from pathlib import Path
from raytkBuild import BuildContext, DocProcessor, chunked_iterable
from raytkTools import RaytkTools
from raytkUtil import RaytkContext, CategoryInfo, IconColors, RaytkTags, focusFirstCustomParameterPage, navigateTo
from typing import Optional, TextIO

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

	def runSnippetBuildOnly(self):
		self.prepareForBuild()
		builder = SnippetsBuilderAsync(self.context)

		async def _build():
			await builder.runBuild()
			self.log('Finished snippet build process')
			self.closeLogFile()

		op.TDAsyncIO.Cancel()
		op.TDAsyncIO.Run([_build()])

	def runToolkitAndSnippetBuilds(self):
		self.prepareForBuild()

		async def _build():
			toolkitBuilder = ToolkitBuilderAsync(self.context)
			await toolkitBuilder.runBuild()
			self.log('Finished toolkit build process')

			snippetBuilder = SnippetsBuilderAsync(self.context)
			await snippetBuilder.runBuild()
			self.log('Finished snippet build process')

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

class BuilderAsyncBase:
	def __init__(self, context: BuildContext):
		self.context = context

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

	async def logStageStart(self, desc: str):
		self.log(f'===[{desc}]===')
		await _asyncYield()

class ToolkitBuilderAsync(BuilderAsyncBase):
	def __init__(self, context: BuildContext):
		super().__init__(context)
		self.docProcessor = None
		if not self.context.experimental:
			self.docProcessor = DocProcessor(
				context,
				dataFolder='docs/_data',
				referenceFolder='docs/_reference',
				imagesFolder='docs/assets/images',
			)
		self.toolkit = None  # type: COMP | None

	async def runBuild(self):
		self.log('Starting build')
		await self.reloadToolkit()
		version = RaytkContext().toolkitVersion()
		self.log(f'Version: {version}' + (' (experimental)' if self.context.experimental else ''))
		self.context.openNetworkPane()

		await self._detachFileSyncOps()

		if self.docProcessor:
			await self.logStageStart('Clearing old docs')
			self.docProcessor.clearPreviousDocs()

		await self.logStageStart('Process thumbnails')
		await self.context.runBuildScript(self.toolkit.op('libraryThumbs/BUILD'))

		await self.logStageStart('Update library info')
		await self._updateLibraryInfo()

		await self.logStageStart('Update library image')
		await self._updateLibraryImage()

		await self.logStageStart('Pre-process components')
		await self._preProcessComponents()

		await self.logStageStart('Process operators')
		await self._processAllOperators()

		await self.logStageStart('Process nested operators')
		await self._processAllNestedOperators()

		await self.logStageStart('Generate operator docs')
		await self._generateAllOperatorDocs()

		await self.logStageStart('Generate category docs')
		await self._generateAllCategoryDocs()

		await self.logStageStart('Lock library info')
		await self._lockLibraryInfo()

		await self.logStageStart('Process tools')
		await self._processTools()

		await self.logStageStart('Lock build lock ops')
		await self._lockAllBuildLockOps()

		await self.logStageStart('Destroy components')
		await self._destroyComponents()

		await self.logStageStart('Clean operators')
		await self._cleanAllOperators()

		await self.logStageStart('Clear operator categories')
		await self._cleanAllCategories()

		await self.logStageStart('Consolidate shared python mods')
		await self._consolidateSharedPythonMods()

		await self.logStageStart('Remove build exclude ops')
		await self._removeAllBuildExcludeOps(self.toolkit)

		await self.logStageStart('Finalize toolkit pars')
		await self._finalizeToolkitPars()

		await self.logStageStart('Generate toolkit docs')
		await self._generateToolkitDocs()

		await self.logStageStart('Finish build')
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
		await self.context.runBuildScript(libraryInfo.op('BUILD'))

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
		await self.context.runBuildScript(tools.op('BUILD'))

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
			self.log(f'Processing chunk {i + 1} of {total}')
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

class SnippetsBuilderAsync(BuilderAsyncBase):
	def __init__(self, context: BuildContext):
		super().__init__(context)
		self.outputFolder = None  # type: Optional[Path]
		self.sourceFolder = Path('snippets')
		self.tempComp = None  # type: Optional[COMP]
		self.sourceToxFiles = []  # type: list[Path]
		self.opTypesByLocalName = {}  # type: dict[str, str]

	async def runBuild(self):
		self.log('Starting snippets build')

		await self.logStageStart('Initialization')
		await self._initializeOutput()
		await self._initializeTempComp()

		await self.logStageStart('Load op table')
		await self._loadOpTable()

		await self.logStageStart('Find source tox files')
		await self._findSourceToxFiles()

		await self.logStageStart('Process source tox files')
		await self._processSourceToxFiles()

		await self.logStageStart('Build zip file')
		await self._buildZipFile()

		await self.logStageStart('Clean output')
		await self._cleanOutput()

		self.log('Build completed!')

	async def _initializeOutput(self):
		tempFolder = Path('build/temp')
		tempFolder.mkdir(parents=True, exist_ok=True)
		folder = tempFolder / 'snippets'
		if folder.exists():
			self.log('Clearing output temp folder ' + folder.as_posix())
			shutil.rmtree(folder)
		self.log('Creating output temp folder ' + folder.as_posix())
		folder.mkdir(parents=True)
		self.outputFolder = folder

	async def _initializeTempComp(self):
		self.tempComp = op('/temp')
		if self.tempComp:
			self.log('Removing old temp comp')
			self.context.safeDestroyOp(self.tempComp)
		self.log('Creating temp comp')
		self.tempComp = root.create(baseCOMP, 'temp')

	async def _loadOpTable(self):
		opTable = RaytkContext().opTable()
		self.opTypesByLocalName = {}
		for i in range(1, opTable.numRows):
			self.opTypesByLocalName[opTable[i, 'name'].val] = opTable[i, 'opType'].val

	async def _findSourceToxFiles(self):
		allFiles = (self.sourceFolder / 'operators').rglob('*.tox')

		for file in allFiles:
			if file.name == 'index.tox':
				continue
			if not file.stem.endswith('_snippet'):
				continue
			opLocalName = file.stem.split('_', maxsplit=1)[0]
			if opLocalName not in self.opTypesByLocalName:
				self.log('Skipping operator-specific snippet' + file.as_posix())
				continue
			self.sourceToxFiles.append(file)

		self.log(f'Found {len(self.sourceToxFiles)} source tox files')

	async def _processSourceToxFiles(self):
		for i, tox in enumerate(self.sourceToxFiles):
			self.log(f'Processing source tox file [{i+1}/{len(self.sourceToxFiles)}]: {tox}')
			await self._processSourceToxFile(tox)

	async def _processSourceToxFile(self, tox: Path):
		snippet = self.tempComp.loadTox(tox.as_posix())
		self.log('Processing snippet comp ' + snippet.path)
		self.context.focusInNetworkPane(snippet)
		self.context.detachTox(snippet)

		await _asyncYield()
		rops = RaytkContext().ropChildrenOf(snippet)
		self.log(f'Updating {len(rops)} ROPs in snippet')
		await _asyncYield()
		for rop in rops:
			await self._processRop(rop)

		await _asyncYield()
		relPath = tox.relative_to(self.sourceFolder)
		outputPath = self.outputFolder / relPath
		outputPath.parent.mkdir(parents=True, exist_ok=True)
		self.log(f'Saving processed snippet to {outputPath}')
		snippet.save(outputPath.as_posix())

	async def _processRop(self, rop: COMP):
		self.log('Processing ROP ' + rop.path, verbose=True)
		self.context.reclone(rop, verbose=True)
		self.context.disableCloning(rop, verbose=True)
		self.context.updateROPInstance(rop)
		if not rop.isPanel and not rop.isObject:
			rop.showCustomOnly = True

	async def _buildZipFile(self):
		toxFiles = list(self.outputFolder.rglob('*.tox'))
		outputFileName = self._getOutputFilePath('RayTKSnippets', 'zip')
		self.log(f'Building zip file {outputFileName} with {len(toxFiles)} files')
		with zipfile.ZipFile(outputFileName, 'w') as archive:
			for file in toxFiles:
				archive.write(file, arcname=file.relative_to(self.outputFolder))
		await _asyncYield()
		self.log('Wrote zip file ' + outputFileName)

	async def _cleanOutput(self):
		shutil.rmtree(self.outputFolder)

async def _asyncYield():
	pass
