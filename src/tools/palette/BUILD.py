# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildContext
	from palette import Palette
	from _stubs import *
	from typing import Union
	from components.opPicker.opPicker import OpPicker
	ext.palette = Palette(COMP())

async def build(context: 'BuildContext'):
	context.log('Updating palette')
	comp = parent()

	if context.experimental:
		comp.par.Defaultshowalpha = True
		comp.par.Defaultshowbeta = True
		comp.par.Defaultshowdeprecated = True
	else:
		comp.par.Defaultshowalpha = False
		comp.par.Defaultshowbeta = True
		comp.par.Defaultshowdeprecated = False

	ext.palette.resetState()
	context.detachTox(comp)

	context.log('Updating opPicker')
	await context.yieldAsync()
	o = op('opPicker')  # type: Union[OpPicker, COMP]
	context.disableCloning(o)
	context.detachTox(o)
	if context.experimental:
		o.SetFilterToggles(alpha=True, beta=True, deprecated=True)
	o.SetThumbToggle(True)
