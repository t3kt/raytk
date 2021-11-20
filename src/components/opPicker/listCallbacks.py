# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .opPicker import OpPicker
	ext.opPicker = OpPicker(COMP())

def onInitCell(comp, row, col, attribs):
	ext.opPicker.onInitCell(row, col, attribs)
def onInitRow(comp, row, attribs):
	ext.opPicker.onInitRow(row, attribs)
def onInitCol(comp, col, attribs):
	ext.opPicker.onInitCol(col, attribs)
def onInitTable(comp, attribs):
	ext.opPicker.onInitTable(attribs)

def onRollover(comp, row, col, coords, prevRow, prevCol, prevCoords):
	ext.opPicker.onRollover(row, col, prevRow, prevCol)
def onSelect(comp, startRow, startCol, startCoords, endRow, endCol, endCoords, start, end):
	ext.opPicker.onSelect(startRow, startCol, endRow, endCol, start, end)
def onRadio(comp, row, col, prevRow, prevCol):
	ext.opPicker.onRadio(row, col, prevRow, prevCol)
def onFocus(comp, row, col, prevRow, prevCol):
	ext.opPicker.onFocus(row, col, prevRow, prevCol)

def onEdit(comp, row, col, val):
	return
def onHoverGetAccept(comp, row, col, coords, prevRow, prevCol, prevCoords, dragItems):
	return False
def onDropGetAccept(comp, row, col, coords, prevRow, prevCol, prevCoords, dragItems):
	return False

