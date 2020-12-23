# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: 'DAT'):
	dat.clear()
	for table in dat.inputs:
		if table.numCols == 0:
			continue
		elif table.numCols == 3:
			dat.appendRows(table.rows())
		elif table.numCols == 1:
			dat.appendRows([
				[''] + [c.val] + ['']
				for c in table.col(0)
			])
		elif table.numCols == 2:
			dat.appendRows([
				['', cells[0], cells[1]]
				for cells in table.rows()
			])
		else:
			dat.appendRows([
				[cells[0], cells[1], ' '.join([c.val for c in cells[2:]])]
				for cells in table.rows()
			])
