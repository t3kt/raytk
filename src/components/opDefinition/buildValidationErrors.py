def onCook(dat):
	dat.clear()
	ext.opDefinition.buildValidationErrors(
		dat,
		inputDefinitions=op('input_defs'),
		elementValidationErrors=ops('../*/validation_errors'),
	)
