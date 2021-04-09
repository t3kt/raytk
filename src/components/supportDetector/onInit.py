# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .supportDetector import buildSupportTable

	mod = object()
	mod.supportDetector = object()
	mod.supportDetector.buildSupportTable = buildSupportTable

def _rebuildTable():
	mod.supportDetector.buildSupportTable(
		op('set_support_table'),
		op('glsl_include_test_top'),
	)

def onStart():
	_rebuildTable()

def onCreate():
	_rebuildTable()
