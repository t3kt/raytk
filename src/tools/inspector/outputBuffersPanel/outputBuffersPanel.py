from raytkUtil import ROPInfo
from typing import List

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class OutputBuffersPanel:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	@staticmethod
	def buildAllBuffersTable(dat: DAT, tableList: DAT):
		dat.clear()
		dat.appendRow(['name', 'label', 'opType', 'localName', 'localLabel', 'enablePar', 'shortOpType'])
		for tablePath in tableList.col('path')[1:]:
			table = op(tablePath)  # type: DAT
			info = ROPInfo(table.parent())
			for row in range(1, table.numRows):
				name = table[row, 'name']
				label = table[row, 'label']
				dat.appendRow([
					f'{info.shortName}_{name}',
					f'{label} ({info.shortName})',
					info.opType,
					name,
					label,
					table[row, 'enable'] or '',
					info.shortName,
				])

	@staticmethod
	def buildOutputOpTypeTable(dat: DAT, tableList: DAT):
		dat.clear()
		dat.appendRow(['name', 'label'])
		for tablePath in tableList.col('path')[1:]:
			info = ROPInfo(op(tablePath).parent())
			opType = info.opType
			dat.appendRow([
				opType,
				opType.rsplit('.', 1)[1],
			])

	@staticmethod
	def onItemReplicate(replicator: COMP, allOps: 'List[panelCOMP]', table: DAT, master: 'panelCOMP'):
		prefix = replicator.par.opprefix.eval()
		for item in allOps:
			name = item.name.replace(prefix, '')
			item.par.clone = master
			item.par.externaltox = ''
			item.par.Name = name
			item.par.Localname = table[name, 'localName']
			item.par.Label = table[name, 'localLabel']
			item.par.Optype = table[name, 'opType']
			parName = str(table[name, 'enablePar'])
			if parName:
				item.par.Hasenable.expr = f'me.par.Targetop and me.par.Targetop.eval().par[{parName!r}] is not None'
				item.par.Enable.bindExpr = f"me.par.Targetop.eval().par[{parName!r}] if me.par.Hasenable else op('./nothing').par.Enable"
			else:
				item.par.Enable = True
			item.par.display = True

	def onSelectItem(self, item: COMP):
		par = self.ownerComp.par.Selectedbuffer
		par.val = item.par.Name.eval()
