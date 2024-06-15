from raytkUtil import RaytkContext, IconColors

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: scriptDAT):
	dat.clear()
	context = RaytkContext()
	dat.appendRow(['version', context.toolkitVersion()])
	status = parent().par.Status.eval()
	if status == 'development':
		dat.appendRow(['status', 'development'])
		dat.appendRow(['bg'] + list(IconColors.betaBgColor))
		dat.appendRow(['fg'] + list(IconColors.betaFgColor))
	elif status == 'experimental':
		dat.appendRow(['status', 'experimental'])
		dat.appendRow(['bg'] + list(IconColors.experimentalBgColor))
		dat.appendRow(['fg'] + list(IconColors.experimentalFgColor))
	else:
		dat.appendRow(['status', ''])
		dat.appendRow(['bg'] + list(IconColors.defaultBgColor))
		dat.appendRow(['fg'] + list(IconColors.defaultFgColor))
