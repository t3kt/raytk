from typing import Optional, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from src.components.inspectorCore.inspectorCoreExt import InspectorCore

	class ipar:
		class inspectorState:
			Selectedview: 'Union[str, Par]'
			Selectedbodytab: 'Union[str, Par]'

class ReturnTypes:
	Sdf = 'Sdf'
	vec4 = 'vec4'
	float = 'float'

	values = [
		Sdf,
		vec4,
		float,
	]

class CoordTypes:
	vec2 = 'vec2'
	vec3 = 'vec3'

	values = [
		vec2,
		vec3,
	]

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

	def Inspect(self, o: 'Union[OP, DAT, COMP, str]'):
		self.core.Inspect(o)
		if self.core.par.Hastarget:
			visualizers = self.ownerComp.op('visualizers')
			visualizerType = self.core.par.Visualizertype.eval()
			if self.core.par.Targettype != 'outputOp':
				outputOp = op(visualizers[visualizerType, 'outputOp'])
				self.core.AttachOutputComp(outputOp)
		self.updateViewMenu()
		if self.core.par.Hastarget:
			self.Openwindow()

	def updateViewMenu(self):
		viewPar = self.state.Selectedview
		if not self.core.par.Hastarget:
			viewPar.menuNames = ['none']
			viewPar.menuLabels = ['None']
		else:
			outputTable = self.ownerComp.op('output_table')
			viewPar.menuNames = ['none'] + outputTable.col('name')[1:]
			viewPar.menuLabels = ['None'] + outputTable.col('label')[1:]

def _pathOrEmpty(o: Optional['OP']):
	return o.path if o else ''
