from typing import Optional
from raytkUtil import InputInfo, TypeTableHelper

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _StatePar:
		Inputhandler: 'OPParamT'

	ipar.state = _StatePar()

class InputEditor:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@property
	def _stubHandler(self) -> 'COMP':
		return self.ownerComp.op('stubHandler')

	@property
	def _handlerComp(self) -> 'Optional[COMP]':
		return ipar.state.Inputhandler.eval()

	@property
	def _inputInfo(self) -> 'Optional[InputInfo]':
		comp = self._handlerComp
		if comp:
			return InputInfo(comp)

	@property
	def hasHandler(self):
		return bool(self._handlerComp)

	@property
	def inputRequiredPar(self) -> 'BoolParamT':
		return (self._handlerComp or self._stubHandler).par.Required

	def Attach(self, handler: 'COMP'):
		ipar.state.Inputhandler = handler
		info = self._inputInfo
		pass

	def Detach(self):
		ipar.state.Inputhandler = ''
		pass

	@property
	def allCoordTypes(self):
		return TypeTableHelper(self.ownerComp.op('typeTable')).coordTypes()

	@property
	def allContextTypes(self):
		return TypeTableHelper(self.ownerComp.op('typeTable')).contextTypes()

	@property
	def allReturnTypes(self):
		return TypeTableHelper(self.ownerComp.op('typeTable')).returnTypes()
