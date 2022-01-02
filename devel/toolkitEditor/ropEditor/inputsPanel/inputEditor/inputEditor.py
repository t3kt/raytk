from typing import List, Optional
from raytkUtil import InputInfo

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

class TypeTableHelper:
	def __init__(self, table: 'DAT'):
		self.table = table

	def _getTypeNames(self, filterColumn: str) -> 'List[str]':
		return [
			self.table[row, 'name'].val
			for row in range(1, self.table.numRows)
			if self.table[row, filterColumn] == '1'
		]

	def isTypeAvailableForCategory(self, typeName: str, filterColumn: str):
		return self.table[typeName, filterColumn] == '1'

	def coordTypes(self):
		return self._getTypeNames('isCoordType')

	def contextTypes(self):
		return self._getTypeNames('isContextType')

	def returnTypes(self):
		return self._getTypeNames('isReturnType')
