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

def _checkType(typeName: str, typeCategory: str, onError: 'Optional[Callable[[str], None]]', ignoreEmpty: bool):
	if not typeName:
		if ignoreEmpty:
			return True
		if onError:
			onError(f'Invalid input {typeCategory}: {typeName!r}')
		return False
	supported = tdu.split(op('supportedTypes')[typeCategory, 'types'] or '')
	if typeName in supported:
		return True
	if onError:
		onError(f'Input does not support {typeCategory} {typeName}')
	return False

def _checkTableTypes(dat: 'DAT', onError: 'Optional[Callable[[str], None]]', ignoreEmpty: bool):
	_checkType(str(dat[1, 'coordType'] or ''), 'coordType', onError, ignoreEmpty)
	_checkType(str(dat[1, 'contextType'] or ''), 'contextType', onError, ignoreEmpty)
	_checkType(str(dat[1, 'returnType'] or ''), 'returnType', onError, ignoreEmpty)

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
