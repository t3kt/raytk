# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Variable')
	page.appendStr('Variabletype', label='Variable Type')
	page.appendStr('Fieldtype', label='Field Type')
	page.appendStr('Returntype', label='Return Type')
	page.appendStr('Defaultexpr', label='Default Expr')
	page.appendStr('Accessexpr', label='Access Expr')
	page.appendStr('Returnexpr', label='Return Expr')

def onCook(dat: 'DAT'):
	dat.clear()
	varType = dat.par.Variabletype.eval()
	fieldType = dat.par.Fieldtype.eval()
	returnType = dat.par.Returntype.eval()
	defaultExpr = dat.par.Defaultexpr.eval()
	accessExpr = dat.par.Accessexpr.eval()
	returnExpr = dat.par.Returnexpr.eval()
	lines = [
		f'{varType} val;',
		'#ifdef THIS_HAS_REF_var',
		'val = THIS_var;',
		'#else',
	]
	if defaultExpr:
		lines.append(f'val = {defaultExpr};')
	else:
		lines.append('initDefVal(val);')
	expr = returnExpr.replace('val', accessExpr)
	lines += [
		'#endif',
		f'res = {expr};',
	]
	code = '\n'.join(lines)
	dat.write(code)

