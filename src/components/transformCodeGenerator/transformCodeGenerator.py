from typing import List, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Pars:
		Transformorder: StrParamT
		Rotateorder: StrParamT
		Enabletranslate: BoolParamT
		Enablerotate: BoolParamT
		Enablescale: BoolParamT
		Enablepivot: BoolParamT
		Scaletype: StrParamT
		Varname: StrParamT
		Useparamvars: BoolParamT
		Force3d: BoolParamT

def _configPar() -> 'Union[_Pars, ParCollection]':
	return parent().par

def _var():
	return _configPar().Varname.eval() or 'p'

def generateInitCode():
	if not _configPar().Useparamvars:
		return ''
	parts = []
	if _configPar().Enablepivot:
		parts += ['vec3 pivot = THIS_Pivot;']
	if _configPar().Enablescale:
		if _configPar().Scaletype == 'uniform':
			parts += ['float uniformscale = THIS_Uniformscale;']
		else:
			parts += ['vec3 scale = THIS_Scale;']
	if _configPar().Enablerotate:
		parts += ['vec3 rotate = THIS_Rotate;']
	if _configPar().Enabletranslate:
		parts += ['vec3 translate = THIS_Translate;']
	return '\n'.join(parts)

def _param(name: str):
	return name if _configPar().Useparamvars else 'THIS_' + name.capitalize()

def generateCode():
	parts = []
	v = _var()
	if _configPar().Enablepivot:
		parts += _branchByCoordType(
			f'{v} -= {_param("pivot")}.xy;',
			f'{v} -= {_param("pivot")};')
	for part in _configPar().Transformorder.eval():
		if part == 's':
			parts += _scaleCode()
		elif part == 'r':
			parts += _rotateCode()
		elif part == 't':
			parts += _translateCode()
	if _configPar().Enablepivot:
		parts += _branchByCoordType(
			f'{v} += {_param("pivot")}.xy;',
			f'{v} += {_param("pivot")};')
	return '\n'.join(parts)

def _scaleCode() -> 'List[str]':
	if not _configPar().Enablescale:
		return []
	v = _var()
	if _configPar().Scaletype == 'uniform':
		return [
			f'{v} /= {_param("uniformscale")};',
			f'valueAdjust /= {_param("uniformscale")};',
		]
	return _branchByCoordType(
		f'{v} /= {_param("scale")}.xy;',
		f'{v} /= {_param("scale")};')

def _rotateCode() -> 'List[str]':
	if not _configPar().Enablerotate:
		return []
	v = _var()
	return _branchByCoordType(
		f'pR({v}, {_param("rotate")}.z);',
		'\n'.join([
				f'{v} *= TDRotate{part.upper()}({_param("rotate")}.{part});'
				for part in _configPar().Rotateorder.eval()
		]))

def _translateCode() -> 'List[str]':
	if not _configPar().Enabletranslate:
		return []
	v = _var()
	return _branchByCoordType(
		f'{v} -= {_param("translate")}.xy;',
		f'{v} -= {_param("translate")};')

def _branchByCoordType(code2d, code3d):
	if _configPar().Force3d:
		return [code3d]
	return [
		'#ifdef THIS_COORD_TYPE_vec2',
		code2d,
		'#else',
		code3d,
		'#endif',
	]

def getParams() -> 'List[str]':
	params = []
	if _configPar().Enablescale:
		if _configPar().Scaletype == 'uniform':
			params.append('Uniformscale')
		else:
			params.append('Scale[xyz]')
	if _configPar().Enablerotate:
		params.append('Rotate[xyz]')
	if _configPar().Enabletranslate:
		params.append('Translate[xyz]')
	if _configPar().Enablepivot:
		params.append('Pivot[xyz]')
	return params
