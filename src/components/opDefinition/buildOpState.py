from opDefinition import buildOpState

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onSetupParameters(dat: 'scriptDAT'):
	page = dat.appendCustomPage('Custom')
	page.appendToggle('Pretty')

def onCook(dat: 'DAT'):
	dat.clear()
	state = buildOpState()
	dat.write(state.toJson(pretty=dat.par.Pretty.eval()))
