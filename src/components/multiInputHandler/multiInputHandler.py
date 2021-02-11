# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildValidationErrors(dat: 'DAT', mergedDefs: 'DAT'):
	dat.clear()
	inputDefs = [
		table
		for table in ops('definition_?')
		if table.numRows > 1
	]
	minCount = int(parent().par.Minimuminputs)
	if len(inputDefs) < minCount:
		dat.appendRow(['path', 'level', 'message'])
		dat.appendRow([parent().path, 'error', f'Only {len(inputDefs)} provided, {minCount} required'])
	if mergedDefs.numRows < 2:
		return
	for typeCategory in ('coordType', 'contextType', 'returnType'):
		vals = [
			table[1, typeCategory].val
			for table in inputDefs
		]
		if len(set(vals)) > 1:
			if not dat.numRows:
				dat.appendRow(['path', 'level', 'message'])
			dat.appendRow([parent().path, 'error', f'Mismatched {typeCategory}: {" ".join(vals)}'])
