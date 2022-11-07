# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

import os.path

def _findCameraTox():
	for path, pattern in (
			(app.samplesFolder + '/Palette/Tools/cameraViewport.tox', 'cameraViewport'),
			(app.samplesFolder + '/Palette/Tools/camera.tox', None),
			(app.samplesFolder + '/Comp/Tools/camera.tox', None),
	):
		if os.path.exists(path):
			return path, pattern
		return None, None

def onPulse(par):
	ui.undo.startBlock('Create camera')
	if par.name == 'Createcamera':
		path, pattern = _findCameraTox()
		if path:
			cam = parent(2).loadTox(path, pattern=pattern)
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
