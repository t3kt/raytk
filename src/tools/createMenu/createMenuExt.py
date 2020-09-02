import json

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class CreateMenu:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.opTable = self.ownerComp.op('opTable')

	def opTableToJson(self, opTable: 'DAT'):
		categoryNames = list(set(c.val for c in opTable.col('category')[1:]))
		categoryNames.sort()
		categories = {}
		for row in range(1, opTable.numRows):
			categoryName = str(opTable[row, 'category'])
			if categoryName in categories:
				category = categories[categoryName]
			else:
				category = categories[categoryName] = {
					'key': categoryName,
					'id': (categoryName,),
					'type': '',
					'children': [],
				}
			opName = str(opTable[row, 'name'])
			category['children'].append({
				'key': opName,
				'id': (categoryName, opName),
				'type': '',
				'value': str(opTable[row, 'path'])
			})
		obj = {
			'items': [
				categories[categoryName]
				for categoryName in sorted(categories.keys())
			]
		}
		return json.dumps(obj, indent='  ')

	def opTableToJsonV2(self, opTable: 'DAT'):
		categoryNames = list(set(c.val for c in opTable.col('category')[1:]))
		categoryNames.sort()
		categories = {}
		for row in range(1, opTable.numRows):
			categoryName = str(opTable[row, 'category'])
			if categoryName in categories:
				category = categories[categoryName]
			else:
				category = categories[categoryName] = []
			opName = str(opTable[row, 'name'])
			category.append(opName)
		return json.dumps(categories, indent='  ')

	def getObjectFromID(self, info: dict):
		objId = info['id']
		jsonObject = info['jsonObject']
		print(f'getObjectFromID(objId: {objId!r}, jsonObject: {jsonObject!r})')
		categoryName = objId
		items = []
		for row in range(1, self.opTable.numRows):
			if self.opTable[row, 'parentPath'] == categoryName:
				pass
			pass
		# print(info)

	def getIDFromObject(self, info: dict):
		obj = info['object']
		jsonID = info['jsonID']
		print(f'getIDFromObject(obj: {obj!r}, jsonID: {jsonID!r})')
		# print(info)

	def getObjectChildren(self, info: dict):
		obj = info['object']
		jsonChildren = info['jsonChildren']
		print(f'getObjectChildren(obj: {obj!r}, jsonChildren: {jsonChildren!r})')
		# print(info)
