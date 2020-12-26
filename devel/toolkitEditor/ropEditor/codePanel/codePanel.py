from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from ..ropEditor import ROPEditor
	ext.ropEditor = ROPEditor(COMP())

	class _Pars(ParCollection):
		Selectedblock: 'StrParamT'

	class _COMP(COMP):
		par: _Pars

class CodePanel:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	def currentBlockPar(self) -> 'Optional[Par]':
		info = ext.ropEditor.ROPInfo
		return info and info.isROP and info.opDefPar[self.ownerComp.par.Selectedblock]

	def currentBlockDat(self) -> 'Optional[DAT]':
		par = self.currentBlockPar()
		dat = par and par.eval()
		if not dat:
			return
		while dat.inputs and not dat.par['file']:
			dat = dat.inputs[0]
		return dat

	def currentBlockFile(self) -> 'Optional[str]':
		dat = self.currentBlockDat()
		if dat and dat.par['file']:
			return dat.par.file.eval()

	def createCurrentBlock(self):
		# TODO: create block
		pass

	def deleteCurrentBlock(self):
		name = self.ownerComp.par.Selectedblock.eval()
		info = ext.ropEditor.ROPInfo
		if not info or not info.isROP:
			return
		blocks = self.ownerComp.op('blocks')
		label = str(blocks[name, 'label'])
		confirmation = ui.messageBox(
			f'Delete {label}',
			f'Are you sure you want to delete the {label} of {info.rop.path}?',
			buttons=['Cancel', 'Continue'])
		if confirmation:
			self._doDeleteBlock(info.opDefPar[name])

	def _doDeleteBlock(self, par: 'Par'):
		pass
