"""
Tools for working with the toolkit in a development environment.

This should only be used within development tools.
"""

from pathlib import Path
from raytkDocs import OpDocManager
from raytkModel import OpDefMeta_OLD, OpSpec_OLD, ROPSpec
from raytkUtil import RaytkContext, ROPInfo, focusFirstCustomParameterPage, RaytkTags, CategoryInfo, ContextTypes, \
	CoordTypes, ReturnTypes
from typing import Callable, List, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class RaytkTools(RaytkContext):
	"""
	Utility that provides tools used to modify the toolkit, for use in development tools.
	"""

	def generateROPType(self, comp: 'COMP'):
		info = ROPInfo(comp)
		if not info.isMaster:
			raise Exception('ROP is not proper master')
		path = self.toolkit().relativePath(comp)
		if path.startswith('./'):
			path = path[2:]
		return 'raytk.' + path.replace('/', '.')

	def updateROPMetadata(self, rop: 'COMP', incrementVersion=False):
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
		info.toolkitVersion = self.toolkitVersion()
		info.helpUrl = f'https://t3kt.github.io/raytk/reference/opType/{info.opType}/'
		# Ensure that status is copied to the opDefinition parameter
		info.opDefPar.Raytkopstatus = info.statusLabel

	@staticmethod
	def updateROPParams(rop: 'COMP'):
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

	@staticmethod
	def updateOPImage(rop: 'COMP'):
		img = rop.op('./*Definition/opImage')
		if not img:
			return
		rop.par.opviewer.val = img
		rop.viewer = True
		return img

	def saveROP(self, rop: 'COMP', incrementVersion=False):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			# TODO: warning?
			return
		self.updateROPMetadata(rop, incrementVersion)
		self.updateROPParams(rop)
		self.saveROPSpec(rop)
		# self.saveROPSpec_NEW(rop)
		OpDocManager(info).pushToParamsAndInputs()
		focusFirstCustomParameterPage(rop)
		tox = info.toxFile
		rop.save(tox)
		ui.status = f'Saved TOX {tox} (version: {info.opVersion})'

	@staticmethod
	def setUpHelp(rop: 'COMP'):
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
	def reloadHelp(rop: 'COMP'):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		manager = OpDocManager(info.rop)
		ui.undo.startBlock('Apply ROP help to params for ' + info.rop.path)
		try:
			manager.pushToParamsAndInputs()
		finally:
			ui.undo.endBlock()

	def _loadROPSpec(self, rop: 'COMP', useFile: bool, usePars: bool) -> 'Optional[OpSpec_OLD]':
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		spec = None
		if useFile:
			specFile = self._getROPRelatedFile(rop, fileSuffix='.json', checkExists=True)
			if specFile:
				text = specFile.read_text()
				spec = OpSpec_OLD.parseJsonStr(text)
		if not spec:
			spec = OpSpec_OLD()
		if not spec.meta:
			spec.meta = OpDefMeta_OLD()
		if usePars:
			if not spec.meta.opType:
				spec.meta.opType = info.opType or self.generateROPType(info.rop)
			if spec.meta.opVersion is None:
				v = info.opVersion
				spec.meta.opVersion = int(v) if v else 0
			spec.meta.opStatus = info.statusLabel
		return spec

	@staticmethod
	def setROPStatus(rop: 'COMP', status: Optional[str]):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		info.opDefPar.Raytkopstatus = status or 'default'
		# note: since applying with status false resets the color, the false ones have to be done before the true one
		if status == 'alpha':
			RaytkTags.beta.apply(info.rop, False)
			RaytkTags.deprecated.apply(info.rop, False)
			RaytkTags.alpha.apply(info.rop, True)
		elif status == 'beta':
			RaytkTags.alpha.apply(info.rop, False)
			RaytkTags.deprecated.apply(info.rop, False)
			RaytkTags.beta.apply(info.rop, True)
		elif status == 'deprecated':
			RaytkTags.alpha.apply(info.rop, False)
			RaytkTags.beta.apply(info.rop, False)
			RaytkTags.deprecated.apply(info.rop, True)
		else:
			RaytkTags.alpha.apply(info.rop, False)
			RaytkTags.beta.apply(info.rop, False)
			RaytkTags.deprecated.apply(info.rop, False)

	@staticmethod
	def _getROPRelatedFile(rop: 'COMP', fileSuffix: str, checkExists: bool) -> 'Optional[Path]':
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

	def reloadROPSpec(self, rop: 'COMP'):
		info = ROPInfo(rop)
		if not info:
			return
		spec = self._loadROPSpec(rop, useFile=True, usePars=True)
		if not spec or not spec.meta:
			return
		info.opType = spec.meta.opType
		info.opVersion = spec.meta.opVersion
		self.setROPStatus(rop, spec.meta.opStatus)

	def saveROPSpec(self, rop: 'COMP'):
		info = ROPInfo(rop)
		if not info:
			return
		spec = self._loadROPSpec(rop, useFile=False, usePars=True)
		specFile = self._getROPRelatedFile(rop, '.json', checkExists=False)
		if specFile and spec:
			specFile.write_text(spec.toJsonStr(minify=False))

	def saveROPSpec_NEW(self, rop: 'COMP'):
		try:
			spec = ROPSpec.extract(rop, skipParams=False)
			specFile = self._getROPRelatedFile(rop, '.yaml', checkExists=False)
			spec.writeToFile(specFile)
		except Exception as err:
			ui.status = f'Failed to generate ROPSpec for {rop}: {err}'
			print(f'Failed to generate ROPSpec for {rop}:\n{err}')

	def updateAllROPToolkitVersions(self):
		version = self.toolkitVersion()
		for rop in self.allMasterOperators():
			info = ROPInfo(rop)
			if info:
				info.toolkitVersion = version

	def _templateForCategory(self, category: str) -> 'Optional[COMP]':
		catInfo = self.categoryInfo(category)
		template = catInfo and catInfo.templateComp
		if template:
			return template
		catInfo = self.categoryInfo('utility')
		return catInfo and catInfo.templateComp

	def createNewRopType(self, typeName: str, category: str) -> 'Optional[COMP]':
		catInfo = self.categoryInfo(category)
		if not catInfo:
			raise Exception(f'Category not found: {category}')
		template = self._templateForCategory(category)
		if not template:
			raise Exception(f'Template not found for category {category}')
		existing = catInfo.category.op('./' + typeName)
		if existing:
			raise Exception(f'ROP {typeName} already exists in category {category}')
		fileDir = f'src/operators/{category}'
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

	def organizeCategory(self, comp: 'COMP', saveIndexTox=True):
		catInfo = CategoryInfo(comp)
		rops = catInfo.operators
		if not rops:
			return
		self._organizeComps(rops)
		if saveIndexTox:
			catInfo.category.save(catInfo.category.par.externaltox)

	@staticmethod
	def _organizeComps(comps: 'List[COMP]'):
		comps = list(comps)
		comps.sort(key=lambda c: c.name)
		for i, o in enumerate(comps):
			o.nodeY = -int(i / 10) * 150
			o.nodeX = int(i % 10) * 200

	def updateContextTypeParMenu(self, ropInfo: 'Optional[ROPInfo]'):
		self._updateTypeParMenu(ropInfo, 'Contexttype', ContextTypes.values)

	def updateCoordTypeParMenu(self, ropInfo: 'Optional[ROPInfo]'):
		self._updateTypeParMenu(ropInfo, 'Coordtype', CoordTypes.values)

	def updateReturnTypeParMenu(self, ropInfo: 'Optional[ROPInfo]'):
		self._updateTypeParMenu(ropInfo, 'Returntype', ReturnTypes.values)

	@staticmethod
	def _updateTypeParMenu(ropInfo: 'Optional[ROPInfo]', parName: str, values: List[str]):
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

