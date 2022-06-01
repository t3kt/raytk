def onCook(dat):
	mod.opDefinition.prepareMacroTable(
		dat,
		inputTable=dat.inputs[0],
		paramSpecTable=dat.inputs[1],
		paramTupletTable=dat.inputs[2])
