from typing import Dict, List, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def _table() -> 'DAT':
	return op('table')

def _hostPar() -> 'Optional[Par]':
	host = parent().par.Hostop.eval()
	return host and host.par[parent().par.Param]

def buildCode():
	mode = parent().par.Switchmode.eval()
	par = _hostPar()
	if par is None:
		return ''
	if mode == 'auto':
		mode = 'inline' if par.readOnly else 'switch'
	table = op('table')
	if mode == 'switch':
		return _buildRuntimeSwitch(table)
	else:  # inline
		return _prepareItemCode(table[par.eval(), 'code'])

def _prepareItemCode(code: 'Cell'):
	return str(code or '').replace(';', ';\n')

def _buildRuntimeSwitch(table: 'DAT'):
	code = f'switch (int(THIS_{parent().par.Param})) {{\n'
	for i in range(1, table.numRows):
		name = str(table[i, 'name'])
		itemCode = _prepareItemCode(table[i, 'code'])
		code += f'\tcase {i - 1}: /*{name}*/\n'
		code += f'\t\t{itemCode};\n'
		code += '\t\tbreak;\n'
	code += '}\n'
	return code

def _updateParamEnableExprs():
	table = _table()
	if table.numRows < 2:
		return
	hostPar = _hostPar()
	if hostPar is None:
		return
	paramModes = {}  # type: Dict[str, List[str]]
	for i in range(1, table.numRows):
		params = tdu.expand(table[i, 'params'].val)
		val = table[i, 'name'].val
		for param in params:
			if param in paramModes:
				paramModes[param].append(val)
			else:
				paramModes[param] = [val]
	host = hostPar.owner
	for param, vals in paramModes.items():
		par = host.par[param]
		par.enableExpr = f'me.par.{hostPar.name} in {repr(tuple(vals))}'

def _updateParamMenu():
	hostPar = _hostPar()
	if hostPar is None:
		return
	table = _table()
	if table.numRows < 2:
		return
	hostPar.menuNames = [c.val for c in table.col('name')[1:]]
	hostPar.menuLabels = [c.val for c in table.col('label')[1:]]

def updateParams():
	_updateParamMenu()
	if parent().par.Manageparamstates:
		_updateParamEnableExprs()
