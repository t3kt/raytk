import os.path
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def _findCameraTox():
	for path, pattern in (
			(app.samplesFolder + '/Palette/Tools/cameraViewport.tox', 'cameraViewport'),
			(app.samplesFolder + '/Palette/Tools/camera.tox', None),
			(app.samplesFolder + '/Comp/Tools/camera.tox', None),
	):
		if os.path.exists(path):
			return path, pattern
		return None, None

def onCreatePulse(par: Par):
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

def getCam() -> 'Optional[cameraCOMP]':
	cam = parent().par.Camera.eval()
	if not cam:
		return None
	if cam.par['Cameraobj']:
		cam = cam.par.Cameraobj.eval()
	elif cam.op('cam1'):
		cam = cam.op('cam1')
	if isinstance(cam, cameraCOMP):
		return cam
	return None

def isUsingCustomProjection():
	cam = getCam()
	return bool(cam and cam.par['projection'] == 'custommatrix')

def buildCustomMatrixChans(chop: 'scriptCHOP'):
	chop.clear()
	if isUsingCustomProjection():
		m = getCam().projection(parent().par.Resx, parent().par.Resy)
	else:
		m = tdu.Matrix()
		m.identity()
	for r in range(4):
		for c in range(4):
			chop.appendChan(f'p{r}{c}')[0] = m[r, c]
