from typing import Optional, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from src.components.inspectorCore.inspectorCoreExt import InspectorCore

	class ipar:
		class inspectorState:
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
		self.UpdateOutputBufferSampleTable(None, None)

	def Inspect(self, o: 'Union[OP, DAT, COMP, str]'):
		self.core.Inspect(o)
		if self.core.par.Hastarget:
			visualizers = self.ownerComp.op('visualizers')
			visualizerType = self.core.par.Visualizertype.eval()
			if self.core.par.Targettype != 'outputOp':
				outputOp = op(visualizers[visualizerType, 'outputOp'])
				self.core.AttachOutputComp(outputOp)
			self.UpdateOutputBufferSampleTable(None, None)
			self.Openwindow()

	def UpdateOutputBufferSampleTable(self, u: Optional[float], v: Optional[float]):
		dat = self.ownerComp.op('set_output_sample')
		dat.clear()
		if u is None or v is None:
			return
		outputs = self.ownerComp.op('output_table')
		for i in range(1, outputs.numRows):
			top = op(outputs[i, 'path'] or '')  # type: TOP
			if not top:
				continue
			value = top.sample(u=u, v=v)
			if not value:
				dat.appendRow([
					outputs[i, 'label'],
					'', '', '', '',
				])
			else:
				dat.appendRow([
					outputs[i, 'label'],
					round(value[0], 2),
					round(value[1], 2),
					round(value[2], 2),
					round(value[3], 2),
				])

def _pathOrEmpty(o: Optional['OP']):
	return o.path if o else ''
