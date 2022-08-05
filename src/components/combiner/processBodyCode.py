# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: 'DAT'):
	code = dat.inputs[0].text

	config = parent()
	swapInputsParam = config.par.Swapinputsparam

	if not code or not swapInputsParam:
		dat.copy(dat.inputs[0])
		return

	effectiveMode = str(dat.inputs[1]['effectiveMode', 1])
	isInline = effectiveMode == 'inline'

	if isInline:
		code = '\n'.join([
			f'#ifdef THIS_{swapInputsParam}',
			'swap(res1, res2);',
			'#endif',
			code
		])
	else:
		code = '\n'.join([
			f'if (IS_TRUE(THIS_{swapInputsParam})) {{',
			'swap(res1, res2);',
			'}',
			code
		])

	dat.clear()
	dat.write(code)
