def onCook(dat):
	ext.opDefinition.combineInputDefinitions(
		dat,
		inDats=dat.inputs,
		defFields=op('inlineFields'),
		supportedTypeTable=op('supportedTypes'),
		)