class ToolkitLoader(RaytkTools):
	def __init__(self, log: 'Callable[[str], None]'):
		self.categoryNameQueue = []  # type: List[str]
		self.log = log

	def loadToolkit(self, thenRun: Callable = None, runArgs: list = None):
		self.categoryNameQueue = []
		self._queueCall(self._loadToolkit_stage, 0, thenRun, runArgs)

	def _loadToolkit_stage(self, stage: int, thenRun: Callable = None, runArgs: list = None):
		if stage == 0:
			self._loadToolkitMetadata()
		elif stage == 1:
			self._loadCategoryComps()
		elif stage == 2:
			self._loadNextCategory(thenRun, runArgs)
			return
		else:
			if thenRun:
				self._queueCall(thenRun, *(runArgs or []))
			return
		self._queueCall(self._loadToolkit_stage, stage + 1, thenRun, runArgs)

	def _loadToolkitMetadata(self):
		self.log('Loading toolkit metadata ... but that is not yet implemented')

	def _loadCategoryComps(self):
		self.log('Loading category comps')
		opsRoot = self.operatorsRoot()
		indexTox = Path(opsRoot.par.externaltox.eval())
		catsDir = indexTox.parent
		catToxes = list(catsDir.glob('*/index.tox'))
		self.log(f'  found {len(catToxes)} category toxes')
		currentCats = list(self.allCategories())
		for o in currentCats:
			try:
				o.destroy()
			except:
				pass
		self.log(f'  cleared out {len(currentCats)} old category comps')
		for tox in catToxes:
			self.log(f'f  loading category tox: {tox.as_posix()}')
			opsRoot.loadTox(tox.as_posix())
		self.categoryNameQueue = [
			o.name
			for o in self.allCategories()
		]
		self.log(f'  loaded {len(self.categoryNameQueue)} categories')

	def _loadNextCategory(self, thenRun: Callable, runArgs: list):
		if not self.categoryNameQueue:
			self._queueCall(thenRun, *(runArgs or []))
			return
		catName = self.categoryNameQueue.pop()
		self._loadCategory(catName, thenRun=self._loadNextCategory, runArgs=[thenRun, runArgs])

	def _loadCategory(self, categoryName: str, thenRun: Callable, runArgs: list):
		self.log(f'Loading category {categoryName}')
		catInfo = self.categoryInfo(categoryName)
		indexTox = Path(catInfo.category.par.externaltox.eval())
		catDir = indexTox.parent
		foundToxes = [
			tox
			for tox in catDir.glob('*.tox')
			if tox.name != 'index.tox'
		]
		foundToxes.sort()
		self.log(f'  found {len(foundToxes)} toxes in category')
		currentOps = list(catInfo.operators)
		self.log(f'  clearing {len(currentOps)} current ops in category')
		for o in currentOps:
			try:
				o.destroy()
			except:
				pass


		self._loadCategoryHelp(catInfo, catDir)

		self.log('  loading category operators...')
		for tox in foundToxes:
			self.log(f'  loading operator tox {tox.as_posix()}')
			catInfo.category.loadTox(tox.as_posix())
		self.log(f'  loaded {len(catInfo.operators)} operators in category')

		for o in catInfo.operators:
			self._initializeOperator(o)

		self._queueCall(thenRun, *(runArgs or []))

	def _loadCategoryHelp(self, catInfo: 'CategoryInfo', catDir: 'Path'):
		helpFile = catDir / 'index.md'
		helpDat = catInfo.helpDAT
		self.log(f'Attempting to load category help from {helpFile.as_posix()}')
		if not helpDat or helpDat.par.file != helpFile.as_posix():
			if helpDat:
				helpDat.destroy()
			if not helpFile.exists():
				self.log('  no help file to load')
				return
			helpDat = catInfo.category.create(textDAT, 'help')
		helpDat.par.file = helpFile.as_posix()
		helpDat.par.loadonstartpulse.pulse()
		RaytkTags.fileSync.apply(helpDat, True)
		helpDat.nodeX = 1125
		helpDat.nodeY = 525
		helpDat.nodeWidth = 350
		helpDat.nodeHeight = 175
		self.log(f'  loaded category help from {helpFile.as_posix()} into {helpDat}')

	def _initializeOperator(self, rop: 'COMP'):
		self.log(f'Initializing operator {rop}')
		ropInfo = ROPInfo(rop)
		if ropInfo and ropInfo.opDefPar:
			ropInfo.toolkitVersion = self.toolkitVersion()

	@staticmethod
	def _queueCall(method: Callable, *args):
		run('args[0](*(args[1:]))', method, *args, delayFrames=5, delayRef=root)
