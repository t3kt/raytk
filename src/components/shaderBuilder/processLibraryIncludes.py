def onCook(dat):
	dat.copy(dat.inputs[0])
	dat.text = ext.shaderBuilder.processLibraryIncludes(dat.text)
	
