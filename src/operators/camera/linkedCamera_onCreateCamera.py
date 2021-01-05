def onPulse(par):
	ui.undo.startBlock('Create camera')
	if par.name == 'Createcamera':
		cam = parent(2).loadTox(app.samplesFolder +'/Comp/Tools/camera.tox')
	else:
		cam = parent(2).create(cameraCOMP)
	o = parent()
	o.par.Camera = cam
	cam.dock = o
	o.showDocked = True
	cam.nodeX = o.nodeX
	cam.nodeY = o.nodeY - o.nodeHeight - 120
	ui.undo.endBlock()
	