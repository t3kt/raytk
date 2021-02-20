# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .outputOpController import OutputOp

	# noinspection PyTypeChecker
	ext.outputOp = OutputOp(COMP())

def onStart():
	ext.outputOp.onInit()

def onCreate():
	ext.outputOp.onInit()
