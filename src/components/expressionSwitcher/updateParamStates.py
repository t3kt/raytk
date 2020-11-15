def onValueChange(par, prev):
	allParams = op('allParams').col(0)
	
	currentParams = str(op('currentExpr')[1, 'params'] or '').split(' ')
	if not currentParams:
		return
	pars = par.owner.pars(*allParams)
	if not pars:
		return
	for par in pars:
		par.enable = par.name in currentParams
