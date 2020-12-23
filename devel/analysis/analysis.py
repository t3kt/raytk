from raytkUtil import RaytkContext, ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildOpDefParamTable(dat: 'DAT'):
	dat.clear()
	paramNames = [
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
	dat.appendRow(['path'] + paramNames)
	context = RaytkContext()
	for rop in context.allMasterOperators():
		info = ROPInfo(rop)
		path = rop.path
		if not info.opDef:
			continue
		dat.appendRow([path])
		for pn in paramNames:
			par = info.opDef.par[pn]
			if par is None:
				continue
			if par.mode == ParMode.CONSTANT:
				dat[path, pn] = par.val
			elif par.mode == ParMode.EXPRESSION:
				dat[path, pn] = f'#: {par.expr}'
			elif par.mode == ParMode.BIND:
				dat[path, pn] = f'@: {par.bindExpr}'
			elif par.mode == ParMode.EXPORT:
				dat[path, pn] = '!EXPORT!'
