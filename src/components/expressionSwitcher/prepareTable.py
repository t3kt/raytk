import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

_argPattern = re.compile(r'\bTHIS_([\w]+)\b')
_paramNamePattern = re.compile(r'[A-Z][a-z0-9]*')

def onCook(dat: 'scriptDAT'):
	dat.clear()
	rawTable = dat.inputs[0]
	otherCols = [
		c.val
		for c in rawTable.row(0)
		if c.val not in ('name', 'label', 'expr', 'params')
	] if rawTable.numRows > 0 else []
	dat.appendRow(['name', 'label', 'expr', 'allArgs', 'params', 'otherArgs'] + otherCols)
	if rawTable.numRows < 2:
		return
	for row in range(1, rawTable.numRows):
		expr = str(rawTable[row, 'expr'] or '')
		allArgs = []
		params = []
		otherArgs = []
		if 'THIS_' in expr:
			allArgs = _argPattern.findall(expr)
			params = []
			otherArgs = []
			for arg in allArgs:
				if _paramNamePattern.fullmatch(arg):
					params.append(arg)
				else:
					otherArgs.append(arg)
		dat.appendRow([
			rawTable[row, 'name'],
			rawTable[row, 'label'] or rawTable[row, 'name'],
			expr,
			' '.join(allArgs),
			' '.join(params),
			' '.join(otherArgs),
		] + [
			rawTable[row, c]
			for c in otherCols
		])
