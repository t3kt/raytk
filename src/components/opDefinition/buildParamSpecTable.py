def onCook(dat):
	mod.opDefinition.buildParamSpecTable(
		dat,
		paramListTable=dat.inputs[0],
		paramGroupTable=parent().par.Paramgrouptable.eval())