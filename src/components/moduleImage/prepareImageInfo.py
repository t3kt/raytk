from raytkUtil import RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: scriptDAT):
	dat.clear()
	dat.appendRow(['name', ''])
	dat.appendRow(['status', ''])
	context = RaytkContext()
	moduleDef = parent().par.Moduledefinition.eval()
	if moduleDef:
		dat['name', 1] = moduleDef.par.Modulename.eval()
		if context.develMode():
			dat['status', 1] = 'development'
		elif moduleDef.par.Experimentalbuild:
			dat['status', 1] = 'experimental'
		else:
			dat['status', 1] = ''
