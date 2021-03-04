def updatePars():
	if not parent().par.Lockbuffermenu:
		return
	op('output_table_path').cook(force=True)
	dat = op('output_table')
	if dat.numRows < 2:
		return
	p = parent().par.Outputbuffer
	p.menuNames = dat.col('name')[1:]
	p.menuLabels = dat.col('label')[1:]

def onTableChange(dat):
	updatePars()
def onValueChange(*_):
	updatePars()