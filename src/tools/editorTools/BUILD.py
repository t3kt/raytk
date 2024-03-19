# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from raytkBuild import BuildContext
	from _stubs import *

async def build(context: 'BuildContext'):
	comp = parent()
	context.detachTox(comp)
	context.detachTox(op('exposeParamDialog'))
