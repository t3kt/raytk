import json

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onSetupParameters(dat: scriptDAT):
	page = dat.appendCustomPage('Custom')
	page.appendToggle('Pretty')

def onCook(dat: DAT):
	mod.opDefinition.ensureExt(parent())
	dat.clear()
	state = ext.opDefinition.buildRopState()
	obj = state.toDict()
	dat.write(json.dumps(obj, indent='  ' if dat.par.Pretty.eval() else None))
