import re
from raytkUtil import getToolkit, getActiveEditor, detachTox, focusCustomParameterPage

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

	@property
	def develEnabled(self):
		return bool(self.ownerComp.par['Devel'])

	@staticmethod
	def buildListTable(dat: 'DAT', opTable: 'DAT'):
		categoryNames = list(set(c.val for c in opTable.col('category')[1:]))
		opNames = [c.val for c in opTable.col('name')[1:]]
		dat.clear()
		dat.appendRow(['indentedName', 'name', 'path', 'type', 'status'])
		for categoryName in sorted(categoryNames):
			dat.appendRow([categoryName, categoryName, '', 'category', ''])
			for name in opNames:
				if opTable[name, 'category'] == categoryName:
					dat.appendRow(['    ' + name, name, opTable[name, 'path'], 'op', opTable[name, 'status']])

	@staticmethod
	def getEventPath(info: dict):
		rowData = info.get('rowData')
		rowObject = rowData and rowData.get('rowObject')
		path = rowObject and rowObject.get('path')
		return path

	def onItemClick(self, info: dict):
		path = self.getEventPath(info)
		if not path:
			return
		self.CreateOp(path)
		self.Close()

	def onSelectRow(self, info: dict):
		path = self.getEventPath(info)
		ipar.createMenuState.Helpoppath = path or ''

	def onRollover(self, info: dict):
		row = info.get('row')
		if row not in (None, -1):
			table = self.ownerComp.op('prepared_op_table')
			cell = table[row + 1, 'path']
			ipar.createMenuState.Helpoppath = cell or ''

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
		ipar.createMenuState.Helpoppath = ''
		self.window.par.winclose.pulse()

	def Show(self, _=None):
		self.ClearFilter()
		ipar.createMenuState.Helpoppath = ''
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
		pane = getActiveEditor()
		if not pane:
			return master
		dest = pane.owner
		if not dest:
			return
		ui.undo.startBlock(f'Create ROP {master.name}')
		if op('/sys/quiet'):
			bufferArea = op('/sys/quiet').create(baseCOMP)
		else:
			bufferArea = dest
		newOp = bufferArea.copy(
			master,
			name=master.name + ('1' if tdu.digits(master.name) is None else ''))  # type: COMP
		pane.placeOPs([newOp])
		newOp.nodeCenterX = pane.x
		newOp.nodeCenterY = pane.y
		detachTox(newOp)
		enableCloning = newOp.par.enablecloning  # type: Par
		enableCloning.expr = ''
		enableCloning.val = bool(self.develEnabled)
		focusCustomParameterPage(newOp, 0)
		newOp.allowCooking = True
		ui.undo.endBlock()
		# newOp.path will still return the temporary path because place may not have completed yet
		print(self.ownerComp, f'Created OP: {dest.path}/{newOp.name} from {master}')
		return newOp

	@staticmethod
	def filterOpTable(dat: 'DAT', inDat: 'DAT', filterText: str):
		dat.clear()
		dat.appendRow(inDat.row(0))
		showBeta = ipar.createMenuState.Showbeta
		if not filterText or filter == '*':
			def testText(_): return True
		elif re.match(r'^\w+$', filterText):
			def testText(val: str):
				return filterText.lower() in val.lower()
		elif re.match(r'^[\w\*\?]+$', filterText):
			def testText(val: str):
				return bool(tdu.match(filterText, [val], caseSensitive=False))
		else:
			def testText(val: str):
				return filterText.lower() in val.lower()
		ignorePrefix = getToolkit().path + '/operators/'
		for i in range(1, inDat.numRows):
			if inDat[i, 'type'] == 'category':
				dat.appendRow(inDat.row(i))
			else:
				if not testText(inDat[i, 'path'].val.replace(ignorePrefix, '')):
					continue
				if not showBeta and 'beta' in inDat[i, 'status'].val:
					continue
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
