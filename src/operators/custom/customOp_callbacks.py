# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from components.customOpController.customOpController import CustomOp

def onCreate(master=None, **kwargs):
	# noinspection PyTypeChecker
	controller = op('customOpController')  # type: CustomOp
	controller.Createfunction()
	controller.Createparamsop()
