def onPulse(par):
	ui.undo.startBlock('Create camera')
	if par.name == 'Createcamera':
		path = app.samplesFolder + '/Palette/Tools/camera.tox'
		if not mod.os.path.exists(path):
			path = app.samplesFolder + '/Comp/Tools/camera.tox'
		if not mod.os.path.exists(path):
			raise Exception('Camera tox not found!')
		cam = parent(2).loadTox(path)
	else:
		cam = parent(2).create(cameraCOMP)
	o = parent()
	o.par.Camera = cam
	cam.dock = o
	o.showDocked = True
	cam.nodeX = o.nodeX
	cam.nodeY = o.nodeY - o.nodeHeight - 120
	ui.undo.endBlock()
	