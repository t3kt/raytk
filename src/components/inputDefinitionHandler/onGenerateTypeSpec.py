# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onPulse(par):
	handler = parent()
	specPar = handler.par.Typespec
	if specPar.eval():
		return
	problemHandlerPars = [
		p.name
		for p in handler.pars('Support*type*')
		if p.mode != ParMode.CONSTANT
	]
	if problemHandlerPars:
		msg = f'Unable to generate type spec due to expr pars: {" ".join(problemHandlerPars)}'
		print(msg)
		ui.status = msg
		return
	ui.undo.startBlock('Generate type spec')
	try:
		autoSpec = op('typeSpec')
		templateSpec = autoSpec.par.clone.eval()
		newSpec = handler.parent().copy(templateSpec, name=handler.name + '_typeSpec')  # type: COMP
		newSpec.nodeCenterX = handler.nodeCenterX + 180
		newSpec.nodeCenterY = handler.nodeCenterY - 50
		newSpec.nodeWidth = 100
		newSpec.nodeHeight = 50
		newSpec.dock = handler
		handler.showDocked = True

		for newPar in newSpec.pars('All*type', 'Coordtype*', 'Contexttype*', 'Returntype*'):
			newPar.val = autoSpec.par[newPar.name].eval()

		specPar.val = newSpec
	finally:
		ui.undo.endBlock()
