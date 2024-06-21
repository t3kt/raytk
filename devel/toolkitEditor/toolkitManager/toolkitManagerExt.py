from pathlib import Path
from raytkUtil import ModuleInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import StrParamT

	class _Pars(ParCollection):
		Testcasefolder: 'StrParamT'
		Prototypefolder: 'StrParamT'

class ToolkitManager:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	@staticmethod
	def prepareSceneTable(dat: DAT, inDat: DAT, opTable: DAT):
		dat.clear()
		dat.appendRow([
			'name', 'label', 'filePath', 'opType', 'group', 'baseName', 'shortLabel'
		])
		for i in range(1, inDat.numRows):
			baseName = str(inDat[i, 'basename'])
			if baseName == 'index':
				continue
			group = inDat[i, 'group']
			rootFolder = Path(str(inDat[i, 'rootfolder']))
			relPath = str(inDat[i, 'relpath'])
			opType = ''
			if group in ('test', 'snippet'):
				opType = str(opTable[baseName.split('_')[0], 'opType'] or '')
			dat.appendRow([
				(rootFolder / relPath).as_posix(),
				f'{group}: {relPath.replace(".tox", "")}',
				(rootFolder / relPath).as_posix(),
				opType,
				group,
				baseName,
				baseName.replace('_', ' '),
			])

	@staticmethod
	def prepareModuleTable(dat: DAT, inDat: DAT):
		dat.clear()
		dat.appendRow(['name', 'moduleRoot', 'moduleDefinition', 'opTable', 'testsFolder'])
		for cell in inDat.col('path')[1:]:
			modDef = op(cell)
			if not modDef:
				continue
			modRoot = modDef.par.Moduleroot.eval()
			modInfo = ModuleInfo(modRoot)
			if not modInfo:
				continue
			dat.appendRow([
				modInfo.moduleName,
				modRoot,
				modDef,
				modDef.par.Optable.eval() or '',
				modDef.par.Testsfolder,
			])
