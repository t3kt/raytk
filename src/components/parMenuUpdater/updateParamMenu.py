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
