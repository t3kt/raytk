from pathlib import Path
from raytkUtil import showPromptDialog, navigateTo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from ..ropEditor.ropEditor import ROPEditor
	from editor.componentLoader.componentLoader import ComponentLoader
	ext.ropEditor = ROPEditor(COMP())
	# noinspection PyTypeHints
	iop.loader = ComponentLoader(COMP())

	class _Par(ParCollection):
		Selectedrop: 'CompParamT'
		Selectedoptype: 'StrParamT'
		Testcasefolder: 'StrParamT'

	class _COMP(COMP):
		par: _Par

class TestEditor:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	@property
	def hostedComponent(self) -> 'Optional[COMP]':
		return iop.loader.Component

	@property
	def currentTestName(self):
		return iop.loader.ComponentName

	@property
	def formattedTestName(self):
		name = self.currentTestName
		if name:
			name = name.replace('_test', '').replace('_', ' ')
		return name

	@property
	def currentTestTox(self):
		return iop.loader.ComponentTox

	def unloadTest(self):
		iop.loader.UnloadComponent()
		self._reloadOutputs()

	def _loadTest(self, name: str, toxPath: Path):
		if name:
			name = name.replace(' ', '_')
			if not name.endswith('_test'):
				name += '_test'
		iop.loader.LoadComponent(tox=toxPath, name=name)
		self._reloadOutputs()

	@staticmethod
	def prepareTestTable(dat: 'DAT', inDat: 'DAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow([
			'name', 'label', 'path', 'opType',
		])
		for i in range(1, inDat.numRows):
			baseName = str(inDat[i, 'basename'])
			if baseName == 'index':
				continue
			if inDat[i, 'type'] == 'File folder':
				continue
			group = inDat[i, 'group']
			rootFolder = Path(str(inDat[i, 'rootfolder']))
			relPath = str(inDat[i, 'relpath'])
			opType = ''
			if group == 'test':
				opType = str(opTable[baseName.split('_')[0], 'opType'] or '')
			dat.appendRow([
				(rootFolder / relPath).stem.replace('_', ' '),
				f'{group}: {relPath.replace(".tox", "")}',
				(rootFolder / relPath).as_posix(),
				opType,
			])

	def createTest(self):
		print(self.ownerComp, 'createTest')
		info = ext.ropEditor.ROPInfo
		if not info:
			print(self.ownerComp, 'there is no rop')
			return
		showPromptDialog(
			title='Create test',
			text='Test name',
			default=info.shortName + '_test',
			textEntry=True,
			ok=lambda name: self._createTest(name),
		)

	def _createTest(self, name: str):
		info = ext.ropEditor.ROPInfo
		if not info:
			return
		name = name.replace(' ', '_')
		if name.endswith('.tox'):
			name = name.replace('.tox', '')
		if not name.endswith('_test'):
			name += '_test'
		toxPath = Path(self.ownerComp.par.Testcasefolder.eval()) / 'operators' / info.categoryName / (name + '_test.tox')
		print(self.ownerComp, f'name: {name!r} toxPath: {toxPath!r}')
		iop.loader.CreateNewComponent(
			tox=toxPath,
			name=name,
			autoSave=True,
		)
		self._reloadOutputs()

	def _reloadOutputs(self):
		def reload():
			self.ownerComp.op('layout_test_outputs').cook(force=True)
		run('args[0]()', reload, delayFrames=5, delayRef=root)

	def listOnSelectRow(self, info: dict):
		# rowData = info['rowData']
		# print(self.ownerComp, 'listOnSelectRow', mod.json.dumps(rowData, indent='  '))
		pass

	def listOnClick(self, info: dict):
		rowData = info.get('rowData')
		rowObj = rowData and rowData.get('rowObject')
		print(self.ownerComp, 'listOnClick', mod.json.dumps(rowData, indent='  '))
		if not rowObj:
			return
		self.unloadTest()
		self._loadTest(rowObj['name'], Path(rowObj['path']))

	@staticmethod
	def showInEditor():
		comp = iop.loader.Component
		if not comp:
			return
		navigateTo(comp, goInto=True)
