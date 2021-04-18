# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Callable, Optional

def checkInputDefinition(dat: 'DAT'):
	dat.clear()
	dat.copy(dat.inputs[0])
	if dat.numRows < 2:
		return
	_checkTableTypes(dat, None, ignoreEmpty=False)

def processInputDefinition(dat: 'DAT'):
	dat.clear()
	dat.copy(dat.inputs[0])
	if dat.numRows < 2:
		return
	if not _checkTableTypes(dat, None, ignoreEmpty=False):
		return
	# TODO: RESTRICT TYPES

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

def onSupportChange():
	_handleChange()

def onInputDefinitionChange():
	_handleChange()

def _handleChange():
	d = op('check_definition')
	if d:
		d.cook(force=True)

def buildValidationErrors(dat: 'DAT', inputDef: 'DAT'):
	dat.clear()

	def _addError(msg):
		if not dat.numRows:
			dat.appendRow(['path', 'level', 'message'])
		dat.appendRow([parent().path, 'error', msg])

	if parent().par.Required and inputDef.numRows < 2:
		_addError('Required input is missing')
	_checkTableTypes(inputDef, _addError, ignoreEmpty=True)
