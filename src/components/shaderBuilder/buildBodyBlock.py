def onCook(dat):
	dat.clear()
	dat.write(ext.shaderBuilder.buildBodyBlock(
		materialTable=op('material_table')))