# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from opDefinition import OpDefinition
	ext.opDefinition = OpDefinition(COMP())

def onTableChange(dat):
	ext.opDefinition.onValidationChange(dat)
