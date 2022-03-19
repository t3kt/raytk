# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Variable')
	page.appendStr('Variabletype', label='Variable Type')
	page.appendStr('Defaultexpr', label='Default Expr')
	page.appendStr('Accessexpr', label='Access Expr')
	page.appendStr('Returnexpr', label='Return Expr')
	page.appendStr('Paramexpr', label='Param Expr')

def onCook(dat: 'DAT'):
	dat.clear()
	varType = dat.par.Variabletype.eval()
	defaultExpr = dat.par.Defaultexpr.eval()
	accessExpr = dat.par.Accessexpr.eval()
	returnExpr = dat.par.Returnexpr.eval()
	paramExpr = dat.par.Paramexpr.eval()
	expr = returnExpr.replace('val', accessExpr)
	lines = [
		f'{varType} val;',
		'#ifdef THIS_HAS_REF_var',
		'val = THIS_var;',
		f'res = {expr};',
		'#else',
	]
	if paramExpr:
		expr = returnExpr.replace('val', paramExpr.replace('val', 'THIS_Defaultval'))
		lines.append(f'res = {expr}')
	elif defaultExpr:
		expr = returnExpr.replace('val', defaultExpr)
		lines.append(f'res = {expr};')
	else:
		lines.append('initDefVal(res);')
	lines += [
		'#endif',
	]
	code = '\n'.join(lines)
	dat.write(code)

