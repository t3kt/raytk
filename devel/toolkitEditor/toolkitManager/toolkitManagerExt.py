from raytkUtil import RaytkContext
from pathlib import Path

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import StrParamT

	class _Pars(ParCollection):
		Testcasefolder: 'StrParamT'
		Prototypefolder: 'StrParamT'

class ToolkitManager:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.context = RaytkContext()

	# @property
	# def Toolkit(self):
	# 	return self.context.toolkit()
	#
	# @property
	# def ToolkitVersion(self):
	# 	return self.context.toolkitVersion()

	def prepareSceneTable(self, dat: 'DAT', inDat: 'DAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow([
			'name', 'label', 'scenePath', 'opType',
		])
		for i in range(1, inDat.numRows):
			baseName = str(inDat[i, 'basename'])
			if baseName == 'index':
				continue
			group = inDat[i, 'group']
			rootFolder = Path(str(inDat[i, 'rootfolder']))
			relPath = str(inDat[i, 'relpath'])
			opType = ''
			if group == 'test':
				opType = str(opTable[baseName.replace('_test', ''), 'opType'] or '')
			dat.appendRow([
				(rootFolder / relPath).as_posix(),
				f'{group}: {relPath.replace(".tox", "")}',
				(rootFolder / relPath).as_posix(),
				opType,
			])
