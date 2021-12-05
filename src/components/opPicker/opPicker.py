from dataclasses import dataclass, field
from typing import Dict, List, Union, Optional, Tuple

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Par(ParCollection):
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
		self.impl = _DefaultPickerImpl(ownerComp)
		# self.impl = _CategoryColumnPickerImpl(ownerComp)
		self.isOpen = tdu.Dependency(False)
		self.Loaditems()

	@property
	def _listComp(self) -> 'listCOMP':
		return self.ownerComp.op('list')

	@property
	def SelectedItem(self) -> 'Optional[_AnyItemT]':
		return self.impl.getSelectedItem()

	def FocusFilterField(self):
		def _focus():
			self.impl.focusFilterField()
		run('args[0]()', _focus, delayFrames=10)

	def Resetstate(self, _=None):
		self.impl.resetState()
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
		self.impl.loadItems(
			self.ownerComp.op('opTable'),
			self.ownerComp.op('opHelpTable'))

	def setFilterText(self, text: str):
		self.impl.setFilterText(text)

	def clearFilterText(self):
		self.impl.clearFilterText()

	def onUIStateChange(self, par: 'Par'):
		if par.name in ('Showalpha', 'Showbeta', 'Showdeprecated'):
			self.impl.applyFilter()
		elif par.name == 'Showthumbs':
			self.impl.refreshList()

	def onKeyboardShortcut(self, shortcutName: str):
		print(self.ownerComp, f'onKeyboardShortcut: {shortcutName}')
		if shortcutName == 'up':
			self.impl.offsetSelection(x=0, y=-1)
		elif shortcutName == 'down':
			self.impl.offsetSelection(x=0, y=1)
		elif shortcutName == 'enter':
			self.onPickItem()
		else:
			ext.callbacks.DoCallback('onKeyboardShortcut', {'shortcut': shortcutName})

	def onPickItem(self):
		item = self.impl.getSelectedItem()
		if not item:
			item = self.impl.selectFirstOpItem()
			if not item:
				return
		ext.callbacks.DoCallback('onPickItem', {'item': item})

	def _printAndStatus(self, msg):
		print(self.ownerComp, msg)
		ui.status = msg

	def onInitCell(self, row: int, col: int, attribs: 'ListAttributes'):
		self.impl.initCell(row, col, attribs)

	def onInitRow(self, row: int, attribs: 'ListAttributes'):
		self.impl.initRow(row, attribs)

	def onInitCol(self, col: int, attribs: 'ListAttributes'):
		self.impl.initCol(col, attribs)

	def onInitTable(self, attribs: 'ListAttributes'):
		self.impl.initTable(attribs)

	def onRollover(
			self,
			row: int, col: int,
			prevRow: int, prevCol: int):
		# note for performance: this gets called frequently as the mouse moves even within a single cell
		if row == prevRow and col == prevCol:
			return
		item = self.impl.getItemForCell(row, col)
		if item:
			self.impl.selectItem(item)
		ext.callbacks.DoCallback('onRolloverItem', {'item': item})

	def onSelect(self, endRow: int, endCol: int, end: bool):
		item = self.impl.getItemForCell(row=endRow, col=endCol)
		self.impl.selectItem(item)
		if not end:
			return
		if item.isCategory:
			self.impl.toggleCategoryExpansion(item)
		else:
			self.onPickItem()

	def onRadio(self, row: int, col: int, prevRow: int, prevCol: int):
		pass

	def onFocus(self, row: int, col: int, prevRow: int, prevCol: int):
		pass

@dataclass
class _LayoutSettings:
	toggleCol: Optional[int]
	labelCol: Optional[int]
	statusCol: Optional[int]
	thumbCol: Optional[int]

	numCols: int

	opRowHeight: int = 26
	catRowHeight: int = 26

	toggleColWidth: int = 26
	statusColWidth: int = 30
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

def _loadItemCategories(opTable: 'DAT', opHelpTable: 'DAT'):
	categories = []
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
		categories.append(category)
		category.ops.sort(key=lambda o: o.path)
		category.isAlpha = all([o.isAlpha for o in category.ops])
		category.isBeta = all([o.isBeta for o in category.ops])
		category.isDeprecated = all([o.isDeprecated for o in category.ops])
	return categories

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
		self.categories = _loadItemCategories(opTable, opHelpTable)
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

