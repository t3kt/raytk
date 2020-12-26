# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *


class ToolkitEditor:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
	
	def Open(self, _=None):
		op('window').par.winopen.pulse()
