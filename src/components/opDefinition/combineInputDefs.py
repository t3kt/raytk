def onCook(dat):
	mod.opDefinition.combineInputDefinitions(
		dat,
		inDats=dat.inputs,
		defFields=op('inlineFields'),
		)
