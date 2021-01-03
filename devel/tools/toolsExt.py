from develCommon import AutoLoader
import popMenu
from raytkTools import RaytkTools
from raytkUtil import RaytkTags, Tag, navigateTo, recloneComp, RaytkContext, TypeTableHelper, CategoryInfo, Version
from typing import List, Tuple, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from devel.toolkitEditor.toolkitEditor import ToolkitEditor

class Tools:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def IncrementMajor():
		version = RaytkContext().toolkitVersion()
		setToolkitVersion(Version(version.major + 1, 0))

	@staticmethod
	def IncrementMinor():
		context = RaytkContext()
		version = context.toolkitVersion()
		setToolkitVersion(Version(version.major, version.minor + 1))

	@staticmethod
	def ShowLibraryParams():
		RaytkContext().toolkit().openParameters()

	def UpdateCurrentROPsMetadata(self, incrementVersion=False):
		rops = self.getCurrentROPs(primaryOnly=False)
		tools = RaytkTools()
		for rop in rops:
			tools.updateROPMetadata(rop, incrementVersion=incrementVersion)

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
		return RaytkContext().currentROPs(
			primaryOnly=primaryOnly,
			exclude=lambda c: c is self.ownerComp or c.path.startswith(self.ownerComp.path + '/'))

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
		RaytkTools().saveROP(rop, incrementVersion)

	def editCurrentROPMaster(self):
		rop = self.GetCurrentROP()
		if not rop:
			return
		rop = rop.par.clone.eval() or rop
		self.NavigateTo(rop.par.clone.eval())
		self.toolkitEditor().EditROP(rop)

	def setCurrentROPBeta(self, state: bool):
		self.applyTagToCurrentROPs(RaytkTags.beta, state)

	def setCurrentROPAlpha(self, state: bool):
		self.applyTagToCurrentROPs(RaytkTags.alpha, state)

	def setCurrentROPDeprecated(self, state: bool):
		self.applyTagToCurrentROPs(RaytkTags.deprecated, state)

	def setUpCurrentROPHelp(self):
		tools = RaytkTools()
		for rop in self.getCurrentROPs():
			tools.setUpHelp(rop)

	def reloadCurrentROPHelp(self):
		tools = RaytkTools()
		for rop in self.getCurrentROPs():
			tools.reloadHelp(rop)

	def addCurrentROPMacroTable(self):
		rop = self.GetCurrentROP()
		if rop:
			self.addMacroTableToROP(rop)

	@staticmethod
	def addMacroTableToROP(rop: 'COMP'):
		opDef = rop.op('opDefinition')
		if not opDef:
			return
		dat = op(opDef.par.Macrotable)
		if dat:
			return
		ui.undo.startBlock('Add macro table to ' + rop.path)
		try:
			exprTable = rop.create(tableDAT, 'macro_exprs')
			exprTable.clear()
			exprTable.appendRow(['', ''])
			evalTable = rop.create(evaluateDAT, 'eval_macros')
			evalTable.inputConnectors[0].connect(exprTable)
			opDef.par.Macrotable = evalTable
			exprTable.nodeY = evalTable.nodeY = opDef.nodeY - 250
			evalTable.nodeCenterX = opDef.nodeCenterX
			exprTable.nodeX = evalTable.nodeX - 150
			exprTable.viewer = evalTable.viewer = True
		finally:
			ui.undo.endBlock()

	def ShowCreateNewRopTypeDialog(self):
		# noinspection PyUnresolvedReferences
		self.ownerComp.op('newRopTypeDialog').ShowDialog()

	def OnCreateNewRopTypeAccept(self, info: dict):
		name = info['opName']
		category = info['opCategory']
		dest = RaytkContext().operatorsRoot().op(category)
		if not dest:
			raise Exception(f'Invalid ROP category: {category!r}')
		template = dest.op('_template')
		if not template:
			raise Exception(f'No template available for category {category!r}')
		newOp = dest.copy(template, name=name)
		newOp.par.clone = newOp.path
		newOp.par.externaltox = f'src/operators/{category}/{name}.tox'
		RaytkTools().updateROPMetadata(newOp)
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

	def setValidationOnSelected(self, state: bool):
		self.applyTagToSelected(RaytkTags.validation, state)

	def recloneSelected(self):
		self.forEachSelected(recloneComp)

	def setShowCustomOnlyOnSelected(self, state: bool):
		def _action(o: 'COMP'):
			o.showCustomOnly = state
		self.forEachSelected(_action)

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
		if not comp:
			return
		helper = TypeTableHelper(self.ownerComp.op('typeTable'))
		par = comp.par['Coordtype']
		if par is not None:
			helper.updateCoordTypePar(par, hasUseInput=None)
		par = comp.par['Contexttype']
		if par is not None:
			helper.updateContextTypePar(par, hasUseInput=None)
		par = comp.par['Returntype']
		if par is not None:
			helper.updateReturnTypePar(par, hasUseInput=None)

	def updateTypeParsOnSelected(self):
		self.forEachSelected(self.updateTypeParsOn)

	def DestroySelectedCustomPars(self):
		def _action(o: 'OP'):
			if hasattr(o, 'destroyCustomPars'):
				o.destroyCustomPars()
		self.forEachSelected(_action)

	def applyTagToSelected(self, tag: 'Tag', state: bool):
		self.forEachSelected(lambda o: tag.apply(o, state))

	def applyTagToCurrentROPs(self, tag: 'Tag', state: bool):
		for rop in self.getCurrentROPs():
			tag.apply(rop, state)

	def setUpAutoLoadOnSelected(self):
		def _action(comp):
			if comp:
				AutoLoader(comp).setUpParameters()
		self.forEachSelected(_action)

	def applyAutoLoadOnSelected(self):
		def _action(comp):
			if comp:
				AutoLoader(comp).applyAutoLoad()
		self.forEachSelected(_action)

	@staticmethod
	def forEachSelected(action):
		editor = RaytkContext().activeEditor()
		if not editor:
			return
		for o in editor.owner.selectedChildren:
			action(o)

	def organizeCurrentCategory(self):
		categories = RaytkContext().currentCategories()
		for cat in categories:
			self.organizeCategory(cat)

	@staticmethod
	def organizeCategory(comp: 'COMP'):
		catInfo = CategoryInfo(comp)
		rops = catInfo.operators
		if not rops:
			return
		rops.sort(key=lambda r: r.name)
		for i, rop in enumerate(rops):
			rop.nodeY = -int(i / 10) * 150
			rop.nodeX = int(i % 10) * 200

	def openToolkitEditor(self):
		self.toolkitEditor().par.Open.pulse()

	@staticmethod
	def toolkitEditor() -> 'Union[ToolkitEditor, COMP]':
		return op('/toolkitEditor')

	def openPrototypeEditor(self):
		self.openEditorWorkspace('devel/prototypes/')

	def openTestCaseEditor(self):
		self.openEditorWorkspace('tests/testCases/')

	@staticmethod
	def openEditorWorkspace(workspaceFolder: str):
		editor = op('/editor')
		# noinspection PyUnresolvedReferences
		editor.Workspace.LoadWorkspaceFolder(workspaceFolder)
		editor.par.Openwindow.pulse()

def _getMonitorHeight(usePrimary=True):
	if usePrimary:
		return monitors.primary.height
	for m in monitors:
		if not m.isPrimary:
			return m.height
	for m in monitors:
		return m.height

def setToolkitVersion(version: Version):
	context = RaytkContext()
	toolkit = context.toolkit()
	if toolkit.par['Raytkversion'] is None:
		page = toolkit.appendCustomPage('RayTK')
		page.appendStr('Raytkversion', label='RayTK Version')
	par = toolkit.par.Raytkversion
	par.val = str(version)
	par.readOnly = True
