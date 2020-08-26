import re
from typing import List, Tuple

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildParamAliaseMacros(dat: 'DAT', paramDetails: 'DAT'):
	dat.clear()
	for name, expr in _getParamAliases(paramDetails):
		dat.appendRow([f'#define {name} {expr}'])

def buildParamAliasTable(dat: 'DAT', paramDetails: 'DAT'):
	dat.clear()
	dat.appendRow(['before', 'after'])
	for name, expr in _getParamAliases(paramDetails):
		dat.appendRow([name, expr])

def _getParamAliases(paramDetails: 'DAT') -> List[Tuple[str, str]]:
	suffixes = 'xyzw'
	partAliases = []
	mainAliases = []
	for i in range(paramDetails.numRows - 1):
		tupletName = paramDetails[i + 1, 'tuplet']
		size = int(paramDetails[i + 1, 'size'])
		if size == 1:
			name = paramDetails[i + 1, 'part1']
			mainAliases.append((str(name), f'vecParams[{i}].x'))
		else:
			if size == 4:
				mainAliases.append((str(tupletName), f'vecParams[{i}]'))
			else:
				mainAliases.append((str(tupletName), f'vec{size}(vecParams[{i}].{suffixes[:size]})'))
			for partI in range(1, 5):
				name = paramDetails[i + 1, f'part{partI}']
				if name:
					suffix = suffixes[partI - 1]
					partAliases.append((str(name), f'vecParams[{i}].{suffix}'))
	return partAliases + mainAliases

def buildMaterialBlock(materialTable: 'DAT'):
	if materialTable.numRows < 2:
		return ''
	output = ''
	for nameCell, pathCell in materialTable.rows()[1:]:
		if not nameCell:
			continue
		codeDat = op(pathCell)
		materialCode = codeDat.text if codeDat else ''
		output += f'else if(m == {nameCell.val}) {{\n'
		output += materialCode + '\n}'
	return output
