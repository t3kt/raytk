# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from compDefinition import CompDefinition
	ext.compDefinition = CompDefinition(COMP())

def onPulse(par):
	action = par.name
	mod.compDefinition.ensureExt(parent())
	if action == 'Inspect':
		ext.compDefinition.inspect()
	elif action == 'Help':
		ext.compDefinition.launchHelp()
	elif action == 'Updateop':
		ext.compDefinition.updateOP()