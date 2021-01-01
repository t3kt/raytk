# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: 'DAT'):
	dat.clear()
	dat.appendCol([
		'objPath',
		'parPath',
	])
	dat.appendCol(['', ''])
	comp = parent().par.Object.eval()
	if not comp:
		return
	if comp.isObject:
		dat['objPath', 1] = comp.path
		return
	if comp.par['Translatex'] is not None and comp.par['Rotatex'] is not None and comp.par['Scalex'] is not None:
		dat['parPath', 1] = comp.path
		return
	geo = comp.op('./arcGeo')  # type: COMP
	if geo and geo.isObject:
		dat['objPath', 1] = geo.path
		return
	raise Exception(f'Unsupported object: {comp}')
