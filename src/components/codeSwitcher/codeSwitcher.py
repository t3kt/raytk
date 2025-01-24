# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildStateTable(dat: DAT):
	_ensureExt()
	ext.codeSwitcher.buildStateTable(dat)

def buildParameterGroupTable(dat: DAT):
	_ensureExt()
	ext.codeSwitcher.buildParameterGroupTable(dat)

def buildMacroTable(dat: DAT, itemInfo: DAT):
	_ensureExt()
	ext.codeSwitcher.buildMacroTable(dat, itemInfo)

def buildCode():
	_ensureExt()
	return ext.codeSwitcher.buildCode()

def updateParams():
	_ensureExt()
	ext.codeSwitcher.updateParams()

def _ensureExt():
	if not hasattr(ext, 'codeSwitcher'):
		parent().par.ext0object = "op('./codeSwitcher').module.CodeSwitcher(me)"
		parent().par.ext0object.readOnly = True
		parent().par.ext0name = 'codeSwitcher'
		parent().par.ext0name.readOnly = True
		parent().par.ext0promote = True
		parent().par.ext0promote.readOnly = True
		parent().par.reinitextensions.pulse()

class CodeSwitcher:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp
		self.table = ownerComp.op('table')

	def _allHostPars(self):
		host = self.ownerComp.par.Hostop.eval()
		if not host:
			return []
		parName = self.ownerComp.par.Param.eval()
		if not parName:
			return []
		return host.pars(*tdu.expand(parName))

	def _firstHostPar(self):
		for p in self._allHostPars():
			return p

	def _effectiveMode(self):
		mode = self.ownerComp.par.Switchmode.eval()
		par = self._firstHostPar()
		if par is not None:
			if mode == 'auto':
				mode = 'inline'if par is None or par.readOnly else 'switch'
			elif mode == 'autoconst':
				mode = 'constswitch' if par is None or par.readOnly else 'switch'
		return mode

	def buildStateTable(self, dat: DAT):
		dat.clear()
		dat.appendRow(['effectiveMode', self._effectiveMode()])

	def buildParameterGroupTable(self, dat:DAT):
		dat.clear()
		dat.appendRow(['names', 'source', 'handling', 'readOnlyHandling', 'conversion', 'enable'])
		mode = self._effectiveMode()
		if self.ownerComp.par.Param:
			if mode == 'none':
				dat.appendRow([self.ownerComp.par.Param, 'param', 'macro', '', '', '1'])
			elif mode == 'constswitch':
				dat.appendRow([self.ownerComp.par.Param, 'param', 'constant', '', '', '1'])
			else:
				dat.appendRow([self.ownerComp.par.Param, 'param', 'runtime', '', '', '1'])
		if self.ownerComp.par.Manageparamstates:
			if mode == 'switch' or mode == 'constswitch' or self.ownerComp.par.Alwaysincludeallparams:
				params = ' '.join(self._paramModes('params').keys()).strip()
				boolParams = ' '.join(self._paramModes('boolParams').keys()).strip()
			else:
				params = str(self.ownerComp.op('currentItemInfo')[1, 'params'] or '').strip()
				boolParams = str(self.ownerComp.op('currentItemInfo')[1, 'boolParams'] or '').strip()
			if params:
				dat.appendRow([params, 'param', 'runtime', 'macro', '', '1'])
			if boolParams:
				dat.appendRow([boolParams, 'param', 'runtime', 'constant', '', '1'])

	@staticmethod
	def buildMacroTable(dat: DAT, itemInfo: DAT):
		dat.clear()
		if itemInfo.numRows < 2:
			return
		val = str(itemInfo[1, 'macros'] or '')
		if not val:
			return
		for v in val.split():
			dat.appendRow(['', v, ''])

	def buildCode(self):
		par = self._firstHostPar()
		if par is None and not self.ownerComp.par.Indexexpr:
			return ''
		mode = self._effectiveMode()
		table = self.table
		if mode == 'switch':
			return self._buildRuntimeSwitch(isConstant=False)
		elif mode == 'constswitch':
			return self._buildRuntimeSwitch(isConstant=True)
		elif mode == 'inline':
			return self._prepareItemCode(table[par.eval(), 'code']) + ';'
		else:
			return ''

	def _buildRuntimeSwitch(self, isConstant: bool):
		paramName = self.ownerComp.par.Param
		expr = self.ownerComp.par.Indexexpr or f'int(THIS_{paramName})'
		code = f'switch ({expr}) {{\n'
		for i in range(1, self.table.numRows):
			name = str(self.table[i, 'name'])
			itemCode = self._prepareItemCode(self.table[i, 'code'])
			if not itemCode.strip():
				continue
			if isConstant and paramName:
				code += f'\tcase THISTYPE_{paramName}_{name}:\n'
			else:
				code += f'\tcase {i - 1}: /*{name}*/\n'
			code += f'\t\t{itemCode};\n'
			code += '\t\tbreak;\n'
		code += '}\n'
		return code

	@staticmethod
	def _prepareItemCode(code: Cell):
		code = str(code or '')
		if code.endswith(';'):
			code = code[:-1]
		return code.replace(';', ';\n')

	def _paramModes(self, column: str):
		if self.table.numRows < 2:
			return {}
		paramModes = {}
		for i in range(1, self.table.numRows):
			params = tdu.expand(self.table[i, column] or '')
			val = self.table[i, 'name'].val
			for param in params:
				if param in paramModes:
					paramModes[param].append(val)
				else:
					paramModes[param] = [val]
		return paramModes

	def _updateParamEnableExprs(self):
		if self.table.numRows < 2:
			return
		hostPar = self._firstHostPar()
		if hostPar is None:
			return
		paramModes = self._paramModes('params')
		paramModes.update(self._paramModes('boolParams'))
		allValues = set(paramModes.keys())
		host = hostPar.owner
		for param, vals in paramModes.items():
			par = host.par[param]
			if par is None:
				continue
			if set(vals) == allValues:
				par.enableExpr = ''
				par.enable = True
			else:
				par.enableExpr = f'me.par.{hostPar.name} in {repr(tuple(vals))}'

	def _updateParamMenu(self):
		if self.table.numRows < 2:
			return
		names = [c.val for c in self.table.col('name')[1:]]
		labels = [c.val for c in self.table.col('label')[1:]]
		for hostPar in self._allHostPars():
			hostPar.menuNames = names
			hostPar.menuLabels = labels

	def updateParams(self):
		self._updateParamMenu()
		if self.ownerComp.par.Manageparamstates:
			self._updateParamEnableExprs()
