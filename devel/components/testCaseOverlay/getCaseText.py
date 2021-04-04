# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	mode = parent().par.Labeltype
	if mode == 'menupar':
		o = op(parent().par.Targetop)
		par = o.par[parent().par.Param]
		text = par.menuLabels[int(par)]
		if parent().par.Showparname:
			text = par.label + ': ' + text
	else:
		text = parent().par.Label

	suffix = parent().par.Suffix
	if suffix:
		if text and not suffix.startswith(' '):
			suffix = ' ' + suffix
		text += suffix
	dat.appendRow([text])
