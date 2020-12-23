# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: 'DAT'):
	dat.clear()
	for table in dat.inputs:
		if table.numCols == 3:
			dat.appendRows(table.rows())
		elif table.numCols < 3:
			dat.appendRows([
				[''] + [c.val for c in cells]
				for cells in table.rows()
			])
		else:
			dat.appendRows([
				[cells[0], cells[1], ' '.join([c.val for c in cells[2:]])]
				for cells in table.rows()
			])
