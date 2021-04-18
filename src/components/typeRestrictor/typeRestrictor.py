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
	if not cells:
		return
	if parent().par.Onlyfirstdef:
		cells = [cells[1]]
	else:
		cells = cells[1:]
	supported = supportedTypes[column, 'types'].val.split(' ')
	for cell in cells:
		types = cell.val.split(' ')
		types = [
			t for t in types if t in supported
		]
		cell.val = ' '.join(types)

