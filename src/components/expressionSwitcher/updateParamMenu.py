def onTableChange(dat):
	host = parent().par.Hostop.eval()
	name = parent().par.Param.eval() if host else None
	par = host.par[name] if name else None
	if par is None:
		return
	par.menuNames = dat.col('name')[1:]
	par.menuLabels = dat.col('label')[1:]