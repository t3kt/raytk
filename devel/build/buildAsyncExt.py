import zipfile

import shutil

from datetime import datetime
from pathlib import Path
from raytkBuild import BuildContext, chunked_iterable
from raytkDocs import CategoryHelp, ROPHelp, ToolkitInfo, OpDocManager
from raytkTools import RaytkTools
from raytkUtil import RaytkContext, RaytkModuleContext, CategoryInfo, IconColors, RaytkTags, \
	focusFirstCustomParameterPage, navigateTo, ROPInfo
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
		self.experimentalMode = False
		self.includeModules = False
		self.logFile = None  # type: TextIO | None
		self.enableVerboseLogging = False

	def OnInit(self):
		self.ClearLog()

	@staticmethod
	def GetToolkitVersion():
		return RaytkContext().toolkitVersion()

	@staticmethod
	def prepareModuleTable(dat: DAT, inDat: DAT):
		dat.clear()
		dat.appendRow(['name', 'moduleRoot', 'moduleDefinition', 'opTable'])
		for cell in inDat.col('path')[1:]:
			modDef = op(cell)
			if not modDef:
				continue
			dat.appendRow([
				modDef.par.Modulename.eval(),
				modDef.par.Moduleroot.eval(),
				modDef.path,
				modDef.par.Optable.eval() or '',
			])

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
		op.TDAsyncIO.Run([_reloadToolkit()])

	def prepareForBuild(self):
		self.experimentalMode = bool(self.ownerComp.op('experimental_toggle').par.Value0)
		self.enableVerboseLogging = bool(self.ownerComp.op('verboseLogging_toggle').par.Value0)
		self.includeModules = bool(self.ownerComp.op('modules_toggle').par.Value0)
		self.logTable.clear()
		self.closeLogFile()
		if self.ownerComp.op('useLogFile_toggle').par.Value0:
			self.startNewLogFile()
		self.context = BuildContext(self.log, self.experimentalMode, self.includeModules)

	def runToolkitBuildOnly(self):
		self.prepareForBuild()

		builder = ToolkitBuilderAsync(self.context, self.ownerComp.op('moduleTable'))

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
			toolkitBuilder = ToolkitBuilderAsync(self.context, self.ownerComp.op('moduleTable'))
			await toolkitBuilder.runBuild()
			self.log('Finished toolkit build process')

			snippetBuilder = SnippetsBuilderAsync(self.context)
			await snippetBuilder.runBuild()
			self.log('Finished snippet build process')

		op.TDAsyncIO.Cancel()
		op.TDAsyncIO.Run([_build()])

	def runDocsBuild(self):
		self.prepareForBuild()
		builder = DocBuilderAsync(self.context, self.ownerComp.op('moduleTable'))
		async def _build():
			await builder.runBuild()
			self.log('Finished docs build process')
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

class LibraryBuilderAsyncBase(BuilderAsyncBase):

	def _getRaytkContext(self) -> RaytkContext:
		raise NotImplementedError()

	def _getRaytkTools(self) -> RaytkTools:
		return RaytkTools(self._getRaytkContext())

	async def _processAllOperators(self):
		context = self._getRaytkContext()
		operatorsComp = context.operatorsRoot()
		self.context.moveNetworkPane(operatorsComp)
		self.context.detachTox(operatorsComp)
		categories = context.allCategories()
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
		tools = self._getRaytkTools()
		tools.updateROPMetadata(comp)
		tools.updateROPParams(comp)
		self.context.applyParamUpdatersIn(comp)
		self.context.resetCustomPars(comp)
		self.context.lockROPPars(comp)
		await self._processOperatorSubCompChildren(comp)
		self.context.consolidateOperatorPythonModules(comp)
		self.context.lockBuildLockOps(comp)
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
		operatorsComp = self._getRaytkContext().operatorsRoot()
		subOps = operatorsComp.findChildren(tags=[RaytkTags.raytkOP.name], depth=3)
		self.log(f'Found {len(subOps)} nested operators')
		for subOp in subOps:
			self.log('Processing sub-operator: ' + subOp.path)
			self.context.updateOrReclone(subOp)
			self.context.detachTox(subOp)
			self.context.disableCloning(subOp)

	async def _lockAllBuildLockOps(self):
		self.context.lockBuildLockOps(self._getRaytkContext().moduleRoot())

	async def _cleanAllOperators(self):
		for comp in self._getRaytkContext().allMasterOperators():
			self.log('Clean operator ' + comp.path)
			self.context.removeOpHelp(comp)
			self.context.cleanOperatorTypeSpecs(comp)
			self.context.cleanOperatorDefPars(comp)

	async def _cleanAllCategories(self):
		for comp in self._getRaytkContext().allCategories():
			self.log('Clean category ' + comp.path)
			self.context.removeCatHelp(comp)

	async def _removeAllBuildExcludeOps(self, scope: COMP):
		self.log(f'Removing buildExclude ops in {scope}')
		toRemove = scope.findChildren(tags=[RaytkTags.buildExclude.name], includeUtility=True)
		chunks = [list(chunk) for chunk in chunked_iterable(toRemove, 100)]
		self.log(f'Found {len(toRemove)} ops to remove in {len(chunks)} chunks')
		total = len(chunks)
		for i in range(total):
			chunk = chunks[i]
			self.log(f'Processing chunk {i + 1} of {total}')
			self.context.safeDestroyOps(chunk, verbose=True)
			await _asyncYield()

