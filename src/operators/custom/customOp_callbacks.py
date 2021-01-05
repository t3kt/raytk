# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCreate(master=None, **kwargs):
	# detach clone, even in devel
	parent().par.enablecloning = False
	op('customOpController').par.Createfunction.pulse()
