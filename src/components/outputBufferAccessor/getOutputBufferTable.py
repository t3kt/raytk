# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	dat.appendRow(['name', 'label', 'path', 'buffer'])
	o = parent().par.Outputop.eval()
	if not o:
		return
	if not o.isCOMP:
		parent().addScriptError('Output OP must be a COMP')
		return
	info = o.op('renderInfo')
	if not info or info.par['Outputtable'] is None:
		parent().addScriptError('Output OP must be a renderer or a render engine')
		return
	table = info.par.Outputtable.eval()
	if not table or table.numRows < 2:
		return
	for i in range(1, table.numRows):
		dat.appendRow([
			table[i, 'name'] or '',
			table[i, 'label'] or '',
			table[i, 'path'] or '',
			table[i, 'buffer'] or '',
		])
