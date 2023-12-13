from raytkUtil import IconColors, RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: DAT):
	dat.clear()
	context = RaytkContext()
	dat.appendRow(['toolkitVersion', context.toolkitVersion()])
	if context.develMode():
		dat.appendRow(['status', 'development'])
		dat.appendRow(['bg'] + list(IconColors.betaBgColor))
		dat.appendRow(['fg'] + list(IconColors.betaFgColor))
	elif context.experimentalMode():
		dat.appendRow(['status', 'experimental'])
		dat.appendRow(['bg'] + list(IconColors.experimentalBgColor))
		dat.appendRow(['fg'] + list(IconColors.experimentalFgColor))
	else:
		dat.appendRow(['status', ''])
		dat.appendRow(['bg'] + list(IconColors.defaultBgColor))
		dat.appendRow(['fg'] + list(IconColors.defaultFgColor))
