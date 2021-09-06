import raytkTypes

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def restrictTypes(dat: 'scriptDAT', supportedTypes: 'DAT'):
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
		cell.val = raytkTypes.restrictExpandedTypes(
			expandedTypes=cell.val,
			supportedTypes=supported)

