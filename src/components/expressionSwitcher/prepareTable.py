import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

_paramPattern = re.compile(r'\bTHIS_([A-Z][a-z0-9]*)\b')

def onCook(dat: 'scriptDAT'):
	dat.clear()
	rawTable = dat.inputs[0]
	otherCols = [
		c.val
		for c in rawTable.row(0)
		if c.val not in ('name', 'label', 'expr', 'params')
	] if rawTable.numRows > 0 else []
	dat.appendRow(['name', 'label', 'expr', 'params'] + otherCols)
	if rawTable.numRows < 2:
		return
	for row in range(1, rawTable.numRows):
		expr = str(rawTable[row, 'expr'] or '')
		paramsCell = rawTable[row, 'params']
		if paramsCell is not None:
			params = paramsCell.val.split(' ') if paramsCell.val else []
		else:
			params = []
			if 'THIS_' in expr:
				params = _paramPattern.findall(expr) or []
		dat.appendRow([
			rawTable[row, 'name'],
			rawTable[row, 'label'] or rawTable[row, 'name'],
			expr,
			' '.join(params),
		] + [
			rawTable[row, c]
			for c in otherCols
		])
