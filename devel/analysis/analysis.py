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
	'Stageinitcode',
	'Functemplate',
	'Materialcode',
	'Paramsop',
	'Params',
	'Specialparams',
	'Angleparams',
	'Macroparams',
	'Buffertable',
	'Texturetable',
	'Macrotable',
	'Variabletable',
	'Referencetable',
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
			'hasHelp',
			'hasInputs',
			'hasSubRops',
			'Coordtype',
			'Returntype',
			'Contexttype',
		] + _opDefParamNames + [
			'hasThumb',
			'paramPages',
		]
	)
	opThumbs = op('opThumbs')
	context = RaytkContext()
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
			hasHelp,
			info.hasROPInputs,
			bool(info.subROPs),
		])
		typeSpec = info.typeSpec
		if typeSpec:
			types = typeSpec.op('supportedTypes')
			dat[rop.path, 'Coordtype'] = types['coordType', 'spec']
			dat[rop.path, 'Contexttype'] = types['contextType', 'spec']
			dat[rop.path, 'Returntype'] = types['returnType', 'spec']
		for pn in _opDefParamNames:
			dat[rop.path, pn] = _formatPar(info.opDefPar[pn])
		dat[rop.path, 'hasThumb'] = bool(opThumbs[rop.path, 'thumb'])
		dat[rop.path, 'paramPages'] = ' '.join([page.name for page in rop.customPages])

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
			if par.name in ('Inspect', 'Help'):
				continue
			cell = dat[info.path, par.tupletName]
			if cell is None:
				dat.appendCol([par.tupletName])
				cell = dat[info.path, par.tupletName]
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
	])
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
			])

def buildOpCurrentExpandedParamsTable(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['path', 'expr', 'expandedParams'])
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
			_formatPar(info.opDefPar.Params),
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
		name = str(testTable[i, 'path']).rsplit('/', maxsplit=1)[1].replace('.tox', '')
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
