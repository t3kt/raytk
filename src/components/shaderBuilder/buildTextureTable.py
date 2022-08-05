# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from shaderBuilder import ShaderBuilder
	ext.shaderBuilder = ShaderBuilder(COMP())

def onCook(dat):
	dat.clear()
	ext.shaderBuilder.V3_buildTextureTable(dat)
