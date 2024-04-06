# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildContext
	from navigator import Navigator
	from _stubs import *
	from components.opPicker.opPicker import OpPicker
	ext.navigator = Navigator(COMP())

async def build(context: 'BuildContext'):
	comp = parent()
	context.log('Processing navigator')
	await context.yieldAsync()
	ext.navigator.resetState()
	context.detachTox(comp)
	context.detachAllFileSyncDatsIn(comp, reloadFirst=True)
	context.lockBuildLockOps(comp)

	o = op('opPicker')  # type: OpPicker | COMP
	context.disableCloning(o)
	context.detachTox(o)
	if context.experimental:
		o.SetFilterToggles(alpha=True, beta=True, deprecated=True)

	context.log('Finished processing navigator')