class _PickerImpl:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.listComp = ownerComp.op('list')  # type: listCOMP
		self.filterTextWidget = ownerComp.op('filterText_textfield')  # type: widgetCOMP
		self.filterTextField = op(self.filterTextWidget.par.Stringfield0).op('./field')  # type: fieldCOMP
		self.selItem = tdu.Dependency()  # value type _AnyItemT
		self.filterText = ''

	def getSelectedItem(self) -> 'Optional[_AnyItemT]':
		return self.selItem.val

	def selectItem(self, item: 'Optional[_AnyItemT]', scroll=False):
		oldItem = self.selItem.val  # type: Optional[_AnyItemT]
		if oldItem == item:
			return
		if oldItem:
			self.setItemHighlight(oldItem, False)
		self.selItem.val = item
		if item:
			self.setItemHighlight(item, True)
			if scroll:
				self.scrollToItem(item)

	def selectFirstOpItem(self) -> 'Optional[_AnyItemT]':
		raise NotImplementedError()

	def focusFilterField(self):
		self.filterTextField.setKeyboardFocus()

	def resetState(self):
		self.refreshList()
		self.selectItem(None)
		self.clearFilterText()

	def loadItems(self, opTable: 'DAT', opHelpTable: 'DAT'):
		raise NotImplementedError()

	def refreshList(self):
		raise NotImplementedError()

	def setFilterText(self, text: str):
		self.filterText = (text or '').strip()
		self.applyFilter()

	def clearFilterText(self):
		self.filterText = ''
		self.filterTextWidget.par.Value0 = ''
		self.applyFilter()

	def _getFilterSettings(self):
		return _Filter(
			self.filterText,
			alpha=ipar.uiState.Showalpha.eval(),
			beta=ipar.uiState.Showbeta.eval(),
			deprecated=ipar.uiState.Showdeprecated.eval(),
		)

	def toggleCategoryExpansion(self, item: 'PickerCategoryItem'):
		item.collapsed = not item.collapsed
		self.applyFilter()
		if item.collapsed:
			self.selectItem(item, scroll=False)
		elif item.ops:
			self.selectItem(item.ops[0], scroll=False)

	def applyFilter(self):
		raise NotImplementedError()

	def getLayout(self):
		layout = _LayoutSettings(
			toggleCol=0,
			labelCol=1,
			statusCol=2,
			thumbCol=None,
			numCols=3,
			thumbColWidth=self.ownerComp.par.Thumbsize.eval(),
		)
		if ipar.uiState.Showthumbs:
			layout.thumbCol = layout.numCols
			layout.numCols += 1
			thumbSize = int(self.ownerComp.par.Thumbsize)
			layout.opRowHeight = thumbSize
			layout.thumbColWidth = thumbSize
			layout.statusColWidth = thumbSize
		return layout

	def setItemHighlight(self, item: 'Optional[_AnyItemT]', selected: bool):
		raise NotImplementedError()

	def offsetSelection(self, x: int, y: int):
		raise NotImplementedError()

	def scrollToItem(self, item: 'Optional[_AnyItemT]'):
		raise NotImplementedError()

	def getItemForCell(self, row: int, col: int) -> 'Optional[_AnyItemT]':
		raise NotImplementedError()

	@staticmethod
	def initTable(attribs: 'ListAttributes'):
		attribs.bgColor = _configColor('Bgcolor')
		attribs.textColor = _configColor('Textcolor')
		attribs.fontFace = 'Roboto'
		attribs.fontSizeX = 18
		attribs.textJustify = JustifyType.CENTERLEFT

	def initCol(self, col: int, attribs: 'ListAttributes'):
		raise NotImplementedError()

	def initRow(self, row: int, attribs: 'ListAttributes'):
		raise NotImplementedError()

	def initCell(self, row: int, col: int, attribs: 'ListAttributes'):
		raise NotImplementedError()

	@staticmethod
	def _applyStatusTextColor(attribs: 'ListAttributes', item: '_AnyItemT'):
		if item.isAlpha:
			attribs.textColor = _configColor('Alphacolor')
		elif item.isBeta:
			attribs.textColor = _configColor('Betacolor')
		elif item.isDeprecated:
			attribs.textColor = _configColor('Deprecatedcolor')

	def _initStatusIconCell(self, attribs: 'ListAttributes', item: '_AnyItemT'):
		if item.isAlpha:
			attribs.top = self.ownerComp.op('alphaIcon')
			attribs.help = 'Alpha (experimental)'
		elif item.isBeta:
			attribs.top = self.ownerComp.op('betaIcon')
			attribs.help = 'Beta'
		elif item.isDeprecated:
			attribs.top = self.ownerComp.op('deprecatedIcon')
			attribs.help = 'Deprecated'

	def _initToggleCell(self, attribs: 'ListAttributes', item: 'PickerCategoryItem'):
		if item.collapsed:
			attribs.top = self.ownerComp.op('expandIcon')
		else:
			attribs.top = self.ownerComp.op('collapseIcon')
		attribs.bgColor = _configColor('Buttonbgcolor')

	def _initThumbCell(self, attribs: 'ListAttributes', item: 'PickerOpItem'):
		thumbRoot = self.ownerComp.par.Thumbroot.eval()
		if thumbRoot and item.thumbPath:
			attribs.top = thumbRoot.op(item.thumbPath) or ''

