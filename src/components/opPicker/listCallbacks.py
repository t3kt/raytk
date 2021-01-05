# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .opPicker import OpPicker
	ext.opPicker = OpPicker(COMP())

# me - this DAT
# 
# comp - the List Component that holds this panel
# row - the row number of the cell being updated
# col - the column number of the cell being updated
#
# attribs contains the following members:
#
# text				   str            cell contents
# help                 str       	  help text
#
# textColor            r g b a        font color
# textOffsetX		   n			  horizontal text offset
# textOffsetY		   n			  vertical text offset
# textJustify		   m			  m is one of:  JustifyType.TOPLEFT, JustifyType.TOPCENTER,
#                        JustifyType.TOPRIGHT, JustifyType.CENTERLEFT,
#                        JustifyType.CENTER, JustifyType.CENTERRIGHT,
#                        JustifyType.BOTTOMLEFT, JustifyType.BOTTOMCENTER,
#                        JustifyType.BOTTOMRIGHT
#
# bgColor              r g b a        background color
#
# leftBorderInColor	   r g b a		  inside left border color
# rightBorderInColor   r g b a		  inside right border color
# bottomBorderInColor  r g b a		  inside bottom border color
# topBorderInColor	   r g b a		  inside top border color
#
# leftBorderOutColor   r g b a		  outside left border color
# rightBorderOutColor  r g b a		  outside right border color
# bottomBorderOutColor r g b a		  outside bottom border color
# topBorderOutColor	   r g b a		  outside top border color
#
# colWidth             w              sets column width
# colStetch            True/False     sets column stretchiness (width is min width)
# rowHeight            h              sets row height
# rowStetch            True/False     sets row stretchiness (height is min height)
# rowIndent            w              offsets entire row by this amount
#
# editable			   int			  number of clicks to activate editing the cell.
# draggable             True/False     allows cell to be drag/dropped elsewhere
# fontBold             True/False     render font bolded
# fontItalic           True/False     render font italicized
# fontSizeX            float		  font X size in pixels
# fontSizeY            float		  font Y size in pixels, if not specified, uses X size
# sizeInPoints         True/False	  If true specify font size in points, rather than pixels.
# fontFace             str			  font face, example 'Verdana'
# wordWrap             True/False     word wrap
#
# top                  TOP			  background TOP operator
#
# select   true when the cell/row/col is currently being selected by the mouse
# rollover true when the mouse is currently over the cell/row/col
# radio    true when the cell/row/col was last selected
# focus    true when the cell/row/col is being edited
#
#

# called when Reset parameter is pulsed, or on load

def onInitCell(comp, row, col, attribs):
	ext.opPicker.onInitCell(row, col, attribs)
def onInitRow(comp, row, attribs):
	ext.opPicker.onInitRow(row, attribs)
def onInitCol(comp, col, attribs):
	ext.opPicker.onInitCol(col, attribs)
def onInitTable(comp, attribs):
	ext.opPicker.onInitTable(attribs)

# called during specific events
#
# coords - a named tuple containing the following members:
#   x
#   y
#   u
#   v

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

# return True if interested in this drop event, False otherwise
def onHoverGetAccept(comp, row, col, coords, prevRow, prevCol, prevCoords, dragItems):
	return False
def onDropGetAccept(comp, row, col, coords, prevRow, prevCol, prevCoords, dragItems):
	return False

