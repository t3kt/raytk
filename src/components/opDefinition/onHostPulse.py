# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from . import opDefinition as _opDef
	from opDefinition import OpDefinition
	mod.opDefinition = _opDef
	ext.opDefinition = OpDefinition(COMP())

def onPulse(par):
	action = par.name
	if action == 'Inspect':
		ext.opDefinition.inspect()
	elif action == 'Help':
		ext.opDefinition.launchHelp()
	elif action == 'Updateop':
		ext.opDefinition.updateOP()
	elif action.startswith('Createref'):
		ext.opDefinition.createVarRef(action.replace('Createref', ''))
	elif action.startswith('Creatersel'):
		ext.opDefinition.createRenderSel(action.replace('Creatersel', ''))
