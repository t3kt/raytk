from develCommon import *
import popMenu
from raytkUtil import RaytkTags, ROPInfo, Tag, getActiveEditor, navigateTo, getROP
from typing import Tuple, List

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class Tools:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def IncrementMajor():
		version = getToolkitVersion()
		setToolkitVersion(Version(version.major + 1, 0))

	@staticmethod
	def IncrementMinor():
		version = getToolkitVersion()
		setToolkitVersion(Version(version.major, version.minor + 1))

	@staticmethod
	def ShowLibraryParams():
		getToolkit().openParameters()

	def UpdateCurrentROPsMetadata(self, incrementVersion=False):
		rops = self.getCurrentROPs(primaryOnly=False)
		for rop in rops:
			updateROPMetadata(rop, incrementVersion=incrementVersion)

	def FillMonitorHeight(self, usePrimary=True):
		height = _getMonitorHeight(usePrimary)
		height -= 270
		self.ownerComp.par.h = height

	@staticmethod
	def NavigateTo(comp: 'COMP'):
		navigateTo(comp)

	def GetCurrentROP(self):
		rops = self.getCurrentROPs(primaryOnly=True)
		return rops[0] if rops else None

	def getCurrentROPs(self, primaryOnly=False):
		pane = getActiveEditor()
		if not pane:
			return []
		comp = pane.owner
		if comp is self.ownerComp or comp.path.startswith(self.ownerComp.path + '/'):
			return None
		rop = getROP(comp) or getROP(comp.currentChild)
		if rop and primaryOnly:
			return [rop]
		rops = [rop]
		for child in comp.selectedChildren:
			rop = getROP(child, checkParents=False)
			if rop and rop not in rops:
				rops.append(rop)
		return rops

	def SaveCurrentROPs(self, incrementVersion=False):
		rops = self.getCurrentROPs(primaryOnly=False)
		if not rops:
			return
		for rop in rops:
			self.SaveROP(incrementVersion=incrementVersion, rop=rop)
		if len(rops) > 1:
			ui.status = f'Saved {len(rops)} ROP TOXs'

	def SaveROP(self, incrementVersion=False, rop: 'COMP' = None):
		if not rop:
			rop = self.GetCurrentROP()
		if not rop:
			# TODO: warning?
			return
		self.updateROPParams(rop)
		updateROPMetadata(rop, incrementVersion=incrementVersion)
		tox = rop.par.externaltox.eval()
		rop.save(tox)
		ui.status = f'Saved TOX {tox} (version: {rop.op("opDefinition").par.Raytkopversion})'
		for dat in getToolkit().ops('opfind_rops', 'opCategoryTable'):
			dat.cook(force=True)

	@staticmethod
	def updateROPParams(rop: 'COMP'):
		if rop.customPages:
			page = rop.customPages[0]
		else:
			page = rop.appendCustomPage('Settings')
		ropInfo = ROPInfo(rop)
		opDef = rop.op('opDefinition')
		if ropInfo.hasROPInputs and not ropInfo.isOutput:
			enablePar = rop.par['Enable']
			if enablePar is None:
				enablePar = page.appendToggle('Enable')[0]
				enablePar.val = True
			enablePar.order = -1
			enablePar.default = True
			if not opDef.par.Enable.expr:
				opDef.par.Enable.expr = "op('..').par.Enable"

		inspectPar = rop.par['Inspect']
		if inspectPar is None:
			inspectPar = page.appendPulse('Inspect')[0]
		inspectPar.startSection = True
		inspectPar.order = 99999

	def editCurrentROPMaster(self):
		rop = self.GetCurrentROP()
		if not rop:
			return
		rop = rop.par.clone.eval() or rop
		self.NavigateTo(rop.par.clone.eval())

	def setCurrentROPBeta(self, beta: bool):
		rops = self.getCurrentROPs()
		for rop in rops:
			opDef = rop.op('opDefinition')
			if opDef:
				RaytkTags.beta.apply(opDef, beta)
			RaytkTags.beta.applyColor(rop, beta)

	def setUpCurrentROPHelp(self):
		rops = self.getCurrentROPs()
		for rop in rops:
			self.setUpROPHelp(rop)

	@staticmethod
	def setUpROPHelp(rop: 'COMP'):
		opDef = rop.op('opDefinition')
		if not opDef:
			return
		par = opDef.par.Help
		dat = par.eval()
		ui.undo.startBlock('Set up ROP help for ' + rop.path)
		try:
			if not dat:
				dat = rop.create(textDAT, 'help')
				dat.nodeY = opDef.nodeY + 500
				dat.nodeWidth = 350
				dat.nodeHeight = 175
				par.val = dat.name
			if not dat.par.file:
				dat.par.file = rop.par.externaltox.eval().replace('.tox', '.md')
			RaytkTags.fileSync.apply(dat, True)
			if not dat.text:
				dat.text = f'# {rop.name} ({rop.parent().name})\n\n'
			dat.viewer = True
		finally:
			ui.undo.endBlock()

	def ShowCreateNewRopTypeDialog(self):
		# noinspection PyUnresolvedReferences
		self.ownerComp.op('newRopTypeDialog').ShowDialog()

	def OnCreateNewRopTypeAccept(self, info: dict):
		name = info['opName']
		category = info['opCategory']
		dest = getToolkit().op('operators/' + category)
		if not dest:
			raise Exception(f'Invalid ROP category: {category!r}')
		template = dest.op('_template')
		if not template:
			raise Exception(f'No template available for category {category!r}')
		newOp = dest.copy(template, name=name)
		newOp.par.clone = newOp.path
		newOp.par.externaltox = f'src/operators/{category}/{name}.tox'
		updateROPMetadata(newOp)
		self.SaveROP(rop=newOp)
		newOp.selected = True
		newOp.nodeX = 0
		newOp.nodeY = -300
		opDef = newOp.op('opDefinition')
		codeDat = opDef.par.Functemplate.eval()
		if codeDat and codeDat.par['file'] is not None:
			codeDat.par.file = f'src/operators/{category}/{name}.glsl'
		self.NavigateTo(dest)

	def OnOperatorsShortcutRightClick(self, button: 'COMP'):
		def goToItem(name, path):
			return popMenu.Item(
				name,
				callback=lambda: self.NavigateTo(op(path)),
			)

		categoryTable = self.ownerComp.op('rop_categories')
		popMenu.fromButton(button, h='Right', v='Top').Show(
			[
				goToItem(categoryTable[i, 'name'].val, categoryTable[i, 'path'])
				for i in range(1, categoryTable.numRows)
			]
		)

	def setBuildExcludeStateOnSelected(self, state: bool):
		self.applyTagToSelected(RaytkTags.buildExclude, state)

	def setBuildLockOnSelected(self, state: bool):
		self.applyTagToSelected(RaytkTags.buildLock, state)

	def setFileSyncOnSelected(self, state: bool):
		self.applyTagToSelected(RaytkTags.fileSync, state)

	def getTypeNamesAndLabels(self, filterColumn: str) -> 'Tuple[List[str], List[str]]':
		names = []
		labels = []
		table = self.ownerComp.op('typeTable')  # type: DAT
		for row in range(1, table.numRows):
			if table[row, filterColumn] != '1':
				continue
			names.append(table[row, 'name'].val)
			labels.append(table[row, 'label'].val)
		return names, labels

	def updateTypeParsOn(self, comp: 'COMP'):
		self.updateTypePar(comp, 'Coordtype', 'isCoordType')
		self.updateTypePar(comp, 'Contexttype', 'isContextType')
		self.updateTypePar(comp, 'Returntype', 'isReturnType')

	def updateTypeParsOnSelected(self):
		self.forEachSelected(self.updateTypeParsOn)

	def updateTypePar(self, comp: 'COMP', parName: str, filterColumn: str):
		if not comp:
			return
		par = comp.par[parName]
		if par is None:
			return
		currentVal = par.eval()
		hasUseInput = 'useinput' in par.menuNames
		names, labels = self.getTypeNamesAndLabels(filterColumn)
		if hasUseInput:
			names = ['useinput'] + names
			labels = ['Use Input'] + labels
		ui.undo.startBlock(f'Updating type parameter {par.owner} {par.name} has useinput: {hasUseInput}')
		par.menuNames = names
		par.menuLabels = labels
		par.val = currentVal
		ui.undo.endBlock()

	def DestroySelectedCustomPars(self):
		def _action(o: 'OP'):
			if hasattr(o, 'destroyCustomPars'):
				o.destroyCustomPars()
		self.forEachSelected(_action)

	def applyTagToSelected(self, tag: 'Tag', state: bool):
		self.forEachSelected(lambda o: tag.apply(o, state))

	@staticmethod
	def forEachSelected(action):
		editor = getActiveEditor()
		if not editor:
			return
		for o in editor.owner.selectedChildren:
			action(o)

def _getMonitorHeight(usePrimary=True):
	if usePrimary:
		return monitors.primary.height
	for m in monitors:
		if not m.isPrimary:
			return m.height
	for m in monitors:
		return m.height

def setToolkitVersion(version: Version):
	toolkit = getToolkit()
	if toolkit.par['Raytkversion'] is None:
		page = toolkit.appendCustomPage('RayTK')
		page.appendStr('Raytkversion', label='RayTK Version')
	par = toolkit.par.Raytkversion
	par.val = str(version)
	par.readOnly = True
