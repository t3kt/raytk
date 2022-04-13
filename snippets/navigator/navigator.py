# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Pars:
		Snippetfolder: StrParamT
		Optable: DatParamT

	class _Comp(COMP):
		par: _Pars

class Navigator:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _Comp

	def buildSnippetTable(self, dat: 'DAT', folderDat: 'DAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow(['snippetPath', 'snippetFile', 'opType', 'label'])
		rootFolder = self.ownerComp.par.Snippetfolder.eval() + '/'
		for i in range(1, folderDat.numRows):
			subFilePath = folderDat[i, 'relpath'].val
			
			pass
		pass
