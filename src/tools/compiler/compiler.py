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
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp
		self.inspectorCore = iop.inspectorCore  # type: InspectorCore | COMP
		self.compilerCore = iop.compilerCore  # type: CompilerCore | COMP
		self.state = ipar.compilerState

	def Reset(self, _=None):
		self.compilerCore.Reset()

	def Load(self, o: OP | COMP | str):
		self.compilerCore.Load(o)
		if not self.compilerCore.OutputOP:
			return
		pass
