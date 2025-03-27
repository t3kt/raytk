"""
Tools for working with the toolkit in a development environment.

This should only be used within development tools.
"""

from pathlib import Path
from raytkDocs import OpDocManager
from raytkModel import ROPSpec, RCompSpec, ROPSpecBase
from raytkUtil import RaytkContext, ROPInfo, focusFirstCustomParameterPage, RaytkTags, CategoryInfo, ContextTypes, \
	CoordTypes, ReturnTypes, IconColors
from typing import Callable

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class RaytkTools:
	def __init__(self, context: RaytkContext | None = None):
		self.context = context or RaytkContext()

	"""
	Utility that provides tools used to modify the toolkit, for use in development tools.
	"""

	def generateROPType(self, comp: COMP):
		info = ROPInfo(comp)
		if not info.isMaster:
			raise Exception('ROP is not proper master')
		path = self.context.moduleRoot().relativePath(comp)
		if path.startswith('./'):
			path = path[2:]
		return self.context.moduleName() + '.' + path.replace('/', '.')

	def updateROPMetadata(self, rop: COMP, incrementVersion=False):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		info.opDefPar.enablecloningpulse.pulse()
		currentOpType = info.opType
		currentOpVersion = info.opVersion
		newType = self.generateROPType(rop)
		info.opType = newType
		if not currentOpVersion or not currentOpType or currentOpType != newType:
			versionVal = 0
		else:
			versionVal = currentOpVersion
			if incrementVersion:
				versionVal = int(versionVal) + 1
		info.opVersion = versionVal
		info.toolkitVersion = self.context.toolkitVersion()
		info.helpUrl = f'https://t3kt.github.io/raytk/reference/opType/{info.opType}/'
		# Ensure that status is copied to the opDefinition parameter
		info.opDefPar.Raytkopstatus = info.statusLabel
		for tag in [RaytkTags.alpha, RaytkTags.beta, RaytkTags.deprecated]:
			if tag.name in info.opDef.tags:
				info.opDef.tags.remove(tag.name)

	def updateROPParams(self, rop: COMP):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		if rop.customPages:
			page = rop.customPages[0]
		else:
			page = rop.appendCustomPage('Settings')

		toolkitAvailableExpr = "hasattr(op, 'raytk') and bool(op.raytk.op('tools/inspector'))"

		# Set up inspect par
		inspectPar = rop.par['Inspect']
		if info.supportsInspect:
			if inspectPar is None:
				inspectPar = page.appendPulse('Inspect')[0]
			inspectPar.startSection = True
			inspectPar.order = 888
			inspectPar.enableExpr = toolkitAvailableExpr
			inspectPar.help = 'Open the Inspector for this OP.\nToolkit tox must be loaded in the project.'
		elif inspectPar is not None:
			inspectPar.destroy()

		# Set up help trigger par
		helpPar = rop.par['Help']
		if info.helpUrl:
			if helpPar is None:
				helpPar = page.appendPulse('Help')[0]
			if inspectPar is None:
				helpPar.startSection = True
			helpPar.order = 999
		elif helpPar is not None:
			helpPar.destroy()

		# Set up update op par
		updatePar = rop.par['Updateop']
		if updatePar is None:
			updatePar = page.appendPulse('Updateop', label='Update OP')[0]
		if inspectPar is None and helpPar is None:
			updatePar.startSection = True
		updatePar.order = 1111
		updatePar.enableExpr = toolkitAvailableExpr
		updatePar.help = 'Update this OP to a new toolkit version.\nNew toolkit tox must be loaded in the project.'

		self._updateVariableRefParams(rop)
		self._updateRenderSelectParams(rop)

	@staticmethod
	def _updateVariableRefParams(rop: COMP):
		if rop.name == 'provideVariable':
			return
		info = ROPInfo(rop)
		if not info.isROP:
			return
		opState = info.opDefExt.getRopState()
		if not opState.variables:
			return
		varNamesAndLabels = [
			(variableObj.localName, variableObj.label)
			for variableObj in opState.variables
		]
		if not varNamesAndLabels:
			return
		varNames = [nl[0] for nl in varNamesAndLabels]
		toDelete = []
		page = rop.appendCustomPage('Variables')
		for par in list(page.pars):
			if par.valid and par.name.startswith('Createref') and par.name.replace('Createref', '') not in varNames:
				toDelete.append(par)
		for i, nl in enumerate(varNamesAndLabels):
			name, label = nl
			par = page.appendPulse('Createref' + name.lower(), label=label)[0]
			par.help = f'Create reference to variable: {label}'
			par.enableExpr = "hasattr(op, 'raytk') and op.raytk.op('tools/palette')"
			par.order = 777 + i
		for par in toDelete:
			if not par.valid:
				continue
			try:
				par.destroy()
			except:
				pass

	@staticmethod
	def _updateRenderSelectParams(rop: COMP):
		table = ROPInfo(rop).outputBufferTable
		if not table:
			return
		names = [str(c) for c in table.col('name')[1:]]
		toDelete = []
		page = rop.appendCustomPage('Outputs')
		for par in list(page.pars):
			if par.valid and par.name.startswith('Creatersel') and par.name.replace('Creatersel', '') not in names:
				toDelete.append(par)
		for i in range(1, table.numRows):
			name = str(table[i, 'name'])
			label = str(table[i, 'label'])
			par = page.appendPulse('Creatersel' + name.lower(), label=f'Select {label}')[0]
			par.help = f'Create renderSelect for output: {label}'
			par.enableExpr = f"hasattr(op, 'raytk') and op.raytk.op('tools/palette') and '{name}' in op('./output_buffers').col('name')[1:]"
			par.order = 888 + i
		for par in toDelete:
			if not par.valid:
				continue
			try:
				par.destroy()
			except:
				pass

	@staticmethod
	def updateOPImage(rop: COMP):
		img = rop.op('./*Definition/opImage')
		if not img:
			return
		rop.par.opviewer.val = img
		rop.viewer = True
		return img

	def saveROP(self, rop: COMP, incrementVersion=False):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			# TODO: warning?
			return
		self.updateROPMetadata(rop, incrementVersion)
		self.updateROPParams(rop)
		self.updateOPImage(rop)
		self.updateROPDATLanguages(rop)
		self.saveROPSpec(rop)
		OpDocManager(info).pushToParams()
		focusFirstCustomParameterPage(rop)
		opDefComp = info.opDef
		if info.isROP:
			opDefComp.par.ext0object = "op('./opDefinition').module.OpDefinition(me)"
			opDefComp.par.ext0name = 'opDefinition'
		if info.isRComp:
			opDefComp.par.ext0object = "op('./compDefinition').module.CompDefinition(me)"
			opDefComp.par.ext0name = 'compDefinition'
		opDefComp.par.ext0object.readOnly = True
		opDefComp.par.ext0name.readOnly = True
		opDefComp.par.ext0promote.readOnly = True
		tox = info.toxFile
		rop.par.savebackup = False
		if rop.par['reloadtoxonstart'] is not None:
			rop.par.reloadtoxonstart.expr = ''
			rop.par.reloadtoxonstart.val = True
		else:
			rop.par.enableexternaltox.expr = ''
			rop.par.enableexternaltox.val = True
		rop.par.reloadcustom.expr = ''
		rop.par.reloadcustom.val = True
		rop.par.reloadbuiltin.expr = ''
		rop.par.reloadbuiltin.val = True
		rop.color = IconColors.defaultBgColor
		rop.save(tox)
		ui.status = f'Saved TOX {tox} (version: {info.opVersion})'

	@staticmethod
	def updateROPDATLanguages(rop: COMP):
		info = ROPInfo(rop)
		if not info.isROP or not info.isMaster:
			return
		for par in [
			info.opDefPar.Opglobals,
			info.opDefPar.Initcode,
			info.opDefPar.Functemplate,
			info.opDefPar.Materialcode,
		]:
			dat = par.eval()
			if dat and isinstance(dat, textDAT):
				langPar = dat.par['language']
				if langPar == 'input':
					dat.par.language = 'glsl'

	@staticmethod
	def setUpHelp(rop: COMP):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		manager = OpDocManager(info.rop)
		ui.undo.startBlock('Set up ROP help for ' + info.rop.path)
		try:
			manager.setUpMissingParts()
		finally:
			ui.undo.endBlock()

	@staticmethod
	def reloadHelp(rop: COMP):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		manager = OpDocManager(info.rop)
		ui.undo.startBlock('Apply ROP help to params for ' + info.rop.path)
		try:
			manager.pushToParams()
		finally:
			ui.undo.endBlock()

	@staticmethod
	def setROPStatus(rop: COMP, status: str | None):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		info.setOpStatus(status)

	@staticmethod
	def _getROPRelatedFile(rop: COMP, fileSuffix: str, checkExists: bool) -> Path | None:
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		tox = info.toxFile
		if not tox:
			return
		file = Path(tox.replace('.tox', fileSuffix))
		if checkExists and not file.exists():
			return
		return file

	def loadROPSpec(self, rop: COMP, checkExists: bool) -> ROPSpecBase | None:
		specFile = self._getROPRelatedFile(rop, '.yaml', checkExists=False)
		if not specFile.exists():
			if checkExists:
				ui.status = f'No ROPSpec file {specFile.as_posix()}'
				return
			return None
		text = specFile.read_text()
		if text.startswith('!rcomp'):
			spec = RCompSpec.parseFromText(text)
		else:
			spec = ROPSpec.parseFromText(text)
		return spec

	def applyROPSpec(self, rop: COMP):
		try:
			ropInfo = ROPInfo(rop)
			if not ropInfo:
				raise Exception(f'Invalid ROP: {rop!r}')
			spec = self.loadROPSpec(rop, checkExists=True)
			if not spec:
				raise Exception(f'No spec found for {rop}')
			if isinstance(spec, ROPSpec):
				if spec.opDef:
					spec.opDef.applyToComp(ropInfo.opDef)
			if spec.meta:
				spec.meta.applyToRopInfo(ropInfo)
			# TODO: inputs, params, etc.
		except Exception as err:
			ui.status = f'Failed to load ROPSpec for {rop}: {err}'
			print(f'Failed to load ROPSpec for {rop}:\n{err}')

	def saveROPSpec(self, rop: COMP):
		try:
			ropInfo = ROPInfo(rop)
			if not ropInfo:
				raise Exception(f'Invalid ROP: {rop!r}')
			spec = self.loadROPSpec(rop, checkExists=False)
			if not spec:
				if ropInfo.isROP:
					spec = ROPSpec()
				else:
					spec = RCompSpec()
			spec.updateFromRop(ropInfo.rop, skipParams=True)
			# TODO: inputs, params, etc.
			specFile = self._getROPRelatedFile(rop, '.yaml', checkExists=False)
			spec.writeToFile(specFile)
		except Exception as err:
			ui.status = f'Failed to generate ROPSpec for {rop}: {err}'
			print(f'Failed to generate ROPSpec for {rop}:\n{err}')

	def saveAllROPSpecs(self):
		rops = self.context.allMasterOperators()
		for rop in rops:
			if not ROPInfo(rop).isROP:
				continue
			print(f'Saving ROP spec for {rop}')
			self.saveROPSpec(rop)

	def saveAllROPs(self, incrementVersion: bool):
		rops = self.context.allMasterOperators()
		for rop in rops:
			if not ROPInfo(rop).isROP:
				continue
			print(f'Saving ROP {rop}')
			self.saveROP(rop, incrementVersion=incrementVersion)
		print('Finished saving all ROPs')

	def _templateForCategory(self, category: str) -> COMP | None:
		catInfo = self.context.categoryInfo(category)
		template = catInfo and catInfo.templateComp
		if template:
			return template
		catInfo = RaytkContext().categoryInfo(category)
		template = catInfo and catInfo.templateComp
		if template:
			return template
		catInfo = self.context.categoryInfo('utility')
		if not catInfo:
			catInfo = RaytkContext().categoryInfo('utility')
		return catInfo and catInfo.templateComp

	def createNewRopType(self, typeName: str, category: str) -> COMP | None:
		catInfo = self.context.categoryInfo(category)
		if not catInfo:
			raise Exception(f'Category not found: {category}')
		template = self._templateForCategory(category)
		if not template:
			raise Exception(f'Template not found for category {category}')
		existing = catInfo.category.op('./' + typeName)
		if existing:
			raise Exception(f'ROP {typeName} already exists in category {category}')
		opsDir = self.context.operatorsFolder()
		if not opsDir:
			raise Exception('Operators folder not found')
		fileDir = opsDir + '/' + category
		rop = catInfo.category.copy(template, name=typeName)  # type: COMP
		rop.par.clone = rop.path
		rop.par.externaltox = f'{fileDir}/{typeName}.tox'
		codeDat = rop.op('./function')
		codeDat.par.file = f'{fileDir}/{typeName}.glsl'
		codeDat.par.syncfile = False
		codeDat.par.writepulse.pulse()
		RaytkTags.fileSync.apply(codeDat, True)
		self.saveROP(rop)
		self.organizeCategory(catInfo.category)
		return rop

	def organizeCategory(self, comp: COMP, saveIndexTox=True):
		catInfo = CategoryInfo(comp)
		rops = catInfo.operators
		if not rops:
			return
		self._organizeComps(rops)
		if saveIndexTox:
			catInfo.category.save(catInfo.category.par.externaltox)

	@staticmethod
	def _organizeComps(comps: list[COMP]):
		comps = list(comps)
		comps.sort(key=lambda c: c.name)
		for i, o in enumerate(comps):
			o.nodeY = -int(i / 10) * 150
			o.nodeX = int(i % 10) * 200

	def updateContextTypeParMenu(self, ropInfo: ROPInfo | None):
		self._updateTypeParMenu(ropInfo, 'Contexttype', ContextTypes.values)

	def updateCoordTypeParMenu(self, ropInfo: ROPInfo | None):
		self._updateTypeParMenu(ropInfo, 'Coordtype', CoordTypes.values)

	def updateReturnTypeParMenu(self, ropInfo: ROPInfo | None):
		self._updateTypeParMenu(ropInfo, 'Returntype', ReturnTypes.values)

	@staticmethod
	def _updateTypeParMenu(ropInfo: ROPInfo | None, parName: str, values: list[str]):
		if not ropInfo:
			return
		par = ropInfo.rop.par[parName]
		if par is None:
			ui.status = f'No {parName} to update on {ropInfo.rop}'
			return
		if par.menuSource:
			ui.status = f'Skipping {parName} on {ropInfo.rop} since it is using menuSource'
			return
		defVal = par.default
		shouldUpdateVal = par.mode == ParMode.CONSTANT and defVal != ''
		hasAuto = 'auto' in par.menuNames
		hasUseInput = 'useinput' in par.menuNames
		names = list(values)
		labels = list(names)
		if hasAuto:
			names = ['auto'] + names
			labels = ['Auto'] + labels
		if hasUseInput:
			names = ['useinput'] + names
			labels = ['Use Input'] + labels
		if par.menuNames == names:
			ui.status = f'{parName} on {ropInfo.rop} already up to date'
			return
		print(f'Updating {parName} on {ropInfo.rop} menu to :\n{names}')
		par.menuNames = names
		par.menuLabels = labels
		par.default = defVal
		if shouldUpdateVal:
			par.val = defVal
		ui.status = f'Updated {parName} on {ropInfo.rop}!'

