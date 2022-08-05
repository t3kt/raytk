# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from shaderBuilder import ShaderBuilder
	ext.shaderBuilder = ShaderBuilder(COMP())

def onCook(dat):
	ext.shaderBuilder.writeShader(
		dat,
		macroTable=dat.inputs[0],
		typeDefMacroTable=dat.inputs[1],
		textureTable=dat.inputs[2],
		outputBufferTable=dat.inputs[3],
		variableTable=dat.inputs[4],
	)
