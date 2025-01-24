def onValueChange(par, prev):
	if par.name == 'Autoupdateparams' and par:
		mod.codeSwitcher.CodeSwitcher(parent()).updateParams()

def onPulse(par):
	if par.name == 'Updateparams':
		mod.codeSwitcher.CodeSwitcher(parent()).updateParams()
