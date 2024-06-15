from raytkUtil import IconColors, RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: DAT):
	dat.clear()
	context = RaytkContext()
	if context.develMode():
		dat.appendRow(['status', 'development'])
	elif context.experimentalMode():
		dat.appendRow(['status', 'experimental'])
	else:
		dat.appendRow(['status', ''])

