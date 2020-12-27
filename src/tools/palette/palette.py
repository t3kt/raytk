from dataclasses import dataclass, field
from typing import Dict, List, Union, Optional
from raytkUtil import RaytkContext, detachTox, focusCustomParameterPage, ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

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

	def Show(self, _=None):
		self.open()

	def open(self):
		self._resetCloseTimer()
		self.ownerComp.op('window').par.winopen.pulse()
		self._resetState()
		self.isOpen.val = True
		ipar.uiState.Pinopen = False

	def close(self):
		self._resetCloseTimer()
		self.ownerComp.op('window').par.winclose.pulse()
		self.isOpen.val = False
		ipar.uiState.Pinopen = False

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
		self.SelectedItem = None

	def refreshList(self):
		listComp = self._listComp
		listComp.par.rows = self.itemLibrary.currentItemCount
		listComp.par.cols = 2
		listComp.par.reset.pulse()

	def _resetState(self):
		self.refreshList()
		self.SelectedItem = None
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
		self.SelectedItem = self.itemLibrary.itemForRow(row % self.itemLibrary.currentItemCount)

	def setFilterText(self, text: str):
		self.filterText = (text or '').strip()
		self._applyFilter()

	def clearFilterText(self):
		self.filterText = ''
		self.ownerComp.op('filterText_textfield').par.Value0 = ''
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
		enableCloning.val = bool(self.ownerComp.par.Devel)
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
		if not toolkit:
			return
		return toolkit.op(path.replace('/raytk/', '', 1))

	def onInitCell(self, row: int, col: int, attribs: 'ListAttributes'):
		item = self.itemLibrary.itemForRow(row)
		if not item:
			return
		if col == 0:
			attribs.text = item.shortName
		if isinstance(item, _CategoryItem):
			if col == 0:
				attribs.textOffsetX = 5
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
		listComp = self._listComp
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
		print(self.ownerComp, f'SELECT startRC: {startRow},{startCol}, endRC: {endRow},{endCol}, start: {start}, end: {end} \n{item}')
		self.SelectedItem = item
		if end:
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

