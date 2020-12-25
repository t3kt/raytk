from raytkUtil import RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import StrParamT

	class _Pars(ParCollection):
		Testcasefolder: 'StrParamT'

class ToolkitManager:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.context = RaytkContext()

	# @property
	# def Toolkit(self):
	# 	return self.context.toolkit()
	#
	# @property
	# def ToolkitVersion(self):
	# 	return self.context.toolkitVersion()

	def prepareSceneTable(self, dat: 'DAT'):
		dat.appendCols([
			['opType'],
		])
		pass