class ToolkitBuilderAsync(LibraryBuilderAsyncBase):
	def __init__(self, context: BuildContext, moduleTable: DAT):
		super().__init__(context)
		self.toolkit = None  # type: COMP | None
		self.moduleTable = moduleTable

	def _getRaytkContext(self) -> RaytkContext:
		return RaytkContext()

	async def runBuild(self):
		self.log('Starting build')
		self.toolkit = await _reloadToolkit()
		# Do this early since it switches off things like automatically writing to the opList.txt file.
		# See https://github.com/t3kt/raytk/issues/95
		self.toolkit.par.Devel = False
		version = RaytkContext().toolkitVersion()
		self.log(f'Version: {version}' + (' (experimental)' if self.context.experimental else ''))
		self.context.openNetworkPane()

		await self._detachFileSyncOps()

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

		await self.logStageStart('Lock library info')
		await self._lockLibraryInfo()

		await self.logStageStart('Process tools')
		await self._processTools()

		if self.context.includeModules:
			await self.logStageStart('Build modules')
			await self._buildModules()

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

		await self.logStageStart('Finish build')
		await self._finishBuild()

	async def _detachFileSyncOps(self):
		self.context.detachAllFileSyncDatsIn(self.toolkit, reloadFirst=True)

	async def _updateLibraryInfo(self):
		moduleDef = self.toolkit.op('moduleDefinition')
		if self.toolkit.par['Experimentalbuild'] is not None:
			self.toolkit.par.Experimentalbuild.val = self.context.experimental
			self.toolkit.par.Experimentalbuild.readOnly = True
		moduleDef.par.Experimentalbuild.val = self.context.experimental
		moduleDef.par.Raytkversion.val = RaytkContext().toolkitVersion()
		self.context.disableCloning(moduleDef)
		for p in moduleDef.customPars:
			p.readOnly = True
		libraryInfo = self.toolkit.op('libraryInfo')
		libraryInfo.par.Forcebuild.pulse()
		self.context.moveNetworkPane(libraryInfo)
		await self.context.runBuildScript(libraryInfo.op('BUILD'))

	async def _updateLibraryImage(self):
		image = RaytkContext().libraryImage()
		self.context.disableCloning(image.op('toxImage'))
		self.context.detachTox(image)
		self.context.lockBuildLockOps(image)
		image.par.Showshortcut = True
		self.toolkit.par.opviewer.val = image
		self.toolkit.par.opviewer.readOnly = True
		self.toolkit.viewer = True

	async def _preProcessComponents(self):
		components = self.toolkit.op('components')
		shared = components.op('shared')
		self.context.lockBuildLockOps(shared)
		# this one has a buildLock typeTable that isn't instance-specific,
		# so we lock it first then delete the stuff that built it
		typeSpec = components.op('typeSpec')
		self.context.lockBuildLockOps(typeSpec)
		opDef = components.op('opDefinition')
		# self.context.lockBuildLockOps(opDef)
		opDef.op('buildOpState').par.Pretty = False
		comps = components.ops(
			'typeSpec', 'typeResolver', 'typeRestrictor',
			# 'opImage',  # this has some instance-dependent stuff
			'opDefinition', 'compDefinition',
			# 'inputHandler',  # don't process inputHandler since it uses buildExclude for the config tables, which
			# won't have been locked yet when this stage runs
			'shaderBuilder',
			'opElement', 'transformCodeGenerator', 'timeProvider',
			'supportDetector', 'expressionSwitcher', 'parMenuUpdater',
			# 'codeSwitcher',
			'aggregateCodeGenerator',
			# 'combiner',  # don't process combiner since it has instance-specific buildLock things depending
			# on buildExclude
			'waveFunction',
		)
		for comp in comps:
			self.context.removeBuildExcludeOps(comp)
			await _asyncYield()

	async def _lockLibraryInfo(self):
		self.context.lockOps(self.toolkit.ops(
			'info', 'opTable', 'opCategoryTable', 'buildInfo'))

	async def _processTools(self):
		tools = self.toolkit.op('tools')
		self.context.moveNetworkPane(tools)
		self.context.reloadTox(tools)
		self.context.detachTox(tools)
		await self.context.runBuildScript(tools.op('BUILD'))

	async def _buildModules(self):
		moduleNames = [
			c.val
			for c in self.moduleTable.col('name')[1:]
			if c.val != 'raytk'
		]
		self.log(f'Found {len(moduleNames)} modules')
		for moduleName in moduleNames:
			await self._buildModule(moduleName)
		self.log('Finished building modules')

	async def _buildModule(self, name: str):
		self.log('Building module: ' + name)
		builder = ModuleBuilderAsync(self.context, name)
		await builder.runBuild()

	async def _destroyComponents(self):
		comp = self.toolkit.op('components')
		self.context.focusInNetworkPane(comp)
		self.context.safeDestroyOp(comp)

	async def _consolidateSharedPythonMods(self):
		self.context.removeRedundantPythonModules(self.toolkit, self.toolkit.ops('tools', 'libraryInfo'))

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

	async def _finishBuild(self):
		comp = self.toolkit
		self.context.focusInNetworkPane(comp)
		toxFile = self._getOutputToxPath('RayTK')
		self.log(f'Saving toolkit to {toxFile}')
		comp.save(toxFile)
		self.log('Finished build')

