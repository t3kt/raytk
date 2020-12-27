from dataclasses import dataclass, field
from typing import Dict, List, Union, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _ListConfigPar(ParCollection):
		Bgcolorr: 'FloatParamT'
		Bgcolorg: 'FloatParamT'
		Bgcolorb: 'FloatParamT'

		Textcolorr: 'FloatParamT'
		Textcolorg: 'FloatParamT'
		Textcolorb: 'FloatParamT'

		Alphacolorr: 'FloatParamT'
		Alphacolorg: 'FloatParamT'
		Alphacolorb: 'FloatParamT'

		Betacolorr: 'FloatParamT'
		Betacolorg: 'FloatParamT'
		Betacolorb: 'FloatParamT'

		Deprecatedcolorr: 'FloatParamT'
		Deprecatedcolorg: 'FloatParamT'
		Deprecatedcolorb: 'FloatParamT'

		Rolloverhighlightcolorr: 'FloatParamT'
		Rolloverhighlightcolorg: 'FloatParamT'
		Rolloverhighlightcolorb: 'FloatParamT'

	class _UIStatePar(ParCollection):
		Showalpha: 'BoolParamT'
		Showbeta: 'BoolParamT'
		Showdeprecated: 'BoolParamT'

	ipar.listConfig = _ListConfigPar()
	ipar.uiState = _UIStatePar()

# columns:
#  name
#  status icon

