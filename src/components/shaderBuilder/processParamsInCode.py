def onCook(dat):
	dat.copy(dat.inputs[0])
	dat.text = ext.shaderBuilder.processParametersInCode(dat.text)
	
