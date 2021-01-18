# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .testEditor import TestEditor
	# noinspection PyTypeChecker
	ext.testEditor = TestEditor(COMP())

# def onInit(info):
# 	info['listerExt'].DefaultRoots = ['/None']

# def getObjectFromID(info):
# 	return {'name': 'TreeObject'}

# def getIDFromObject(info):
# 	return '/None'

# def getObjectChildren(info):
# 	return []

def onSelectRow(info):
	ext.testEditor.listOnSelectRow(info)

def onClick(info):
	ext.testEditor.listOnClick(info)
