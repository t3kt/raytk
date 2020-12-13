def show():
	w = op('splash_window')
	w.par.winopen.pulse()
	if parent().par.Autohide:
		run('args[0]()', hide, delayMilliSeconds=1000*parent().par.Duration)

def hide():
	w = op('splash_window')
	w.par.winclose.pulse()


def onPulse(par):
	show()

def onStart():
	show()