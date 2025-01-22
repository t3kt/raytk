def onCook(dat):
	ext.opDefinition.buildDefinitionTable(dat,
		supportedTypes=dat.inputs[0],
		inputDefs=op('input_def_1'))
