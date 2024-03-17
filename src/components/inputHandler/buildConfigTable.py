# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from inputHandler import _HandlerPar

	class _HandlerParFull(_HandlerPar):
		Localalias: StrParamT
		Variables: StrParamT
		Variableinputs: StrParamT

# Everything in this table gets frozen at build time.
def onCook(dat: scriptDAT):
	dat.clear()
	host = _parentPar().Hostop.eval()
	ownIn = _getAttachedInDAT()
	baseName, localName = _parseHandlerName()

	index = _determineAutoIndex(host=host, ownIn=ownIn, baseName=baseName)
	if _parentPar().Localalias:
		alias = _parentPar().Localalias
	else:
		alias = f'inputOp{index}'
	dat.appendRows([
		['alias', alias],
		['vars', _parentPar().Variables],
		['varInputs', _parentPar().Variableinputs],
	])


def _parentPar() -> '_HandlerParFull':
	# noinspection PyTypeChecker
	return parent().par

def _getAttachedInDAT() -> inDAT | None:
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
