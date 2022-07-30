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

def _parentPar() -> '_HandlerPar':
	# noinspection PyTypeChecker
	return parent().par

# WARNING: This reaches outside into the host OP and looks for opDefinition.
def shouldBypass() -> bool:
	host = _parentPar().Hostop.eval()
	opDef = host and host.op('opDefinition')
	if not opDef or opDef.par['Enable'] is None:
		return False
	return not opDef.par.Enable and not opDef.par['Useruntimebypass']

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

def buildValidationErrors(dat: 'DAT'):
	dat.clear()
	if hasattr(parent, 'raytk'):
		return

	def _addError(msg):
		if not dat.numRows:
			dat.appendRow(['path', 'level', 'message'])
		dat.appendRow([parent().path, 'error', msg])

	resolveSourceParDefinition(_addError)
