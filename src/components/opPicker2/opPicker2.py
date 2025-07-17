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
			opItem.thumbPath = thumbRoot.op(thumb).path
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
