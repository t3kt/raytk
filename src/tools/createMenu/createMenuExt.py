import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _stubs.ListerExt import ListerExt
	from typing import Any, Union, Optional
	ipar.createMenuState = Any()

class CreateMenu:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.opTable = self.ownerComp.op('opTable')
		self.lister = self.ownerComp.op('lister')  # type: Union[COMP, ListerExt]
		self.window = self.ownerComp.op('window')  # type: windowCOMP

	@staticmethod
	def buildListTable(dat: 'DAT', opTable: 'DAT'):
		categoryNames = list(set(c.val for c in opTable.col('category')[1:]))
		opNames = [c.val for c in opTable.col('name')[1:]]
		dat.clear()
		dat.appendRow(['indentedName', 'name', 'path', 'type'])
		for categoryName in sorted(categoryNames):
			dat.appendRow([categoryName, categoryName, '', 'category'])
			for name in opNames:
				if opTable[name, 'category'] == categoryName:
					dat.appendRow(['    ' + name, name, opTable[name, 'path'], 'op'])

	def onItemClick(self, info: dict):
		rowData = info.get('rowData')
		rowObject = rowData and rowData.get('rowObject')
		path = rowObject and rowObject.get('path')
		if not path:
			return
		self.CreateOp(path)
		self.Close()

	def onFilterFieldKey(self, key: str):
		table = self.ownerComp.op('prepared_op_table')
		if table.numRows < 2:
			return
		selectedRows = self.lister.SelectedRows
		if selectedRows:
			selPath = str(table[selectedRows[0]+1, 'path'] or '')
		else:
			selPath = None
		if key == 'enter':
			if selPath:
				self.CreateOp(selPath)
				self.Close()
		elif key in ['up', 'down']:
			if not selectedRows:
				if key == 'down':
					selRow = 0
				else:
					selRow = table.numRows - 2
			else:
				offset = 1 if key == 'down' else -1
				selRow = selectedRows[0] + offset
				if selRow >= table.numRows - 1:
					selRow = 0
				elif selRow < 0:
					selRow = table.numRows - 2
			for row in selectedRows:
				self.lister.DeselectRow(row)
			self.lister.SelectRow(selRow)

	def updateRowSelection(self, selRow: 'Optional[int]'):
		for row in self.lister.SelectedRows:
			self.lister.DeselectRow(row)
		if selRow is not None:
			self.lister.SelectRow(selRow)

	def Close(self):
		self.window.par.winclose.pulse()

	def Show(self, _=None):
		self.ClearFilter()
		self.window.par.winopen.pulse()
		run('args[0].ClearFilter()', self, delayFrames=3)
		field = self.ownerComp.op('filterText_textfield/stringField0/field')  # type: fieldCOMP
		if field:
			run('args[0].setKeyboardFocus()', field, delayFrames=5)

	def ClearFilter(self):
		self.setFilter('')

	def setFilter(self, val: str):
		ipar.createMenuState.Filtertext = val
		self.updateRowSelection(None)

	def CreateOp(self, masterPath: str):
		if not masterPath:
			return
		print(self.ownerComp, 'Creating OP from', masterPath)
		master = op(masterPath)
		if not master:
			return None
		pane = _getActiveEditor()
		if not pane:
			return master
		dest = pane.owner
		if not dest:
			return
		try:
			primarySelected = dest.currentChild if dest and _isRop(dest.currentChild) else None
		except:
			primarySelected = None
		inputOps = [
			o
			for o in dest.selectedChildren
			if _isRop(o)
		]
		if inputOps and not primarySelected:
			inputOps.sort(key=lambda o: -o.nodeX)
			primarySelected = inputOps[0]
		inputOps.sort(key=lambda o: -o.nodeY)
		if primarySelected:
			posX = primarySelected.nodeX + primarySelected.nodeWidth + 150
			posY = primarySelected.nodeY
		else:
			posX, posY = pane.x, pane.y
		ui.undo.startBlock(f'Create ROP {master.name}')
		newOp = dest.copy(
			master,
			name=master.name + ('1' if tdu.digits(master.name) is None else ''))  # type: COMP
		newOp.nodeX = posX
		newOp.nodeY = posY
		ui.undo.endBlock()
		# if inputOps and len(newOp.inputConnectors):
		# 	datInputs = [
		# 		conn
		# 		for conn in newOp.inputConnectors
		# 		if conn.inOP and conn.inOP.isDAT
		# 	]
		# 	for i, datInput in enumerate(datInputs):
		# 		if i < len(inputOps):
		# 			datInput.disconnect()
		# 			datInput.connect(inputOps[i])
		print(self.ownerComp, f'Created OP: {newOp} from {master}')
		return newOp

	@staticmethod
	def filterOpTable(dat: 'DAT', inDat: 'DAT', filterText: str):
		if not filterText or filterText == '*':
			dat.copy(inDat)
			return
		dat.clear()
		dat.appendRow(inDat.row(0))
		if re.match(r'^\w+$', filterText):
			test = lambda val: filterText.lower() in val.lower()
		elif re.match(r'^[\w\*\?]+$', filterText):
			test = lambda val: bool(tdu.match(filterText, [val], caseSensitive=False))
		else:
			test = lambda val: filterText.lower() in val.lower()
		ignorePrefix = op.raytk.path + '/operators/'
		for i in range(1, inDat.numRows):
			if inDat[i, 'type'] == 'category' or test(inDat[i, 'path'].val.replace(ignorePrefix, '')):
				dat.appendRow(inDat.row(i))
	
	def onMouseOverChange(self, value):
		timer = self.ownerComp.op('close_timer')
		if value:
			timer.par.initialize.pulse()
			timer.par.active = False
		else:
			timer.par.active = True
			timer.par.start.pulse()
	
	def onCloseTimerDone(self):
		timer = self.ownerComp.op('close_timer')
		timer.par.initialize.pulse()
		timer.par.active = False
		self.Close()

# noinspection PyTypeChecker
def _getActiveEditor() -> 'NetworkEditor':
	pane = ui.panes.current
	if pane.type == PaneType.NETWORKEDITOR:
		return pane
	for pane in ui.panes:
		if pane.type == PaneType.NETWORKEDITOR:
			return pane

def _isRop(o: OP):
	return bool(o) and o.isCOMP and 'raytkOP' in o.tags
