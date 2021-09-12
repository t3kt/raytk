from typing import List, Optional
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
		if mode in ('common', 'bestcommon', 'besteach'):
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
				dat[category, 'replacement'] = _firstMatch(preferredTypes, commonTypes) or ''
			elif mode == 'besteach':
				preferredTypes = tdu.split(parent().par[parPrefix + 'typepreference'])
				dat[category, 'replacement'] = ' '.join(preferredTypes)

def _firstMatch(vals, matchVals):
	for val in vals:
		if val in matchVals:
			return val

def buildValidationErrors(dat: 'DAT', mergedDefs: 'DAT', typeSettings: 'DAT'):
	dat.clear()
	processedInputDefs = [
		table
		for table in ops('proc_definition_?')
		if table.numRows > 1
	]

	def addRow(level, msg):
		if not dat.numRows:
			dat.appendRow(['path', 'level', 'message'])
		dat.appendRow([parent().path, level, msg])

	minCount = int(parent().par.Minimuminputs)
	if len(processedInputDefs) < minCount:
		addRow('error', f'Only {len(processedInputDefs)} provided, {minCount} required')
	if mergedDefs.numRows < 2:
		return
	for typeCategory in raytkTypes.allTypeCategories:
		if typeSettings[typeCategory, 'mode'].val == 'besteach':
			for inDef in processedInputDefs:
				current = inDef[1, typeCategory]
				if not current:
					addRow('error', f'No matching {typeCategory} for input {inDef.digits}')
		else:
			repl = _getTypeReplacement(typeSettings, typeCategory, None)
			if repl is None:
				continue
			if repl == '':
				addRow('error', f'Inputs have no matching {typeCategory}')

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
		repl = _getTypeReplacement(typeSettings, category, dat[1, category])
		if repl is not None:
			dat[1, category] = repl

def _getTypeReplacement(typeSettings: 'DAT', category: str, current: 'Optional[Cell]'):
	mode = typeSettings[category, 'mode'].val
	replacement = typeSettings[category, 'replacement'].val
	if mode == 'besteach':
		preferredTypes = tdu.split(replacement)
		supportedTypes = tdu.split(current)
		return _firstMatch(preferredTypes, supportedTypes)
	if mode not in ('common', 'bestcommon'):
		return None
	return replacement
