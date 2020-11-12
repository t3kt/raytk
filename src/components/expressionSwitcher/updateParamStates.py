def onValueChange(par, prev):
	allParams = op('allParams').col(0)
	
	currentParams = str(op('currentExpr')[1, 'params'] or '').split(' ')
	for par in par.owner.pars(*allParams):
		par.enable = par.name in currentParams