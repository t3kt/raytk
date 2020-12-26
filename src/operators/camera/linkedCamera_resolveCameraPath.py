# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	cam = _getCam()
	dat.appendRow([cam or ''])

def _getCam():
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
