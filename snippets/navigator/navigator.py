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

	def buildSnippetTable(self, dat: 'DAT', snippetTable: 'DAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow(['opType', 'name', 'relPath', 'label'])
		for i in range(1, snippetTable.numRows):
			relPath = snippetTable[i, 'relPath'].val
			name = snippetTable[i, 'name'].val
			opName = name.split('_')[0]
			opType = opTable[opName, 'opType']
			dat.appendRow([
				opType,
				name,
				relPath,
				name.replace('_', ' ')
			])
