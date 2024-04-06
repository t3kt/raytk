# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onStartup():
	_updatePrimaryInput()
	_fixPixelFormat()

def onParamPulse(par):
	if par.name == 'Initialize':
		_updatePrimaryInput()
		_fixPixelFormat()

def onParamChange(par):
	if par.name == 'Useprimaryinput':
		_updatePrimaryInput()

def _updatePrimaryInput():
	render = op('render_glsl')
	primaryInput = op('primaryImage_in')
	if parent().par.Useprimaryinput:
		if primaryInput not in render.inputs:
			render.inputConnectors[0].connect(primaryInput)
	else:
		if primaryInput in render.inputs:
			render.inputConnectors[0].disconnect()

def _fixPixelFormat():
	render = op('render_glsl')
	render.par.format.mode = ParMode.CONSTANT
	render.par.format.mode = ParMode.BIND
