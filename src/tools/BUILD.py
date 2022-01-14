# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from _stubs import *

context = args[0]  # type: BuildTaskContext

def runStage(stage: int):
	if stage == 0:
		context.runBuildScript(
			op('inspector/BUILD'),
			thenRun=runStage,
			runArgs=[stage + 1])
	elif stage == 1:
		context.runBuildScript(
			op('updater/BUILD'),
			thenRun=runStage,
			runArgs=[stage + 1])
	elif stage == 2:
		context.log('Stripping out the compiler')
		context.safeDestroyOp(op('compiler'))
		context.queueAction(runStage, stage + 1)
	elif stage == 3:
		context.log('Stripping out the sceneEditor')
		context.safeDestroyOp(op('sceneEditor'))
		context.queueAction(runStage, stage + 1)
	elif stage == 4:
		if not context.experimental:
			context.log('Stripping out the editorTools')
			context.safeDestroyOp(op('editorTools'))
			context.queueAction(runStage, stage + 1)
		else:
			context.runBuildScript(
				op('editorTools/BUILD'),
				thenRun=runStage,
				runArgs=[stage + 1])
	elif stage == 5:
		context.runBuildScript(
			op('palette/BUILD'),
			thenRun=context.finishTask,
			runArgs=[])

runStage(0)
