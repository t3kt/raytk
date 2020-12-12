from raytkUtil import datText, incrementMarkdownHeaders, stripFirstMarkdownHeader

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class DocManager:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def categoryHelpTable(self) -> 'DAT':
		return self.ownerComp.op('opCategoryHelpTable')

	def opHelpTable(self) -> 'DAT':
		return self.ownerComp.op('opHelpTable')

	def opTable(self) -> 'DAT':
		return self.ownerComp.op('opTableByType')

	def buildCombinedOpDocs(self, dat: 'DAT'):
		categoryHelpTable = self.categoryHelpTable()
		dat.clear()
		textParts = ['# Operators']
		for categoryI in range(1, categoryHelpTable.numRows):
			categoryName = str(categoryHelpTable[categoryI, 'category'])
			helpText = datText(categoryHelpTable[categoryI, 'helpPath'])
			textParts.append(f'## {categoryName.capitalize()} category\n')
			if helpText:
				helpText = stripFirstMarkdownHeader(helpText)
				helpText = incrementMarkdownHeaders(helpText, 1)
				textParts.append(helpText)
			textParts += self.getCategoryOpDocs(categoryName)

		dat.write('\n\n'.join(textParts))
		dat.write('\n')

	def getCategoryOpDocs(self, category: str):
		opHelpTable = self.opHelpTable()
		opTable = self.opTable()
		textParts = []
		for i in range(1, opHelpTable.numRows):
			if opHelpTable[i, 'category'] != category:
				continue
			opType = str(opHelpTable[i, 'opType'])
			shortName = opType.rsplit('.', 1)[1]
			helpText = datText(opHelpTable[i, 'helpPath'])
			if helpText:
				helpText = stripFirstMarkdownHeader(helpText)
				helpText = incrementMarkdownHeaders(helpText, 2)
			status = str(opTable[opType, 'status'])
			statusSuffix = f' `{status.upper()}`' if status else ''
			textParts.append(
				f'### {shortName}{statusSuffix}\n\n' + helpText
			)
		return textParts

	# def docTextForCategory(self, category: str):
	# 	categoryHelpTable = self.categoryHelpTable()
	# 	helpText = datText(categoryHelpTable[category, 'helpPath'])
	# 	textParts = [f'# {category.capitalize()} category\n']
	# 	if helpText:
	# 		helpText = stripFirstMarkdownHeader(helpText)
	# 		helpText = incrementMarkdownHeaders(helpText, 1)
	# 		textParts.append(helpText)
	#
	# 	pass
