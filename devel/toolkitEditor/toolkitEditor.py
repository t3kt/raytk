from raytkTools import RaytkTools

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .ropEditor.ropEditor import ROPEditor
	from typing import Union
	# noinspection PyTypeHints
	iop.ropEditor = ROPEditor(COMP())  # type: Union[ROPEditor, COMP]


class ToolkitEditor:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
	
	def Open(self, _=None):
		op('window').par.winopen.pulse()

	def EditROP(self, rop: 'COMP'):
		self.Open()
		iop.ropEditor.LoadROP(rop)

	@staticmethod
	def saveAllROPSpecs():
		RaytkTools().saveAllROPSpecs()
