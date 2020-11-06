# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def modifyCode(dat: 'textDAT'):
	dat.copy(dat.inputs[0])
	pass

def _getAdapter():
	return _adapters.get(parent().par.Adapter.eval())

def processDefinition(dat: 'scriptDAT'):
	dat.copy(dat.inputs[0])
	clearAdapterErrors()
	if dat.numRows < 2:
		return
	adapter = _getAdapter()
	if not adapter:
		return
	try:
		if not adapter.checkDefinition(dat):
			return
		adapter.processDefinition(dat)
	except _AdaptException as error:
		reportAdapterError(error)

def processFunction(dat: 'scriptDAT', definitionDat: 'DAT'):
	clearAdapterErrors()
	code = dat.inputs[0].text
	dat.clear()
	if not code:
		return
	adapter = _getAdapter()
	if not adapter:
		return
	try:
		if not adapter.checkDefinition(definitionDat):
			return
		code = adapter.processFunction(code, definitionDat[1, 'name'].val)
		dat.write(code)
	except _AdaptException as error:
		reportAdapterError(error)

def reportAdapterError(error: '_AdaptException'):
	parent().addScriptError('Adapter error: ' + str(error))

def clearAdapterErrors():
	parent().clearScriptErrors(error='Adapter error: *')

class _Adapter:
	def checkDefinition(self, dat: 'tableDAT') -> bool:
		raise NotImplementedError()

	def processDefinition(self, dat: 'scriptDAT'):
		raise NotImplementedError()

	def processFunction(self, code: str, name: str) -> str:
		raise NotImplementedError()

class _ReturnFloatToVec4X(_Adapter):
	def checkDefinition(self, dat: 'tableDAT'):
		retType = dat[1, 'returnType'].val
		if retType == 'vec4':
			return False
		elif retType == 'float':
			return True
		else:
			raise _AdaptException(f'Unsupported return type: {retType}')

	def processDefinition(self, dat: 'scriptDAT'):
		dat[1, 'returnType'] = 'float'

	def processFunction(self, code: str, name: str):
		if f' {name}(' not in code:
			raise _AdaptException(f'Function {name!r} not found in code:\n{code}')
		modName = name + '_o'
		code = code.replace(f' {name}(', f' {modName}(')
		if not code.endswith('\n'):
			code += '\n'
		code += f'#define {name}(p, ctx) vec4({modName}(p, ctx), 0., 0., 0.)'
		return code

class _AdaptException(Exception):
	pass

_adapters = {
	'returnfloattovec4x': _ReturnFloatToVec4X(),
}
