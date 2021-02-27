from dataclasses import dataclass, field
from typing import Dict, List, Union, Optional
from raytkUtil import RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Par(ParCollection):
		Showedit: 'BoolParamT'
	class _COMP(panelCOMP):
		par: _Par

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

		Categorybgcolorr: 'FloatParamT'
		Categorybgcolorg: 'FloatParamT'
		Categorybgcolorb: 'FloatParamT'

		Categorytextcolorr: 'FloatParamT'
		Categorytextcolorg: 'FloatParamT'
		Categorytextcolorb: 'FloatParamT'

		Buttonbgcolorr: 'FloatParamT'
		Buttonbgcolorg: 'FloatParamT'
		Buttonbgcolorb: 'FloatParamT'

		Buttonrolloverbgcolorr: 'FloatParamT'
		Buttonrolloverbgcolorg: 'FloatParamT'
		Buttonrolloverbgcolorb: 'FloatParamT'

	class _UIStatePar(ParCollection):
		Showalpha: 'BoolParamT'
		Showbeta: 'BoolParamT'
		Showdeprecated: 'BoolParamT'
		Showhelp: 'BoolParamT'
		Pinopen: 'BoolParamT'

	ipar.listConfig = _ListConfigPar()
	ipar.uiState = _UIStatePar()
	from _stubs.TDCallbacksExt import CallbacksExt
	ext.callbacks = CallbacksExt(None)

