from arrange import loadState

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Optional

def onCook(dat: 'DAT'):
	dat.clear()
	dat.appendRow(['names', 'source', 'handling', 'readOnlyHandling', 'conversion', 'enable'])
	state = loadState()
	def _addPar(par: 'Optional[Par]'):
		if par is not None and par.mode != ParMode.CONSTANT:
			dat.appendRow([par.name, 'param', 'runtime', 'macro', '', '1'])
	_addPar(state.rad)
	_addPar(state.num)
	_addPar(state.off)
	for stage in state.stages:
		if stage.hasTranslate():
			_addPar(stage.tra[0])
			_addPar(stage.tra[1])
			_addPar(stage.tra[2])
