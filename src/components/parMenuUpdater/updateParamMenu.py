def update():
	try:
		host = parent().par.Hostop.eval()
		name = parent().par.Param.eval() if host else None
		par = host.par[name] if name else None
		if par is None:
			return
		dat = parent().par.Table.eval()
		if not dat or dat.numRows < 2:
			return
		par.menuNames = dat.col('name')[1:]
		par.menuLabels = dat.col('label')[1:]
	except BaseException as e:
		print(f'Error attempting to update paramMenu in {parent()}: {e}')


def onValueChange(par, prev):
	if par.name == 'Autoupdate' and par:
		update()

def onTableChange(dat):
	update()

def onPulse(par):
	if par.name == 'Update':
		update()
