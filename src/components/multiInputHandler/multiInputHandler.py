from typing import List
import raytkTypes

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildTypeSettings(dat: 'scriptDAT'):
	dat.clear()
	dat.appendRow(['category', 'mode', 'replacement', 'scope'])
	allInputDefs = ops('definition_in_?')
	for category in raytkTypes.allTypeCategories:
		parPrefix = category.replace('Type', '').capitalize()
		mode = parent().par[parPrefix + 'typereductionmode']
		dat.appendRow([
			category,
			mode,
		])
		if mode in ('common', 'bestcommon'):
			scopeIndices = _parseInputScope(
				parent().par[parPrefix + 'typereductionscope'].eval(),
				maxInputs=len(allInputDefs))
			inScopeCells = [
				table[1, category]
				for table in allInputDefs
				if table.digits in scopeIndices
			]
			dat[category, 'scope'] = ' '.join(str(i) for i in scopeIndices)
			commonTypes = raytkTypes.getCommonTypesFromCells(inScopeCells)
			if mode == 'common':
				dat[category, 'replacement'] = ' '.join(commonTypes)
			elif mode == 'bestcommon':
				preferredTypes = tdu.split(parent().par[parPrefix + 'typepreference'])
				dat[category, 'replacement'] = ''
				for prefType in preferredTypes:
					if prefType in commonTypes:
						dat[category, 'replacement'] = prefType
						break

def buildValidationErrors(dat: 'DAT', mergedDefs: 'DAT', typeSettings: 'DAT'):
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
	for typeCategory in raytkTypes.allTypeCategories:
		repl = _getTypeReplacement(typeSettings, typeCategory)
		if repl is None:
			continue
		if repl == '':
			if not dat.numRows:
				dat.appendRow(['path', 'level', 'message'])
			dat.appendRow([parent().path, 'error', f'Inputs have no matching {typeCategory}'])

def _parseInputScope(val: str, maxInputs: int) -> List[int]:
	val = val.strip()
	if val == '*':
		return list(range(1, maxInputs + 1))
	return [int(p) for p in tdu.expand(val)]

def applyTypeSettings(dat: 'scriptDAT', index: int, typeSettings: 'DAT'):
	if dat.numRows < 2:
		return
	for category in raytkTypes.allTypeCategories:
		if str(index) not in typeSettings[category, 'scope'].val.split(' '):
			continue
		repl = _getTypeReplacement(typeSettings, category)
		if repl is not None:
			dat[1, category] = repl

def _getTypeReplacement(typeSettings: 'DAT', category: str):
	if typeSettings[category, 'mode'].val not in ('common', 'bestcommon'):
		return None
	return typeSettings[category, 'replacement'].val
