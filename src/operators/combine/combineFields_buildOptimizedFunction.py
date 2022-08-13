from io import StringIO
import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	dat.write(_buildCode())

def _buildCode():
	out = StringIO()
	out.write('ReturnT thismap(CoordT p, ContextT ctx) {\n')
	if op('typeSpec').par.Returntypevec4:
		returnType = 'vec4'
		adaptFunc = 'fillToVec4'
	else:
		returnType = 'float'
		adaptFunc = ''
	template = op('operations')[parent().par.Operation.eval(), 'code'].val
	if parent().par.Swaporder:
		template = re.sub(r'\ba\b', 'X', re.sub(r'\bb\b', 'res', template))
	else:
		template = re.sub(r'\ba\b', 'res', re.sub(r'\bb\b', 'X', template))
	inputs = [
		i
		for i in range(1, 9)
		if op(f'definition_{i}').numRows > 1
	]
	def inCall(i):
		if adaptFunc:
			return f'{adaptFunc}(inputOp{i}(p,ctx))'
		return f'inputOp{i}(p,ctx)'
	if not inputs:
		out.write(f'return {returnType}(0.);\n')
	elif len(inputs) == 1:
		out.write(f'return {inCall(inputs[0])};\n')
	else:
		out.write(f'ReturnT res = {inCall(inputs[0])};\n')
		for i in inputs[1:]:
			out.write(template.replace('X', inCall(i)))
			out.write(';\n')
		out.write('return res;\n')
	out.write('}\n')
	return out.getvalue()
