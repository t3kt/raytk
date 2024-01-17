from pathlib import Path
from raytkModel import EditorItemGraph
from raytkUtil import RaytkTags
import subprocess

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from devel.toolkitEditor.ropEditor.ropEditor import ROPEditor
	ext.ropEditor = ROPEditor(COMP())

	class _Pars(ParCollection):
		Selecteditem: StrParamT

	class _COMP(COMP):
		par: _Pars

class DatEditorPanel:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	@property
	def _opDef(self) -> COMP | None:
		if not hasattr(ext, 'ropEditor'):
			return
		info = ext.ropEditor.ROPInfo
		return info and info.opDef

	@property
	def _currentItemPar(self) -> Par | None:
		currentTable = self._currentItemTable
		if currentTable.numRows < 2:
			return
		hostOp = op(currentTable[1, 'hostOp'])
		parName = currentTable[1, 'parName']
		if hostOp and parName:
			return hostOp.par[parName]

	def prepareItemTable(self, dat: scriptDAT):
		dat.copy(dat.inputs[0])
		opDef = self._opDef
		if not opDef:
			return
		for i in range(1, dat.numRows):
			name = dat[i, 'name']
			if dat[i, 'hostOp']:
				hostOp = op(dat[i, 'hostOp'])
			else:
				hostOp = opDef
				dat[i, 'hostOp'] = opDef or ''
			dat[i, 'parName'] = dat[i, 'parName'] or name
			if not hostOp:
				continue
			if hostOp.par[name]:
				dat[i, 'label'] = '* ' + dat[i, 'label'].val + ' *'

	@property
	def currentSourceDat(self) -> DAT | None:
		graph = self._currentItemGraph
		return graph and graph.sourceDat

	@property
	def currentEvalDat(self) -> evaluateDAT | None:
		graph = self._currentItemGraph
		return graph and graph.evalDat

	@property
	def _currentItemGraph(self) -> EditorItemGraph | None:
		par = self._currentItemPar
		if par is None:
			return
		graph = EditorItemGraph.fromPar(par)
		if graph.supported:
			return graph

	@property
	def externalizeEnabled(self):
		graph = self._currentItemGraph
		return graph and bool(graph.sourceDat) and graph.file is not None and not bool(graph.file.eval())

	@property
	def fileParameterVisible(self):
		if not self.ownerComp.par.Showfile:
			return False
		graph = self._currentItemGraph
		return graph and graph.file is not None

	@property
	def _itemTable(self) -> DAT:
		return self.ownerComp.op('itemTable')

	@property
	def _currentItemTable(self) -> DAT:
		return self.ownerComp.op('currentItem')

	def buildItemGraphInfo(self, dat: DAT):
		dat.clear()
		dat.appendCol([
			'endDat',
			'sourceDat',
			'hasEval',
			'evalDat',
			'supported',
			'file',
		])
		dat.appendCol([''])
		graph = self._currentItemGraph
		if not graph:
			return
		dat['endDat', 1] = graph.endDat or ''
		dat['sourceDat', 1] = graph.sourceDat or ''
		dat['evalDat', 1] = graph.evalDat or ''
		dat['hasEval', 1] = int(graph.hasEval)
		dat['supported', 1] = 1
		dat['file', 1] = graph.file or ''

	def onCreateClick(self):
		print(self.ownerComp, 'onCreateClick')
		info = ext.ropEditor.ROPInfo
		if not info:
			self._printAndStatus('Unable to create DAT, no current ROP')
			return
		itemGraph = self._currentItemGraph
		if itemGraph and itemGraph.sourceDat:
			self._printAndStatus('DAT already exists!')
			return
		itemName = self.ownerComp.par.Selecteditem.eval()
		datType = self._itemTable[itemName, 'type'] or 'text'
		srcName = self._itemTable[itemName, 'datName']
		evalName = self._itemTable[itemName, 'evalDatName']
		ui.undo.startBlock(f'Creating {datType} {srcName}')
		try:
			if datType == 'table':
				srcDat = info.rop.create(tableDAT, srcName)
			elif datType == 'text':
				srcDat = info.rop.create(textDAT, srcName)
			else:
				self._printAndStatus(f'Unsupported DAT type: {datType}')
				return
			template = op(self._itemTable[itemName, 'template'])
			if template:
				srcDat.copy(template)
			srcDat.nodeY = -300 - (self._itemTable[itemName, 0].row * 300)
			srcDat.nodeX = -475
			evalDat = None
			if evalName:
				evalDat = info.rop.create(evaluateDAT, evalName)
				if datType == 'table' and srcDat.numRows > 0 and srcDat.numCols > 0 and not any(c.val.startswith('\'') for c in srcDat.row(0)):
					evalDat.par.xfirstrow = True
				evalDat.nodeY = srcDat.nodeY
				evalDat.nodeX = srcDat.nodeX + 200
				evalDat.inputConnectors[0].connect(srcDat)
			self._currentItemPar.val = evalDat or srcDat
			self._externalize(self._currentItemGraph, srcDat)
		finally:
			ui.undo.endBlock()

	def onDeleteClick(self):
		info = ext.ropEditor.ROPInfo
		itemGraph = self._currentItemGraph
		if not info or not itemGraph or not self._confirmDelete(itemGraph):
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

	def onExternalizeClick(self):
		info = ext.ropEditor.ROPInfo
		itemGraph = self._currentItemGraph
		if not info or not itemGraph or not itemGraph.sourceDat or itemGraph.file is None or itemGraph.file.eval():
			return
		dat = itemGraph.sourceDat
		ui.undo.startBlock(f'Externalizing {dat}')
		try:
			self._externalize(itemGraph, dat)
		finally:
			ui.undo.endBlock()

	def _externalize(self, itemGraph: EditorItemGraph, dat: DAT):
		info = ext.ropEditor.ROPInfo
		if not info or not itemGraph or not itemGraph.sourceDat:
			return
		if itemGraph.file is None:
			self._printAndStatus(f'Unable to externalize, no file parameter on {itemGraph.sourceDat}!')
			return
		if itemGraph.file.eval():
			self._printAndStatus(f'No need to externalize, already have external file: {itemGraph.file}')
			return
		tox = info.toxFile
		if not tox:
			self._printAndStatus(f'Unable to externalize, no tox file for {itemGraph.par.name}')
			return
		suffix = str(self._itemTable[itemGraph.par.name, 'fileSuffix'] or '')
		if not suffix:
			self._printAndStatus(f'Unable to externalize, no file suffix found for {itemGraph.par.name}')
			return
		file = Path(tox.replace('.tox', suffix))
		itemGraph.sourceDat.par.defaultreadencoding = 'utf8'
		itemGraph.sourceDat.save(file.as_posix())
		itemGraph.file.val = file.as_posix()
		RaytkTags.fileSync.apply(dat, True)
		self._printAndStatus(f'Externalized {itemGraph.sourceDat} to file {file.as_posix()}')

	def onExternalEditClick(self):
		graph = self._currentItemGraph
		if graph and graph.sourceDat and graph.sourceDat.par['edit'] is not None:
			# TODO: make this path configurable or at least more portable
			binPath = Path(r'C:\Users\tekt\AppData\Local\JetBrains\Toolbox\apps\PyCharm-P\ch-0\202.7660.27\bin\pycharm64.exe')
			if binPath.exists():
				subprocess.Popen([str(binPath), graph.file.val])
				return
			graph.sourceDat.par.edit.pulse()

	@staticmethod
	def _confirmDelete(itemGraph: EditorItemGraph):
		info = ext.ropEditor.ROPInfo
		return ui.messageBox(
			f'Delete {itemGraph.par.label}?',
			f'Are you sure you want to delete the {itemGraph.par.label} of {info.rop.path}?',
			buttons=['Cancel', 'Delete'],
		)

	def _printAndStatus(self, msg):
		print(self.ownerComp, msg)
		ui.status = msg
