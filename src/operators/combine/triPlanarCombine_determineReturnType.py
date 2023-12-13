# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	dat.appendRow([_getType(dat)])

def _getType(dat: DAT):
	typeSetting = parent().par.Returntype.eval()
	if typeSetting != 'auto':
		return typeSetting
	xyType = str(dat.inputs[0][1, 'returnType'] or '')
	yzType = str(dat.inputs[1][1, 'returnType'] or '')
	zxType = str(dat.inputs[2][1, 'returnType'] or '')
	if not any([xyType, yzType, zxType]):
		return 'vec4'
	if 'vec4' in xyType or 'vec4' in yzType or 'vec4' in zxType:
		return 'vec4'
	return 'float'
