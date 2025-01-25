# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from opDefinition import OpDefinition
	ext.opDefinition = OpDefinition(COMP())

def onTableChange(dat):
	mod.opDefinition.ensureExt(parent())
	ext.opDefinition.onValidationChange(dat)
