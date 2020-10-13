from typing import List, Tuple, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

	class _OwnerCompPar:
		Globalprefix: 'Union[DAT, str, Par]'
		Predeclarations: 'Union[DAT, str, Par]'
		Textureindexoffset: 'Union[int, Par]'
		Globalmacrotable: 'Union[DAT, str, Par]'
		Libraries: 'Union[str, Par]'
		Bodytemplate: 'Union[DAT, str, Par]'
		Useoutputbuffertable: 'Union[bool, Par]'
		Outputbuffertable: 'Union[DAT, str, Par]'
		Parammode: 'Union[str, Par]'
		Inlineparameteraliases: 'Union[bool, Par]'
		Simplifynames: 'Union[bool, Par]'

	class _OwnerComp(COMP):
		par: '_OwnerCompPar'

class ShaderBuilder:
	def __init__(self, ownerComp: '_OwnerComp'):
		self.ownerComp = ownerComp

def buildParamAliasMacros(dat: 'DAT', paramDetails: 'DAT'):
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

def wrapCodeSection(code: str, name: str):
	return f'///----BEGIN {name}\n{code}\n///----END {name}' if code else ''
