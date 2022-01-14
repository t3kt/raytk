# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from _stubs import *


context = args[0]  # type: BuildTaskContext

comp = parent()

context.detachTox(comp)

context.finishTask()
