def onCook(dat):
	dat.clear()
	dat.write(ext.shaderBuilder.buildOpDataTypedefBlock(typeDefMacroTable=dat.inputs[0]))
