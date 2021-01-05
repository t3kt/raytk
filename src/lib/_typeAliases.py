from typing import Union, Optional

from _stubs import *

class StrParamT(Par, Union[Par, str]):
	def eval(self) -> str: pass

class IntParamT(Par, Union[Par, str, int]):
	def eval(self) -> int: pass

class FloatParamT(Par, Union[Par, str, float, int]):
	def eval(self) -> float: pass

class DatParamT(Par, Union[Par, str, DAT]):
	def eval(self) -> Optional[DAT]: pass

class CompParamT(Par, Union[Par, str, COMP]):
	def eval(self) -> Optional[COMP]: pass

class OPParamT(Par, Union[Par, str, OP, COMP, DAT, SOP, TOP, CHOP, MAT]):
	def eval(self) -> Optional[Union[OP, COMP, DAT, SOP, TOP, CHOP, MAT]]: pass

class BoolParamT(Par, Union[Par, bool, int]):
	def eval(self) -> bool: pass
