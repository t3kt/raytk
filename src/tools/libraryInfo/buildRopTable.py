def onCook(dat):
	ext.libraryInfo.buildROPTable(
		dat,
		thumbTable=dat.inputs[0],
		chipTable=dat.inputs[1])
