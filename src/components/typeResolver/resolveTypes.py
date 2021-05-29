def onCook(dat):
	dat.copy(dat.inputs[0])
	mod.typeResolver.resolveTypes(dat)
