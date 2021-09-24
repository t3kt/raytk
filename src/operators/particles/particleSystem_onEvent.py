def _reset():
	parent().par.Resetpulse.pulse()

def onStart():
	_reset()

def onCreate():
	_reset()
	