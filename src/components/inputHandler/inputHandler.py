# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class InputHandler:
	def __init__(self, handlerComp: COMP):
		self.handlerComp = handlerComp

	def ResolveSourceParDefinition(self, errorTable: DAT | None = None):
		p = self.handlerComp.par.Source
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
			mp = self.handlerComp.par.Source.bindMaster
			errorTable.appendRow([
				self.handlerComp.path, 'error',
				f'Invalid {"input" if mp is None else mp.label} source. Only ROPs and definition DATs are allowed.'])

	def BuildValidationErrors(self, dat: DAT):
		dat.clear()
		if not hasattr(parent, 'raytk'):
			self.ResolveSourceParDefinition(dat)

	def _shouldBypass(self):
		host = self.handlerComp.par.Hostop.eval()
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
		dat.appendCol(['input:handler', self.handlerComp])

	def BuildConfigTable(self, dat: DAT):
		dat.clear()
		host = self.handlerComp.par.Hostop.eval()
		ownIn = self._getAttachedInDAT()
		baseName, localName = self._parseHandlerName()
		sourcePar = self.handlerComp.par.Source.bindMaster
		index = _determineAutoIndex(host=host, ownIn=ownIn, baseName=baseName)
		defaultName = f'inputOp{index}'
		if sourcePar is not None:
			name = sourcePar.name
		elif localName:
			name = localName
		elif ownIn:
			name = ownIn.name
		else:
			name = defaultName
		if self.handlerComp.par.Label:
			label = self.handlerComp.par.Label
		elif ownIn and ownIn.par.label:
			label = ownIn.par.label
		elif sourcePar is not None:
			label = sourcePar.label
		else:
			label = name.replace('_', ' ')
		if self.handlerComp.par.Localalias:
			alias = self.handlerComp.par.Localalias
		else:
			alias = defaultName
		dat.appendRows([
			['name', name],
			['label', label],
			['alias', alias],
			['vars', self.handlerComp.par.Variables],
			['varInputs', self.handlerComp.par.Variableinputs],
		])

	def _getAttachedInDAT(self) -> inDAT | None:
		handler = self.handlerComp
		host = handler.par.Hostop.eval()
		if not host:
			return
		if len(handler.inputConnectors) < 1:
			return
		conn = handler.inputConnectors[0]
		if len(conn.connections) < 1:
			return
		o = conn.connections[0].owner
		if isinstance(o, inDAT):
			return o
		if isinstance(o, nullDAT) and o.inputs and isinstance(o.inputs[0], inDAT):
			return o.inputs[0]

	# returns e.g. ("inputHandler5", "stuffField")
	def _parseHandlerName(self):
		name = self.handlerComp.name
		if name == 'inputHandler':
			return 'None', None
		if not name.startswith('inputHandler'):
			return None, name
		if '_' in name:
			return name.split('_', maxsplit=1)
		return name, None

def _isValidDefinitionDat(o: OP | DAT | None):
	if not o or not o.isDAT:
		return False
	return o and o.isDAT and o.isTable and o.numRows > 0 and o[0, 0] == 'name'

def _restrictExpandedTypes(expandedTypes: str, supportedTypes: list[str]) -> str:
	return ' '.join([t for t in expandedTypes.split(' ') if t in supportedTypes])

def _determineAutoIndex(
		host: COMP | None,
		ownIn: inDAT | None,
		baseName: str | None):
	if not host:
		return 0
	# Look for digits in the first part of the name, with support for:
	# inputHandler3_foo5 -> 3
	# inputHandler5 -> 5
	if baseName:
		i = tdu.digits(baseName)
		if i is not None:
			return i
	# Check where the associated inDAT sits in the hosts inputs list
	if ownIn:
		for conn in host.inputConnectors:
			if conn.inOP and conn.inOP.isDAT and ownIn is conn.inOP:
				return 1 + conn.index
	return 0
