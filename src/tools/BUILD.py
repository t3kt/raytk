# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildContext
	from _stubs import *

async def build(context: 'BuildContext'):
	await context.runBuildScript(op('inspector/BUILD'))
	await context.runBuildScript(op('updater/BUILD'))

	context.log('Stripping out the compiler')
	await context.yieldAsync()
	context.safeDestroyOp(op('compiler'))

	context.log('Stripping out the sceneEditor')
	await context.yieldAsync()
	context.safeDestroyOp(op('sceneEditor'))

	await context.runBuildScript(op('editorTools/BUILD'))

	await context.runBuildScript(op('palette/BUILD'))
