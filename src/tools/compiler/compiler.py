from raytkUtil import InspectorTargetTypes
from typing import Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from src.components.inspectorCore.inspectorCoreExt import InspectorCore
	from .compilerCore.compilerCore import CompilerCore

	iop.inspectorCore = InspectorCore(COMP())
	ipar.inspectorCore = InspectorCore(COMP()).state
	iop.compilerCore = CompilerCore(COMP())

	class _CompilerState:
		pass

	ipar.compilerState = _CompilerState()

class Compiler:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.inspectorCore = iop.inspectorCore  # type: Union[InspectorCore, COMP]
		self.compilerCore = iop.compilerCore  # type: Union[CompilerCore, COMP]
		self.state = ipar.compilerState

	def Reset(self, _=None):
		self.compilerCore.Reset()

	def Load(self, o: 'Union[OP, COMP, str]'):
		self.compilerCore.Load(o)
		if not self.compilerCore.OutputOP:
			return
		pass
