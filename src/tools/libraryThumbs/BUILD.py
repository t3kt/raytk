# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildTaskContext
	from _stubs import *

context = args[0]  # type: BuildTaskContext

def runStage(stage: int):
	if stage == 0:
		context.log('Replicating thumbnail TOPs')
		repl = op('thumbFileReplicator')
		repl.par.recreateall.pulse()
	elif stage == 1:
		context.log('Reloading images')
		for o in ops('thumbImages/thumb_*'):
			o.par.reloadpulse.pulse()
	else:
		context.finishTask()
		return
	context.queueAction(runStage, stage + 1)

def stripCompiler():
	context.log('Stripping out the compiler')
	context.safeDestroyOp(op('compiler'))

runStage(0)
