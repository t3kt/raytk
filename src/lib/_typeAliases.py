import typing as T

from _stubs import *

class StrParamT(Par, T.Union[Par, str]):
	def eval(self) -> str: pass

class IntParamT(Par, T.Union[Par, str, int]):
	def eval(self) -> int: pass

class FloatParamT(Par, T.Union[Par, str, float, int]):
	def eval(self) -> float: pass

class DatParamT(Par, T.Union[Par, str, DAT]):
	def eval(self) -> T.Optional[DAT]: pass

class CompParamT(Par, T.Union[Par, str, COMP]):
	def eval(self) -> T.Optional[COMP]: pass

class OPParamT(Par, T.Union[Par, str, OP, COMP, DAT, SOP, TOP, CHOP, MAT]):
	def eval(self) -> T.Optional[T.Union[OP, COMP, DAT, SOP, TOP, CHOP, MAT]]: pass

class BoolParamT(Par, T.Union[Par, bool, int]):
	def eval(self) -> bool: pass

ValT = T.TypeVar('ValT')
class PythonParamT(T.Generic[ValT], Par, T.Union[Par, None, ValT]):
	def eval(self) -> T.Optional[ValT]:
