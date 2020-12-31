from pathlib import Path
from typing import Optional
from raytkUtil import RaytkTags

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from ..ropEditor import ROPEditor
	ext.ropEditor = ROPEditor(COMP())
	from components.datEditorPanel.datEditorPanel import EditorItemGraph

	class _Pars(ParCollection):
		Selectedblock: 'StrParamT'

	class _COMP(COMP):
		par: _Pars

class CodePanel:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	@property
	def opDef(self) -> 'Optional[COMP]':
		info = ext.ropEditor.ROPInfo
		return info and info.opDef

	@property
	def _blockTable(self) -> 'DAT':
		return self.ownerComp.op('blocks')

	def onCreateItem(self, itemGraph: 'EditorItemGraph'):
		pass

	def onDeleteItem(self, itemGraph: 'EditorItemGraph'):
		info = ext.ropEditor.ROPInfo
		if not info or not self._confirmDelete(itemGraph):
			return
		ui.undo.startBlock(f'Delete {itemGraph.par.label} from {info.rop.path}')
		try:
			if itemGraph.file:
				file = Path(itemGraph.file.eval())
				file.unlink(missing_ok=True)
				itemGraph.file.val = ''
			itemGraph.par.val = ''
			if itemGraph.endDat and itemGraph.endDat.valid:
				itemGraph.endDat.destroy()
			if itemGraph.sourceDat and itemGraph.sourceDat.valid:
				itemGraph.sourceDat.destroy()
		finally:
			ui.undo.endBlock()

	def onExternalizeItem(self, itemGraph: 'EditorItemGraph'):
		info = ext.ropEditor.ROPInfo
		if not info or not itemGraph.sourceDat or itemGraph.file is None or itemGraph.file.eval():
			return
		if itemGraph.file is None:
			ui.status = f'Unable to externalize, no file parameter on {itemGraph.sourceDat}!'
			return
		if itemGraph.file.eval():
			ui.status = f'No need to externalize, already have external file: {itemGraph.file}'
			return
		tox = info.toxFile
		if not tox:
			ui.status = f'Unable to externalize, no tox file for {itemGraph.par.name}'
			return
		suffix = str(self._blockTable[itemGraph.par.name, 'fileSuffix'] or '')
		if not suffix:
			ui.status = f'Unable to externalize, no file suffix found for {itemGraph.par.name}'
			return
		file = Path(tox.replace('.tox', suffix))
		file.touch(exist_ok=True)
		itemGraph.file.val = file.as_posix()
		ui.status = f'Externalized {itemGraph.sourceDat} to file {file.as_posix()}'

	@staticmethod
	def _confirmDelete(itemGraph: 'EditorItemGraph'):
		info = ext.ropEditor.ROPInfo
		return ui.messageBox(
			f'Delete {itemGraph.par.label}?',
			f'Are you sure you want to delete the {itemGraph.par.label} of {info.rop.path}?',
			buttons=['Cancel', 'Delete'],
		)
