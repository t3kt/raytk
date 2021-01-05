# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from .palette import Palette
	from _stubs import *
	ext.palette = Palette(COMP())


context = args[0]  # type: BuildTaskContext


ext.palette.resetState()
comp = parent()

context.detachTox(comp)

context.finishTask()