class _ModuleLoader(RaytkTools):
	def __init__(
			self,
			context: RaytkContext,
			operatorsComp: COMP,
			operatorsFolder: Path,
			log: 'Callable[[str], None]',
	):
		super().__init__(context)
		self.operatorsComp = operatorsComp
		self.operatorsFolder = operatorsFolder
		self._log = log

	def log(self, msg):
		if self._log:
			self._log(msg)

	async def load(self, clearExisting: bool):
		if clearExisting:
			await self._clearExisting()
		categoryFolders = list(self.operatorsFolder.glob('*/'))
		self.log('Loading category folders: ' + ', '.join(f.name for f in categoryFolders))
		for catFolder in categoryFolders:
			await self._loadCategory(catFolder)
		self.log('Finished loading categories')

	async def _clearExisting(self):
		self.log('Clearing existing COMPs')
		for o in self.operatorsComp.children:
			self.log('Removing ' + o.path)
			try:
				o.destroy()
			except:
				pass

	async def _loadCategory(self, categoryFolder: Path):
		catName = categoryFolder.name
		self.log(f'Loading category {catName} from {categoryFolder.as_posix()}')
		catComp = self.operatorsComp.op(catName)
		if catComp:
			self.log('Using existing COMP ' + catComp.path)
		else:
			catComp = self.operatorsComp.create(baseCOMP, catName)
			compToxFile = categoryFolder / 'index.tox'
			catComp.par.externaltox = compToxFile.as_posix()
			catComp.par.savebackup = True
			catComp.save(compToxFile.as_posix())
			self.log('Created new COMP ' + catComp.path)
		opToxFiles = list(sorted([
			f
			for f in categoryFolder.glob('*.tox')
			if f.name != 'index.tox'
		]))
		self.log(f'Found {len(opToxFiles)} operator tox files')
		for toxFile in opToxFiles:
			await self._loadOperator(catComp, toxFile)
		helpFile = categoryFolder / 'index.md'
		await self._loadCategoryHelp(catComp, helpFile)
		await self._applyCategoryLayout(catComp)
		self.log(f'Finished loading category {catName}')

	async def _loadOperator(self, categoryComp: COMP, toxFile: Path):
		self.log(f'Loading operator from {toxFile.as_posix()} into {categoryComp}')
		name = toxFile.stem
		o = categoryComp.op(name)
		if o:
			self.log(f'  Reloading existing operator {o}')
			o.par.enableexternaltoxpulse.pulse()
		else:
			o = categoryComp.loadTox(toxFile.as_posix())
			self.log(f'Loaded operator {o}')

	async def _loadCategoryHelp(self, categoryComp: COMP, helpFile: Path):
		helpDat = categoryComp.op('help')
		if not helpFile:
			if helpDat:
				self.log(f'Removing help DAT {helpDat}')
				helpDat.destroy()
			return
		self.log(f'Loading help file {helpFile.as_posix()}')
		if not helpDat:
			helpDat = categoryComp.create(textDAT, 'help')
		helpDat.par.file = helpFile.as_posix()
		helpDat.par.syncfile = True
		RaytkTags.fileSync.apply(helpDat, True)

	async def _applyCategoryLayout(self, categoryComp: COMP):
		self.log(f'Updating layout in {categoryComp}')
		templateComp = categoryComp.op('__template')
		helpDat = categoryComp.op('help')
		operatorComps = [
			o
			for o in categoryComp.children
			if o.isCOMP and o != templateComp
		]
		operatorComps.sort(key=lambda o: o.name)
		for i, o in enumerate(operatorComps):
			o.nodeX = 200 * (i % 10)
			o.nodeY = -200 * (i // 10)
		if templateComp:
			templateComp.nodeX = -275
			templateComp.nodeY = 325
		if helpDat:
			helpDat.nodeWidth = 350
			helpDat.nodeHeight = 175
			helpDat.nodeX = 675
			helpDat.nodeY = 275
		self.log('Finished updating layout')
