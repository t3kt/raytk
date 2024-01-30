# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

# me - this DAT.
# engineComp - the connected Engine COMP

# onInitialize(): if return value > 0, it will be
# called again after the returned number of frames.
# callCount increments with each attempt, starting at 1

def onInitialize(engineComp, callCount):
	print('ON INITIALIZE', engineComp, callCount)
	return 0

def onReady(engineComp):
	print('ON READY', engineComp)

def onStart(engineComp):
	print('ON START', engineComp)
	op('controller').InitializeEngine()
	return

def whileRunning(engineComp):
	return

def onDone(engineComp):
	print('ON DONE', engineComp)
	return

def onError(engineComp):
	print('ON ERROR', engineComp)
	return
	