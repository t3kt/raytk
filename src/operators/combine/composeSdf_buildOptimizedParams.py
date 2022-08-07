from composeSdf import loadStages

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Optional

def onCook(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['names', 'source', 'handling', 'readOnlyHandling', 'conversion', 'enable'])
	def _addPar(par: 'Optional[Par]'):
		if par is not None and par.mode != ParMode.CONSTANT:
			dat.appendRow([par.name, 'param', 'runtime', 'macro', '', '1'])
	for stage in loadStages():
		_addPar(stage.tra[0])
		_addPar(stage.tra[1])
		_addPar(stage.tra[2])
		_addPar(stage.rad)
		_addPar(stage.num)
		_addPar(stage.off)
