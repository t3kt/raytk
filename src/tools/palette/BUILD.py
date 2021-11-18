# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from .palette import Palette
	from _stubs import *
	from typing import Union
	from components.opPicker.opPicker import OpPicker
	ext.palette = Palette(COMP())


context = args[0]  # type: BuildTaskContext


ext.palette.resetState()
comp = parent()
context.detachTox(comp)
if context.experimental:
	comp.par.Defaultshowalpha = True
	comp.par.Defaultshowbeta = True
	comp.par.Defaultshowdeprecated = True
else:
	comp.par.Defaultshowalpha = False
	comp.par.Defaultshowbeta = True
	comp.par.Defaultshowdeprecated = False

o = op('opPicker')  # type: Union[OpPicker, COMP]
context.disableCloning(o)
context.detachTox(o)
if context.experimental:
	o.SetFilterToggles(alpha=True, beta=True, deprecated=True)

context.finishTask()
