# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	mode = parent().par.Labeltype.eval()
	if mode == 'par':
		o = op(parent().par.Targetop)
		par = o.par[parent().par.Param]
		if par is None:
			text = ''
		elif par.isMenu:
			text = par.menuLabels[int(par)]
		elif par.isFloat:
			text = str(round(par.eval(), 4))
		else:
			text = str(par)
		if par is not None and parent().par.Showparname:
			text = par.label + ': ' + text
	else:
		text = parent().par.Label

	suffix = parent().par.Suffix.eval()
	if suffix:
		if text and not suffix.startswith(' '):
			suffix = ' ' + suffix
		text += suffix
	text = str(text or '').replace('|', '\n')
	dat.write(text)
