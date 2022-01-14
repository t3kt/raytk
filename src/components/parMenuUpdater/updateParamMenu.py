# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def update():
	try:
		host = parent().par.Hostop.eval()
		if not host:
			return
		dat = parent().par.Table.eval()
		if not dat or dat.numRows < 2:
			return
		names = []
		labels = []
		for i in range(1, dat.numRows):
			name = dat[i, 'name'].val
			if name.startswith('-'):
				continue
			names.append(name)
			labels.append(dat[i, 'label'].val)
		pars = host.pars(*(mod.tdu.split(parent().par.Param)))
		for par in pars:
			par.menuNames = names
			par.menuLabels = labels
		if parent().par.Manageparamstates:
			updateParamEnableExprs(host, dat)
	except BaseException as e:
		print(f'Error attempting to update paramMenu in {parent()}: {e}')

def updateParamEnableExprs(host: 'OP', table: 'DAT'):
	hostPar = host.par[parent().par.Param]
	if hostPar is None:
		return
	paramModes = _paramModes(table)
	allValues = set(paramModes.keys())
	for param, vals in paramModes.items():
		par = host.par[param]
		if set(vals) == allValues:
			par.enableExpr = ''
			par.enable = True
		else:
			par.enableExpr = f'me.par.{hostPar.name} in {repr(tuple(vals))}'

def _paramModes(table: 'DAT'):
	paramModes = {}
	for i in range(1, table.numRows):
		params = tdu.expand(table[i, 'params'].val)
		val = table[i, 'name'].val
		for param in params:
			if param in paramModes:
				paramModes[param].append(val)
			else:
				paramModes[param] = [val]
	return paramModes

def onValueChange(par, prev):
	if par.name == 'Autoupdate' and par:
		update()

def onTableChange(dat):
	update()

def onPulse(par):
	if par.name == 'Update':
		update()
