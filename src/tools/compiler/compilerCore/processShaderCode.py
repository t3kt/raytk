# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .compilerCore import CompilerCore
	ext.compilerCore = CompilerCore(COMP())

def onCook(dat):
	dat.clear()
	dat.write(ext.compilerCore.processShaderCode(dat.inputs[0].text))
