from raytkState import RopState

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from _typeAliases import *

	class _InspectorCorePars(ParCollection):
		Hastarget: 'BoolParamT'
		Definitiontable: 'DatParamT'
		Targetcomp: 'CompParamT'
	ipar.inspectorCore = _InspectorCorePars()

	class _StatePar(ParCollection):
		XYZ: 'BoolParamT'
	ipar.elementsPanelState = _StatePar()

class ElementsPanel:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	@staticmethod
	def buildItemTable(dat: DAT):
		dat.clear()
		dat.appendRow(['name', 'label', 'hostOp', 'parName', 'datName', 'evalDatName', 'fileSuffix'])
		rop = ipar.inspectorCore.Targetcomp.eval()
		if not rop:
			return
		stateDat = rop.op('opDefinition/opState')
		if not stateDat:
			return
		state = RopState.fromJson(stateDat.text)
		if not state or not state.opElements:
			return
		for element in state.opElements:
			elementRoot = op(element.elementRoot)
			if not elementRoot:
				continue
			for par in elementRoot.customPars:
				if par.style != DAT:
					continue
				table = par.eval()
				if not table:
					continue
				itemName = elementRoot.name + ':' + par.name
				dat.appendRow([
					itemName,
					elementRoot.name.replace('_', ':'),
					elementRoot,
					par.name,
					table.name,
					'', '',
				])
