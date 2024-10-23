# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from raytkBuild import BuildContext
	import libraryInfoExt
	mod.libraryInfoExt = libraryInfoExt

async def build(context: 'BuildContext'):
	context.log('Updating library info')
	context.detachTox(parent())
	context.safeDestroyOps(ops('write_*'))
	mod.libraryInfoExt.forceBuild()
	context.lockOps(ops('opCategoryTable', 'versionInfo', 'info_text'))
	context.disableCloning(parent())
	context.disableCloning(op('moduleInfoBuilder'))
