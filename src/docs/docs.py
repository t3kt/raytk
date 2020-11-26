import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Union

class DocManager:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def categoryHelpTable(self) -> 'DAT':
		return self.ownerComp.op('opCategoryHelpTable')

	def opHelpTable(self) -> 'DAT':
		return self.ownerComp.op('opHelpTable')

	def buildCombinedOpDocs(self, dat: 'DAT'):
		categoryHelpTable = self.categoryHelpTable()
		dat.clear()

		textParts = []

		for categoryI in range(1, categoryHelpTable.numRows):
			categoryName = str(categoryHelpTable[categoryI, 'category'])
			helpText = _datText(categoryHelpTable[categoryI, 'helpPath'])
			textParts.append(f'# {categoryName.capitalize()} category\n')
			if helpText:
				helpText = _stripFirstHeader(helpText)
				textParts.append(helpText)
			textParts += self.getCategoryOpDocs(categoryName)

		dat.write('\n\n'.join(textParts))

	def getCategoryOpDocs(self, category: str):
		opHelpTable = self.opHelpTable()
		textParts = []
		for i in range(1, opHelpTable.numRows):
			if opHelpTable[i, 'category'] != category:
				continue
			opType = str(opHelpTable[i, 'opType'])
			shortName = opType.rsplit('.', 1)[1]
			helpText = _datText(opHelpTable[i, 'helpPath'])
			if helpText:
				helpText = _stripFirstHeader(helpText)
				helpText = _incrementHeaders(helpText)
			textParts.append(
				f'## {shortName} ({category})\n\n' + helpText
			)
		return textParts

_mainHeaderFullPattern = re.compile(r'^# .*\n')

_headerPattern = re.compile(r'^#', re.MULTILINE)

def _stripFirstHeader(text: str):
	if not text:
		return ''
	if not text.startswith('# '):
		return text
	return text.split('\n', 1)[1].strip()

def _incrementHeaders(text: str):
	if not text:
		return ''
	return _headerPattern.sub('##', text)

def _datText(path: 'Union[str, Cell]'):
	dat = op(path)
	return dat.text.strip() if dat else ''
