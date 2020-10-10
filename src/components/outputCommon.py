from typing import List

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def updateTextureInputs(
		comp: 'COMP',
		glslTop: 'TOP',
		textureTable: 'DAT',
		fixedInputs: 'List[TOP]' = None):
	for conn in glslTop.inputConnectors:
		conn.disconnect()
	if fixedInputs:
		for inputTop in fixedInputs:
			if inputTop:
				inputTop.outputConnectors[0].connect(glslTop)
	parent().clearScriptErrors(error='texerr*')
	for i in range(textureTable.numRows):
		texSelect = comp.op(f'sel_texture_{i}')
		if not texSelect:
			parent().addScriptError(f'texerr: Too many texture sources (failed on #{i})')
			return
		texSelect.outputConnectors[0].connect(glslTop)

def resetInfoParams(comp: 'COMP'):
	for page in comp.customPages:
		if page.name == 'Info':
			for par in page.pars:
				if not par.readOnly and not par:
					par.val = par.default
