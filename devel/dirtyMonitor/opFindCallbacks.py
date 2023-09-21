# me - this DAT
# dat - the DAT that is querying
# curOp - the OP being queried
# row - the table row index

# Uncomment following two functions to add custom columns

def onInitGetColumnNames(dat):
	return [
		'tox',
		'dirty'
	]

def onFindOPGetValues(dat, curOp, row):
	return [
		curOp.par['externaltox'],
		curOp.dirty,
	]


# Return True / False to include / exclude an operator in the table

def onFindOPGetInclude(dat, curOp, row):
	return bool(curOp.par['externaltox']) and not curOp.par['clone']


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

	