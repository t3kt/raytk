# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	iop.host = COMP()

class CustomOp:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
