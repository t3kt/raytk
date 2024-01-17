# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onSetupParameters(dat):
	page = dat.appendCustomPage('Custom')
	page.appendPython('Parameter', label='Parameter')

def onCook(dat):
	dat.clear()
	dat.appendRow(['name', 'label'])
	p = dat.par.Parameter.eval()
	if p is None:
		return
	if not isinstance(p, Par):
		raise Exception('Parameter must be a Par reference')

	for n, l in zip(p.menuNames, p.menuLabels):
		dat.appendRow([n, l])
