from typing import Union, Optional
from raytkUtil import ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from components.inspectorCore.inspectorCoreExt import InspectorCore
	# noinspection PyTypeHints
	iop.inspectorCore = InspectorCore(COMP())  # type: Union[COMP, InspectorCore]

class ROPEditor:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def loadROP(o: 'Union[OP, DAT, COMP, str]'):
		iop.inspectorCore.Inspect(o)

	@property
	def ROP(self) -> 'Optional[COMP]':
		return iop.inspectorCore.TargetComp

	@property
	def ROPInfo(self):
		return ROPInfo(self.ROP)
