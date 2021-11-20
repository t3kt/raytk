def onCook(dat):
	dat.clear()
	ext.shaderBuilder.processVariableTable(
		dat,
		rawVarTable=dat.inputs[0],
		procRefTable=dat.inputs[1]
	)
