# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _StatePar(ParCollection):
		XYZ: 'BoolParamT'
	ipar.elementsPanelState = _StatePar()

class ElementsPanel:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def buildItemTable(dat: 'DAT', elementTable: 'DAT'):
		dat.clear()
		dat.appendRow(['name', 'label', 'hostOp', 'parName', 'datName', 'evalDatName', 'fileSuffix'])
		for row in range(1, elementTable.numRows):
			elementRoot = op(elementTable[row, 'elementRoot'])
			if not elementRoot:
				continue
			for par in elementRoot.customPars:
				if par.style != 'DAT':
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
