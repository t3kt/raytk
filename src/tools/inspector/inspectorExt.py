from typing import List, Union
from raytkUtil import InspectorTargetTypes

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from src.components.inspectorCore.inspectorCoreExt import InspectorCore

	class ipar:
		class inspectorState:
			Selectedbodytab: 'Union[str, Par]'
			Showpointsampling: 'Union[bool, Par]'
			Samplepointu: 'Union[float, Par]'
			Samplepointv: 'Union[float, Par]'
	from src.components.bufferInspector.bufferInspectorExt import BufferInspector
	iop.bufferInspector = BufferInspector(COMP())

def updateStateMenus():
	p = ipar.inspectorState.Selectedbodytab
	table = op('body_tabs')
	p.menuNames = table.col('name')[1:]
	p.menuLabels = table.col('label')[1:]

class Inspector:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.state = ipar.inspectorState
		self.core = iop.inspectorCore  # type: Union[InspectorCore, COMP]

	def Openwindow(self, _=None):
		self.ownerComp.op('window').par.winopen.pulse()

	def Reset(self, _=None):
		self.core.Reset()
		iop.bufferInspector.Clear()

	def Inspect(self, o: 'Union[OP, DAT, COMP, str]'):
		self.core.Inspect(o)
		if self.core.par.Hastarget:
			visualizers = self.ownerComp.op('visualizers')
			visualizerType = self.core.par.Visualizertype.eval()
			if self.core.par.Targettype != InspectorTargetTypes.outputOp:
				outputOp = op(visualizers[visualizerType, InspectorTargetTypes.outputOp])
				self.core.AttachOutputComp(outputOp)
			iop.bufferInspector.Clear()
			self.Openwindow()

	@staticmethod
	def onRightClickPreview(previewPanel: 'PanelCOMP'):
		# noinspection PyUnresolvedReferences
		u, v = previewPanel.panel.u, previewPanel.panel.v
		iop.bufferInspector.Sample(u, v)

	@staticmethod
	def getSimplifiedNames(fullNames: List[Union[str, 'Cell']]):
		if not fullNames:
			return []
		fullNames = [str(n) for n in fullNames]
		if len(fullNames) != 1 and not any('_' not in n for n in fullNames):
			prefixes = [
				n.rsplit('_', maxsplit=1)[0] + '_'
				for n in fullNames
			]
			commonPrefix = _longestCommonPrefix(prefixes)
			if commonPrefix and not commonPrefix.endswith('_'):
				commonPrefix = commonPrefix.rsplit('_', maxsplit=1)[0] + '_'
			if commonPrefix:
				prefixLen = len(commonPrefix)
				return [
					n[prefixLen:]
					for n in fullNames
				]
		return fullNames

	def buildSimplifiedNames(self, dat: 'DAT', inDat: 'DAT'):
		dat.clear()
		fullNames = inDat.col('name')[1:]
		simplifiedNames = self.getSimplifiedNames(fullNames)
		dat.appendCol(fullNames)
		dat.appendCol(simplifiedNames)


def _longestCommonPrefix(strs):
	if not strs:
		return []
	for i, letter_group in enumerate(zip(*strs)):
		if len(set(letter_group)) > 1:
			return strs[0][:i]
	else:
		return min(strs)
