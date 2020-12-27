from typing import Union

from _stubs import *

StrParamT = Union[Par, str]
IntParamT = Union[Par, str, int]
FloatParamT = Union[Par, str, float, int]
DatParamT = Union[Par, str, DAT]
CompParamT = Union[Par, str, COMP]
BoolParamT = Union[Par, bool, int]
OPParamT = Union[Par, OP, COMP, DAT, SOP, TOP, CHOP, str]
