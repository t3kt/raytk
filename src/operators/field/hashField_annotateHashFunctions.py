# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: scriptDAT):
	dat.copy(dat.inputs[0])
	typeLabels = {
		'uint': 'X[u]',
		'uvec2': 'XY[u]',
		'uvec3': 'XYZ[u]',
		'uvec4': 'XYZW[u]',
		'float': 'X',
		'vec2': 'XY',
		'vec3': 'XYZ',
		'vec4': 'XYZW',
	}
	for i in range(1, dat.numRows):
		inLabel = dat[i, 'inputType'].val
		inLabel = typeLabels.get(inLabel) or inLabel
		outLabel = dat[i, 'outputType'].val
		outLabel = typeLabels.get(outLabel) or outLabel
		dat[i, 'label'] += f'  ({inLabel} -> {outLabel})'
