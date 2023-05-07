import json

from raytkUtil import RaytkContext, ROPInfo, InputInfo, CategoryInfo
from typing import Dict, List, Optional
import raytkDocs

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

_opDefParamNames = [
	'Typespec',
	'Useruntimebypass',
	'Disableinspect',
	'Opglobals',
	'Initcode',
	'Functemplate',
	'Materialcode',
	'Paramsop',
	'Paramgrouptable',
	'Buffertable',
	'Texturetable',
	'Macrotable',
	'Variabletable',
	'Referencetable',
	'Dispatchtable',
	'Librarynames',
	'Help',
	'Helpurl',
	'Keywords',
	'Shortcuts',
	'Callbacks',
	'Raytkoptype',
	'Raytkopversion',
]

def _formatPar(par: 'Optional[Par]'):
	if par is None:
		return ''
	if par.mode == ParMode.CONSTANT:
		return par.val
	elif par.mode == ParMode.EXPRESSION:
		return f'#: {par.expr}'
	elif par.mode == ParMode.BIND:
		return f'@: {par.bindExpr}'
	elif par.mode == ParMode.EXPORT:
		return '!EXPORT!'
	else:
		return '??'

def buildOpInfoTable(dat: 'DAT'):
	dat.clear()
	dat.appendRow(
		[
			'path',
			'kind',
			'status',
			'category',
			'hasHelp',
			'hasInputs',
			'hasSubRops',
			'Coordtype',
			'Returntype',
			'Contexttype',
		] + _opDefParamNames + [
			'hasThumb',
			'hasSnippet',
			'paramPages',
			'hasInputVarSettings',
		]
	)
	opThumbs = op('opThumbs')
	context = RaytkContext()
	snippetTable = op('snippetTable')
	snippetTypes = set([c.val for c in snippetTable.col('opType')[1:]])
	for rop in context.allMasterOperators():
		info = ROPInfo(rop)
		if not info:
			continue
		helpDat = info.helpDAT
		if not helpDat:
			hasHelp = False
		elif '## Parameters' in helpDat.text or len(helpDat.text.split()) > 6:
			hasHelp = True
		else:
			hasHelp = False
		dat.appendRow([
			rop.path,
			info.ropKind or '',
			info.statusLabel or 'stable',
			info.displayCategoryName or info.categoryName or '',
			hasHelp,
			info.hasROPInputs,
			bool(info.subROPs),
		])
		typeSpec = info.typeSpec
		if typeSpec:
			types = info.opDef.op('supportedTypes')
			dat[rop.path, 'Coordtype'] = types['coordType', 'spec']
			dat[rop.path, 'Contexttype'] = types['contextType', 'spec']
			dat[rop.path, 'Returntype'] = types['returnType', 'spec']
		for pn in _opDefParamNames:
			dat[rop.path, pn] = _formatPar(info.opDefPar[pn])
		dat[rop.path, 'hasThumb'] = bool(opThumbs[rop.path, 'thumb'])
		dat[rop.path, 'hasSnippet'] = bool(info.opType in snippetTypes)
		dat[rop.path, 'paramPages'] = ' '.join([page.name for page in rop.customPages])
		dat[rop.path, 'hasInputVarSettings'] = _opHasInputVarSettings(info)

def _opHasInputVarSettings(info: 'ROPInfo'):
	inputs = info.inputHandlers
	if not inputs:
		return ''
	for inputHandler in inputs:
		if _parHasSetting(inputHandler.par.Variables):
			return True
		if _parHasSetting(inputHandler.par.Variableinputs):
			return True
	return False

def _parHasSetting(par: 'Par'):
	if par.eval():
		return True
	if par.expr or par.bindExpr:
		return True
	return False

def buildOpParamsTable(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['path', 'kind'])
	for rop in RaytkContext().allMasterOperators():
		info = ROPInfo(rop)
		if not info:
			continue
		dat.appendRow([
			info.path,
			info.ropKind or '',
		])
		for tuplet in info.rop.customTuplets:
			par = tuplet[0]
			if par.name in ('Inspect', 'Help', 'Updateop') or par.name.startswith('Createref') or par.name.startswith('Creatersel'):
				continue
			cell = dat[info.path, par.tupletName]
			if cell is None:
				dat.appendCol([par.tupletName])
				cell = dat[info.path, par.tupletName]
			if par.isMenu:
				opts = ','.join(par.menuNames)
				cell.val = f'Menu: {opts}'
			else:
				cell.val = par.style

