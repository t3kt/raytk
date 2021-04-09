# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .testEditor import TestEditor
	# noinspection PyTypeChecker
	ext.testEditor = TestEditor(COMP())

def onPreCook(changeOp):
	return

def onPostCook(changeOp):
	return

def onDestroy():
	return

def onFlagChange(changeOp, flag):
	return

def onWireChange(changeOp):
	return

def onNameChange(changeOp):
	return

def onPathChange(changeOp):
	return

def onUIChange(changeOp):
	return

def onNumChildrenChange(changeOp):
	ext.testEditor.reloadOutputs()

def onChildRename(changeOp):
	ext.testEditor.reloadOutputs()

def onCurrentChildChange(changeOp):
	return

def onExtensionChange(changeOp, extension):
	return
	