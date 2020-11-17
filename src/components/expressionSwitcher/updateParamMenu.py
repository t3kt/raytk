def update():
	host = parent().par.Hostop.eval()
	name = parent().par.Param.eval() if host else None
	par = host.par[name] if name else None
	if par is None:
		return
	dat = op('table')
	par.menuNames = dat.col('name')[1:]
	par.menuLabels = dat.col('label')[1:]

def onTableChange(dat):
	update()

def onPulse(par):
	update()
