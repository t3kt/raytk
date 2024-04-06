# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from shaderPanel import ShaderPanel
	ext.shaderPanel = ShaderPanel(COMP())

def onCook(dat: DAT):
	dat.clear()
	ext.shaderPanel.fillPreparedCode(
		dat,
		codeBlocks=dat.inputs[0],
		selectedName=ipar.shaderPanelState.Codeblock.eval(),
		definition=dat.inputs[1],
	)
