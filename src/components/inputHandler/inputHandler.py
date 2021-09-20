# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from typing import Callable, Optional, Union

	class _HandlerPar:
		Hostop: OPParamT
		Source: OPParamT
		Required: BoolParamT
		Autoindex: BoolParamT
		Index: IntParamT
		Name: StrParamT
		Label: StrParamT
		Localalias: StrParamT
		Help: StrParamT

def _parentPar() -> '_HandlerPar':
	# noinspection PyTypeChecker
	return parent().par

# WARNING: This reaches outside into the host OP and looks for opDefinition.
def shouldBypass() -> bool:
	host = _parentPar().Hostop.eval()
	opDef = host and host.op('opDefinition')
	if not opDef or opDef.par['Enable'] is None:
		return False
	return not opDef.par.Enable

def _isValidDefinitionDat(o: 'Optional[Union[OP, DAT]]'):
	if not o or not o.isDAT:
		return False
	return o and o.isDAT and o.isTable and o.numRows > 0 and o[0, 0] == 'name'

def resolveSourceParDefinition(onError: 'Optional[Callable[[str], None]]' = None) -> 'Optional[DAT]':
	p = _parentPar().Source
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
	if onError:
		mp = parent().par.Source.bindMaster
		if mp is None:
			msg = 'Invalid input source.'
		else:
			msg = f'Invalid {mp.label} source.'
		onError(msg + ' Only ROPs and defintion DATs are allowed.')

def _getAttachedInDAT() -> 'Optional[inDAT]':
	host = _parentPar().Hostop.eval()
	if not host:
		return
	handler = parent()
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
def _parseHandlerName():
	name = parent().name
	if name == 'inputHandler':
		return 'None', None
	if not name.startswith('inputHandler'):
		return None, name
	if '_' in name:
		return name.split('_', maxsplit=1)
	return name, None

# Everything in this table gets frozen at build time.
def buildConfigTable(dat: 'scriptDAT'):
	dat.clear()
	host = _parentPar().Hostop.eval()
	ownIn = _getAttachedInDAT()
	baseName, localName = _parseHandlerName()
	sourcePar = _parentPar().Source.bindMaster

	if not _parentPar().Autoindex:
		index = int(_parentPar().Index)
	else:
		index = _determineAutoIndex(host=host, ownIn=ownIn, baseName=baseName)
	defaultName = f'inputOp{index}'
	if _parentPar().Name:
		name = _parentPar().Name
	elif sourcePar is not None:
		name = sourcePar.name
	elif localName:
		name = localName
	elif ownIn:
		name = ownIn.name
	else:
		name = defaultName
	if _parentPar().Label:
		label = _parentPar().Label
	elif ownIn and ownIn.par.label:
		label = ownIn.par.label
	elif sourcePar is not None:
		label = sourcePar.label
	else:
		label = name.replace('_', ' ')
	if _parentPar().Localalias:
		alias = _parentPar().Localalias
	else:
		alias = defaultName
	if _parentPar().Help:
		helpText = _parentPar().Help
	elif sourcePar is not None and sourcePar.help:
		helpText = sourcePar.help
	else:
		helpText = ''
	dat.appendRows([
		['index', index],
		['name', name],
		['label', label],
		['alias', alias],
		['help', helpText],
	])

def _determineAutoIndex(
		host: 'Optional[COMP]',
		ownIn: 'Optional[inDAT]',
		baseName: 'Optional[str]'):
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

def buildValidationErrors(dat: 'DAT', inputDef: 'DAT'):
	dat.clear()

	def _addError(msg):
		if not dat.numRows:
			dat.appendRow(['path', 'level', 'message'])
		dat.appendRow([parent().path, 'error', msg])

	resolveSourceParDefinition(_addError)
	if parent().par.Required and inputDef.numRows < 2:
		_addError('Required input is missing')
	_checkTableTypes(inputDef, _addError, ignoreEmpty=True)

def _checkType(typeName: str, typeCategory: str, onError: 'Optional[Callable[[str], None]]', ignoreEmpty: bool):
	if not typeName:
		if ignoreEmpty:
			return True
		if onError:
			onError(f'Invalid input {typeCategory}: {typeName!r}')
		return False
	supported = tdu.split(op('supportedTypes')[typeCategory, 'types'] or '')
	if ' ' in typeName:
		if any(t in supported for t in typeName.split(' ')):
			return True
	else:
		if typeName in supported:
			return True
	if onError:
		onError(f'Input does not support {typeCategory} {typeName}')
	return False

def _checkTableTypes(dat: 'DAT', onError: 'Optional[Callable[[str], None]]', ignoreEmpty: bool):
	validCoord = _checkType(str(dat[1, 'coordType'] or ''), 'coordType', onError, ignoreEmpty)
	validContext = _checkType(str(dat[1, 'contextType'] or ''), 'contextType', onError, ignoreEmpty)
	validReturn = _checkType(str(dat[1, 'returnType'] or ''), 'returnType', onError, ignoreEmpty)
	return validCoord and validContext and validReturn
