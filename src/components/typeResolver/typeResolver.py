from typing import Dict

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def resolveTypes(dat: 'scriptDAT'):
	_resolveTypeCategory(dat, 'coordType')
	_resolveTypeCategory(dat, 'contextType')
	_resolveTypeCategory(dat, 'returnType')

def _resolveTypeCategory(dat: 'scriptDAT', column: str):
	# BEFORE definitions are reversed, so a def's inputs are always BELOW it in the table
	typesByName = {}  # type: Dict[str, str]
	cells = dat.col(column)
	if not cells:
		return
	for cell in cells[1:]:
		name = dat[cell.row, 'name'].val
		if cell.val.startswith('@'):
			refName = cell.val.replace('@', '', 1)
			if refName not in typesByName:
				raise Exception(f'Type resolution error for {name}: {cell.val!r}')
			cell.val = typesByName[refName]
		typesByName[name] = cell.val
