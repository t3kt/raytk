from dataclasses import dataclass, field
from typing import Callable, List, Union, Optional, Tuple

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
	opDef: 'Optional[COMP]'
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
		return RaytkTags.beta.isOn(self.opDef)

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

	@property
	def hasROPInputs(self):
		for conn in self.opDef.inputConnectors:
			if conn.connections and conn.inOP.isDAT:
				return True
		return False

	@property
	def isOutput(self):
		return RaytkTags.raytkOutput.isOn(self.rop)

def isROP(o: 'OP'):
	return bool(o) and o.isCOMP and RaytkTags.raytkOP.isOn(o)

def isROPDef(o: 'OP'):
	return bool(o) and o.isCOMP and o.name == 'opDefinition'

def getROP(comp: 'COMP', checkParents=True):
	if not comp or comp is root:
		return None
	if isROP(comp):
		return comp
	if isROPDef(comp):
		host = comp.par.Hostop.eval()
		if isROP(host):
			return host
	if checkParents:
		return getROP(comp.parent(), checkParents=checkParents)

def getROPDef(o: 'OP') -> 'Optional[OP]':
	if isROPDef(o):
		return o
	if isROP(o):
		return o.op('opDefinition')

def getROPVersion(o: 'OP'):
	opDef = getROPDef(o)
	return opDef and str(opDef.par['Raytkopversion'] or '')

@dataclass
class ROPSignature:
	returnTypes: List[str] = field(default_factory=list)
	coordTypes: List[str] = field(default_factory=list)
	contextTypes: List[str] = field(default_factory=list)

def recloneComp(o: 'COMP'):
	if o and o.par['enablecloningpulse'] is not None:
		o.par.enablecloningpulse.pulse()

_defaultNodeColor = 0.545, 0.545, 0.545
_buildExcludeColor = 0.1, 0.1, 0.1
_fileSyncColor = 0.65, 0.5, 1
_betaColor = 1, 0, 0.5
_buildLockColor = 0, 0.68, 0.543

class Tag:
	def __init__(
			self,
			name: str,
			color: Tuple[float, float, float] = None,
			update: Callable[['OP', bool], None] = None):
		self.name = name
		self.color = color
		self.update = update

	def apply(self, o: 'OP', state: bool):
		"""
		Add/remove the tag on an OP, and update the color (if applicable), and apply the update function (if applicable)
		"""
		self.applyTag(o, state)
		self.applyColor(o, state)
		self.applyUpdate(o, state)

	def applyUpdate(self, o: 'OP', state: bool):
		"""
		Apply the tag's update function to an OP, performing tag-specific changes.
		"""
		if o and self.update:
			self.update(o, state)

	def applyTag(self, o: 'OP', state: bool):
		"""
		Add/remove the tag on an OP
		"""
		if not o:
			return
		if state:
			o.tags.add(self.name)
		elif self.name in o.tags:
			o.tags.remove(self.name)

	def applyColor(self, o: 'OP', state: bool):
		"""
		If applicable, set the color of an OP to either the tag's color or the default color.
		"""
		if self.color:
			o.color = self.color if state else _defaultNodeColor

	def __str__(self):
		return self.name

	def isOn(self, o: 'OP'):
		return bool(o) and self.name in o.tags

def _updateFileSyncPars(o: 'OP', state: bool):
	if o.isDAT:
		par = o.par['syncfile']
		if par is not None:
			par.expr = ''
			par.val = state
			if not state:
				for par in o.pars('loadonstart', 'loadonstartpulse', 'write', 'writepulse'):
					par.expr = ''
					par.val = False
		else:
			for par in o.pars('loadonstart', 'loadonstartpulse', 'write', 'writepulse'):
				par.expr = ''
				par.val = state
	else:
		# TODO: support for other types of OPs
		raise Exception(f'updateFileSyncPars does not yet support op: {o}')

class RaytkTags:
	raytkOP = Tag('raytkOP')
	raytkOutput = Tag('raytkOutput')
	buildExclude = Tag('buildExclude', _buildExcludeColor)
	buildLock = Tag('buildLock', _buildLockColor)
	fileSync = Tag('fileSync', _fileSyncColor, _updateFileSyncPars)
	beta = Tag('raytkBeta', _betaColor)

def getActiveEditor() -> 'NetworkEditor':
	pane = ui.panes.current
	if pane.type == PaneType.NETWORKEDITOR:
		return pane
	for pane in ui.panes:
		if pane.type == PaneType.NETWORKEDITOR:
			return pane

def getPaneByName(name: str):
	for pane in ui.panes:
		if pane.name == name:
			return pane

def getEditorPane(name: Optional[str] = None, popup=False):
	if name:
		pane = getPaneByName(name)
	else:
		pane = getActiveEditor()
	if pane:
		if popup:
			return pane.floatingCopy()
		return pane
	else:
		return ui.panes.createFloating(type=PaneType.NETWORKEDITOR, name=name)

def navigateTo(o: 'OP', name: Optional[str] = None, popup=False, goInto=True):
	if not o:
		return
	pane = getEditorPane(name, popup)
	if not pane:
		return
	if goInto and o.isCOMP:
		pane.owner = o
	else:
		pane.owner = o.parent()
		o.current = True
		o.selected = True
		pane.homeSelected(zoom=False)

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
	Light = 'Light'

	values = [
		Sdf,
		vec4,
		float,
		Ray,
		Light,
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

class RaytkContext:
	def __init__(self):
		pass

	@staticmethod
	def activeEditor():
		return getActiveEditor()

	@staticmethod
	def currentROPs(
			primaryOnly=False,
			exclude: Callable[['COMP'], None] = None,
			masterOnly=False,
	):
		pane = getActiveEditor()
		if not pane:
			return []
		comp = pane.owner
		if exclude and exclude(comp):
			return None
		rop = getROP(comp) or getROP(comp.currentChild)
		if masterOnly and not _isMaster(rop):
			rop = None
		if rop and primaryOnly:
			return [rop]
		rops = [rop]
		for child in comp.selectedChildren:
			rop = getROP(child, checkParents=False)
			if masterOnly and not _isMaster(rop):
				continue
			if rop and rop not in rops:
				rops.append(rop)
		return rops

def _isMaster(o: 'COMP'):
	return o and o.par['clone'] is not None and (o.par.clone.eval() or o.par.clone.expr)
