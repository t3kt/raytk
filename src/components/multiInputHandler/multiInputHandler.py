from dataclasses import dataclass

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def _getCommonTypesFromCells(cells: list[Cell]) -> list[str]:
	cells = [cell for cell in cells if cell]
	if not cells:
		return []
	typeCounts = {}  # type: dict[str, int]
	for cell in cells:
		for part in cell.val.split(' '):
			if not part:
				continue
			typeCounts[part] = typeCounts.get(part, 0) + 1
	n = len(cells)
	return [
		t
		for t, count in typeCounts.items()
		if count == n
	]

def _firstMatch(vals, matchVals):
	for val in vals:
		if val in matchVals:
			return val

def _parseInputScope(val: str, maxInputs: int) -> list[int]:
	val = val.strip()
	if val == '*':
		return list(range(1, maxInputs + 1))
	return [int(p) for p in tdu.expand(val)]

@dataclass
class _TypeSettings:
	mode: str | None = None
	replacement: str | None = None
	scope: list[int] | None = None

def _buildTypeSettingsCategory(category: str, parPrefix: str, inputDefs: list[DAT]):
	mode = parent().par[parPrefix + 'typereductionmode'].eval()
	settings = _TypeSettings(mode=mode)
	if mode in ('common', 'bestcommon', 'besteach'):
		scopeIndices = _parseInputScope(
			parent().par[parPrefix + 'typereductionscope'].eval(),
			maxInputs=len(inputDefs))
		inScopeCells = [
			table[1, category]
			for table in inputDefs
			if table.digits in scopeIndices
		]
		settings.scope = scopeIndices
		commonTypes = _getCommonTypesFromCells(inScopeCells)
		if mode == 'common':
			settings.replacement = ' '.join(commonTypes)
		elif mode == 'bestcommon':
			preferredTypes = tdu.split(parent().par[parPrefix + 'typepreference'])
			settings.replacement = _firstMatch(preferredTypes, commonTypes) or ''
		elif mode == 'besteach':
			preferredTypes = tdu.split(parent().par[parPrefix + 'typepreference'])
			settings.replacement = ' '.join(preferredTypes)
	return settings

def _applyTypeSettingsCategory(dat: scriptDAT, i: int,  settings: _TypeSettings, category: str):
	if not settings.scope or i not in settings.scope:
		return
	repl = _getTypeReplacement(settings, dat[i, category].val)
	if repl is not None:
		dat[str(i), category] = repl

def _getTypeReplacement(settings: _TypeSettings, current: str | None):
	if settings.mode == 'besteach':
		preferredTypes = tdu.split(settings.replacement)
		supportedTypes = tdu.split(current) if current else []
		return _firstMatch(preferredTypes, supportedTypes)
	if settings.mode not in ('common', 'bestcommon'):
		return None
	return settings.replacement

def processInputs(dat: scriptDAT):
	dat.clear()
	dat.appendRow([
		'head',
		'name', 'path', 'opType', 'coordType', 'contextType', 'returnType',
		'definitionPath', 'statePath', 'tags',
		'input:alias', 'input:vars', 'input:varInputs', 'input:handler',
	])
	inputDefs = ops('definition_in_?')
	coordSettings = _buildTypeSettingsCategory('coordType', 'Coord', inputDefs)
	contextSettings = _buildTypeSettingsCategory('contextType', 'Context', inputDefs)
	returnSettings = _buildTypeSettingsCategory('returnType', 'Return', inputDefs)
	haveIndices = []

	for i, inDef in enumerate(inputDefs):
		if inDef.numRows < 2:
			continue
		i += 1
		haveIndices.append(i)
		dat.appendRow([i] + inDef.row(1))
		# dat.appendRow([
		# 	i,
		# 	inDef['name', 1], inDef['path', 1], inDef['opType', 1],
		# 	inDef['coordType', 1], inDef['contextType', 1], inDef['returnType', 1],
		# 	inDef['definitionPath', 1], inDef['statePath', 1], inDef['tags', 1],
		# 	inDef['input:alias', 1], inDef['input:vars', 1], inDef['input:varInputs', 1], inDef['input:handler', 1],
		# ])
		for inRow in range(2, inDef.numRows):
			dat.appendRow([str(i) + '_'] + inDef.row(inRow))
		_applyTypeSettingsCategory(dat, i, coordSettings, 'coordType')
		_applyTypeSettingsCategory(dat, i, contextSettings, 'contextType')
		_applyTypeSettingsCategory(dat, i, returnSettings, 'returnType')

	def addValidation(level, msg):
		if dat['validation', 0] is None:
			dat.appendRow(['validation', 'path', 'level', 'message'])
		dat.appendRow(['validation', parent().path, level, msg])

	def validateCategory(category, settings: _TypeSettings):
		if settings.mode == 'besteach':
			for i in haveIndices:
				current = dat[str(i), category]
				if not current:
					addValidation('error', f'No matching {category} for input {i}')
		else:
			repl = _getTypeReplacement(settings, None)
			if repl == '':
				addValidation('error', f'Inputs have no matching {category}')

	minCount = int(parent().par.Minimuminputs)
	if len(haveIndices) < minCount:
		addValidation('error', f'Only {len(haveIndices)} provided, {minCount} required')
	if len(haveIndices) >= 2:
		validateCategory('coordType', coordSettings)
		validateCategory('contextType', contextSettings)
		validateCategory('returnType', returnSettings)

	dat.appendRow(['info', 'inputCount', len(haveIndices)])
	effectiveIndex = 1
	for i in range(1, 9):
		dat.appendRow(['info', f'hasInput{i}', int(i in haveIndices)])
		if i in haveIndices:
			dat.appendRow(['macro', f'THIS_INPUT_{effectiveIndex} inputOp{i}'])
			effectiveIndex += 1
	dat.appendRow(['macro', 'THIS_INPUT_COUNT ' + str(len(haveIndices))])
