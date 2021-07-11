# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

import os.path

def _findCameraTox():
	for path in (
			app.samplesFolder + '/Palette/Tools/cameraViewport.tox',
			app.samplesFolder + '/Palette/Tools/camera.tox',
			app.samplesFolder + '/Comp/Tools/camera.tox',
	):
		if os.path.exists(path):
			return path

def onPulse(par):
	ui.undo.startBlock('Create camera')
	if par.name == 'Createcamera':
		path = _findCameraTox()
		if path:
			cam = parent(2).loadTox(path)
		else:
			msg = 'Unable to find camera tox from palette, using basic Camera COMP'
			ui.status = msg
			print(parent(), msg)
			cam = parent(2).create(cameraCOMP)
	else:
		cam = parent(2).create(cameraCOMP)
	o = parent()
	o.par.Camera = cam
	cam.dock = o
	o.showDocked = True
	cam.nodeX = o.nodeX
	cam.nodeY = o.nodeY - o.nodeHeight - 120
	ui.undo.endBlock()
