# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from compDefinition import CompDefinition
	ext.compDefinition = CompDefinition(COMP())

def onPulse(par):
	action = par.name
	if action == 'Inspect':
		ext.compDefinition.inspect()
	elif action == 'Help':
		ext.compDefinition.launchHelp()
	elif action == 'Updateop':
		mod.compDefinition.updateOP()