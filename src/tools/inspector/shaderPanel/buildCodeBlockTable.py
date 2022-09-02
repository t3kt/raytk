# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from shaderPanel import ShaderPanel
	ext.shaderPanel = ShaderPanel(COMP())

def onCook(dat):
	dat.clear()
	ext.shaderPanel.buildCodeBlockTable(
		dat,
		includes=dat.inputs[0],
		mainCode=dat.inputs[1],
		definition=dat.inputs[2],
	)