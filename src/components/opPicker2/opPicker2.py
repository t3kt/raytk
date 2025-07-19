from dataclasses import dataclass, field
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _stubs.TreeListerExt import TreeListerExt
	from _stubs.ListerExt import ListerExt
	from _typeAliases import *

	class _Par(ParCollection):
		Thumbsize: IntParamT
		Thumbroot: OPParamT
	class _COMP(panelCOMP):
		par: _Par

	class _UIStatePar(ParCollection):
		Showalpha: BoolParamT
		Showbeta: BoolParamT
		Showdeprecated: BoolParamT
		Showhelp: BoolParamT
		Showthumbs: BoolParamT
		Showstatuschips: BoolParamT
		Usedisplaycategories: BoolParamT
		Pinopen: BoolParamT
		Flatmode: BoolParamT
		Filtertext: StrParamT

	ipar.uiState = _UIStatePar()
	from _stubs.TDCallbacksExt import CallbacksExt
	ext.callbacks = CallbacksExt(None)

class OpPicker2:
	def __init__(self, ownerComp: COMP):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.opTable = ownerComp.op('opTypesById')  # type: DAT
		self.treeLister = ownerComp.op('treeLister')  # type: COMP | TreeListerExt
		self.flatLister = ownerComp.op('flatLister')  # type: COMP | ListerExt

	def _getAllOpItems(self) -> list['_OpItem']:
		items = []
		thumbRoot = self._getThumbRoot()
		for row in range(1, self.opTable.numRows):
			opItem = self._itemFromRow(self.opTable, row, thumbRoot)
			if opItem:
				items.append(opItem)
		return items

	def _getThumbRoot(self):
		thumbRoot = self.ownerComp.par.Thumbroot.eval()
		return thumbRoot or getattr(op, 'raytk', None)

	def _itemFromRow(self, table: DAT, row: int, thumbRoot: COMP | None) -> Optional['_OpItem']:
		text = ' '.join([
			table[row, 'name'].val,
			table[row, 'keywords'].val,
			table[row, 'shortcuts'].val,
		])
		opItem = _OpItem(
			shortName=table[row, 'name'].val,
			opType=table[row, 'opType'].val,
			path=table[row, 'path'].val,
			category=table[row, 'category'].val,
			displayCategory=table[row, 'displayCategory'].val or None,
			isAlpha=table[row, 'status'] == 'alpha',
			isBeta=table[row, 'status'] == 'beta',
			isDeprecated=table[row, 'status'] == 'deprecated',
			searchText=text,
		)
		thumb = self.opTable[row, 'thumb'].val
		if thumb and thumbRoot:
			top = thumbRoot.op(thumb)
			if top:
				opItem.thumbPath = top.path
		if opItem.isAlpha:
			opItem.status = 'alpha'
			if not ipar.uiState.Showalpha:
				return None
		elif opItem.isBeta:
			opItem.status = 'beta'
			if not ipar.uiState.Showbeta:
				return None
		elif opItem.isDeprecated:
			opItem.status = 'deprecated'
			if not ipar.uiState.Showdeprecated:
				return None
		else:
			opItem.status = ''
		return opItem

	def buildTreeTable(self, dat: DAT):
		dat.clear()
		dat.appendRow(['name', 'path', 'compPath', 'type', 'category', 'opType', 'status', 'thumb', 'searchText'])
		categoriesByName: dict[str, _CategoryItem] = {}
		useDisplayCategories = ipar.uiState.Usedisplaycategories
		allItems = self._getAllOpItems()
		for opItem in allItems:
			if useDisplayCategories:
				catName = opItem.displayCategory or opItem.category
			else:
				catName = opItem.category
			if catName not in categoriesByName:
				categoriesByName[catName] = _CategoryItem(name=catName)
			categoriesByName[catName].ops.append(opItem)
		for catName in sorted(categoriesByName.keys()):
			catItem = categoriesByName[catName]
			dat.appendRow([catItem.name, catItem.name, '', 'category', '', '', ''])
			for opItem in sorted(catItem.ops, key=lambda x: x.shortName):
				dat.appendRow([
					opItem.shortName,
					f"{catItem.name}/{opItem.shortName}",
					opItem.path,
					'op',
					catItem.name,
					opItem.opType,
					opItem.status,
					opItem.thumbPath or '',
					opItem.searchText or '',
				])

	def buildFlatTable(self, dat: DAT):
		dat.clear()
		dat.appendRow(['name', 'path', 'compPath', 'type', 'category', 'opType', 'status', 'thumb', 'searchText'])
		allItems = self._getAllOpItems()
		for opItem in sorted(allItems, key=lambda x: x.shortName):
			dat.appendRow([
				opItem.shortName,
				f"{opItem.category}/{opItem.shortName}",
				opItem.path,
				'op',
				opItem.category,
				opItem.opType,
				opItem.status,
				opItem.thumbPath or '',
				opItem.searchText or '',
			])

	def applyFilter(self):
		text = ipar.uiState.Filtertext.eval()
		if not text:
			self.flatLister.par.Filterstring = ''
			ipar.uiState.Flatmode.val = False
		else:
			self.flatLister.par.Filterstring = text
			self.flatLister.par.Filtercols = '4'
			ipar.uiState.Flatmode.val = True

	def clearFilterText(self):
		ipar.uiState.Filtertext.val = ''

	def onListCellClick(self, info: dict):
		rowData = info.get('rowData')
		rowObject = rowData and rowData.get('rowObject')
		opType = rowObject and rowObject.get('opType')
		if not opType:
			return
		# print('OP TYPE SELECTED:', opType)
		cell = self.opTable[opType, 0]
		if cell is None:
			return
		item = self._itemFromRow(self.opTable, cell.row, self._getThumbRoot())
		if item:
			ext.callbacks.DoCallback('onPickItem', {'path': item.path, 'opType': opType})

	@staticmethod
	def SetFilterToggles(
			alpha: bool | None = None,
			beta: bool | None = None,
			deprecated: bool | None = None,
	):
		if alpha is not None:
			ipar.uiState.Showalpha.val = alpha
		if beta is not None:
			ipar.uiState.Showbeta.val = beta
		if deprecated is not None:
			ipar.uiState.Showdeprecated.val = deprecated

	@staticmethod
	def SetViewOptions(
			statusChips: bool | None = None,
			displayCategories: bool | None = None,
	):
		if statusChips is not None:
			ipar.uiState.Showstatuschips.val = statusChips
		if displayCategories is not None:
			ipar.uiState.Usedisplaycategories.val = displayCategories

	@staticmethod
	def SetThumbToggle(showThumbs: bool):
		ipar.uiState.Showthumbs.val = showThumbs

	def Resetstate(self, _=None):
		ipar.uiState.Flatmode.val = ''
		ipar.uiState.Filtertext.val = ''

	def FocusFilterField(self):
		def _focus():
			self.ownerComp.op('filterTextField').setKeyboardFocus()
		run('args[0]()', _focus, delayFrames=10)

	def ExpandAll(self):
		self.treeLister.par.Expandall.pulse()

	def CollapseAll(self):
		self.treeLister.par.Collapseall.pulse()

	def onKeyboardShortcut(self, shortcutName: str):
		print(self.ownerComp, f'onKeyboardShortcut: {shortcutName}')
		ext.callbacks.DoCallback('onKeyboardShortcut', {'shortcut': shortcutName})

	def onListRollover(self, info: dict):
		# print(self.ownerComp, f'onListRollover: {info}')
		opType, path = self._resolveRow(info)
		ext.callbacks.DoCallback('onRolloverItem', {'path': path, 'opType': opType})

	@staticmethod
	def _resolveRow(info: dict) -> tuple[str | None, str | None]:
		comp = info.get('ownerComp')  # type: COMP | ListerExt | None
		data = getattr(comp, 'Data', None)
		if not data:
			return None, None
		row = info.get('row')
		if row is None or row < 0 or row >= len(data):
			return None, None
		rowData = data[row]
		rowObject = rowData.get('rowObject')
		if not rowObject:
			return None, None
		opType = rowObject.get('opType')
		if not opType:
			return None, None
		path = rowObject.get('compPath')
		return opType, path


@dataclass
class _OpItem:
	shortName: str
	opType: str
	path: str
	category: str
	displayCategory: str | None
	isAlpha: bool = False
	isBeta: bool = False
	isDeprecated: bool = False
	status: str = ''
	thumbPath: str | None = None
	searchText: str | None = None
	isOP = True

@dataclass
class _CategoryItem:
	name: str
	ops: list[_OpItem] = field(default_factory=list)
