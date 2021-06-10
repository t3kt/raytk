from raytkUtil import ROPInfo
from typing import Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from src.components.inspectorCore.inspectorCoreExt import InspectorCore

	iop.inspectorCore = InspectorCore(COMP())
	ipar.inspectorCore = InspectorCore(COMP()).state

class CompilerCore:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.core = iop.inspectorCore  # type: Union[InspectorCore, COMP]

	def Reset(self, _=None):
		self.core.Reset()

	def Load(self, o: 'OP'):
		pass

	@property
	def OutputOP(self) -> 'Optional[COMP]':
		return iop.inspectorCore.TargetComp

	@property
	def OutputOPInfo(self):
		return ROPInfo(self.OutputOP)
