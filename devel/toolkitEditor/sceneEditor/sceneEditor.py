from pathlib import Path

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class SceneEditor:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def prepareSceneTable(dat: 'DAT', inDat: 'DAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow([
			'name', 'label', 'path', 'opType',
		])
		foundRootFolders = set()
		for i in range(1, inDat.numRows):
			baseName = str(inDat[i, 'basename'])
			if baseName == 'index':
				continue
			group = inDat[i, 'group']
			rootFolder = Path(str(inDat[i, 'rootfolder']))
			if rootFolder not in foundRootFolders:
				dat.appendRow([
					rootFolder.name,
					rootFolder.name,
					rootFolder.absolute().as_posix(),
					'',
				])
				foundRootFolders.add(rootFolder)
			relPath = str(inDat[i, 'path'])
			opType = ''
			if group == 'test':
				opType = str(opTable[baseName.split('_')[0], 'opType'] or '')
			dat.appendRow([
				(rootFolder / relPath).stem.replace('_test', '').replace('_', ' '),
				f'{group}: {relPath.replace(".tox", "")}',
				(rootFolder / relPath).as_posix(),
				opType,
			])
