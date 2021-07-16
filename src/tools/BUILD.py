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
		stripCompiler()
		context.queueAction(runStage, stage + 1)
	elif stage == 3:
		context.runBuildScript(
			op('palette/BUILD'),
			thenRun=context.finishTask,
			runArgs=[])

def stripCompiler():
	context.log('Stripping out the compiler')
	context.safeDestroyOp(op('compiler'))

runStage(0)
