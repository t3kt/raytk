# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from _stubs import *

context = args[0]  # type: BuildTaskContext

def clean():
	context.log('Cleaning unecessary OPs')
	for o in parent().findChildren(type=COMP, maxDepth=1):
		context.disableCloning(o)
		context.detachTox(o)
	for o in parent().findChildren(type=DAT, maxDepth=1):
		if o is me:
			continue
		context.detachDat(o)

def runStage(stage: int):
	if stage == 0:
		clean()
		context.queueAction(runStage, stage + 1)
	elif stage == 1:
		context.finishTask()

runStage(0)
