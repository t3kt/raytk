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
		Typespec: CompParamT
		Autoindex: BoolParamT
		Index: IntParamT
		Name: StrParamT
		Label: StrParamT
		Localalias: StrParamT

def _parentPar() -> '_HandlerPar':
	# noinspection PyTypeChecker
	return parent().par

def _isValidDefinitionDat(o: 'Optional[Union[OP, DAT]]'):
	if not o or not o.isDAT:
		return False
	return o and o.isDAT and o.isTable and o.numRows > 0 and o[0, 0] == 'name'

def resolveSourceParDefinition(onError: 'Optional[Callable[[str], None]]' = None) -> 'Optional[DAT]':
	p = _parentPar().Source  # type: Par
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

def determineIndex():
	if not _parentPar().Autoindex:
		return _parentPar().Index.eval()
	host = _parentPar().Hostop.eval()  # type: COMP
	if not host:
		return 0
	# Check where the associated inDAT sits in the hosts inputs list
	ownIn = _getAttachedInDAT()
	if ownIn:
		for conn in host.inputConnectors:
			if conn.inOP and conn.inOP.isDAT and ownIn is conn.inOP:
				return 1 + conn.index
	# Look for digits in the first part of the name, with support for:
	# inputHandler3_foo5 -> 3
	# inputHandler5 -> 5
	handlerName = parent().name
	if handlerName.startswith('inputHandler'):
		if '_' in handlerName:
			handlerName = handlerName.split('_', maxsplit=1)[0]
		i = tdu.digits(handlerName)
		if i is not None:
			return i
	return 0

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
	dat.appendCol([
		'Index',
		'Defaultname',
		'Name',
		'Label',
		'Localalias',
	])
	dat.appendCol([''])
	host = _parentPar().Hostop.eval()
	ownIn = _getAttachedInDAT()
	baseName, localName = _parseHandlerName()

	if not _parentPar().Autoindex:
		index = int(_parentPar().Index)
	else:
		index = _determineAutoIndex(host=host, ownIn=ownIn, baseName=baseName)
	dat['Index', 1] = index
	dat['Defaultname', 1] = f'inputOp{index}'
	if _parentPar().Name:
		dat['Name', 1] = _parentPar().Name
	elif localName:
		dat['Name', 1] = localName
	elif ownIn:
		dat['Name', 1] = ownIn.name
	else:
		dat['Name', 1] = dat['Defaultname', 1]
	if _parentPar().Label:
		dat['Label', 1] = _parentPar().Label
	elif ownIn and ownIn.par.label:
		dat['Label', 1] = ownIn.par.label
	else:
		dat['Label', 1] = dat['Name', 1]
	if _parentPar().Localalias:
		dat['Localalias', 1] = _parentPar().Localalias
	else:
		dat['Localalias', 1] = dat['Defaultname', 1]

def _determineAutoIndex(
		host: 'Optional[COMP]',
		ownIn: 'Optional[inDAT]',
		baseName: 'Optional[str]'):
	if not host:
		return 0
	# Check where the associated inDAT sits in the hosts inputs list
	if ownIn:
		for conn in host.inputConnectors:
			if conn.inOP and conn.inOP.isDAT and ownIn is conn.inOP:
				return 1 + conn.index
	# Look for digits in the first part of the name, with support for:
	# inputHandler3_foo5 -> 3
	# inputHandler5 -> 5
	if baseName:
		i = tdu.digits(baseName)
		if i is not None:
			return i
	return 0
