from raytkUtil import RaytkContext, ROPInfo, InputInfo
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

_opDefParamNames = [
	'Coordtype',
	'Returntype',
	'Contexttype',
	'Disableinspect',
	'Opglobals',
	'Initcode',
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
	'Librarynames',
	'Help',
	'Helpurl',
	'Keywords',
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
		] + _opDefParamNames + [
			'macroCols',
		]
	)
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
			_ropKind(info),
			info.statusLabel,
			hasHelp,
			info.hasROPInputs,
			bool(info.subROPs),
		])
		for pn in _opDefParamNames:
			dat[rop.path, pn] = _formatPar(info.opDefPar[pn])
		if info.isROP:
			macros = info.opDefPar.Macrotable.eval()
			if macros:
				dat[rop.path, 'macroCols'] = macros.numCols

def _ropKind(info: 'ROPInfo'):
	if info.isOutput:
		return 'ROutput'
	elif info.isROP:
		return 'ROP'
	elif info.isRComp:
		return 'RComp'
	else:
		return ''

def buildOpParamsTable(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['path', 'kind'])
	for rop in RaytkContext().allMasterOperators():
		info = ROPInfo(rop)
		if not info:
			continue
		dat.appendRow([
			info.path,
			_ropKind(info)
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
			cell.val.rsplit('_', maxsplit=1)[1]
			for cell in info.opDef.op('params').col(0)
		])
		dat.appendRow([
			info.path,
			_formatPar(info.opDefPar.Params),
			expanded,
		])
