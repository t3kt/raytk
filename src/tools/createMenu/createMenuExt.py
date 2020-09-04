# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

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
		self.ownerComp.op('window').par.winopen.pulse()

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
		primarySelected = dest.currentChild if _isRop(dest.currentChild) else None
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
		newOp = dest.copy(
			master,
			name=master.name + ('1' if tdu.digits(master.name) is None else ''))  # type: COMP
		newOp.nodeX = posX
		newOp.nodeY = posY
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
