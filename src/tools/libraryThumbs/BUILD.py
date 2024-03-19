# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildContext
	from _stubs import *

async def build(context: 'BuildContext'):
	context.detachTox(parent())

	context.log('Replicating thumbnail TOPs')
	await context.yieldAsync()
	repl = op('thumbFileReplicator')
	repl.par.recreateall.pulse()

	context.log(f'Destroying replicator {repl}')
	await context.yieldAsync()
	context.safeDestroyOp(repl)
	thumbs = ops('thumbImages/thumb_*')
	context.log(f'Post replication, have {len(thumbs)} thumb images')
	await context.yieldAsync()

	context.log('Reloading images')
	await context.yieldAsync()
	thumbs = ops('thumbImages/thumb_*')
	context.log(f'Found {len(thumbs)} images')
	for o in thumbs:
		o.par.reloadpulse.pulse()
	await context.yieldAsync()

	context.log('Locking images')
	await context.yieldAsync()
	thumbs = ops('thumbImages/thumb_*')
	context.lockOps(thumbs)
	context.safeDestroyOps(ops('imageTemplate', 'layoutThumbImages'))
	await context.yieldAsync()
