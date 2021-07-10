def onCook(dat):
	dat.copy(dat.inputs[0])
	mod.opDefinition.processInputDefinitionTypes(
		dat,
		dat.inputs[1],
	)