class _DefaultPickerImpl(_PickerImpl):
	def __init__(self, ownerComp: 'COMP'):
		super().__init__(ownerComp)
		self.itemLibrary = _ItemLibrary()

	def loadItems(self, opTable: 'DAT', opHelpTable: 'DAT'):
		self.itemLibrary.loadTables(opTable, opHelpTable)
		self.refreshList()
		self.applyFilter()
		self.selectItem(None)

	def refreshList(self):
		listComp = self.listComp
		listComp.par.rows = self.itemLibrary.currentItemCount
		layout = self.getLayout()
		listComp.par.cols = layout.numCols
		listComp.par.reset.pulse()

	def offsetSelection(self, x: int, y: int):
		if not self.itemLibrary or y == 0:
			return
		item = self.getSelectedItem()
		if item:
			row = self.itemLibrary.rowForItem(item)
			if row == -1:
				row = y
			else:
				row += y
		else:
			row = y
		self.selectItem(self.itemLibrary.itemForRow(row % self.itemLibrary.currentItemCount), scroll=True)

	def applyFilter(self):
		item = self.getSelectedItem()
		settings = self._getFilterSettings()
		self.itemLibrary.applyFilter(settings)
		if item:
			row = self.itemLibrary.rowForItem(item)
			if row < 0:
				self.selectItem(None)
			else:
				self.setItemHighlight(item, True)
		self.refreshList()

	def selectFirstOpItem(self) -> 'Optional[_AnyItemT]':
		item = self.itemLibrary.firstOpItem
		if not item:
			return
		self.selectItem(item)
		return item

	def setItemHighlight(self, item: 'Optional[_AnyItemT]', selected: bool):
		row = self.itemLibrary.rowForItem(item)
		if row < 0:
			return
		# print(self.ownerComp, f'setRowHighlight(row: {row!r}, sel: {selected!r})')
		if selected:
			color = _configColor('Rolloverhighlightcolor')
		else:
			color = 0, 0, 0, 0
		listComp = self.listComp
		layout = self.getLayout()
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

	def scrollToItem(self, item: 'Optional[_AnyItemT]'):
		row = self.itemLibrary.rowForItem(item)
		if row >= 0:
			self.listComp.scroll(row, 0)

	def getItemForCell(self, row: int, col: int) -> 'Optional[_AnyItemT]':
		if row < 0:
			return None
		return self.itemLibrary.itemForRow(row)

	def initCol(self, col: int, attribs: 'ListAttributes'):
		if col is None:
			return
		layout = self.getLayout()
		if col == layout.toggleCol:
			attribs.colWidth = layout.toggleColWidth
		elif col == layout.labelCol:
			attribs.colStretch = True
		elif col == layout.statusCol:
			attribs.colWidth = layout.statusColWidth
		elif col == layout.thumbCol:
			attribs.colWidth = layout.thumbColWidth

	def initRow(self, row: int, attribs: 'ListAttributes'):
		item = self.itemLibrary.itemForRow(row)
		if not item:
			return
		layout = self.getLayout()
		if item.isAlpha or item.isBeta or item.isDeprecated:
			attribs.fontItalic = True
		if isinstance(item, PickerCategoryItem):
			attribs.rowHeight = layout.catRowHeight
			attribs.textColor = _configColor('Categorytextcolor')
			attribs.bgColor = _configColor('Categorybgcolor')
		elif isinstance(item, PickerOpItem):
			attribs.rowHeight = layout.opRowHeight
		self._applyStatusTextColor(attribs, item)

	def initCell(self, row: int, col: int, attribs: 'ListAttributes'):
		item = self.getItemForCell(row=row, col=col)
		if not item:
			return
		layout = self.getLayout()
		if col == layout.labelCol:
			attribs.text = item.shortName
		if isinstance(item, PickerCategoryItem):
			if col == layout.toggleCol:
				self._initToggleCell(attribs, item)
			elif col == layout.labelCol:
				attribs.textOffsetX = 5
		elif isinstance(item, PickerOpItem):
			attribs.help = item.helpSummary or ''
			if col == layout.labelCol:
				attribs.textOffsetX = 20
			elif col == layout.statusCol:
				self._initStatusIconCell(attribs, item)
			elif col == layout.thumbCol:
				self._initThumbCell(attribs, item)

