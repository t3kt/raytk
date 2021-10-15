# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List

def onCook(dat):
	dat.copy(dat.inputs[0])
	supportedTypes = dat.inputs[1]
	_restrictTypeCategory(dat, supportedTypes, 'coordType')
	_restrictTypeCategory(dat, supportedTypes, 'contextType')
	_restrictTypeCategory(dat, supportedTypes, 'returnType')

def _restrictTypeCategory(dat: 'scriptDAT', supportedTypes: 'DAT', column: str):
	cells = dat.col(column)
	if not cells or len(cells) < 2:
		return
	if parent().par.Onlyfirstdef:
		cells = [cells[1]]
	else:
		cells = cells[1:]
	supported = supportedTypes[column, 'types'].val.split(' ')
	for cell in cells:
		cell.val = _restrictExpandedTypes(
			expandedTypes=cell.val,
			supportedTypes=supported)

def _restrictExpandedTypes(expandedTypes: str, supportedTypes: 'List[str]') -> str:
	return ' '.join([t for t in expandedTypes.split(' ') if t in supportedTypes])
