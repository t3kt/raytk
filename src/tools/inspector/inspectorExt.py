from typing import Optional, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

	class ipar:
		class inspectorState:
			Hastarget: bool
			Hasownviewer: bool
			Targettype: 'Union[str, Par]'
			Rawtarget: 'Union[str, OP, DAT, COMP]'
			Definitiontable: 'Union[str, DAT]'
			Targetcomp: 'Union[str, COMP]'
			Visualizertype: 'Union[str, Par]'
			Returntype: str
			Coordtype: str
			Contexttype: str
			Selectedview: 'Union[str, Par]'
			Selectedbodytab: 'Union[str, Par]'

class TargetTypes:
	none = 'none'
	rop = 'rop'
	outputOp = 'outputOp'
	definitionTable = 'definitionTable'

	values = [
		none,
		rop,
		outputOp,
		definitionTable,
	]

class VisualizerTypes:
	none = 'none'
	field = 'field'
	render2d = 'render2d'
	render3d = 'render3d'

	values = [
		none,
		field,
		render2d,
		render3d,
	]

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
	p = ipar.inspectorState.Targettype  # type: Par
	p.menuNames = p.menuLabels = TargetTypes.values
	p = ipar.inspectorState.Visualizertype
	p.menuNames = p.menuLabels = VisualizerTypes.values
	p = ipar.inspectorState.Selectedbodytab
	table = op('body_tabs')
	p.menuNames = table.col('name')[1:]
	p.menuLabels = table.col('label')[1:]

class Inspector:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.state = ipar.inspectorState

	def Reset(self, _=None):
		self.state.Hastarget = False
		self.state.Targettype = TargetTypes.none
		self.state.Rawtarget = ''
		self.state.Targetcomp = ''
		self.state.Definitiontable = ''
		self.state.Visualizertype = VisualizerTypes.none

	def Inspect(self, o: 'Union[OP, DAT, COMP, str]'):
		o = o and op(o)
		if not o:
			self.Reset()
			return
		if o.isCOMP and o.name == 'opDefinition' and o.par['Hostop']:
			o = o.par.Hostop.eval()
		if o.isDAT and o.isTable and o.numRows > 1:
			self.inspectDefinitionTable(o)
		elif o.isCOMP and 'raytkOP' in o.tags:
			self.inspectComp(o)
		else:
			# TODO: better error handling
			raise Exception(f'Unsupported OP: {o!r}')

	def inspectDefinitionTable(self, dat: 'DAT'):
		if 'raytkOP' in dat.parent().tags and dat.name == 'definition' and dat[1, 'path'] == dat.parent().path:
			self.inspectComp(dat.parent())
			return
		self.state.Rawtarget = dat
		self.state.Targettype = TargetTypes.definitionTable
		self.state.Definitiontable = _pathOrEmpty(dat)
		self.state.Targetcomp = _pathOrEmpty(op(dat[1, 'path']))
		self.state.Hastarget = True
		self.state.Hasownviewer = False
		self.updateVisualizerType()

	def inspectComp(self, comp: 'COMP'):
		self.state.Rawtarget = _pathOrEmpty(comp)
		self.state.Targetcomp = _pathOrEmpty(comp)
		isOutput = 'raytkOutput' in comp.tags
		if isOutput:
			self.state.Targettype = TargetTypes.outputOp
		else:
			self.state.Targettype = TargetTypes.rop
		self.state.Definitiontable = _pathOrEmpty(comp.op('definition'))
		self.state.Hastarget = True
		self.state.Hasownviewer = isOutput
		self.updateVisualizerType()

	# noinspection PyTypeChecker
	def updateVisualizerType(self):
		self.state.Visualizertype = VisualizerTypes.none
		if self.state.Hastarget:
			if self.state.Returntype == ReturnTypes.Sdf:
				if self.state.Coordtype == CoordTypes.vec2:
					self.state.Visualizertype = VisualizerTypes.render2d
				elif self.state.Coordtype == CoordTypes.vec3:
					self.state.Visualizertype = VisualizerTypes.render3d
			elif self.state.Returntype in [ReturnTypes.float, ReturnTypes.vec4]:
				self.state.Visualizertype = VisualizerTypes.field
		views = self.ownerComp.op('available_views')
		p = self.state.Selectedview
		p.menuNames = ['none'] + views.row(1)
		p.menuLabels = ['None'] + views.row(0)
		if len(p.menuNames) > 1:
			p.val = p.menuNames[1]
		else:
			p.val = 'none'

def _pathOrEmpty(o: Optional['OP']):
	return o.path if o else ''
