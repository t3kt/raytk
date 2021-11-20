def onCook(dat):
	dat.clear()
	dat.write(ext.shaderBuilder.buildLibraryIncludes(
		onWarning=dat.addWarning
	))
