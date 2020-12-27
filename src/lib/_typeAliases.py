from typing import Union, Optional

from _stubs import *

class StrParamT(Union[Par, str]):
	def eval(self) -> str: pass

class IntParamT(Union[Par, str, int]):
	def eval(self) -> int: pass

class FloatParamT(Union[Par, str, float, int]):
	def eval(self) -> float: pass

class DatParamT(Union[Par, str, DAT]):
	def eval(self) -> Optional[DAT]: pass

class CompParamT(Union[Par, str, COMP]):
	def eval(self) -> Optional[COMP]: pass

class OPParamT(Union[Par, str, OP, COMP, DAT, SOP, TOP, CHOP, MAT]):
	def eval(self) -> Optional[Union[OP, COMP, DAT, SOP, TOP, CHOP, MAT]]: pass

class BoolParamT(Union[Par, bool, int]):
	def eval(self) -> bool: pass
