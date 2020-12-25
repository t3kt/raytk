from raytkUtil import RaytkContext, ROPInfo
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
		if info.isOutput:
			kind = 'ROutput'
		elif info.isROP:
			kind = 'ROP'
		elif info.isRComp:
			kind = 'RComp'
		else:
			kind = ''
		dat.appendRow([
			rop.path,
			kind,
			info.statusLabel,
			bool(info.helpDAT),
			info.hasROPInputs,
			bool(info.subROPs),
		])
		for pn in _opDefParamNames:
			dat[rop.path, pn] = _formatPar(info.opDefPar[pn])
		if info.isROP:
			macros = info.opDefPar.Macrotable.eval()
			if macros:
				dat[rop.path, 'macroCols'] = macros.numCols
