def onValueChange(par, prev):
	if par.name == 'Locked':
		mod.sceneState.updateLockStates(par.eval())

def onPulse(par):
	if par.name == 'Update':
		mod.sceneState.updateLockStates(parent().par.Locked.eval())
