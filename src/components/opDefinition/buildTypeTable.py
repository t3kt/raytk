def onCook(dat):
	mod.opDefinition.buildTypeTable(
		dat,
		supportedTypes=dat.inputs[0],
		inputDefs=op('input_def_1'))
