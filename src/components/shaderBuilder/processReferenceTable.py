def onCook(dat):
	dat.clear()
	ext.shaderBuilder.processReferenceTable(
		dat,
		rawRefTable=dat.inputs[0],
		rawVarTable=dat.inputs[1]
	)
