def onValueChange(par, prev):
	if par.name == 'Autoupdateparams' and par:
		mod.codeSwitcher.updateParams()

def onPulse(par):
	if par.name == 'Updateparams':
		mod.codeSwitcher.updateParams()
