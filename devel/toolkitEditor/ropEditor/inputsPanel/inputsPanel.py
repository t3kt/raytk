from raytkUtil import ROPInfo, InputInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _InspectorCorePars(ParCollection):
		Hastarget: 'BoolParamT'
		Definitiontable: 'DatParamT'
		Targetcomp: 'CompParamT'
	ipar.inspectorCore = _InspectorCorePars()

class InputsPanel:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def buildInputTable(dat: 'DAT'):
		dat.clear()
		dat.appendRow(['name', 'label', 'handler', 'multi'])
		info = ROPInfo(ipar.inspectorCore.Targetcomp)
		if not info:
			return
		for handler in info.inputHandlers:
			inInfo = InputInfo(handler)
			dat.appendRow([
				inInfo.name,
				inInfo.label or '',
				handler.path,
				inInfo.multiHandler or '',
			])
