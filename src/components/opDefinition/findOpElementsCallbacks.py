# me - this DAT
# dat - the DAT that is querying
# curOp - the OP being queried
# row - the table row index

# Uncomment following two functions to add custom columns

def onInitGetColumnNames(dat):
	return ['paramListTable', 'macroTable', 'placeholder1', 'code1', 'placeholder2', 'code2']

def onFindOPGetValues(dat, curOp, row):
	return [
		curOp.par['Paramlisttable'] or '',
		curOp.par['Macrotable'] or '',
		curOp.par['Placeholder1'] or '',
		curOp.par['Code1'] or '',
		curOp.par['Placeholder2'] or '',
		curOp.par['Code2'] or '',
	]


# Return True / False to include / exclude an operator in the table

def onFindOPGetInclude(dat, curOp, row):
	return True


# Provide an extensive dictionary of what was matched for each operator.
# Multiple matching tags, parameters and cells will be included.
# For each match, a corresponding key is included in the dictionary:
#
#  results:
#
#  'name': curOp.name
#  'type': curOp.OPType
#  'path': curOp.path
#  'parent' : curOp.parent()
#  'comment': curOp.comment
#  'tags' : [list of strings] or empty list
#  'text' : [list of Cells] or empty list
#  'par': dictionary of matching parameter attributes.
#    example entries:
#        tx : { 'name': True, 'value':True , 'expression':True } # Parameter tx matched on name, value, expression
#        ty : { 'value' : True } # Parameter ty matched on value
#

def onOPFound(dat, curOp, row, results):
	return

	