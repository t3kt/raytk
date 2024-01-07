def onCook(dat):
	dat.clear()
	for i in range(1, 9):
		if op('definition_'+str(i)).numRows > 1:
			dat.appendRow(['THIS_INPUT_'+str(dat.numRows+1) + ' inputOp' + str(i)])
	dat.appendRow(['THIS_INPUT_COUNT ' + str(dat.numRows)])

