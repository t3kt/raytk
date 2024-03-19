# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildContext
	from _stubs import *

async def build(context: 'BuildContext'):
	context.log('Updating updater')
	comp = parent()
	context.detachTox(comp)
