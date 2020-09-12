import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Any
	ipar.createMenuState = Any()

class CreateMenu:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.opTable = self.ownerComp.op('opTable')
		# print(info)

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
		print(self.ownerComp, 'OMG onItemClick', repr(info))
		rowData = info.get('rowData')
		rowObject = rowData and rowData.get('rowObject')
		path = rowObject and rowObject.get('path')
		print(' .... path: ', repr(path))
		if not path:
			return
		self.CreateOp(path)
		self.ownerComp.op('window').par.winclose.pulse()

	def Show(self, _=None):
		self.ClearFilter()
		self.ownerComp.op('window').par.winopen.pulse()

	@staticmethod
	def ClearFilter():
		ipar.createMenuState.Filtertext = ''

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
		for i in range(1, inDat.numRows):
			if inDat[i, 'type'] == 'category' or test(inDat[i, 'path'].val):
				dat.appendRow(inDat.row(i))

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
