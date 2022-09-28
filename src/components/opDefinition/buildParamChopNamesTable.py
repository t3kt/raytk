def onCook(dat):
	dat.clear()
	mod.opDefinition.buildParamChopNamesTable(
		dat,
		paramSpecTable=dat.inputs[0])