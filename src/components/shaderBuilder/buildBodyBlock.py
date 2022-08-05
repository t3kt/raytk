def onCook(dat):
	dat.clear()
	dat.write(ext.shaderBuilder.buildBodyBlock(
		dispatchTable=op('dispatch_table')))