def buildOpVariablesTable(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['path'])
	for rop in RaytkContext().allMasterOperators():
		info = ROPInfo(rop)
		if not info.isROP:
			continue
		varTable = info.opDefPar.Variabletable.eval()
		if varTable and isinstance(varTable, evaluateDAT):
			varTable = varTable.inputs[0]
		if not varTable:
			continue
		dat.appendRow([info.path])
		for i in range(1, varTable.numRows):
			name = varTable[i, 'name'] or varTable[i, 0]
			dataType = varTable[i, 'dataType'] or varTable[i, 2]
			cell = dat[info.path, name]
			if cell is None:
				dat.appendCol([name])
				cell = dat[info.path, name]
			cell.val = dataType

def buildOpInputsTable(dat: 'DAT'):
	dat.clear()
	parNames = [
		'Source',
		'Label',
		'Localalias',
		'Variables',
		'Variableinputs',
		'Help',
	]
	dat.appendRow([
		'path',
		'index',
		'handler',
		'name',
		'label',
		'required',
		'multi',
		'coordTypes',
		'contextTypes',
		'returnTypes',
		'hasExprs',
	] + parNames)
	for rop in RaytkContext().allMasterOperators():
		info = ROPInfo(rop)
		if not info:
			continue
		for i, handler in enumerate(info.inputHandlers):
			inInfo = InputInfo(handler)
			dat.appendRow([
				rop.path,
				i + 1,
				handler.name,
				inInfo.name or '',
				inInfo.label or '',
				_formatPar(inInfo.handlerPar.Required),
				bool(inInfo.multiHandler),
				' '.join(inInfo.supportedCoordTypes),
				' '.join(inInfo.supportedContextTypes),
				' '.join(inInfo.supportedReturnTypes),
				any([p.mode != ParMode.CONSTANT for p in handler.customPars]),
			] + [
				_formatPar(inInfo.handlerPar[parName])
				for parName in parNames
			])

def buildOpCurrentExpandedParamsTable(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['path', 'expandedParams'])
	for rop in RaytkContext().allMasterOperators():
		info = ROPInfo(rop)
		if not info or not info.isROP:
			continue
		expanded = ' '.join([
			cell.val
			for cell in info.opDef.op('paramSpecTable').col('localName')[1:]
		])
		dat.appendRow([
			info.path,
			expanded,
		])

def buildOpTestTable(dat: 'DAT', testTable: 'DAT'):
	dat.clear()
	dat.appendRow([
		'path',
		'testCount',
		'test1',
	])
	testsByOpType = {}  # type: Dict[str, List[str]]
	for i in range(1, testTable.numRows):
		opType = str(testTable[i, 'opType'])
		name = str(testTable[i, 'filePath']).rsplit('/', maxsplit=1)[1].replace('.tox', '')
		if not opType:
			continue
		elif opType not in testsByOpType:
			testsByOpType[opType] = [name]
		else:
			testsByOpType[opType].append(name)
	for rop in RaytkContext().allMasterOperators():
		opType = ROPInfo(rop).opType
		tests = testsByOpType.get(opType) or []
		tests.sort()
		dat.appendRow([
			rop.path,
			len(tests),
		] + tests)
	for cell in dat.row(0)[2:]:
		cell.val = 'test' + str(cell.col - 1)

def buildOpTagTable(dat: 'DAT'):
	dat.clear()
	opPaths = []  # type: List[str]
	opTagExprs = {}  # type: Dict[str, Dict[str, str]]
	for rop in RaytkContext().allMasterOperators():
		info = ROPInfo(rop)
		if not info or not info.isROP:
			continue
		tagTable = info.opDefPar.Tagtable.eval()
		if not tagTable:
			continue
		if tagTable.inputs:
			tagTable = tagTable.inputs[0]
		for i in range(1, tagTable.numRows):
			tag = tagTable[i, 'name'].val
			expr = tagTable[i, 'enable'].val
			if tag in opTagExprs:
				opTagExprs[tag][info.path] = expr
			else:
				opTagExprs[tag] = {info.path: expr}
		opPaths.append(info.path)
	opPaths.sort()
	dat.appendRow(['path'] + list(sorted(opTagExprs.keys())))
	for path in opPaths:
		dat.appendRow([path])
		for tag, pathExprs in opTagExprs.items():
			dat[dat.numRows - 1, tag] = pathExprs.get(path, '')

def buildToolkitIndexJson():
	toolkitIndex = {
		'categories': {
			CategoryInfo(cat).categoryName: _buildCategoryIndexObj(cat)
			for cat in RaytkContext().allCategories()
		}
	}
	return json.dumps(toolkitIndex, indent='  ')

def _buildCategoryIndexObj(cat: 'COMP'):
	catHelp = raytkDocs.CategoryHelp.extractFromComp(cat)
	return catHelp.toFrontMatterData()
