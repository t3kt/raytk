# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildValidationErrors(dat: 'DAT', mergedDefs: 'DAT'):
	dat.clear()
	if mergedDefs.numRows < 2:
		return
	for typeCategory in ('coordType', 'contextType', 'returnType'):
		vals = [c.val for c in mergedDefs.col(typeCategory)[1:]]
		if len(set(vals)) > 1:
			if not dat.numRows:
				dat.appendRow(['path', 'level', 'message'])
			dat.appendRow([parent().path, 'error', f'Mismatched {typeCategory}: {" ".join(vals)}'])
