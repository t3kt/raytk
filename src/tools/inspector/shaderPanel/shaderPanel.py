# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from components.inspectorCore.inspectorCoreExt import InspectorCore
	ext.inspectorCore = InspectorCore(COMP())

class ShaderPanel:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
