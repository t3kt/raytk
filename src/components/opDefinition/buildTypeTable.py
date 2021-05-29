def onCook(dat):
	mod.opDefinition.buildTypeTable(
		dat,
		supportedTypes=dat.inputs[0],
		inputDefs=dat.inputs[1])
