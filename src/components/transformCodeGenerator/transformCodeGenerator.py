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

def _configPar() -> 'Union[_Pars, ParCollection]':
	return parent().par

def _var():
	return _configPar().Varname.eval() or 'p'

def generateCode():
	parts = []
	v = _var()
	if _configPar().Enablepivot:
		parts += _branchByCoordType(
			f'{v} -= vec2(THIS_Pivotx, THIS_Pivoty);',
			f'{v} -= THIS_Pivot;')
	for part in _configPar().Transformorder.eval():
		if part == 's':
			parts += _scaleCode()
		elif part == 'r':
			parts += _rotateCode()
		elif part == 't':
			parts += _translateCode()
	if _configPar().Enablepivot:
		parts += _branchByCoordType(
			f'{v} += vec2(THIS_Pivotx, THIS_Pivoty);',
			f'{v} += THIS_Pivot;')
	return '\n'.join(parts)

def _scaleCode() -> 'List[str]':
	if not _configPar().Enablescale:
		return []
	v = _var()
	if _configPar().Scaletype == 'uniform':
		return [
			f'{v} /= THIS_Uniformscale;',
			'valueAdjust /= THIS_Uniformscale;',
		]
	return _branchByCoordType(
		f'{v} /= vec2(THIS_Scalex, THIS_Scaley);',
		f'{v} /= THIS_Scale;')

def _rotateCode() -> 'List[str]':
	if not _configPar().Enablerotate:
		return []
	v = _var()
	return _branchByCoordType(
		f'pR({v}, THIS_Rotatez);',
		'\n'.join([
				f'{v} *= TDRotate{part.upper()}(THIS_Rotate{part});'
				for part in _configPar().Rotateorder.eval()
		]))

def _translateCode() -> 'List[str]':
	if not _configPar().Enabletranslate:
		return []
	v = _var()
	return _branchByCoordType(
		f'{v} -= vec2(THIS_Translatex, THIS_Translatey);',
		f'{v} -= THIS_Translate;')

def _branchByCoordType(code2d, code3d):
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
