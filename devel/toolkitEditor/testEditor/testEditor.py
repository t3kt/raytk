from pathlib import Path
from raytkUtil import showPromptDialog

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from ..ropEditor.ropEditor import ROPEditor
	ext.ropEditor = ROPEditor(COMP())

	class _Par(ParCollection):
		Selectedrop: 'CompParamT'
		Selectedoptype: 'StrParamT'
		Testcasefolder: 'StrParamT'

	class _COMP(COMP):
		par: _Par

class TestEditor:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp
		self._currentTestName = tdu.Dependency()
		self._currentTestTox = tdu.Dependency()

	@property
	def _container(self):
		return self.ownerComp.op('componentHost')

	@property
	def hostedComponent(self) -> 'Optional[COMP]':
		for o in self._container.children:
			return o

	@property
	def currentTestName(self):
		return self._currentTestName.val

	@property
	def currentTestTox(self):
		return self._currentTestTox.val

	def _unloadTest(self):
		self._currentTestName.val = ''
		self._currentTestTox.val = ''
		comp = self.hostedComponent
		if comp and comp.valid:
			# noinspection PyBroadException
			try:
				comp.destroy()
			except:
				pass

	def UnloadTest(self):
		self._unloadTest()

	def _loadTest(self, name: str, toxPath: Path):
		container = self._container
		comp = container.create(baseCOMP, 'component')
		self._currentTestName.val = name
		self._currentTestTox.val = toxPath.as_posix()
		if toxPath.exists():
			comp.par.externaltox = toxPath.as_posix()
			comp.par.reinitnet.pulse()
		else:
			comp.par.externaltox = toxPath.as_posix()
			comp.save(toxPath.as_posix(), createFolders=True)

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
		if name.endswith('_test'):
			name = name.replace('_test', '')
		toxPath = Path(self.ownerComp.par.Testcasefolder.eval()) / 'operators' / info.categoryName / (name + '_test.tox')
		print(self.ownerComp, f'name: {name!r} toxPath: {toxPath!r}')
		self._unloadTest()
		self._loadTest(name, toxPath)

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
		self._unloadTest()
		self._loadTest(rowObj['name'], Path(rowObj['path']))