class ModuleBuilderAsync(LibraryBuilderAsyncBase):
	addonsRoot: COMP
	moduleContext: RaytkModuleContext
	moduleRoot: COMP

	def __init__(self, context: BuildContext, moduleName: str):
		super().__init__(context)
		self.moduleName = moduleName

	def _getRaytkContext(self) -> RaytkContext:
		return self.moduleContext

	async def runBuild(self):
		self.log('Starting build')

		await self.logStageStart('Reloading addons')
		await self.reloadAddons()

		await self.logStageStart(f'Locating module: {self.moduleName}')
		await self._locateModule()

		await self.logStageStart('Detaching file sync ops')
		await self._detachFileSyncOps()

		await self.logStageStart('Updating module info')
		await self._updateModuleInfo()

		await self.logStageStart('Updating module image')
		await self._updateModuleImage()

		await self.logStageStart('Processing operators')
		await self._processAllOperators()

		await self.logStageStart('Process nested operators')
		await self._processAllNestedOperators()

		await self.logStageStart('Lock build lock ops')
		await self._lockAllBuildLockOps()

		await self.logStageStart('Run module-specific build')
		await self._runModuleSpecificBuild()

		await self.logStageStart('Clean operators')
		await self._cleanAllOperators()

		await self.logStageStart('Clear operator categories')
		await self._cleanAllCategories()

		await self.logStageStart('Remove build exclude ops')
		await self._removeAllBuildExcludeOps(self.moduleRoot)

		await self.logStageStart('Finalize module pars')
		await self._finalizeModulePars()

		await self.logStageStart('Finish build')
		await self._finishBuild()

	async def _runModuleSpecificBuild(self):
		build = self.moduleRoot.op('BUILD')
		if build:
			await self.context.runBuildScript(build)

	async def reloadAddons(self):
		self.addonsRoot = getattr(op, 'raytkAddons')
		if self.addonsRoot:
			self.context.safeDestroyOp(self.addonsRoot)
		self.addonsRoot = root.loadTox('addons/src/raytkAddons.tox')
		self.log('Addons loaded: ' + self.addonsRoot.path)

	async def _locateModule(self):
		for comp in self.addonsRoot.findChildren(tags=['raytkModule'], depth=1):
			moduleContext = RaytkModuleContext(comp)
			if moduleContext and moduleContext.moduleName() == self.moduleName:
				self.log('Found module: ' + comp.path)
				self.moduleContext = moduleContext
				self.moduleRoot = moduleContext.moduleRoot()
				self.log('Reloading module: ' + comp.path)
				self.context.reloadTox(comp)
				return
		self.log('Module not found: ' + self.moduleName)
		raise Exception('Module not found: ' + self.moduleName)

	async def _detachFileSyncOps(self):
		self.context.detachAllFileSyncDatsIn(self.moduleRoot, reloadFirst=True)

	async def _updateModuleInfo(self):
		moduleDef = self.moduleContext.moduleDefinition()
		moduleDef.par.Experimentalbuild.val = self.context.experimental
		moduleDef.par.Raytkversion.val = RaytkContext().toolkitVersion()
		self.context.disableCloning(moduleDef)
		for p in moduleDef.customPars:
			p.readOnly = True
		for p in moduleDef.pars('Operatorsfolder', 'Testsfolder'):
			p.destroy()
		infoBuilder = self.moduleContext.moduleRoot().op('moduleInfoBuilder')
		self.context.detachTox(infoBuilder)
		self.context.disableCloning(infoBuilder)

	async def _updateModuleImage(self):
		image = self.moduleRoot.op('moduleImage')
		self.context.disableCloning(image.op('toxImage'))
		self.context.disableCloning(image)
		self.context.detachTox(image)
		self.moduleRoot.par.opviewer.val = image
		self.moduleRoot.par.opviewer.readOnly = True
		self.moduleRoot.viewer = True

	async def _finalizeModulePars(self):
		comp = self.moduleRoot
		self.context.moveNetworkPane(comp)
		if not comp.customPages:
			comp.appendCustomPage('Module')
		page = comp.customPages[0]
		p = page.appendToggle('Experimentalbuild', label='Experimental Build')[0]
		p.val = self.context.experimental
		p.readOnly = True
		p = page.appendToggle('Devel', label='Development Mode')[0]
		p.val = False
		p.readOnly = True
		p = page.appendStr('Raytkversion', label='RayTK Version')[0]
		p.val = RaytkContext().toolkitVersion()
		p.readOnly = True
		self.context.detachTox(comp)
		focusFirstCustomParameterPage(comp)

	async def _finishBuild(self):
		comp = self.moduleRoot
		self.context.focusInNetworkPane(comp)
		toxFile = self._getOutputToxPath(self.moduleName[0].upper() + self.moduleName[1:])
		self.log(f'Saving module to {toxFile}')
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

