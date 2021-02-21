import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Dict, List, Optional, Union
	from raytkUtil import OpDefParsT
	from _stubs.PopDialogExt import PopDialogExt


def parentPar() -> 'Union[ParCollection, OpDefParsT]':
	return parent().par

def _host() -> 'Optional[COMP]':
	return parentPar().Hostop.eval()

def buildName():
	host = _host()
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

def _getParamsOp() -> 'Optional[COMP]':
	return parentPar().Paramsop.eval() or _host()

def _getRegularParams() -> 'List[Par]':
	host = _getParamsOp()
	if not host:
		return []
	paramNames = tdu.expand(parentPar().Params.eval().strip())
	if not paramNames:
		return []
	return [
			p
			for p in host.pars(*[pn.strip() for pn in paramNames])
			if p.isCustom and not (p.isPulse and p.name == 'Inspect')
		]

def _getSpecialParamNames():
	return tdu.expand(parentPar().Specialparams.eval())

def buildParamTable(dat: 'DAT'):
	dat.clear()
	host = _getParamsOp()
	if not host:
		return
	name = parentPar().Name.eval()
	allParamNames = [p.name for p in _getRegularParams()] + _getSpecialParamNames()
	dat.appendCol([(name + '_' + pn) if pn != '_' else '_' for pn in allParamNames])

def buildParamDetailTable(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['tuplet', 'source', 'size', 'part1', 'part2', 'part3', 'part4', 'status'])
	name = parentPar().Name.eval()
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
	p = parentPar().Librarynames  # type: Par
	libs = libsComp.findChildren(type=DAT, maxDepth=1, tags=['library'])
	libs.sort(key=lambda l: -l.nodeY)
	p.menuNames = [lib.name for lib in libs]

def prepareMacroTable(dat: 'scriptDAT', typeTable: 'DAT', inputTable: 'DAT', macroParamTable: 'DAT'):
	dat.clear()
	# 'THIS_' + me.inputCell.val.replace('Type', '').upper() + '_TYPE_' + me.inputCell.offset(0, 1)
	for kind, typeName in typeTable.rows():
		dat.appendRow([
			'',
			f'THIS_{kind.val.replace("Type", "").upper()}_TYPE_{typeName.val}',
			'',
		])
	for cell in inputTable.col('inputFunc')[1:]:
		if not cell.val:
			continue
		dat.appendRow([
			'',
			f'THIS_HAS_INPUT_{tdu.digits(cell.val)}',
			'',
		])
	for row in range(1, macroParamTable.numRows):
		name = macroParamTable[row, 'name']
		val = macroParamTable[row, 'value']
		style = macroParamTable[row, 'style']
		if style in ('Menu', 'Str', 'StrMenu'):
			dat.appendRow(['', f'THIS_{name}_{val}', ''])
			dat.appendRow(['', f'THIS_{name}', val])
		elif style == 'Toggle':
			if val:
				dat.appendRow(['', f'THIS_{name}', ''])
		else:
			dat.appendRow(['', f'THIS_{name}', val])
	for table in [op(parentPar().Macrotable)] + parentPar().Generatedmacrotables.evalOPs():
		if not table or table.numCols == 0 or table.numRows == 0:
			continue
		elif table.numCols == 3:
			dat.appendRows(table.rows())
		elif table.numCols == 1:
			dat.appendRows([
				['', c.val, '']
				for c in table.col(0)
			])
		elif table.numCols == 2:
			dat.appendRows([
				['', cells[0], cells[1]]
				for cells in table.rows()
			])
		else:
			dat.appendRows([
				[cells[0], cells[1], ' '.join([c.val for c in cells[2:]])]
				for cells in table.rows()
			])

def onValidationChange(dat: 'DAT'):
	host = _host()
	if not host:
		return
	host.clearScriptErrors()
	cells = dat.col('message')
	if not cells:
		return
	err = '\n'.join([c.val for c in cells])
	host.addScriptError(err)

def onHostNameChange():
	# Workaround for dependency update issue (#295) when the host is renamed.
	op('sel_funcTemplate').cook(force=True)

def _popDialog() -> 'PopDialogExt':
	# noinspection PyUnresolvedReferences
	return op.TDResources.op('popDialog')

def inspect(rop: 'COMP'):
	if hasattr(op, 'raytk'):
		inspector = op.raytk.op('tools/inspector')
		if inspector and hasattr(inspector, 'Inspect'):
			inspector.Inspect(rop)
			return
	_popDialog().Open(
		title='Warning',
		text='The RayTK inspector is only available when the main toolkit tox has been loaded.',
		escOnClickAway=True,
	)

def _useLocalHelp():
	return hasattr(op, 'raytk') and bool(op.raytk.par['Devel'])

def launchHelp():
	url = parentPar().Helpurl.eval()
	if not url:
		return
	if _useLocalHelp():
		url = url.replace('https://t3kt.github.io/raytk/', 'http://localhost:4000/raytk/')
	url += '?utm_source=raytkLaunch'
	ui.viewFile(url)

def updateOP():
	if not hasattr(op, 'raytk'):
		_popDialog().Open(
			title='Warning',
			text='Unable to update OP because RayTK toolkit is not available.',
			escOnClickAway=True,
		)
		return
	host = _host()
	if not host:
		return
	toolkit = op.raytk
	updater = toolkit.op('tools/updater')
	if updater and hasattr(updater, 'UpdateOP'):
		updater.UpdateOP(host)
		return
	if not host.par.clone:
		_popDialog().Open(
			title='Warning',
			text='Unable to update OP because master is not found in the loaded toolkit.',
			escOnClickAway=True,
		)
		return
	if host and host.par.clone:
		host.par.enablecloningpulse.pulse()