@dataclass
class _CategoryColumn:
	category: PickerCategoryItem
	allOps: List[PickerOpItem]
	filteredOps: Optional[List[PickerOpItem]] = None

	def applyFilter(self, filt: Optional[_Filter]) -> bool:
		if not filt:
			self.filteredOps = None
			return True
		else:
			self.filteredOps = [o for o in self.allOps if o.matches(filt)]
			return bool(self.filteredOps)

	@property
	def currentOpList(self):
		return self.filteredOps if self.filteredOps is not None else self.allOps

	@property
	def currentItemCount(self):
		return 1 + len(self.currentOpList)

	def getItemByRow(self, i: int) -> Optional[_AnyItemT]:
		if i < 0:
			return None
		if i == 0:
			return self.category
		i -= 1
		curOps = self.currentOpList
		return curOps[i] if i < len(curOps) else None

	def getRowByItem(self, item: Optional[_AnyItemT]):
		if not item:
			return -1
		if item == self.category:
			return 0
		try:
			return 1 + self.currentOpList.index(item)
		except ValueError:
			return -1

class _CategoryColumnLibrary:
	allItems: List[_AnyItemT]
	allColumns: List[_CategoryColumn]
	filteredColumns: Optional[List[_CategoryColumn]]

	def __init__(self):
		self.allItems = []
		self.allCategories = []
		self.filteredColumns = None

	def loadTables(self, opTable: 'DAT', opHelpTable: 'DAT'):
		self.allItems = []
		self.allColumns = []
		for category in _loadItemCategories(opTable, opHelpTable):
			self.allColumns.append(_CategoryColumn(
				category,
				allOps=list(category.ops),
			))
		self.applyFilter(None)

	@property
	def currentColList(self):
		return self.filteredColumns if self.filteredColumns is not None else self.allColumns

	def getCurrentSize(self) -> Tuple[int, int]:
		cols = self.currentColList
		if not cols:
			return 1, 1
		maxOps = max([col.currentItemCount for col in cols])
		return maxOps, len(cols)

	def applyFilter(self, filt: Optional[_Filter] = None):
		if not filt:
			self.filteredColumns = None
			for col in self.allColumns:
				col.applyFilter(None)
		else:
			self.filteredColumns = []
			for col in self.allColumns:
				if col.applyFilter(filt):
					self.filteredColumns.append(col)

	def getCol(self, col: int) -> Optional[_CategoryColumn]:
		cols = self.currentColList
		return cols[col] if 0 <= col < len(cols) else None

	def getPosForItem(self, item: Optional[_AnyItemT]):
		if not item:
			return None, None
		for colI, col in enumerate(self.currentColList):
			row = col.getRowByItem(item)
			if row != -1:
				return row, colI
		return None, None

	def getItemByPos(self, row:int, col: int) -> Optional[_AnyItemT]:
		if col < 0:
			return None
		cols = self.currentColList
		if 0 <= col < len(cols):
			return cols[col].getItemByRow(row)

