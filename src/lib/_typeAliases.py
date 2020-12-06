from typing import Union

from _stubs import *

StrParamT = Union[Par, str]
IntParamT = Union[Par, str, int]
DatParamT = Union[Par, str, DAT]
BoolParamT = Union[Par, bool, int]
OPParamT = Union[Par, OP, COMP, DAT, SOP, TOP, CHOP]
