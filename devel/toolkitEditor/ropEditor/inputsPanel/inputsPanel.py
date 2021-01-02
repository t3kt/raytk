from raytkUtil import ROPInfo, inputHandlerNameAndLabel

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
		multiHandler = info.multiInputHandler
		for handler in info.inputHandlers:
			name, label = inputHandlerNameAndLabel(handler)
			multi = False
			if multiHandler:
				output = handler.outputs[0]
				if output.isDAT:
					output = output.outputs[0]
				if output.isCOMP and output.name == 'multiInputHandler':
					multi = True
			dat.appendRow([
				name,
				label,
				handler.path,
				multiHandler.path if multi else '',
			])
