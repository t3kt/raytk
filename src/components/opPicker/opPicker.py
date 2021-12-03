from dataclasses import dataclass, field
from typing import Dict, List, Union, Optional, Tuple
from raytkUtil import RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Par(ParCollection):
		Showedit: 'BoolParamT'
		Thumbsize: 'IntParamT'
		Thumbroot: 'OPParamT'
	class _COMP(panelCOMP):
		par: _Par

	class _UIStatePar(ParCollection):
		Showalpha: 'BoolParamT'
		Showbeta: 'BoolParamT'
		Showdeprecated: 'BoolParamT'
		Showhelp: 'BoolParamT'
		Showthumbs: 'BoolParamT'
		Pinopen: 'BoolParamT'

	ipar.listConfig = ParCollection()
	ipar.uiState = _UIStatePar()
	from _stubs.TDCallbacksExt import CallbacksExt
	ext.callbacks = CallbacksExt(None)

def _configColor(name: str) -> 'Tuple[Par, Par, Par, int]':
	p = ipar.listConfig
	return p[name + 'r'], p[name + 'g'], p[name + 'b'], 1

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

	@staticmethod
	def SetFilterToggles(
			alpha: 'Optional[bool]' = None,
			beta: 'Optional[bool]' = None,
			deprecated: 'Optional[bool]' = None,
	):
		if alpha is not None:
			ipar.uiState.Showalpha = alpha
		if beta is not None:
			ipar.uiState.Showbeta = beta
		if deprecated is not None:
			ipar.uiState.Showdeprecated = deprecated

	def Loaditems(self, _=None):
		opTable = self.ownerComp.op('opTable')  # type: DAT
		opHelpTable = self.ownerComp.op('opHelpTable')  # type: DAT
		self.itemLibrary.loadTables(opTable, opHelpTable)
		self.refreshList()
		self._applyFilter()
		self._selectItem(None)

	def refreshList(self):
		listComp = self._listComp
		listComp.par.rows = self.itemLibrary.currentItemCount
		layout = self._getLayout()
		listComp.par.cols = layout.numCols
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

	def onUIStateChange(self, par: 'Par'):
		if par.name in ('Showalpha', 'Showbeta', 'Showdeprecated'):
			self.onFilterSettingChange()
		elif par.name == 'Showthumbs':
			self.refreshList()

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
		layout = self._getLayout()
		if col == layout.labelCol:
			attribs.text = item.shortName
		if isinstance(item, PickerCategoryItem):
			if col == layout.toggleCol:
				if item.collapsed:
					attribs.top = self.ownerComp.op('expandIcon')
				else:
					attribs.top = self.ownerComp.op('collapseIcon')
				attribs.bgColor = _configColor('Buttonbgcolor')
			elif col == layout.labelCol:
				attribs.textOffsetX = 5
		elif isinstance(item, PickerOpItem):
			if col == layout.labelCol:
				attribs.textOffsetX = 20
			elif col == layout.statusCol:
				if item.isAlpha:
					attribs.top = self.ownerComp.op('alphaIcon')
				elif item.isBeta:
					attribs.top = self.ownerComp.op('betaIcon')
				elif item.isDeprecated:
					attribs.top = self.ownerComp.op('deprecatedIcon')
			elif col == layout.editCol:
				attribs.top = self.ownerComp.op('editIcon')
				attribs.bgColor = _configColor('Bgcolor')
			elif col == layout.thumbCol:
				thumbRoot = self.ownerComp.par.Thumbroot.eval()
				if thumbRoot and item.thumbPath:
					attribs.top = thumbRoot.op(item.thumbPath) or ''

	def onInitRow(self, row: int, attribs: 'ListAttributes'):
		item = self.itemLibrary.itemForRow(row)
		if not item:
			return
		layout = self._getLayout()
		if item.isAlpha or item.isBeta or item.isDeprecated:
			attribs.fontItalic = True
		if isinstance(item, PickerCategoryItem):
			attribs.rowHeight = layout.catRowHeight
			attribs.textColor = _configColor('Categorytextcolor')
			attribs.bgColor = _configColor('Categorybgcolor')
		elif isinstance(item, PickerOpItem):
			attribs.rowHeight = layout.opRowHeight
		if item.isAlpha:
			attribs.textColor = _configColor('Alphacolor')
		elif item.isBeta:
			attribs.textColor = _configColor('Betacolor')
		elif item.isDeprecated:
			attribs.textColor = _configColor('Deprecatedcolor')

	def onInitCol(self, col: int, attribs: 'ListAttributes'):
		if col is None:
			return
		layout = self._getLayout()
		if col == layout.toggleCol:
			attribs.colWidth = layout.toggleColWidth
		elif col == layout.labelCol:
			attribs.colStretch = True
		elif col == layout.statusCol:
			attribs.colWidth = layout.statusColWidth
		elif col == layout.editCol:
			attribs.colWidth = layout.opRowHeight  # so icons end up square
		elif col == layout.thumbCol:
			attribs.colWidth = layout.thumbColWidth

	@staticmethod
	def onInitTable(attribs: 'ListAttributes'):
		attribs.bgColor = _configColor('Bgcolor')
		attribs.textColor = _configColor('Textcolor')
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
			color = _configColor('Buttonrolloverbgcolor')
		else:
			color = _configColor('Buttonbgcolor')
		attribs.bgColor = color

	def _setRowHighlight(self, row: int, selected: bool):
		if row < 0:
			return
		# print(self.ownerComp, f'setRowHighlight(row: {row!r}, sel: {selected!r})')
		if selected:
			color = _configColor('Rolloverhighlightcolor')
		else:
			color = 0, 0, 0, 0
		listComp = self._listComp
		layout = self._getLayout()
		rowAttribs = listComp.rowAttribs[row]
		if rowAttribs:
			rowAttribs.topBorderOutColor = color
			rowAttribs.bottomBorderOutColor = color
		cellAttribs = listComp.cellAttribs[row, 0]
		if cellAttribs:
			cellAttribs.leftBorderInColor = color
		cellAttribs = listComp.cellAttribs[row, layout.numCols - 1]
		if cellAttribs:
			cellAttribs.rightBorderOutColor = color

	def onRollover(
			self,
			row: int, col: int,
			prevRow: int, prevCol: int):
		# note for performance: this gets called frequently as the mouse moves even within a single cell
		if row == prevRow and col == prevCol:
			return
		layout = self._getLayout()
		item = None
		if row >= 0:
			item = self.itemLibrary.itemForRow(row)
			self._selectItem(item)
			if col == layout.editCol and isinstance(item, PickerOpItem):
				self._setButtonHighlight(row, col, True)
		if prevRow >= 0 and prevCol == layout.editCol:
			item = self.itemLibrary.itemForRow(prevRow)
			if isinstance(item, PickerOpItem):
				self._setButtonHighlight(prevRow, prevCol, False)
		ext.callbacks.DoCallback('onRolloverItem', {'item': item})

	def _toggleCategoryExpansion(self, item: 'PickerCategoryItem'):
		item.collapsed = not item.collapsed
		self._applyFilter()
		if item.collapsed:
			self._selectItem(item, scroll=False)
		elif item.ops:
			self._selectItem(item.ops[0], scroll=False)

	def onSelect(self, endRow: int, endCol: int, end: bool):
		item = self.itemLibrary.itemForRow(endRow)
		self._selectItem(item)
		if not end:
			return
		layout = self._getLayout()
		if item.isCategory:
			self._toggleCategoryExpansion(item)
		elif endCol == layout.editCol and layout.editCol is not None:
			self.onEditItem()
		else:
			self.onPickItem()

	def onRadio(self, row: int, col: int, prevRow: int, prevCol: int):
		pass

	def onFocus(self, row: int, col: int, prevRow: int, prevCol: int):
		pass

	def _getLayout(self):
		showEdit = self._showEdit
		layout = _Layout(
			toggleCol=0,
			labelCol=1,
			statusCol=2,
			editCol=3 if showEdit else None,
			thumbCol=None,
			numCols=4 if showEdit else 3,
			thumbColWidth=self.ownerComp.par.Thumbsize.eval(),
		)
		if ipar.uiState.Showthumbs:
			layout.thumbCol = layout.numCols
			layout.numCols += 1
			thumbSize = int(self.ownerComp.par.Thumbsize)
			layout.opRowHeight = thumbSize
			layout.editColWidth = thumbSize
			layout.thumbColWidth = thumbSize
			layout.statusColWidth = thumbSize
		return layout

@dataclass
class _Layout:
	toggleCol: Optional[int]
	labelCol: Optional[int]
	statusCol: Optional[int]
	editCol: Optional[int]
	thumbCol: Optional[int]

	numCols: int

	opRowHeight: int = 26
	catRowHeight: int = 26

	toggleColWidth: int = 26
	statusColWidth: int = 30
	editColWidth: int = 26
	thumbColWidth: int = 50

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
	keywords: List[str] = field(default_factory=list)
	thumbPath: Optional[str] = None
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
		for keyword in self.keywords:
			if keyword.startswith(filtText):
				return True
		if not self.words or len(filtText) > len(self.words):
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
			keywords = tdu.split(opTable[row, 'keywords'])
			words = _splitCamelCase(shortName)
			opItem.words = [w.lower() for w in words]
			opItem.keywords += [k.lower() for k in keywords]
			opItem.thumbPath = str(opTable[row, 'thumb'] or '')
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
			if filt is None:
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
	splits = [i for i, e in enumerate(s) if e.isupper() or e.isdigit()] + [len(s)]
	if not splits:
		return [s]
	splits = [0] + splits
	return [s[x:y] for x, y in zip(splits, splits[1:])]
