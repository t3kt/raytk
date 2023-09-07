from io import StringIO

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: 'scriptDAT'):
	dat.clear()
	varTable = op('eval_variables')
	out = StringIO()
	out.write('ReturnT thismap(CoordT p, ContextT ctx) {\n')
	for i in range(1, 8):
		if varTable[i, 'enable'] != '1':
			continue
		varName = varTable[i, 'name'].val
		out.write(f'  #ifdef THIS_EXPOSE_{varName}\n')
		out.write(f'    THIS_{varName} = THIS_{varName}_asVarT(inputOp_variable{i}(p, ctx));\n')
		out.write('  #endif\n')
		pass
	out.write('  return inputOp_output(p, ctx);\n')
	out.write('}\n')
	dat.write(out.getvalue())
