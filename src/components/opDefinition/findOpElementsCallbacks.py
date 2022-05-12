def onInitGetColumnNames(dat):
	return ['paramListTable', 'paramGroupTable', 'macroTable', 'placeholder1', 'code1', 'placeholder2', 'code2']

def onFindOPGetValues(dat, curOp, row):
	return [
		curOp.par['Paramlisttable'] or '',
		curOp.par['Paramgrouptable'] or '',
		curOp.par['Macrotable'] or '',
		curOp.par['Placeholder1'] or '',
		curOp.par['Code1'] or '',
		curOp.par['Placeholder2'] or '',
		curOp.par['Code2'] or '',
	]


def onFindOPGetInclude(dat, curOp, row):
	return True


def onOPFound(dat, curOp, row, results):
	return

	