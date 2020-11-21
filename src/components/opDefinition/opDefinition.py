import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Dict, List

def buildName():
	host = parent().par.Hostop.eval()
	if not host:
		return ''
	pathParts = host.path[1:].split('/')
	for i in range(len(pathParts)):
		if pathParts[i].startswith('_'):
			pathParts[i] = 'U' + pathParts[i][1:]
	name = '_'.join(pathParts)
	name = re.sub('_+', '_', name)
	if name.startswith('_'):
		name = 'o_' + name
	return 'RTK_' + name

def evaluateTypeProperty(par: 'Par', fieldName: str, defVal: str):
	if par != 'useinput':
		return str(par)
	inputDef = op('input_defs')
	if inputDef.numRows > 1:
		val = inputDef[1, fieldName]
		if val and val != 'useinput':
			return str(val)
	return defVal

def buildInputTable(dat: 'DAT', inDats: 'List[DAT]'):
	dat.clear()
	dat.appendRow(['slot', 'inputFunc', 'name'])
	for i, inDat in enumerate(inDats):
		slot = f'inputName{i + 1}'
		if inDat.numRows < 2 or not inDat[1, 'name'].val:
			dat.appendRow([slot])
		else:
			dat.appendRow([
				slot,
				f'inputOp{i + 1}',
				inDat[1, 'name'],
			])

def combineInputDefinitions(dat: 'DAT', inDats: 'List[DAT]'):
	dat.clear()
	if not inDats:
		return
	for d in inDats:
		if d.numRows > 0:
			dat.appendRow(d.row(0))
			break
	inDats = [d for d in inDats if d.numRows > 1]
	if not inDats:
		return
	usedNames = set()
	for d in reversed(inDats):
		insertRow = 0
		for cells in d.rows()[1:]:
			name = cells[0].val
			if not name or name in usedNames:
				continue
			usedNames.add(name)
			dat.appendRow(cells, insertRow)
			insertRow += 1

def _getRegularParams() -> 'List[Par]':
	host = parent().par.Hostop.eval()
	if not host:
		return []
	paramNames = parent().par.Params.eval().strip().split(' ')
	return [
			p
			for p in host.pars(*[pn.strip() for pn in paramNames])
			if p.isCustom and not (p.isPulse and p.name == 'Inspect')
		]

def _getSpecialParamNames():
	return tdu.expand(parent().par.Specialparams.eval())

def buildParamTable(dat: 'DAT'):
	dat.clear()
	host = parent().par.Hostop.eval()
	if not host:
		return
	name = parent().par.Name.eval()
	allParamNames = [p.name for p in _getRegularParams()] + _getSpecialParamNames()
	dat.appendCol([(name + '_' + pn) if pn != '_' else '_' for pn in allParamNames])

def buildParamDetailTable(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['tuplet', 'source', 'size', 'part1', 'part2', 'part3', 'part4', 'status'])
	name = parent().par.Name.eval()
	params = _getRegularParams()
	if params:
		paramsByTuplet = {}  # type: Dict[str, List[Par]]
		for par in params:
			if par.tupletName in paramsByTuplet:
				paramsByTuplet[par.tupletName].append(par)
			else:
				paramsByTuplet[par.tupletName] = [par]
		for tupletName, tupletPars in paramsByTuplet.items():
			tupletPars.sort(key=lambda p: p.vecIndex)
			row = dat.numRows
			dat.appendRow(
				[
					f'{name}_{tupletName}',
					'param',
					len(tupletPars)
				])
			for i, p in enumerate(tupletPars):
				dat[row, 'part' + str(i + 1)] = f'{name}_{p.name}'
			dat[row, 'status'] = 'readOnly' if _canBeReadOnlyTuplet(tupletPars) else ''
	specialNames = _getSpecialParamNames()
	if specialNames:
		parts = []
		specialIndex = 0

		def addSpecial():
			cleanParts = [p for p in parts if p != '_']
			tupletName = _getTupletName(cleanParts) or f'special{specialIndex}'
			dat.appendRow([f'{name}_{tupletName}', 'special', len(cleanParts)] + [
				f'{name}_{part}' for part in cleanParts
			])

		for specialName in specialNames:
			parts.append(specialName)
			if len(parts) == 4:
				addSpecial()
				parts.clear()
				specialIndex += 1
		if parts:
			addSpecial()

def _canBeReadOnlyTuplet(pars: 'List[Par]'):
	if not pars[0].readOnly:
		return False
	for par in pars:
		if par.mode != ParMode.CONSTANT:
			return False
	return True

def _getTupletName(parts: 'List[str]'):
	if len(parts) <= 1 or len(parts[0]) <= 1:
		return None
	prefix = parts[0][:-1]
	for part in parts[1:]:
		if not part.startswith(prefix):
			return None
	return prefix

def buildParamTupletAliases(dat: 'DAT', paramTable: 'DAT'):
	dat.clear()
	for i in range(1, paramTable.numRows):
		size = int(paramTable[i, 'size'])
		if size > 1:
			dat.appendRow([
				'#define {} vec{}({})'.format(paramTable[i, 'tuplet'].val, size, ','.join([
					paramTable[i, f'part{j + 1}'].val
					for j in range(size)
				]))
			])

def substituteWords(dat: 'DAT'):
	if not dat.inputs:
		dat.text = ''
		return
	dat.copy(dat.inputs[0])
	text = dat.text
	for repls in dat.inputs[1:]:
		if repls.numRows == 0 or repls.numCols < 2:
			continue
		if repls[0, 0] == 'before' and repls[0, 1] == 'after':
			startRow = 1
		else:
			startRow = 0
		for row in range(startRow, repls.numRows):
			text = re.sub(r'\b' + repls[row, 0].val + r'\b', repls[row, 1].val, text)
	dat.text = text

def updateLibraryMenuPar(libsComp: 'COMP'):
	p = parent().par.Librarynames  # type: Par
	libs = libsComp.findChildren(type=DAT, maxDepth=1, tags=['library'])
	libs.sort(key=lambda l: -l.nodeY)
	p.menuNames = [lib.name for lib in libs]

def prepareMacroTable(dat: 'scriptDAT', typeTable: 'DAT'):
	dat.clear()
	# 'THIS_' + me.inputCell.val.replace('Type', '').upper() + '_TYPE_' + me.inputCell.offset(0, 1)
	for kind, typeName in typeTable.rows():
		dat.appendRow([
			'',
			f'THIS_{kind.val.replace("Type", "").upper()}_TYPE_{typeName.val}',
			'',
		])
	macros = parent().par.Macrotable.eval()  # type: DAT
	if macros:
		if macros.numCols == 2:
			dat.appendRows([
				[''] + [c.val for c in cells]
				for cells in macros.rows()
			])
		elif macros.numCols == 1:
			dat.appendRows([
				['', c.val, '']
				for c in macros.col(0)
			])
		else:
			dat.appendRows(macros.rows())
