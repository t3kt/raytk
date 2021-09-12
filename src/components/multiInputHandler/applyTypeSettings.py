def onCook(dat):
	dat.copy(dat.inputs[0])
	mod.multiInputHandler.applyTypeSettings(
		dat,
		index=dat.digits,
		typeSettings=op('typeSettings'),
	)
