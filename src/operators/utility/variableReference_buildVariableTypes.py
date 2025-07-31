import raytkTypes

def onCook(dat):
	raytkTypes.buildTypeTable(dat, lambda dt: dt.isVariable)
