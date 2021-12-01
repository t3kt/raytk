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
		repl = op('thumbFileReplicator')
		context.log(f'Destroying replicator {repl}')
		context.safeDestroyOp(repl)
		thumbs = ops('thumbImages/thumb_*')
		context.log(f'Post replication, have {len(thumbs)} thumb images')
	elif stage == 2:
		context.log('Reloading images')
		thumbs = ops('thumbImages/thumb_*')
		context.log(f'Found {len(thumbs)} images')
		for o in thumbs:
			o.par.reloadpulse.pulse()
	elif stage == 3:
		context.log('Locking images')
		thumbs = ops('thumbImages/thumb_*')
		context.lockOps(thumbs)
		context.safeDestroyOps(ops('imageTemplate', 'layoutThumbImages'))
	else:
		context.finishTask()
		return
	context.queueAction(runStage, stage + 1)

runStage(0)
