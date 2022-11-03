def onCook(dat):
	dat.clear()
	ext.shaderBuilder.processVariableTable(
		dat,
		procRefTable=dat.inputs[0]
	)
