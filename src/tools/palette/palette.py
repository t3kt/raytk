from dataclasses import dataclass, field
from typing import Dict, List, Union, Optional
from raytkUtil import RaytkContext, detachTox, focusCustomParameterPage, ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from devel.toolkitEditor.toolkitEditor import ToolkitEditor

	# noinspection PyTypeHints
	op.raytkDevelEditor = ToolkitEditor(COMP())  # type: Optional[Union[ToolkitEditor, COMP]]

	class _Par(ParCollection):
		Devel: 'BoolParamT'
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

# columns:
#  name
#  status icon

class Palette:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.itemLibrary = _ItemLibrary()
		self.selItem = tdu.Dependency()  # value type _AnyItemT
		self.filterText = ''
		self.isOpen = tdu.Dependency(False)
		self.loadItems()

	@property
	def _listComp(self) -> 'listCOMP':
		return self.ownerComp.op('list')

	@property
	def _closeTimer(self) -> 'timerCHOP':
		# noinspection PyTypeChecker
		return self.ownerComp.op('closeTimer')

	@property
	def _filterTextWidget(self) -> 'widgetCOMP':
		return self.ownerComp.op('filterText_textfield')

	@property
	def _filterTextField(self) -> 'fieldCOMP':
		widget = self._filterTextWidget
		if widget:
			return op(widget.par.Stringfield0).op('./field')

	@property
	def _develMode(self):
		return bool(self.ownerComp.par.Devel)

	@property
	def SelectedItem(self) -> 'Optional[_AnyItemT]':
		return self.selItem.val

	def _selectItem(self, item: 'Optional[_AnyItemT]', scroll=False):
		oldItem = self.selItem.val  # type: Optional[_AnyItemT]
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

	def Show(self, _=None):
		self.open()

	def open(self):
		self._resetCloseTimer()
		self.ownerComp.op('window').par.winopen.pulse()
		self._resetState()
		self.isOpen.val = True
		ipar.uiState.Pinopen = False
		filterField = self._filterTextField
		if filterField:
			run('args[0]()', filterField.setKeyboardFocus, delayFrames=10)

	def close(self):
		self._resetCloseTimer()
		self.ownerComp.op('window').par.winclose.pulse()
		self.isOpen.val = False
		ipar.uiState.Pinopen = False

	def resetState(self):
		self._resetCloseTimer()
		self._resetState()

	def onCloseTimerComplete(self):
		if ipar.uiState.Pinopen:
			self._resetCloseTimer()
			return
		self.close()

	def _resetCloseTimer(self):
		timer = self._closeTimer
		timer.par.initialize.pulse()
		timer.par.active = False

	def _startCloseTimer(self):
		timer = self._closeTimer
		timer.par.active = True
		timer.par.start.pulse()

	def onPanelInsideChange(self, val: bool):
		if val:
			self._resetCloseTimer()
		else:
			self._startCloseTimer()

	def loadItems(self):
		opTable = self.ownerComp.op('opTable')  # type: DAT
		opHelpTable = self.ownerComp.op('opHelpTable')  # type: DAT
		self.itemLibrary.loadTables(opTable, opHelpTable)
		self.refreshList()
		self._selectItem(None)

	def refreshList(self):
		listComp = self._listComp
		listComp.par.rows = self.itemLibrary.currentItemCount
		listComp.par.cols = 3 if self._develMode else 2
		listComp.par.reset.pulse()

	def _resetState(self):
		self.refreshList()
		self._selectItem(None)
		self.clearFilterText()
		self.isOpen.val = False

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
		if shortcutName == 'up':
			self._offsetSelection(-1)
		elif shortcutName == 'down':
			self._offsetSelection(1)
		elif shortcutName == 'enter':
			self.createSelectedItem()
		elif shortcutName == 'esc':
			self.close()

	def createSelectedItem(self):
		item = self.SelectedItem
		if not item:
			return
		if isinstance(item, _CategoryItem):
			# TODO: maybe expand/collapse?
			return
		template = self._getTemplate(item)
		if not template:
			self._printAndStatus(f'Unable to find template for path: {item.path}')
			return
		context = RaytkContext()
		pane = context.activeEditor()
		dest = pane.owner if pane else None
		if not dest:
			self._printAndStatus('Unable to find active network editor pane')
			return
		ui.undo.startBlock(f'Create ROP {item.shortName}')
		bufferArea = dest
		newOp = bufferArea.copy(
			template,
			name=template.name + ('1' if tdu.digits(template.name) is None else ''),
		)  # type: COMP
		newOp.nodeCenterX = pane.x
		newOp.nodeCenterY = pane.y
		detachTox(newOp)
		enableCloning = newOp.par.enablecloning  # type: Par
		enableCloning.expr = ''
		enableCloning.val = self._develMode
		focusCustomParameterPage(newOp, 0)
		for par in newOp.customPars:
			if par.readOnly or par.isPulse or par.isMomentary or par.isDefault:
				continue
			if par.mode in (ParMode.EXPORT, ParMode.BIND):
				continue
			if par.defaultExpr and par.defaultExpr != par.default:
				par.expr = par.defaultExpr
			else:
				par.val = par.default
		newOp.allowCooking = True
		ropInfo = ROPInfo(newOp)
		ropInfo.invokeCallback('onCreate', master=template)
		ui.undo.endBlock()
		self._printAndStatus(f'Created OP: {newOp} from {template}')
		if not ipar.uiState.Pinopen:
			self.close()

	def editSelectedItem(self):
		item = self.SelectedItem
		if not item or not isinstance(item, _OpItem):
			return
		if not hasattr(op, 'raytkDevelEditor'):
			return
		template = self._getTemplate(item)
		if template:
			op.raytkDevelEditor.EditROP(template)

	def _printAndStatus(self, msg):
		print(self.ownerComp, msg)
		ui.status = msg

	@staticmethod
	def _getTemplate(item: '_Item'):
		if not item or not isinstance(item, _OpItem):
			return
		path = item.path
		if not path.startswith('/raytk/'):
			return op(path)
		context = RaytkContext()
		toolkit = context.toolkit()
		if toolkit and toolkit.path == '/raytk':
			return op(path)
		if not toolkit:
			return op(path)
		return op(path.replace('/raytk/', f'/{toolkit.path}/', 1))

	def onInitCell(self, row: int, col: int, attribs: 'ListAttributes'):
		item = self.itemLibrary.itemForRow(row)
		if not item:
			return
		if col == 0:
			attribs.text = item.shortName
		if isinstance(item, _CategoryItem):
			if col == 0:
				attribs.textOffsetX = 5
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
			elif col == 2:
				attribs.top = self.ownerComp.op('editIcon')
				attribs.bgColor = ipar.listConfig.Buttonbgcolorr, ipar.listConfig.Buttonbgcolorg, ipar.listConfig.Buttonbgcolorb, 1

	def onInitRow(self, row: int, attribs: 'ListAttributes'):
		item = self.itemLibrary.itemForRow(row)
		if not item:
			return
		if item.isAlpha or item.isBeta or item.isDeprecated:
			attribs.fontItalic = True
		if isinstance(item, _CategoryItem):
			attribs.textColor = ipar.listConfig.Categorytextcolorr, ipar.listConfig.Categorytextcolorg, ipar.listConfig.Categorytextcolorb, 1
			attribs.bgColor = ipar.listConfig.Categorybgcolorr, ipar.listConfig.Categorybgcolorg, ipar.listConfig.Categorybgcolorb, 1
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
		elif col == 2:
			attribs.colWidth = 26

	def onInitTable(self, attribs: 'ListAttributes'):
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
		cellAttribs = listComp.cellAttribs[row, 2 if self._develMode else 1]
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
			if col == 2 and isinstance(item, _OpItem):
				self._setButtonHighlight(row, col, True)
		if prevRow >= 0 and prevCol == 2:
			item = self.itemLibrary.itemForRow(prevRow)
			if isinstance(item, _OpItem):
				self._setButtonHighlight(prevRow, prevCol, False)

	def onSelect(
			self,
			startRow: int, startCol: int,
			endRow: int, endCol: int,
			start: bool, end: bool):
		item = self.itemLibrary.itemForRow(endRow)
		# print(self.ownerComp, f'SELECT startRC: {startRow},{startCol}, endRC: {endRow},{endCol}, start: {start}, end: {end} \n{item}')
		self._selectItem(item)
		if end:
			if endCol == 2 and self._develMode:
				self.editSelectedItem()
			else:
				self.createSelectedItem()

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
	words: List[str] = field(default_factory=list)

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
		if filt.text in self.categoryName.lower():
			return True
		# TODO: filter using word initials
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
			shortName = str(opTable[row, 'name'])
			path = str(opTable[row, 'path'])
			status = str(opTable[row, 'status'])
			categoryName = str(opTable[row, 'category'])
			opItem = _OpItem(
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
			words = _splitCamelCase(shortName) + _splitCamelCase(categoryName)
			opItem.words = [w.lower() for w in words]
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

def _splitCamelCase(s: str):
	splits = [i for i, e in enumerate(s) if e.isupper()] + [len(s)]
	if not splits:
		return [s]
	splits = [0] + splits
	return [s[x:y] for x, y in zip(splits, splits[1:])]

