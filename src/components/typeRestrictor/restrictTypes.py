def onCook(dat):
	dat.copy(dat.inputs[0])
	mod.typeRestrictor.restrictTypes(
		dat,
		supportedTypes=dat.inputs[1])
