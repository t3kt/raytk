# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from . import opDefinition as _opDef
	mod.opDefinition = _opDef

def onPulse(par):
	action = par.name
	if action == 'Inspect':
		mod.opDefinition.inspect(par.owner)
	elif action == 'Help':
		mod.opDefinition.launchHelp()
	elif action == 'Updateop':
		mod.opDefinition.updateOP()