class Palette:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.itemLibrary = _ItemLibrary()
		self.selItem = tdu.Dependency()  # value type _AnyItemT
		self.filterText = ''
		self.loadItems()

	@property
	def listComp(self) -> 'listCOMP':
		return self.ownerComp.op('list')

	@property
	def SelectedItem(self) -> 'Optional[_AnyItemT]':
		return self.selItem.val

	@SelectedItem.setter
	def SelectedItem(self, val: 'Optional[_AnyItemT]'):
		oldItem = self.selItem.val  # type: Optional[_AnyItemT]
		if oldItem:
			row = self.itemLibrary.rowForItem(oldItem)
			self._setRowHighlight(row, (0, 0, 0, 0))
		# print(self.ownerComp, f'setting selected item to: {val!r}')
		self.selItem.val = val
		if val:
			color = ipar.listConfig.Rolloverhighlightcolorr, ipar.listConfig.Rolloverhighlightcolorg, ipar.listConfig.Rolloverhighlightcolorb, 1
			row = self.itemLibrary.rowForItem(val)
			self._setRowHighlight(row, color)
			# self.listComp.scroll(row, 0)

	def loadItems(self):
		opTable = self.ownerComp.op('opTable')  # type: DAT
		opHelpTable = self.ownerComp.op('opHelpTable')  # type: DAT
		self.itemLibrary.loadTables(opTable, opHelpTable)
		self.refreshList()
		self.SelectedItem = None

	def refreshList(self):
		listComp = self.listComp
		listComp.par.rows = self.itemLibrary.currentItemCount
		listComp.par.cols = 2
		listComp.par.reset.pulse()

	def resetState(self):
		self.refreshList()
		self.SelectedItem = None
		self.filterText = ''
		self.ownerComp.op('filterText_textfield').par.Value0 = ''

	def _resolveRow(self, row: int) -> 'Optional[_AnyItemT]':
		if not self.itemLibrary:
			return None
		item = self.itemLibrary.itemForRow(row)
		if not item:
			print(self.ownerComp, f'Unable to find item for row: {row!r}')
		return item

	def _offsetSelection(self, offset: int):
		if not self.itemLibrary:
			return
		item = self.SelectedItem
		if item:
			row = self.itemLibrary.rowForItem(item)
			if row == -1:
				row = offset
			else:
				row += offset
		else:
			row = offset
		self.SelectedItem = self.itemLibrary.itemForRow(row % self.itemLibrary.currentItemCount)

	def setFilterText(self, text: str):
		self.filterText = (text or '').strip()
		self._applyFilter()

	def _applyFilter(self):
		filt = _Filter(
			self.filterText,
			alpha=ipar.uiState.Showalpha.eval(),
			beta=ipar.uiState.Showbeta.eval(),
			deprecated=ipar.uiState.Showdeprecated.eval(),
		)
		self.itemLibrary.applyFilter(filt)
		self.refreshList()

	def onFilterSettingChange(self):
		self._applyFilter()

	def onKeyboardShortcut(self, shortcutName: str):
		# print(self.ownerComp, 'onKeyboardShortcut', shortcutName)
		if shortcutName == 'up':
			self._offsetSelection(-1)
		elif shortcutName == 'down':
			self._offsetSelection(1)

	def onKey(self, key: str, time, state):
		# print(self.ownerComp, 'onKey', key, 'time: ', time, 'state: ', state)
		pass

	def onInitCell(self, row: int, col: int, attribs: 'ListAttributes'):
		item = self._resolveRow(row)
		if not item:
			return
		if col == 0:
			attribs.text = item.shortName
		if isinstance(item, _CategoryItem):
			pass
		elif isinstance(item, _OpItem):
			if col == 0:
				attribs.textOffsetX = 20
			elif col == 1:
				if item.isAlpha:
					attribs.top = self.ownerComp.op('alphaIcon')
				elif item.isBeta:
					attribs.top = self.ownerComp.op('betaIcon')
				elif item.isDeprecated:
					attribs.top = self.ownerComp.op('deprecatedIcon')

	def onInitRow(self, row: int, attribs: 'ListAttributes'):
		item = self._resolveRow(row)
		if not item:
			return
		if item.isAlpha or item.isBeta or item.isDeprecated:
			attribs.fontItalic = True
		if item.isAlpha:
			attribs.textColor = ipar.listConfig.Alphacolorr, ipar.listConfig.Alphacolorg, ipar.listConfig.Alphacolorb
		elif item.isBeta:
			attribs.textColor = ipar.listConfig.Betacolorr, ipar.listConfig.Betacolorg, ipar.listConfig.Betacolorb
		elif item.isDeprecated:
			attribs.textColor = ipar.listConfig.Deprecatedcolorr, ipar.listConfig.Deprecatedcolorg, ipar.listConfig.Deprecatedcolorb

	def onInitCol(self, col: int, attribs: 'ListAttributes'):
		if col == 0:
			attribs.colStretch = True
		elif col == 1:
			attribs.colWidth = 30


	def onInitTable(self, attribs: 'ListAttributes'):
		attribs.rowHeight = 26
		attribs.bgColor = ipar.listConfig.Bgcolorr, ipar.listConfig.Bgcolorg, ipar.listConfig.Bgcolorb
		attribs.textColor = ipar.listConfig.Textcolorr, ipar.listConfig.Textcolorg, ipar.listConfig.Textcolorb
		attribs.fontFace = 'Roboto'
		attribs.fontSizeX = 18
		attribs.textJustify = JustifyType.CENTERLEFT

	def _setRowHighlight(self, row: int, color: tuple):
		if row < 0:
			return
		listComp = self.listComp
		rowAttribs = listComp.rowAttribs[row]
		rowAttribs.topBorderInColor = color
		rowAttribs.bottomBorderInColor = color
		cellAttribs = listComp.cellAttribs[row, 0]
		cellAttribs.leftBorderInColor = color
		cellAttribs = listComp.cellAttribs[row, 1]
		cellAttribs.rightBorderInColor = color

	def onRollover(
			self,
			row: int, col: int, coords: 'XYUVTuple',
			prevRow: int, prevCol: int, prevCoords: 'XYUVTuple'):
		# if prevRow >= 0:
		# 	color = 0, 0, 0, 0
		# 	self._setRowHighlight(prevRow, color)
		if row >= 0:
			# color = ipar.listConfig.Rolloverhighlightcolorr, ipar.listConfig.Rolloverhighlightcolorg, ipar.listConfig.Rolloverhighlightcolorb, 1
			# self._setRowHighlight(row, color)
			self.SelectedItem = self.itemLibrary.itemForRow(row)
		pass

	def onSelect(
			self,
			startRow: int, startCol: int, startCoords: 'XYUVTuple',
			endRow: int, endCol: int, endCoords: 'XYUVTuple',
			start, end):
		item = self.itemLibrary.itemForRow(endRow)
		# print(self.ownerComp, f'SELECT startRC: {startRow},{startCol}, endRC: {endRow},{endCol}, start: {start}, end: {end} \n{item}')
		self.SelectedItem = item
		pass

	def onRadio(self, row: int, col: int, prevRow: int, prevCol: int):
		pass

	def onFocus(self, row: int, col: int, prevRow: int, prevCol: int):
		pass

