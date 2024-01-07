def onCook(dat):
	dat.clear()
	mod.opDefinition.buildValidationErrors(
		dat,
		inputDefinitions=op('input_defs'),
		elementValidationErrors=ops('../*/validation_errors'),
	)
