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
		mod.opDefinition.inspect(par.owner)
	elif action == 'Help':
		mod.opDefinition.launchHelp()
	elif action == 'Updateop':
		mod.opDefinition.updateOP()
	elif action.startswith('Createref'):
		ext.opDefinition.createVarRef(action.replace('Createref', ''))
