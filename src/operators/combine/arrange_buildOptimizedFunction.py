from io import StringIO
from arrange import loadState, parCode, State

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	state = loadState()
	dat.write(_buildCode(state))

def _buildCode(state: 'State'):
	out = StringIO()
	out.write('void THIS_exposeIndex(int i) {\n#ifdef THIS_EXPOSE_index\nTHIS_index =i;\n#endif\n}\n')
	out.write('ReturnT thismap(CoordT p, ContextT ctx) {\n')
	if not state.stages:
		out.write('return createNonHitSdf();\n}\n')
		return out.getvalue()
	out.write('THIS_exposeIndex(0);\n')
	out.write(f'ReturnT res = {state.stages[0].inputCall()};\n')
	suffix = ''
	if state.rad is not None:
		suffix += ',' + parCode(state.rad)
	if state.num is not None:
		suffix += ',' + parCode(state.num) + ',' + parCode(state.off)
	if len(state.stages) > 1:
		for stage in state.stages[1:]:
			out.write(f'THIS_exposeIndex({stage.i});')
			if state.swap:
				out.write(f'res = cmb_{state.cmb}({stage.inputCall()},res{suffix});\n')
			else:
				out.write(f'res = cmb_{state.cmb}(res,{stage.inputCall()}{suffix});\n')
	out.write('return res;\n}\n')
	return out.getvalue()
