# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class CreateMenu:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.opTable = self.ownerComp.op('opTable')
		# print(info)

	def buildListTable(self, dat: 'DAT', opTable: 'DAT'):
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
		path = info.get('path')
		if not path:
			return
		pass
