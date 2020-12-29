# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from _stubs import *

context = args[0]  # type: BuildTaskContext

def runStage(stage: int):
	if stage == 0:
		context.runBuildScript(
			op('createMenu/BUILD'),
			thenRun=runStage,
			runArgs=[stage + 1])
	elif stage == 1:
		context.runBuildScript(
			op('inspector/BUILD'),
			thenRun=runStage,
			runArgs=[stage + 1])
	elif stage == 2:
		context.runBuildScript(
			op('palette/BUILD'),
			thenRun=context.finishTask,
			runArgs=[])

runStage(0)
