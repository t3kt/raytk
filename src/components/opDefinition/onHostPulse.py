# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from opDefinition import OpDefinition
	ext.opDefinition = OpDefinition(COMP())

def onPulse(par):
	mod.opDefinition.ensureExt(parent())
	action = par.name
	if action == 'Inspect':
		ext.opDefinition.inspect()
	elif action == 'Help':
		ext.opDefinition.launchHelp()
	elif action == 'Updateop':
		mod.opDefinition.updateOP()
	elif action.startswith('Createref'):
		ext.opDefinition.createVarRef(action.replace('Createref', ''))
	elif action.startswith('Creatersel'):
		ext.opDefinition.createRenderSel(action.replace('Creatersel', ''))