class OpPicker:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.itemLibrary = _ItemLibrary()
		self.selItem = tdu.Dependency()  # value type _AnyItemT
		self.filterText = ''
		self.isOpen = tdu.Dependency(False)
		self.Loaditems()

	@property
	def opTable(self) -> 'Optional[DAT]':
		return RaytkContext().opTable()

	@property
	def opHelpTable(self) -> 'Optional[DAT]':
		return RaytkContext().opHelpTable()

	@property
	def _listComp(self) -> 'listCOMP':
		return self.ownerComp.op('list')

	@property
	def _filterTextWidget(self) -> 'widgetCOMP':
		return self.ownerComp.op('filterText_textfield')

	@property
	def _filterTextField(self) -> 'fieldCOMP':
		widget = self._filterTextWidget
		if widget:
			return op(widget.par.Stringfield0).op('./field')

	@property
	def _showEdit(self):
		return bool(self.ownerComp.par.Showedit)

	@property
	def SelectedItem(self) -> 'Optional[_AnyItemT]':
		return self.selItem.val

	def _selectItem(self, item: 'Optional[_AnyItemT]', scroll=False):
		oldItem = self.selItem.val  # type: Optional[_AnyItemT]
		if oldItem == item:
			return
		if oldItem:
			row = self.itemLibrary.rowForItem(oldItem)
			self._setRowHighlight(row, False)
		# print(self.ownerComp, f'setting selected item to: {item!r}')
		self.selItem.val = item
		if item:
			row = self.itemLibrary.rowForItem(item)
			self._setRowHighlight(row, True)
			if scroll:
				self._listComp.scroll(row, 0)

	def FocusFilterField(self):
		filterField = self._filterTextField
		if filterField:
			run('args[0]()', filterField.setKeyboardFocus, delayFrames=10)

	def Resetstate(self, _=None):
		self.refreshList()
		self._selectItem(None)
		self.clearFilterText()
		self.isOpen.val = False

	def Loaditems(self, _=None):
		opTable = self.ownerComp.op('opTable')  # type: DAT
		opHelpTable = self.ownerComp.op('opHelpTable')  # type: DAT
		self.itemLibrary.loadTables(opTable, opHelpTable)
		self.refreshList()
		self._selectItem(None)

	def refreshList(self):
		listComp = self._listComp
		listComp.par.rows = self.itemLibrary.currentItemCount
		listComp.par.cols = 4 if self._showEdit else 3
		listComp.par.reset.pulse()

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
		self._selectItem(self.itemLibrary.itemForRow(row % self.itemLibrary.currentItemCount), scroll=True)

	def setFilterText(self, text: str):
		self.filterText = (text or '').strip()
		self._applyFilter()

	def clearFilterText(self):
		self.filterText = ''
		self._filterTextWidget.par.Value0 = ''
		self._applyFilter()

	def _applyFilter(self):
		item = self.SelectedItem
		filt = _Filter(
			self.filterText,
			alpha=ipar.uiState.Showalpha.eval(),
			beta=ipar.uiState.Showbeta.eval(),
			deprecated=ipar.uiState.Showdeprecated.eval(),
		)
		self.itemLibrary.applyFilter(filt)
		if item:
			row = self.itemLibrary.rowForItem(item)
			if row < 0:
				self._selectItem(None)
			else:
				self._setRowHighlight(row, True)
		self.refreshList()

	def onFilterSettingChange(self):
		self._applyFilter()

	def onKeyboardShortcut(self, shortcutName: str):
		print(self.ownerComp, f'onKeyboardShortcut: {shortcutName}')
		if shortcutName == 'up':
			self._offsetSelection(-1)
		elif shortcutName == 'down':
			self._offsetSelection(1)
		elif shortcutName == 'enter':
			self.onPickItem()
		else:
			ext.callbacks.DoCallback('onKeyboardShortcut', {'shortcut': shortcutName})

	def onPickItem(self):
		item = self.SelectedItem
		if not item:
			item = self.itemLibrary.firstOpItem
			if not item:
				return
			else:
				self._selectItem(item)
		ext.callbacks.DoCallback('onPickItem', {'item': item})

	def onEditItem(self):
		item = self.SelectedItem
		if not item:
			return
		ext.callbacks.DoCallback('onEditItem', {'item': item})

	def _printAndStatus(self, msg):
		print(self.ownerComp, msg)
		ui.status = msg

	def onInitCell(self, row: int, col: int, attribs: 'ListAttributes'):
		item = self.itemLibrary.itemForRow(row)
		if not item:
			return
		if col == 1:
			attribs.text = item.shortName
		if isinstance(item, PickerCategoryItem):
			if col == 0:
				if item.collapsed:
					attribs.top = self.ownerComp.op('expandIcon')
				else:
					attribs.top = self.ownerComp.op('collapseIcon')
				attribs.bgColor = ipar.listConfig.Buttonbgcolorr, ipar.listConfig.Buttonbgcolorg, ipar.listConfig.Buttonbgcolorb, 1
			elif col == 1:
				attribs.textOffsetX = 5
		elif isinstance(item, PickerOpItem):
			if col == 1:
				attribs.textOffsetX = 20
			elif col == 2:
				if item.isAlpha:
					attribs.top = self.ownerComp.op('alphaIcon')
				elif item.isBeta:
					attribs.top = self.ownerComp.op('betaIcon')
				elif item.isDeprecated:
					attribs.top = self.ownerComp.op('deprecatedIcon')
			elif col == 3:
				attribs.top = self.ownerComp.op('editIcon')
				attribs.bgColor = ipar.listConfig.Buttonbgcolorr, ipar.listConfig.Buttonbgcolorg, ipar.listConfig.Buttonbgcolorb, 1

	def onInitRow(self, row: int, attribs: 'ListAttributes'):
		item = self.itemLibrary.itemForRow(row)
		if not item:
			return
		if item.isAlpha or item.isBeta or item.isDeprecated:
			attribs.fontItalic = True
		if isinstance(item, PickerCategoryItem):
			attribs.textColor = ipar.listConfig.Categorytextcolorr, ipar.listConfig.Categorytextcolorg, ipar.listConfig.Categorytextcolorb, 1
			attribs.bgColor = ipar.listConfig.Categorybgcolorr, ipar.listConfig.Categorybgcolorg, ipar.listConfig.Categorybgcolorb, 1
		if item.isAlpha:
			attribs.textColor = ipar.listConfig.Alphacolorr, ipar.listConfig.Alphacolorg, ipar.listConfig.Alphacolorb
		elif item.isBeta:
			attribs.textColor = ipar.listConfig.Betacolorr, ipar.listConfig.Betacolorg, ipar.listConfig.Betacolorb
		elif item.isDeprecated:
			attribs.textColor = ipar.listConfig.Deprecatedcolorr, ipar.listConfig.Deprecatedcolorg, ipar.listConfig.Deprecatedcolorb

	@staticmethod
	def onInitCol(col: int, attribs: 'ListAttributes'):
		if col == 0:
			attribs.colWidth = 26
		elif col == 1:
			attribs.colStretch = True
		elif col == 2:
			attribs.colWidth = 30
		elif col == 3:
			attribs.colWidth = 26

	@staticmethod
	def onInitTable(attribs: 'ListAttributes'):
		attribs.rowHeight = 26
		attribs.bgColor = ipar.listConfig.Bgcolorr, ipar.listConfig.Bgcolorg, ipar.listConfig.Bgcolorb
		attribs.textColor = ipar.listConfig.Textcolorr, ipar.listConfig.Textcolorg, ipar.listConfig.Textcolorb
		attribs.fontFace = 'Roboto'
		attribs.fontSizeX = 18
		attribs.textJustify = JustifyType.CENTERLEFT

	def _setButtonHighlight(self, row: int, col: int, highlight: bool):
		if row < 0 or col < 0:
			return
		attribs = self._listComp.cellAttribs[row, col]
		if not attribs:
			return
		if highlight:
			color = ipar.listConfig.Buttonrolloverbgcolorr, ipar.listConfig.Buttonrolloverbgcolorg, ipar.listConfig.Buttonrolloverbgcolorb, 1
		else:
			color = ipar.listConfig.Buttonbgcolorr, ipar.listConfig.Buttonbgcolorg, ipar.listConfig.Buttonbgcolorb, 1
		attribs.bgColor = color

	def _setRowHighlight(self, row: int, selected: bool):
		if row < 0:
			return
		# print(self.ownerComp, f'setRowHighlight(row: {row!r}, sel: {selected!r})')
		if selected:
			color = ipar.listConfig.Rolloverhighlightcolorr, ipar.listConfig.Rolloverhighlightcolorg, ipar.listConfig.Rolloverhighlightcolorb, 1
		else:
			color = 0, 0, 0, 0
		listComp = self._listComp
		rowAttribs = listComp.rowAttribs[row]
		if rowAttribs:
			rowAttribs.topBorderOutColor = color
			rowAttribs.bottomBorderOutColor = color
		cellAttribs = listComp.cellAttribs[row, 0]
		if cellAttribs:
			cellAttribs.leftBorderInColor = color
		cellAttribs = listComp.cellAttribs[row, 3 if self._showEdit else 2]
		if cellAttribs:
			cellAttribs.rightBorderOutColor = color

	def onRollover(
			self,
			row: int, col: int,
			prevRow: int, prevCol: int):
		# note for performance: this gets called frequently as the mouse moves even within a single cell
		if row == prevRow and col == prevCol:
			return
		if row >= 0:
			item = self.itemLibrary.itemForRow(row)
			self._selectItem(item)
			if col == 3 and isinstance(item, PickerOpItem):
				self._setButtonHighlight(row, col, True)
		if prevRow >= 0 and prevCol == 3:
			item = self.itemLibrary.itemForRow(prevRow)
			if isinstance(item, PickerOpItem):
				self._setButtonHighlight(prevRow, prevCol, False)

	def _toggleCategoryExpansion(self, item: 'PickerCategoryItem'):
		item.collapsed = not item.collapsed
		self._applyFilter()
		if item.collapsed:
			self._selectItem(item, scroll=False)
		elif item.ops:
			self._selectItem(item.ops[0], scroll=False)

	def onSelect(
			self,
			startRow: int, startCol: int,
			endRow: int, endCol: int,
			start: bool, end: bool):
		item = self.itemLibrary.itemForRow(endRow)
		# print(self.ownerComp, f'SELECT startRC: {startRow},{startCol}, endRC: {endRow},{endCol}, start: {start}, end: {end} \n{item}')
		self._selectItem(item)
		if end:
			if item.isCategory:
				self._toggleCategoryExpansion(item)
			elif endCol == 3 and self._showEdit:
				self.onEditItem()
			else:
				self.onPickItem()

	def onRadio(self, row: int, col: int, prevRow: int, prevCol: int):
		pass

	def onFocus(self, row: int, col: int, prevRow: int, prevCol: int):
		pass

