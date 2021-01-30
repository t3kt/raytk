from pathlib import Path
from raytkDocs import OpDocManager
from raytkModel import OpDefMeta, OpSpec
from raytkUtil import RaytkContext, ROPInfo, focusCustomParameterPage
from typing import List, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class RaytkTools(RaytkContext):
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

	@staticmethod
	def updateROPParams(rop: 'COMP'):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		if rop.customPages:
			page = rop.customPages[0]
		else:
			page = rop.appendCustomPage('Settings')

		# Set up inspect par
		inspectPar = rop.par['Inspect']
		if info.supportsInspect:
			if inspectPar is None:
				inspectPar = page.appendPulse('Inspect')[0]
			inspectPar.startSection = True
			inspectPar.order = 888
		elif inspectPar is not None:
			inspectPar.destroy()

		# Set up help trigger par
		helpPar = rop.par['Help']
		if info.helpUrl:
			if helpPar is None:
				helpPar = page.appendPulse('Help')[0]
			helpPar.startSection = True
			helpPar.order = 999
		elif helpPar is not None:
			helpPar.destroy()

		# Set up update op par
		updatePar = rop.par['Updateop']
		if updatePar is None:
			updatePar = page.appendPulse('Updateop', label='Update OP')[0]
		updatePar.startSection = True
		updatePar.order = 1111

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
		OpDocManager(info).pushToParamsAndInputs()
		focusCustomParameterPage(rop, 0)
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

	def _loadROPSpec(self, rop: 'COMP', useFile: bool, usePars: bool) -> 'Optional[OpSpec]':
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		spec = None
		if useFile:
			specFile = self._getROPSpecFile(rop, checkExists=True)
			if specFile:
				text = specFile.read_text()
				spec = OpSpec.parseJsonStr(text)
		if not spec:
			spec = OpSpec()
		if not spec.meta:
			spec.meta = OpDefMeta()
		if usePars:
			if not spec.meta.opType:
				spec.meta.opType = info.opType or self.generateROPType(info.rop)
			if spec.meta.opVersion is None:
				v = info.opVersion
				spec.meta.opVersion = int(v) if v else 0
		return spec

	@staticmethod
	def _getROPSpecFile(rop: 'COMP', checkExists: bool) -> 'Optional[Path]':
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		tox = info.toxFile
		if not tox:
			return
		file = Path(tox.replace('.tox', '.json'))
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

	def saveROPSpec(self, rop: 'COMP'):
		info = ROPInfo(rop)
		if not info:
			return
		spec = self._loadROPSpec(rop, useFile=False, usePars=True)
		specFile = self._getROPSpecFile(rop, checkExists=False)
		if specFile and spec:
			specFile.write_text(spec.toJsonStr(minify=False))

	def updateAllROPToolkitVersions(self):
		version = self.toolkitVersion()
		for rop in self.allMasterOperators():
			info = ROPInfo(rop)
			if info:
				info.toolkitVersion = version

class AutoLoader:
	def __init__(self, folderComp: 'COMP'):
		self.folderComp = folderComp

	def setUpParameters(self):
		if not self.folderComp.par.externaltox:
			ui.status = f'Component does not have a tox, so auto-load does not apply: {self.folderComp}'
			return
		ui.undo.startBlock(f'Add auto-load parameters to {self.folderComp}')
		page = self.folderComp.appendCustomPage('Auto Load')
		if not self.folderComp.par['Autoloadfolder']:
			p = page.appendFolder('Autoloadfolder', label='Auto Load Folder')[0]
			toxPath = self.folderComp.par.externaltox.eval()
			if toxPath:
				p.val = Path(toxPath).parent.as_posix() + '/'
		if self.folderComp.par['Autoloaddeletemissing'] is None:
			page.appendToggle('Autoloaddeletemissing', label='Delete Missing Components')
		if self.folderComp.par['Autoloadalwaysreloadall'] is None:
			page.appendToggle('Autoloadalwaysreloadall', label='Always Reload All')
		ui.undo.endBlock()

	def applyAutoLoad(self):
		print(f'Applying auto load to {self.folderComp}')
		if not self.folderComp.par['Autoloadfolder']:
			return
		folder = self.folderComp.par.Autoloadfolder.eval()
		folderPath = Path(folder)
		if not folderPath.exists() or not folderPath.is_dir():
			raise Exception(f'Invalid auto-load folder: {folder!r}')
		parentToxPath = Path(self.folderComp.par.externaltox.eval()).as_posix()
		deleteMissing = bool(self.folderComp.par['Autoloaddeletemissing'])
		alwaysReload = bool(self.folderComp.par['Autoloadalwaysreloadall'])

		currentCompsByTox = {
			Path(c.par.externaltox.eval()).as_posix(): c
			for c in self.folderComp.findChildren(type=COMP, maxDepth=1)
			if c.par.externaltox
		}

		toxPaths = [
			p.as_posix()
			for p in sorted(folderPath.glob('*.tox'))
			if p.as_posix() != parentToxPath
		]
		print(f'Auto load found current comps:')
		for t, c in currentCompsByTox.items():
			print(f'   {c} : {t}')
		print(f'Auto load found toxes:')
		for t in toxPaths:
			print(f'   {t}')

		toDelete = []  # type: List[COMP]
		toxsToLoad = []  # type: List[str]

		if alwaysReload:
			toDelete = list(currentCompsByTox.values())
			toxsToLoad = list(toxPaths)
		else:
			if deleteMissing:
				toDelete = [
					comp
					for tox, comp in currentCompsByTox.items()
					if tox not in toxPaths
				]
			toxsToLoad = [
				tox
				for tox in toxPaths
				if tox not in currentCompsByTox
			]

		# print(f'Auto load for {self.folderComp} will destroy:')
		# print('\n'.join([c.name for c in toDelete]))
		# print('and will load:')
		# print('\n'.join(toxsToLoad))

		ui.undo.startBlock(f'Applying auto load in {self.folderComp}')

		for child in toDelete:
			print(f'Auto load is removing {child}')
			try:
				child.destroy()
			except:
				pass

		for i, tox in enumerate(toxsToLoad):
			print(f'Auto load is loading {tox}')
			comp = self.folderComp.loadTox(tox)
			comp.nodeY = 500 - i * 150

		ui.undo.endBlock()