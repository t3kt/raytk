from io import StringIO
from composeSdf import loadStages, parCode, Stage

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List

def onCook(dat):
	dat.clear()
	stages = loadStages()
	dat.write(_buildCode(stages))

def _buildCode(stages: 'List[Stage]'):
	out = StringIO()
	out.write('ReturnT thismap(CoordT p, ContextT ctx) {\n')
	if not stages:
		out.write('return createNonHitSdf();\n}\n')
		return out.getvalue()
	out.write(f'ReturnT res = {stages[0].inputCall()};\n')
	if len(stages) > 1:
		for stage in stages:
			out.write(f'res = cmb_{stage.cmb}(res, {stage.inputCall()}')
			if stage.rad is not None:
				out.write(f', {parCode(stage.rad)}')
			if stage.num is not None:
				out.write(f', {parCode(stage.num)}, {parCode(stage.off)}')
			out.write(');\n')
	out.write('return res;\n}\n')
	return out.getvalue()
