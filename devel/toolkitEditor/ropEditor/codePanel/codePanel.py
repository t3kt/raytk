# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from ..ropEditor import ROPEditor
	ext.ropEditor = ROPEditor(COMP())

	class _Pars(ParCollection):
		Selectedblock: 'StrParamT'

	class _COMP(COMP):
		par: _Pars

class CodePanel:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	def createCurrentBlock(self):
		# TODO: create block
		pass

	def deleteCurrentBlock(self):
		# TODO: delete block
		pass
