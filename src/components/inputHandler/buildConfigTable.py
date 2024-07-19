# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

# Everything in this table gets frozen at build time.
def onCook(dat: scriptDAT):
	mod.inputHandler.InputHandler(parent()).BuildConfigTable(dat)
