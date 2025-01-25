def onCook(dat):
	mod.opDefinition.ensureExt(parent())
	dat.clear()
	ext.opDefinition.buildValidationErrors(
		dat,
		inputDefinitions=op('input_defs'),
		elementValidationErrors=ops('../*/validation_errors'),
	)
