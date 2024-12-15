# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	dat.appendRow([getMessage() or ''])

def getMessage():
	toolkit = getattr(op, 'raytk', None)
	if not toolkit:
		return 'RayTK\nComp\nMissing'
	modDef = parent().par.Moduledefinition.eval()
	if not modDef:
		return
	modVersion = modDef.par.Raytkversion.eval()
	toolkitVersion = toolkit.par.Raytkversion.eval()
	if modVersion != toolkitVersion:
		return f'RayTK\nComp\nVersion Mismatch\n\nRayTK: {toolkitVersion}\nComp: {modVersion}'
