# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _HandlerPar:
		Hostop: OPParamT
		Source: OPParamT
		Required: BoolParamT

	class _Comp(COMP):
		par: _HandlerPar

class InputHandler:
	def __init__(self, handlerComp: 'COMP'):
		self.handlerPar = handlerComp.par

	def ResolveSourceParDefinition(self, errorTable: DAT | None = None):
		p = self.handlerPar.Source
		if p.bindMaster is not None:
			p = p.bindMaster
		o = p.eval()
		if not o:
			return
		if _isValidDefinitionDat(o):
			return o
		if o.isCOMP:
			d = o.op('definition')
			if _isValidDefinitionDat(d):
				return d
		if errorTable:
			mp = parent().par.Source.bindMaster
			if mp is None:
				msg = 'Invalid input source.'
			else:
				msg = f'Invalid {mp.label} source.'
			msg += ' Only ROPs and definition DATs are allowed.'
			errorTable.appendRow([parent().path, 'error', msg])

	def BuildValidationErrors(self, dat: DAT):
		dat.clear()
		if not hasattr(parent, 'raytk'):
			self.ResolveSourceParDefinition(dat)

	def _shouldBypass(self):
		host = self.handlerPar.Hostop.eval()
		opDef = host and host.op('opDefinition')
		if not opDef or opDef.par['Enable'] is None:
			return False
		return not opDef.par.Enable and not opDef.par['Useruntimebypass']

	def ProcessDefinitions(self, dat: DAT, inputDefs: DAT, supportedTypes: DAT, config: DAT):
		dat.copy(inputDefs)
		if dat.numRows < 2 or self._shouldBypass():
			return
		for column in ('coordType', 'contextType', 'returnType'):
			cell = dat[1, column]
			if cell:
				cell.val = _restrictExpandedTypes(cell.val, supportedTypes[column, 'types'].val.split(' '))
		dat.appendCol(['input:alias', config['alias', 1]])
		dat.appendCol(['input:vars', config['vars', 1]])
		dat.appendCol(['input:varInputs', config['varInputs', 1]])
		dat.appendCol(['input:handler', self.handlerPar.owner])

def _isValidDefinitionDat(o: OP | DAT | None):
	if not o or not o.isDAT:
		return False
	return o and o.isDAT and o.isTable and o.numRows > 0 and o[0, 0] == 'name'

def _restrictExpandedTypes(expandedTypes: str, supportedTypes: list[str]) -> str:
	return ' '.join([t for t in expandedTypes.split(' ') if t in supportedTypes])
