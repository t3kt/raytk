from raytkUtil import ROPInfo, IconColors

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: 'DAT'):
	dat.clear()
	info = ROPInfo(parent().par.Definitionop.eval())
	if not info:
		dat.appendRow(['typeName', ''])
		dat.appendRow(['category', ''])
	else:
		dat.appendRow(['typeName', info.shortName or ''])
		dat.appendRow(['category', info.categoryName or ''])
	if info and info.isDeprecated:
		dat.appendRow(['statusIcon', '\uFB7E'])
		dat.appendRow(['fg'] + list(IconColors.deprecatedFgColor))
		dat.appendRow(['bg'] + list(IconColors.deprecatedBgColor))
	elif info and info.isAlpha:
		dat.appendRow(['statusIcon', '\uF02B'])
		dat.appendRow(['fg'] + list(IconColors.alphaFgColor))
		dat.appendRow(['bg'] + list(IconColors.alphaBgColor))
	elif info and info.isBeta:
		dat.appendRow(['statusIcon', '\uF0A1'])
		dat.appendRow(['fg'] + list(IconColors.betaFgColor))
		dat.appendRow(['bg'] + list(IconColors.betaBgColor))
	else:
		dat.appendRow(['statusIcon', ''])
		dat.appendRow(['fg'] + list(IconColors.defaultFgColor))
		dat.appendRow(['bg'] + list(IconColors.defaultBgColor))
