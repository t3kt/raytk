# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .opPicker import OpPicker
	ext.opPicker = OpPicker(COMP())

def onInitCell(comp, row, col, attribs):
	if hasattr(ext.opPicker, 'onInitCell'):
		ext.opPicker.onInitCell(row, col, attribs)
def onInitRow(comp, row, attribs):
	if hasattr(ext.opPicker, 'onInitRow'):
		ext.opPicker.onInitRow(row, attribs)
def onInitCol(comp, col, attribs):
	if hasattr(ext.opPicker, 'onInitCol'):
		ext.opPicker.onInitCol(col, attribs)
def onInitTable(comp, attribs):
	if hasattr(ext.opPicker, 'onInitTable'):
		ext.opPicker.onInitTable(attribs)

def onRollover(comp, row, col, coords, prevRow, prevCol, prevCoords):
	if hasattr(ext.opPicker, 'onRollover'):
		ext.opPicker.onRollover(row, col, prevRow, prevCol)
def onSelect(comp, startRow, startCol, startCoords, endRow, endCol, endCoords, start, end):
	if hasattr(ext.opPicker, 'onSelect'):
		ext.opPicker.onSelect(endRow, endCol, end)
def onRadio(comp, row, col, prevRow, prevCol):
	if hasattr(ext.opPicker, 'onRadio'):
		ext.opPicker.onRadio(row, col, prevRow, prevCol)
def onFocus(comp, row, col, prevRow, prevCol):
	if hasattr(ext.opPicker, 'onFocus'):
		ext.opPicker.onFocus(row, col, prevRow, prevCol)

def onEdit(comp, row, col, val):
	return
def onHoverGetAccept(comp, row, col, coords, prevRow, prevCol, prevCoords, dragItems):
	return False
def onDropGetAccept(comp, row, col, coords, prevRow, prevCol, prevCoords, dragItems):
	return False

