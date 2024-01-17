# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: DAT):
	effectiveMode = str(dat.inputs[1]['effectiveMode', 1])
	paramGroupTable = dat.inputs[0]  # type: DAT
	config = parent()
	dat.clear()

	periodParam = config.par.Periodparam
	phaseParam = config.par.Phaseparam
	periodField = config.par.Periodfield
	phaseField = config.par.Phasefield
	coordType = config.par.Coordtype or 'float'
	isInline = effectiveMode == 'inline'

	if isInline:
		usedParams = []
		for row in range(1, paramGroupTable.numRows):
			if paramGroupTable[row, 'handling'] == 'runtime':
				usedParams += tdu.split(paramGroupTable[row, 'names'])
		needPeriod = periodParam in usedParams
		needPhase = phaseParam in usedParams
	else:
		needPeriod = True
		needPhase = True

	lines = []

	if needPeriod:
		lines += [
			f'{coordType} period = THIS_{periodParam};',
		]
		if periodField:
			lines += [
				f'#ifdef THIS_HAS_INPUT_{periodField}',
				f'period *= inputOp_{periodField}(p, ctx);',
				'#endif'
			]
	if needPhase:
		lines += [
			f'{coordType} phase = THIS_{phaseParam};'
		]
		if phaseField:
			lines += [
				f'#ifdef THIS_HAS_INPUT_{phaseField}',
				f'phase += inputOp_{phaseField}(p, ctx);',
				'#endif',
			]
	lines += [
		'q = (q / period) + phase;',
	]

	dat.write('\n'.join('\t' + line for line in lines))