class _CategoryColumnPickerImpl(_PickerImpl):
	def __init__(self, ownerComp: 'COMP'):
		super().__init__(ownerComp)
		self.itemLibrary = _CategoryColumnLibrary()

	def getLayout(self):
		layout = super().getLayout()
		layout.toggleCol = None
		layout.numCols -= 1
		return layout

	def selectFirstOpItem(self) -> 'Optional[_AnyItemT]':
		for col in self.itemLibrary.currentColList:
			colOps = col.currentOpList
			if colOps:
				item = colOps[0]
				self.selectItem(item)
				return item

	def loadItems(self, opTable: 'DAT', opHelpTable: 'DAT'):
		self.itemLibrary.loadTables(opTable, opHelpTable)
		self.refreshList()
		self.applyFilter()
		self.selectItem(None)

	def refreshList(self):
		listComp = self.listComp
		rows, cols = self.itemLibrary.getCurrentSize()
		layout = self.getLayout()
		listComp.par.rows = rows
		listComp.par.cols = cols * layout.numCols

	def applyFilter(self):
		item = self.getSelectedItem()
		settings = self._getFilterSettings()
		self.itemLibrary.applyFilter(settings)
		if item:
			pass
		pass

	def _getCellAttribsForItem(self, item: 'Optional[_AnyItemT]') -> 'List[ListAttributes]':
		row, col = self.itemLibrary.getPosForItem(item)
		if row is None:
			return []
		return [
			self.listComp.cellAttribs[row, col + i]
			for i in range(self.getLayout().numCols)
		]

	def setItemHighlight(self, item: 'Optional[_AnyItemT]', selected: bool):
		cellAttribs = self._getCellAttribsForItem(item)
		if not cellAttribs:
			return
		if selected:
			color = _configColor('Rolloverhighlightcolor')
		else:
			color = 0, 0, 0, 0
		for ca in cellAttribs:
			ca.topBorderOutColor = color
			ca.bottomBorderOutColor = color
		cellAttribs[0].leftBorderInColor = color
		cellAttribs[len(cellAttribs) - 1].rightBorderOutColor = color

	def offsetSelection(self, x: int, y: int):
		if not self.itemLibrary or (x == 0 and y == 0):
			return
		# item = self.getSelectedItem()
		# if item:
		# 	row, col = self.itemLibrary.getPosForItem(item)
		# 	if row is None:
		# 		pass
		# 	pass
		raise NotImplementedError()

	def scrollToItem(self, item: 'Optional[_AnyItemT]'):
		row, col = self.itemLibrary.getPosForItem(item)
		if row is None:
			return
		self.listComp.scroll(row, col * self.getLayout().numCols)

	def getItemForCell(self, row: int, col: int) -> 'Optional[_AnyItemT]':
		if row < 0 or col < 0:
			return None
		layout = self.getLayout()
		return self.itemLibrary.getItemByPos(
			row=row,
			col=int(col / layout.numCols)
		)

	def initCol(self, col: int, attribs: 'ListAttributes'):
		if col is None:
			return
		layout = self.getLayout()
		col = col % layout.numCols
		if col == layout.labelCol:
			# attribs.colStretch = True
			attribs.colWidth = 200
		elif col == layout.statusCol:
			attribs.colWidth = layout.statusColWidth
		elif col == layout.thumbCol:
			attribs.colWidth = layout.thumbColWidth

	def initRow(self, row: int, attribs: 'ListAttributes'):
		layout = self.getLayout()
		if row == 0:
			attribs.rowHeight = layout.catRowHeight
			attribs.textColor = _configColor('Categorytextcolor')
			attribs.bgColor = _configColor('Categorybgcolor')
		else:
			attribs.rowHeight = layout.opRowHeight

	def initCell(self, row: int, col: int, attribs: 'ListAttributes'):
		layout = self.getLayout()
		colPart = col % layout.numCols
		colIndex = int(col / layout.numCols)
		catCol = self.itemLibrary.getCol(colIndex)
		if not catCol:
			return
		item = catCol.getItemByRow(row)
		if not item:
			return
		if colPart == layout.labelCol:
			attribs.text = item.shortName
		if isinstance(item, PickerOpItem):
			attribs.help = item.helpSummary or ''
			self._applyStatusTextColor(attribs, item)
			if colPart == layout.labelCol:
				if item.isAlpha or item.isBeta or item.isDeprecated:
					attribs.fontItalic = True
				attribs.textOffsetX = 5
			elif colPart == layout.statusCol:
				self._initStatusIconCell(attribs, item)
			elif colPart == layout.thumbCol:
				self._initThumbCell(attribs, item)
