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
		names = [c.val for c in dat.col('name')[1:]]
		labels = [c.val for c in dat.col('label')[1:]]
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
