from raytkUtil import navigateTo
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from components.opPicker.opPicker import PickerItem

	class _Pars:
		Snippetsroot: CompParamT
		Optable: DatParamT

	class _Comp(COMP):
		par: _Pars

	class _StatePars:
		Selectedoptype: StrParamT
		Selectedsnippet: StrParamT

	ipar.navigatorState = _StatePars()

class Navigator:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _Comp
		self.currentSnippetTable = ownerComp.op('currentSnippets')  # type: DAT
		self.fullSnippetTable = ownerComp.op('snippetTable')  # type: DAT

	@staticmethod
	def buildSnippetTable(dat: 'DAT', snippetTable: 'DAT', opTable: 'DAT'):
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

	def onOpPickerPickItem(self, item: 'PickerItem'):
		if item.isCategory:
			return
		ipar.navigatorState.Selectedoptype = item.opType
		self.ownerComp.op('snippetList').par.Refresh.pulse()
		ipar.navigatorState.Selectedsnippet = self.currentSnippetTable[1, 'name'] or ''

	def onSnippetListSelect(self, snippetName: str):
		relPath = self.currentSnippetTable[snippetName, 'relPath']
		if not relPath:
			return
		snippet = self.ownerComp.par.Snippetsroot.eval().op(relPath)
		self._updateSnippetCooking(snippet)
		navigateTo(snippet, name='raytkSnippet', popup=True, goInto=True)

	def _updateSnippetCooking(self, targetSnippet: 'Optional[COMP]'):
		snippetsRoot = self.ownerComp.par.Snippetsroot.eval()
		allSnippets = snippetsRoot.ops(*self.fullSnippetTable.col('relPath')[1:])
		for o in allSnippets:
			if o is not targetSnippet and o.allowCooking:
				o.allowCooking = False
		if targetSnippet and not targetSnippet.allowCooking:
			targetSnippet.allowCooking = True
