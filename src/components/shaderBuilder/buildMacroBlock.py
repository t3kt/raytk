def onCook(dat):
	dat.clear()
	dat.write(ext.shaderBuilder.buildMacroBlock(
		macroTable=dat.inputs[0]))
