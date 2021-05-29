from typing import List
import raytkTypes

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildValidationErrors(dat: 'DAT', mergedDefs: 'DAT'):
	dat.clear()
	processedInputDefs = [
		table
		for table in ops('definition_?')
		if table.numRows > 1
	]
	minCount = int(parent().par.Minimuminputs)
	if len(processedInputDefs) < minCount:
		dat.appendRow(['path', 'level', 'message'])
		dat.appendRow([parent().path, 'error', f'Only {len(processedInputDefs)} provided, {minCount} required'])
	if mergedDefs.numRows < 2:
		return
	commonTypes = op('commonTypes')
	for typeCategory in ('coordType', 'contextType', 'returnType'):
		if not commonTypes[typeCategory, 1].val:
			if not dat.numRows:
				dat.appendRow(['path', 'level', 'message'])
			dat.appendRow([parent().path, 'error', f'Inputs have no matching {typeCategory}'])

def buildCommonTypeTable(dat: 'scriptDAT'):
	dat.clear()
	inputDefs = [
		table
		for table in ops('definition_in_?')
		if table.numRows > 1
	]
	dat.appendRow(['coordType', _getCombinedTypesForCategory('coordType', inputDefs)])
	dat.appendRow(['returnType', _getCombinedTypesForCategory('returnType', inputDefs)])
	dat.appendRow(['contextType', _getCombinedTypesForCategory('contextType', inputDefs)])

def _getCombinedTypesForCategory(category: str, inputDefs: 'List[DAT]'):
	return ' '.join(raytkTypes.getCommonTypesFromCells([
		d[1, category]
		for d in inputDefs
	]))
