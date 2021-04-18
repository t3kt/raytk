def onCook(dat):
	dat.copy(dat.inputs[0])
	ext.shaderBuilder.preprocessDefinitions(dat)
