def onCook(dat):
	mod.multiInputHandler.buildValidationErrors(
		dat,
		dat.inputs[0],
		typeSettings=op('typeSettings'))