class DocBuilderAsync(BuilderAsyncBase):
	def __init__(self, context: BuildContext, moduleTable: DAT):
		super().__init__(context)
		self.toolkit = None  # type: COMP | None
		self.moduleTable = moduleTable
		self.categoryHelps = {}  # type: dict[str, CategoryHelp]
		self.addonsRoot = None  # type: COMP | None
		self.moduleContexts = []  # type: list[RaytkModuleContext]
		self.imagesFolder = Path('docs/assets/images')
		self.referenceFolder = Path('docs/_reference')
		self.dataFolder = Path('docs/_data')
		self.opsByType = {}  # type: dict[str, COMP]

	async def runBuild(self):
		self.log('Starting docs build')
		self.log('Reloading toolkit...')
		self.toolkit = await _reloadToolkit()

		await self.logStageStart('Reloading addons')
		await self.reloadAddons()

		await self.logStageStart('Clearing old docs')
		await self._clearPreviousDocs()

		await self.logStageStart('Load main toolkit categories')
		await self._loadMainToolkitCategories()

		await self.logStageStart('Load all module categories')
		await self._loadAllModuleCategories()

		await self.logStageStart('Strip alpha ops')
		await self._stripAlphaOps()

		await self.logStageStart('Remove empty categories')
		await self._removeEmptyCategories()

		await self.logStageStart('Write category list page')
		await self._writeCategoryListPage()

		await self.logStageStart('Write category pages')
		await self._writeCategoryPages()

		await self.logStageStart('Write operator pages')
		await self._writeOperatorPages()

		await self.logStageStart('Write toolkit doc data')
		await self._writeToolkitDocData()

		self.log('Finished build')

	async def reloadAddons(self):
		self.addonsRoot = getattr(op, 'raytkAddons')
		if self.addonsRoot:
			self.context.safeDestroyOp(self.addonsRoot)
		self.addonsRoot = root.loadTox('addons/src/raytkAddons.tox')
		self.log('Addons loaded: ' + self.addonsRoot.path)
		for comp in self.addonsRoot.findChildren(tags=['raytkModule'], depth=1):
			moduleContext = RaytkModuleContext(comp)
			if moduleContext:
				self.log('Reloading module ' + comp.path)
				self.context.reloadTox(comp)
				self.moduleContexts.append(moduleContext)

	async def _loadMainToolkitCategories(self):
		for comp in RaytkContext().allCategories():
			self.log(f'Loading category {comp}')
			categoryHelp = CategoryHelp.extractFromComp(comp, self.imagesFolder)
			self.categoryHelps[categoryHelp.name] = categoryHelp
			for opHelp in categoryHelp.operators:
				rop = comp.op(opHelp.name)
				self.opsByType[opHelp.opType] = rop
			await _asyncYield()

	async def _loadAllModuleCategories(self):
		self.log(f'Found {len(self.moduleContexts)} modules')
		for moduleContext in self.moduleContexts:
			await self._loadModuleCategories(moduleContext)

	async def _loadModuleCategories(self, moduleContext: RaytkModuleContext):
		self.log("Loading categories from module: " + moduleContext.moduleName())
		for categoryComp in moduleContext.allCategories():
			categoryHelp = CategoryHelp.extractFromComp(categoryComp, self.imagesFolder)
			if categoryHelp.name in self.categoryHelps:
				self.log(f'Merging {categoryComp} with existing category')
				self.categoryHelps[categoryHelp.name].mergeFrom(categoryHelp)
			else:
				self.log('Adding new category: ' + categoryComp.path)
				self.categoryHelps[categoryHelp.name] = categoryHelp
			for opHelp in categoryHelp.operators:
				rop = categoryComp.op(opHelp.name)
				self.opsByType[opHelp.opType] = rop
			await _asyncYield()
		self.log('Finished loading categories from module: ' + moduleContext.moduleName())

	async def _stripAlphaOps(self):
		for categoryHelp in self.categoryHelps.values():
			toRemove = [
				opHelp
				for opHelp in categoryHelp.operators
				if opHelp.isAlpha
			]
			self.log('Removing ' + str(len(toRemove)) + ' alpha ops from ' + categoryHelp.name)
			for opHelp in toRemove:
				categoryHelp.operators.remove(opHelp)

	async def _removeEmptyCategories(self):
		namesToRemove = []
		for categoryName in self.categoryHelps.keys():
			if not self.categoryHelps[categoryName].operators:
				namesToRemove.append(categoryName)
		for categoryName in namesToRemove:
			self.log(f'Removing empty category: {categoryName}')
			del self.categoryHelps[categoryName]

	async def _writeCategoryListPage(self):
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
		for categoryName in sorted(self.categoryHelps.keys()):
			categoryHelp = self.categoryHelps[categoryName]
			docText += f'* [{categoryHelp.name.capitalize()}]({categoryHelp.name}/) - {categoryHelp.summary}\n'
		self._writeDocs(Path('operators/index.md'), docText)

	async def _writeCategoryPages(self):
		for categoryHelp in self.categoryHelps.values():
			await self._writeCategoryPage(categoryHelp)

	async def _writeCategoryPage(self, categoryHelp: CategoryHelp):
		docText = categoryHelp.formatAsListPage()
		self._writeDocs(Path(f'operators/{categoryHelp.name}/index.md'), docText)

	async def _writeOperatorPages(self):
		for categoryHelp in self.categoryHelps.values():
			for opHelp in categoryHelp.operators:
				await self._writeOperatorPage(opHelp)

	async def _writeOperatorPage(self, opHelp: ROPHelp):
		self.log('Writing operator page for ' + opHelp.name)
		rop = self.opsByType.get(opHelp.opType)
		if not rop:
			self.log('ERROR unable to find ROP: ' + opHelp.opType)
			return
		docManager = OpDocManager(rop)
		opHelp = docManager.extractForBuild(self.imagesFolder)
		docText = opHelp.formatAsFullPage(ROPInfo(rop))
		self._writeDocs(Path(f'operators/{opHelp.category}/{opHelp.name}.md'), docText)

	def _writeDocs(self, relativePath: Path, docText: str):
		outFile = self.referenceFolder / relativePath
		outFile.parent.mkdir(parents=True, exist_ok=True)
		self.context.log(f'Writing docs to {outFile}')
		with outFile.open('w') as f:
			f.write(docText)

	async def _clearPreviousDocs(self):
		if not self.referenceFolder.exists():
			self.log(f"No previous docs to clear in {self.referenceFolder}")
			return
		self.log(f'Clearing old docs from {self.referenceFolder}')
		paths = list(sorted(self.referenceFolder.iterdir()))
		for path in paths:
			self.context.log(f'Clearing {path}')
			shutil.rmtree(path)

	async def _writeToolkitDocData(self):
		info = ToolkitInfo(toolkitVersion=str(RaytkContext().toolkitVersion()))
		text = info.formatAsDataFile()
		self.dataFolder.mkdir(parents=True, exist_ok=True)
		outFile = self.dataFolder / 'toolkit.yaml'
		with outFile.open('w') as f:
			f.write(text)

async def _reloadToolkit():
	toolkit = RaytkContext().toolkit()
	toolkit.par.externaltox = 'src/raytk.tox'
	toolkit.par.reinitnet.pulse()
	return toolkit


async def _asyncYield():
	pass
