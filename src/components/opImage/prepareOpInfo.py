from raytkUtil import ROPInfo

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
		dat.appendRow(['fg'] + list(_deprecatedFgColor))
		dat.appendRow(['bg'] + list(_deprecatedBgColor))
	elif info and info.isAlpha:
		dat.appendRow(['statusIcon', '\uF02B'])
		dat.appendRow(['fg'] + list(_alphaFgColor))
		dat.appendRow(['bg'] + list(_alphaBgColor))
	elif info and info.isBeta:
		dat.appendRow(['statusIcon', '\uF0A1'])
		dat.appendRow(['fg'] + list(_betaFgColor))
		dat.appendRow(['bg'] + list(_betaBgColor))
	else:
		dat.appendRow(['statusIcon', ''])
		dat.appendRow(['fg'] + list(_defaultFgColor))
		dat.appendRow(['bg'] + list(_defaultBgColor))

_defaultBgColor = 0.0477209, 0.111349, 0.114
_defaultFgColor = 0.135166, 0.816, 0.816
_alphaBgColor = 0.24, 0.306, 0.405
_alphaFgColor = _defaultFgColor
_betaBgColor = 0.1, 0.155, 0.238
_betaFgColor = _defaultFgColor
_deprecatedBgColor = 0.185, 0.21, 0.21
_deprecatedFgColor = 0.635, 0.816, 0.816

