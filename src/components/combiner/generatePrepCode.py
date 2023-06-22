# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: 'DAT'):
	paramGroupTable = dat.inputs[0]  # type: DAT
	effectiveMode = str(dat.inputs[1]['effectiveMode', 1])
	config = parent()
	dat.clear()

	radiusParam = config.par.Radiusparam
	numberParam = config.par.Numberparam
	offsetParam = config.par.Offsetparam
	radiusField = config.par.Radiusfield
	numberField = config.par.Numberfield
	offsetField = config.par.Offsetfield
	isInline = effectiveMode == 'inline'

	if isInline:
		usedParams = []
		for row in range(1, paramGroupTable.numRows):
			if paramGroupTable[row, 'handling'] == 'runtime':
				usedParams += tdu.split(paramGroupTable[row, 'names'])
		needRadius = radiusParam in usedParams
		needNumber = numberParam in usedParams
		needOffset = offsetParam in usedParams
	else:
		needRadius = True
		needNumber = True
		needOffset = True

	lines = []

	if needRadius:
		lines += [
			f'float r = THIS_{radiusParam};',
		]
		if radiusField:
			lines += [
				f'#ifdef THIS_HAS_INPUT_{radiusField}',
				f'r *= inputOp_{radiusField}(p, ctx);',
				'#endif'
			]
	if needNumber:
		if numberField:
			lines += [
				f'#ifdef THIS_HAS_INPUT_{numberField}',
				f'float n = inputOp_{numberField}(p, ctx);',
				'#else',
				f'float n = THIS_{numberParam};',
				'#endif',
			]
		else:
			lines += [
				f'float n = THIS_{numberParam};'
			]
	if needOffset:
		lines += [
			f'float o = THIS_{offsetParam};'
		]
		if offsetField:
			lines += [
				f'#ifdef THIS_HAS_INPUT_{offsetField}',
				f'o += inputOp_{offsetField}(p, ctx);',
				'#endif',
			]
		else:
			# this causes problems with offset fields, so only do it when not using a field
			lines += ['o = mod(o, r / n * 2.);']

	dat.write('\n'.join('\t' + line for line in lines))
