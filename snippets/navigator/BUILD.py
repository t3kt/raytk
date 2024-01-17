# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from navigator import Navigator
	from _stubs import *
	from components.opPicker.opPicker import OpPicker
	ext.navigator = Navigator(COMP())

context = args[0]  # type: BuildTaskContext

context.log('Processing navigator')

ext.navigator.resetState()
comp = parent()
context.detachTox(comp)
context.detachAllFileSyncDatsIn(comp, reloadFirst=True)
context.lockBuildLockOps(comp)

o = op('opPicker')  # type: OpPicker | COMP
context.disableCloning(o)
context.detachTox(o)
if context.experimental:
	o.SetFilterToggles(alpha=True, beta=True, deprecated=True)

context.log('Finished processing navigator')
context.finishTask()
