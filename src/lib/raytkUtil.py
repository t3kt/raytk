from dataclasses import dataclass
from typing import Union, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	op.raytk = COMP()

def getToolkit() -> 'COMP':
	return op.raytk

class _OpDefPars:
	Raytkoptype: 'Union[Par, str]'
	Raytkopversion: 'Union[Par, str, int]'
	Raytkversion: 'Union[Par, str]'
	Help: 'Union[Par, DAT, str]'

class ROPInfo:
	rop: 'Optional[OP]'
	opDef: 'Optional[OP]'
	opDefPar: 'Optional[_OpDefPars]'

	def __init__(self, o: 'Union[OP, str, Cell]'):
		o = op(o)
		if not o:
			return
		if isROP(o):
			self.rop = o
			self.opDef = o.op('opDefinition')
		elif isROPDef(o):
			self.rop = o.par.Hostop.eval()
			self.opDef = o
		else:
			return
		# noinspection PyTypeChecker
		self.opDefPar = self.opDef.par

	def __bool__(self):
		return bool(self.rop)

	@property
	def opVersion(self):
		return str(self.opDefPar.Raytkopversion or '')

	@opVersion.setter
	def opVersion(self, val):
		self.opDefPar.Raytkopversion = val if val is not None else ''

	@property
	def opType(self):
		return str(self.opDefPar.Raytkoptype or '')

	@property
	def isBeta(self):
		return RaytkTag.raytkBeta in self.opDef.tags

	@property
	def isMaster(self):
		if not self.rop:
			return False
		toolkit = getattr(self.rop.parent, 'raytk', None)
		if not toolkit:
			return False
		if toolkit.op('operators') and toolkit.op('operators').path in self.rop.parent().path:
			return True
		return False

	@property
	def helpDAT(self) -> 'Optional[DAT]':
		dat = op(self.opDefPar.Help)
		if dat:
			return dat
		dat = self.rop.op('help')
		if dat and dat.isDAT:
			return dat

	@helpDAT.setter
	def helpDAT(self, dat: 'Optional[DAT]'):
		self.opDefPar.Help = dat or ''

def isROP(o: 'OP'):
	return bool(o) and o.isCOMP and RaytkTag.raytkOP in o.tags

def isOutputROP(o: 'OP'):
	return isROP(o) and RaytkTag.raytkOutput in o.tags

def isROPDef(o: 'OP'):
	return bool(o) and o.isCOMP and o.name == 'opDefinition'

def getROPDef(o: 'OP') -> 'Optional[OP]':
	if isROPDef(o):
		return o
	if isROP(o):
		return o.op('opDefinition')

def getROPVersion(o: 'OP'):
	opDef = getROPDef(o)
	return opDef and str(opDef.par['Raytkopversion'] or '')

class RaytkTag:
	raytkOP = 'raytkOP'
	raytkOutput = 'raytkOutput'
	buildExclude = 'buildExclude'
	fileSync = 'fileSync'
	raytkBeta = 'raytkBeta'

def getActiveEditor() -> 'NetworkEditor':
	pane = ui.panes.current
	if pane.type == PaneType.NETWORKEDITOR:
		return pane
	for pane in ui.panes:
		if pane.type == PaneType.NETWORKEDITOR:
			return pane

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
	Ray = 'Ray'

	values = [
		Sdf,
		vec4,
		float,
		Ray,
	]

class CoordTypes:
	vec2 = 'vec2'
	vec3 = 'vec3'

	values = [
		vec2,
		vec3,
	]

class ContextTypes:
	Context = 'Context'
	MaterialContext = 'MaterialContext'
	CameraContext = 'CameraContext'
	none = 'none'

	values = [
		Context,
		none,
		MaterialContext,
		CameraContext,
	]

class InspectorTargetTypes:
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
