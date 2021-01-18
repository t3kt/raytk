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

	@property
	def _container(self):
		return self.ownerComp.op('componentHost')

	@property
	def hostedComponent(self) -> 'Optional[COMP]':
		for o in self._container.children:
			return o

	def _unloadTest(self):
		comp = self.hostedComponent
		if comp and comp.valid:
			# noinspection PyBroadException
			try:
				comp.destroy()
			except:
				pass

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
		toxPath = Path(self.ownerComp.par.Testcasefolder.eval()) / 'operators' / info.categoryName / (name + '_test.tox')
		print(self.ownerComp, f'name: {name!r} toxPath: {toxPath!r}')
		self._unloadTest()
		container = self._container
		comp = container.create(baseCOMP, name=name)
		comp.save(toxPath.as_posix(), createFolders=True)
