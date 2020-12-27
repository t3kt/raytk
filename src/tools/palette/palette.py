from dataclasses import dataclass, field
from typing import Dict, List, Union, Optional
from raytkUtil import RaytkTags

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
	ipar.listConfig = _ListConfigPar()

# columns:
#  name
#  status icon

class Palette:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.itemLibrary = None  # type: Optional[_ItemLibrary]
		self.selItem = tdu.Dependency()  # value type _AnyItemT
		self.loadItems()

	@property
	def listComp(self) -> 'listCOMP':
		return self.ownerComp.op('list')

	@property
	def SelectedItem(self) -> 'Optional[_Item]':
		return self.selItem.val

	@SelectedItem.setter
	def SelectedItem(self, val: 'Optional[_Item]'):
		oldItem = self.selItem.val  # type: Optional[_AnyItemT]
		if oldItem:
			self._setRowHighlight(oldItem.row, (0, 0, 0, 0))
		print(self.ownerComp, f'setting selected item to: {val!r}')
		self.selItem.val = val
		if val:
			color = ipar.listConfig.Rolloverhighlightcolorr, ipar.listConfig.Rolloverhighlightcolorg, ipar.listConfig.Rolloverhighlightcolorb, 1
			self._setRowHighlight(val.row, color)
			self.listComp.scroll(val.row, 0)

	def loadItems(self):
		listComp = self.listComp
		opTable = self.ownerComp.op('opTable')  # type: DAT
		opHelpTable = self.ownerComp.op('opHelpTable')  # type: DAT
		self.itemLibrary = _ItemLibrary()
		self.itemLibrary.loadTables(opTable, opHelpTable)
		listComp.par.rows = len(self.itemLibrary.allItems)
		listComp.par.cols = 2
		listComp.par.reset.pulse()
		self.SelectedItem = None

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
			row = item.row + offset
		else:
			row = offset
		row = row % len(self.itemLibrary.allItems)
		self.SelectedItem = self._resolveRow(row)

	def onKeyboardShortcut(self, shortcutName: str):
		print(self.ownerComp, 'onKeyboardShortcut', shortcutName)
		if shortcutName == 'up':
			self._offsetSelection(-1)
		elif shortcutName == 'down':
			self._offsetSelection(1)

	def onKey(self, key: str, time, state):
		# print(self.ownerComp, 'onKey', key, 'time: ', time, 'state: ', state)
		pass

	def onInitCell(self, listComp: 'listCOMP', row: int, col: int, attribs: 'ListAttributes'):
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

	def onInitRow(self, listComp: 'listCOMP', row: int, attribs: 'ListAttributes'):
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

	def onInitCol(self, listComp: 'listCOMP', col: int, attribs: 'ListAttributes'):
		if col == 0:
			attribs.colStretch = True
		elif col == 1:
			attribs.colWidth = 30


	def onInitTable(self, listComp: 'listCOMP', attribs: 'ListAttributes'):
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
			listComp: 'listCOMP',
			row: int, col: int, coords: 'XYUVTuple',
			prevRow: int, prevCol: int, prevCoords: 'XYUVTuple'):
		# if prevRow >= 0:
		# 	color = 0, 0, 0, 0
		# 	self._setRowHighlight(prevRow, color)
		# if row >= 0:
		# 	# color = ipar.listConfig.Rolloverhighlightcolorr, ipar.listConfig.Rolloverhighlightcolorg, ipar.listConfig.Rolloverhighlightcolorb, 1
		# 	# self._setRowHighlight(row, color)
		# 	self.SelectedItem = self._resolveRow(row)
		pass

	def onSelect(
			self,
			listComp: 'listCOMP',
			startRow: int, startCol: int, startCoords: 'XYUVTuple',
			endRow: int, endCol: int, endCoords: 'XYUVTuple',
			start, end):
		item = self._resolveRow(endRow)
		# print(self.ownerComp, f'SELECT startRC: {startRow},{startCol}, endRC: {endRow},{endCol}, start: {start}, end: {end} \n{item}')
		self.SelectedItem = item
		pass

	def onRadio(
			self,
			listComp: 'listCOMP',
			row: int, col: int, prevRow: int, prevCol: int):
		pass

	def onFocus(
			self,
			listComp: 'listCOMP',
			row: int, col: int, prevRow: int, prevCol: int):
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
	row: Optional[int] = None

@dataclass
class _CategoryItem(_Item):
	ops: List['_OpItem'] = field(default_factory=list)

@dataclass
class _OpItem(_Item):
	pass

_AnyItemT = Union[_CategoryItem, _OpItem]

class _ItemLibrary:
	allItems: List[_AnyItemT]
	categories: Dict[str, _CategoryItem]
	ops: List[_OpItem]

	def __init__(self):
		self.allItems = []
		self.categories = {}
		self.ops = []

	def loadTables(self, opTable: 'DAT', opHelpTable: 'DAT'):
		self.allItems = []
		self.categories = {}
		self.ops = []

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
			if categoryName in self.categories:
				self.categories[categoryName].ops.append(opItem)
			else:
				self.categories[categoryName] = _CategoryItem(
					shortName=categoryName, ops=[opItem])
			self.ops.append(opItem)

		self.ops.sort(key=lambda o: o.path)
		for categoryName in sorted(self.categories.keys()):
			category = self.categories[categoryName]
			category.row = len(self.allItems)
			self.allItems.append(category)
			category.ops.sort(key=lambda o: o.path)
			category.isAlpha = all([o.isAlpha for o in category.ops])
			category.isBeta = all([o.isBeta for o in category.ops])
			category.isDeprecated = all([o.isDeprecated for o in category.ops])
			for o in category.ops:
				o.row = len(self.allItems)
				self.allItems.append(o)

	def itemForRow(self, row: int) -> 'Optional[_AnyItemT]':
		if row < 0 or row >= len(self.allItems):
			return None
		return self.allItems[row]
