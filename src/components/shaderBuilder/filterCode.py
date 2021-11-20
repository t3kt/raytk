def onCook(dat):
	dat.clear()
	dat.write(ext.shaderBuilder.filterCode(dat.inputs[0].text, typeDefMacroTable=dat.inputs[1]))

