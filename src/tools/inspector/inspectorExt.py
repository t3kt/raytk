from typing import Union
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

			# this should not be necessary...
			self.ownerComp.op('target_comp_parameters').cook(force=True)

			self.Openwindow()

	@staticmethod
	def onRightClickPreview(previewPanel: 'PanelCOMP'):
		# noinspection PyUnresolvedReferences
		u, v = previewPanel.panel.u, previewPanel.panel.v
		iop.bufferInspector.Sample(u, v)
