def onCook(dat):
	dat.clear()
	try:
		dat.write(ext.specPanel.generateSpec() or '')
	except Exception as err:
		dat.write(err)
