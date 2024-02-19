from raytkUtil import IconColors

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: scriptDAT):
	dat.clear()
	dat.appendRow(['name', 'r', 'g', 'b'])
	dat.appendRow(['default.bg', *IconColors.defaultBgColor])
	dat.appendRow(['default.fg', *IconColors.defaultFgColor])
	dat.appendRow(['alpha.bg', *IconColors.alphaBgColor])
	dat.appendRow(['alpha.fg', *IconColors.alphaFgColor])
	dat.appendRow(['beta.bg', *IconColors.betaBgColor])
	dat.appendRow(['beta.fg', *IconColors.betaFgColor])
	dat.appendRow(['deprecated.bg', *IconColors.deprecatedBgColor])
	dat.appendRow(['deprecated.fg', *IconColors.deprecatedFgColor])
	dat.appendRow(['experimental.bg', *IconColors.experimentalBgColor])
	dat.appendRow(['experimental.fg', *IconColors.experimentalFgColor])
