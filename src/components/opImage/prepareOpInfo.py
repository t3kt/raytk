from raytkUtil import ROPInfo, IconColors

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: DAT):
	dat.clear()
	info = ROPInfo(parent().par.Definitionop.eval())
	dat.appendRow(['res', 320, 256])
	dat.appendRow(['name', ''])
	dat.appendRow(['category', ''])
	dat.appendRow(['toolkitVersion', ''])
	dat.appendRow(['statusIcon', ''])
	dat.appendRow(['useOverlay', '0'])
	dat.appendRow(['fg'] + list(IconColors.defaultFgColor))
	dat.appendRow(['bg'] + list(IconColors.defaultBgColor))
	if not info:
		return
	showStatus = True
	if info.opStyle == 'variable':
		dat['category', 1] = 'variable'
		dat['useOverlay', 1] = '1'
		# dat.replaceRow('res', ['res', 256, 160])
		showStatus = False
	else:
		dat['name', 1] = info.shortName or ''
		dat['category', 1] = info.categoryName or ''
	version = info.toolkitVersion
	if version:
		version = 'v' + version
	dat['toolkitVersion', 1] = version or ''
	if info.isDeprecated:
		if showStatus:
			dat['statusIcon', 1] = '\uFB7E'
		dat.replaceRow('fg', ['fg'] + list(IconColors.deprecatedFgColor))
		dat.replaceRow('bg', ['bg'] + list(IconColors.deprecatedBgColor))
	elif info.isAlpha:
		if showStatus:
			dat['statusIcon', 1] = '\uF02B'
		dat.replaceRow('fg', ['fg'] + list(IconColors.alphaFgColor))
		dat.replaceRow('bg', ['bg'] + list(IconColors.alphaBgColor))
	elif info.isBeta:
		if showStatus:
			dat['statusIcon', 1] = '\uF0A1'
		dat.replaceRow('fg', ['fg'] + list(IconColors.betaFgColor))
		dat.replaceRow('bg', ['bg'] + list(IconColors.betaBgColor))
