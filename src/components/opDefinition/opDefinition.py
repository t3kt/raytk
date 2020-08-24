import re
from typing import Dict, List, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

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
	return name

def evaluateTypeProperty(par: 'Par', fieldName: str, defVal: str):
	if par != 'useinput':
		return str(par)
	inputDef = op('input_def_1')
	if inputDef.numRows > 1:
		val = inputDef[1, fieldName]
		if val and val != 'useinput' and str(val) in par.menuNames:
			return str(val)
	return defVal

def extractInputNames(dat: 'DAT', inDats: List['DAT']):
	dat.clear()
	for inDat in inDats:
		name = str(inDat[1, 'name'] or '')
		dat.appendRow([f'inputName{inDat.digits}', name])

def mergeInputDefs(dat: 'DAT', inDats: List['DAT']):
	dat.clear()
	for inDat in inDats:
		if inDat.numRows < 2:
			continue
		if dat.numRows == 0:
			dat.appendRow(inDat.row(0))
		for row in range(1, inDat.numRows):
			# skip rows already added in an earlier input
			if dat[inDat[row, 0], 0] is None:
				dat.appendRow(inDat.row(row))

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
	dat.appendRow(['tuplet', 'source', 'size', 'part1', 'part2', 'part3', 'part4'])
	name = parent().par.Name.eval()
	params = _getRegularParams()
	if params:
		processedTupletNames = set()
		for par in params:
			if par.tupletName in processedTupletNames:
				continue
			dat.appendRow(
				[f'{name}_{par.tupletName}', 'param', len(par.tuplet)] + [
					f'{name}_{p.name}' for p in par.tuplet])
			processedTupletNames.add(par.tupletName)
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

def _getTupletName(parts: List[str]):
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