@dataclass
class PickerItem:
	shortName: str
	helpSummary: Optional[str] = None
	status: Optional[str] = None
	isAlpha: bool = False
	isBeta: bool = False
	isDeprecated: bool = False
	path: Optional[str] = None
	opType: Optional[str] = None
	categoryName: Optional[str] = None

	isOP = None
	isCategory = None

@dataclass
class PickerCategoryItem(PickerItem):
	ops: List['PickerOpItem'] = field(default_factory=list)
	collapsed = False
	isOP = False
	isCategory = True

@dataclass
class PickerOpItem(PickerItem):
	words: List[str] = field(default_factory=list)
	isOP = True
	isCategory = False

	def matches(self, filt: '_Filter'):
		if self.isAlpha and not filt.alpha:
			return False
		if self.isBeta and not filt.beta:
			return False
		if self.isDeprecated and not filt.deprecated:
			return False
		if not filt.text:
			return True
		filtText = filt.text.lower()
		if filtText in self.shortName.lower():
			return True
		if not self.words:
			return False
		for w, f in zip(self.words, filtText):
			if w[0] != f:
				return False
		return True

_AnyItemT = Union[PickerCategoryItem, PickerOpItem]

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
	categories: List[PickerCategoryItem]
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

	@property
	def firstOpItem(self) -> 'Optional[PickerOpItem]':
		for item in self._currentItemList:
			if item.isOP:
				return item

	def loadTables(self, opTable: 'DAT', opHelpTable: 'DAT'):
		self.categories = []
		self.filteredItems = None
		categoriesByName = {}  # type: Dict[str, PickerCategoryItem]

		for row in range(1, opTable.numRows):
			shortName = str(opTable[row, 'name'])
			path = str(opTable[row, 'path'])
			status = str(opTable[row, 'status'])
			categoryName = str(opTable[row, 'category'])
			opItem = PickerOpItem(
				shortName=shortName,
				path=path,
				opType=str(opTable[row, 'opType']),
				categoryName=categoryName,
				status=status,
				isAlpha=status == 'alpha',
				isBeta=status == 'beta',
				isDeprecated=status == 'deprecated',
				helpSummary=str(opHelpTable[path, 'summary'] or ''),
			)
			words = _splitCamelCase(shortName)
			opItem.words = [w.lower() for w in words]
			if categoryName in categoriesByName:
				categoriesByName[categoryName].ops.append(opItem)
			else:
				categoriesByName[categoryName] = PickerCategoryItem(
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
				if not category.collapsed:
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
		self.filteredItems = self._buildFlatList(filt)

def _splitCamelCase(s: str):
	splits = [i for i, e in enumerate(s) if e.isupper()] + [len(s)]
	if not splits:
		return [s]
	splits = [0] + splits
	return [s[x:y] for x, y in zip(splits, splits[1:])]
