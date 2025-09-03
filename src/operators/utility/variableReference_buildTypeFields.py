import raytkTypes

def onCook(dat):
	raytkTypes.buildTypeFieldTable(dat, lambda dt: dt.isVariable)