@dataclass
class _Item:
	shortName: str
	helpSummary: Optional[str] = None
	status: Optional[str] = None
	isAlpha: bool = False
	isBeta: bool = False
	isDeprecated: bool = False
	path: Optional[str] = None
	opType: Optional[str] = None
	categoryName: Optional[str] = None

@dataclass
class _CategoryItem(_Item):
	ops: List['_OpItem'] = field(default_factory=list)

@dataclass
class _OpItem(_Item):
	def matches(self, filt: '_Filter'):
		if self.isAlpha and not filt.alpha:
			return False
		if self.isBeta and not filt.beta:
			return False
		if self.isDeprecated and not filt.deprecated:
			return False
		if not filt.text:
			return True
		if filt.text in self.shortName.lower():
			return True
		# if filt.text in self.categoryName.lower():
		# 	return True
		return False

_AnyItemT = Union[_CategoryItem, _OpItem]

@dataclass
class _Filter:
	text: Optional[str] = None
	alpha: bool = False
	beta: bool = False
	deprecated: bool = False

	def __bool__(self):
		return bool(self.text or not self.alpha or not self.beta or not self.deprecated)

class _ItemLibrary:
	allItems: List[_AnyItemT]
	categories: List[_CategoryItem]
	filteredItems: Optional[List[_AnyItemT]]

	def __init__(self):
		self.allItems = []
		self.categories = []
		self.filteredItems = None

	@property
	def _currentItemList(self):
		return self.filteredItems if self.filteredItems is not None else self.allItems

	@property
	def currentItemCount(self):
		return len(self._currentItemList)

	def loadTables(self, opTable: 'DAT', opHelpTable: 'DAT'):
		self.categories = []
		self.filteredItems = None
		categoriesByName = {}  # type: Dict[str, _CategoryItem]

		for row in range(1, opTable.numRows):
			path = str(opTable[row, 'path'])
			status = str(opTable[row, 'status'])
			categoryName = str(opTable[row, 'category'])
			opItem = _OpItem(
				shortName=str(opTable[row, 'name']),
				path=path,
				opType=str(opTable[row, 'opType']),
				categoryName=categoryName,
				status=status,
				isAlpha=status == 'alpha',
				isBeta=status == 'beta',
				isDeprecated=status == 'deprecated',
				helpSummary=str(opHelpTable[path, 'summary'] or ''),
			)
			if categoryName in categoriesByName:
				categoriesByName[categoryName].ops.append(opItem)
			else:
				categoriesByName[categoryName] = _CategoryItem(
					shortName=categoryName, ops=[opItem])

		for categoryName in sorted(categoriesByName.keys()):
			category = categoriesByName[categoryName]
			self.categories.append(category)
			category.ops.sort(key=lambda o: o.path)
			category.isAlpha = all([o.isAlpha for o in category.ops])
			category.isBeta = all([o.isBeta for o in category.ops])
			category.isDeprecated = all([o.isDeprecated for o in category.ops])

		self.allItems = self._buildFlatList(None)

	def _buildFlatList(self, filt: 'Optional[_Filter]') -> 'List[_AnyItemT]':
		flatItems = []
		for category in self.categories:
			if not filt:
				matchedOps = category.ops
			else:
				matchedOps = [
					o
					for o in category.ops
					if o.matches(filt)
				]
			if matchedOps:
				flatItems.append(category)
				flatItems += matchedOps
		return flatItems

	def itemForRow(self, row: int) -> 'Optional[_AnyItemT]':
		items = self._currentItemList
		if not items or row < 0 or row >= len(items):
			return None
		return items[row]

	def rowForItem(self, item: 'Optional[_AnyItemT]') -> int:
		if not item:
			return -1
		items = self._currentItemList
		if not items:
			return -1
		try:
			return items.index(item)
		except ValueError:
			return -1

	def applyFilter(self, filt: 'Optional[_Filter]'):
		if not filt:
			self.filteredItems = None
		else:
			self.filteredItems = self._buildFlatList(filt)
