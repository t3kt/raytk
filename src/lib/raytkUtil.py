from functools import total_ordering
import re
from typing import Callable, List, Union, Optional, Tuple

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _typeAliases import *
	op.raytk = COMP()

def getToolkit() -> 'COMP':
	if hasattr(parent, 'raytk'):
		return parent.raytk
	if hasattr(op, 'raytk'):
		return op.raytk

@total_ordering
class Version:
	pattern = re.compile(r'([0-9])+(?:\.([0-9]+))?')

	def __init__(self, majorOrString: Union[str, int, Cell, Par] = None, minor: int = None):
		if isinstance(majorOrString, (Cell, Par)):
			majorOrString = str(majorOrString)
		if isinstance(majorOrString, str):
			s = majorOrString  # type: str
			if minor is not None:
				raise Exception('Cannot specify both string and major/minor')
			match = Version.pattern.match(s)
			if not match:
				raise Exception(f'Invalid version string: {s!r}')
			majorPart = match.group(1)
			minorPart = match.group(2)
			major = int(majorPart)
			minor = int(minorPart) if minorPart else 0
		else:
			major = majorOrString
		if major is None:
			raise Exception('Must specify either string or `major`')
		self.major = major
		self.minor = minor or 0

	def __str__(self):
		return f'{self.major}.{self.minor}'

	def __repr__(self):
		return f'Version({self.major}, {self.minor})'

	def __eq__(self, other: 'Version'):
		return self.major == other.major and self.minor == self.minor

	def __ne__(self, other: 'Version'):
		return not (self == other)

	def __lt__(self, other: 'Version'):
		if self.major < other.major:
			return True
		elif self.major == other.major:
			return self.minor < other.minor
		else:
			return False

def getToolkitVersion():
	toolkit = getToolkit()
	par = toolkit.par['Raytkversion']
	return Version(str(par or '0.1'))

class _OpMetaPars:
	enablecloningpulse: 'Par'
	Raytkoptype: 'StrParamT'
	Raytkopversion: 'IntParamT'
	Raytkversion: 'StrParamT'

class CompDefParsT(_OpMetaPars):
	Help: 'DatParamT'
	Helpurl: 'StrParamT'
	Rops: 'StrParamT'

class OpDefParsT(_OpMetaPars):
	Hostop: 'OPParamT'
	Name: 'StrParamT'
	Enable: 'BoolParamT'
	Opglobals: 'DatParamT'
	Initcode: 'DatParamT'
	Functemplate: 'DatParamT'
	Materialcode: 'DatParamT'
	Macrotable: 'DatParamT'
	Params: 'StrParamT'
	Specialparams: 'StrParamT'
	Callbacks: 'DatParamT'
	Librarynames: 'StrParamT'
	Help: 'DatParamT'
	Helpurl: 'StrParamT'
	Disableinspect: 'BoolParamT'

class ROPInfo:
	rop: 'Optional[Union[OP, COMP]]'
	opDef: 'Optional[COMP]'
	opDefPar: 'Optional[Union[ParCollection, OpDefParsT, CompDefParsT]]'

	def __init__(self, o: 'Union[OP, str, Cell, Par]'):
		o = op(o)
		if not o:
			return
		if isROP(o):
			self.rop = o
			self.opDef = o.op('opDefinition')
			# noinspection PyTypeChecker
			self.opDefPar = self.opDef.par
		elif isROPDef(o):
			self.rop = o.par.Hostop.eval()
			self.opDef = o
			# noinspection PyTypeChecker
			self.opDefPar = self.opDef.par
		elif _isRComp(o):
			self.rop = o
			self.opDef = o.op('compDefinition')
			# noinspection PyTypeChecker
			self.opDefPar = self.opDef.par
		elif _isRCompDef(o):
			self.rop = o.par.Hostop.eval()
			self.opDef = o
			# noinspection PyTypeChecker
			self.opDefPar = self.opDef.par
		else:
			self.rop = None
			self.opDef = None
			self.opDefPar = None

	def __bool__(self):
		return bool(self.rop)

	@property
	def path(self):
		if self:
			return self.rop.path

	@property
	def opVersion(self):
		return str(self.opDefPar.Raytkopversion or '')

	@opVersion.setter
	def opVersion(self, val):
		self.opDefPar.Raytkopversion = val if val is not None else ''

	@property
	def toolkitVersion(self):
		return str(self.opDefPar.Raytkversion or '')

	@toolkitVersion.setter
	def toolkitVersion(self, val):
		self.opDefPar.Raytkversion = val if val is not None else ''

	@property
	def opType(self):
		return str(self.opDefPar.Raytkoptype or '')

	@opType.setter
	def opType(self, val: str):
		self.opDefPar.Raytkoptype = val

	@property
	def helpUrl(self):
		return str(self.opDefPar.Helpurl or '')

	@helpUrl.setter
	def helpUrl(self, val):
		self.opDefPar.Helpurl = val

	@property
	def isROP(self):
		return isROP(self.rop)

	@property
	def isRComp(self):
		return _isRComp(self.rop)

	@property
	def isBeta(self):
		return RaytkTags.beta.isOn(self.rop)

	@property
	def isAlpha(self):
		return RaytkTags.alpha.isOn(self.rop)

	@property
	def isDeprecated(self):
		return RaytkTags.deprecated.isOn(self.rop)

	@property
	def statusLabel(self):
		if self.isDeprecated:
			return 'deprecated'
		elif self.isAlpha:
			return 'alpha'
		elif self.isBeta:
			return 'beta'
		else:
			return ''

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

	def toMaster(self):
		if not self or self.isMaster:
			return self
		return ROPInfo(self.rop.par.clone.eval())

	@property
	def categoryName(self):
		if not self:
			return None
		if self.isMaster:
			return self.rop.parent().name
		elif self.rop.par.clone:
			return self.rop.par.clone.eval().parent().name

	@property
	def shortName(self):
		t = self.opType
		if not t:
			return None
		return t.rsplit('.', 1)[-1]

	@property
	def subROPs(self):
		if not self or not self.isRComp or not self.opDefPar['Rops']:
			return []
		return self.opDefPar.Rops.evalOPs()

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
	def inputHandlers(self) -> 'List[COMP]':
		if not self:
			return []
		handlers = self.rop.ops('inputDefinitionHandler_*')
		handlers.sort(key=lambda o: o.nodeY, reverse=True)
		return handlers

	@property
	def multiInputHandler(self) -> 'Optional[COMP]':
		if self:
			return self.rop.op('multiInputHandler')

	@property
	def isOutput(self):
		return RaytkTags.raytkOutput.isOn(self.rop)

	@property
	def toxFile(self) -> 'Optional[str]':
		return self.rop.par.externaltox.eval() or None

	@property
	def supportsInspect(self):
		if not self:
			return False
		if self.isROP:
			return not self.opDefPar.Disableinspect
		for sub in self.subROPs:
			subInfo = ROPInfo(sub)
			if subInfo.supportsInspect:
				return True
		return False

	@property
	def callbacksDAT(self) -> 'Optional[DAT]':
		if not self.opDefPar or not self.opDefPar.Callbacks:
			return None
		return self.opDefPar.Callbacks.eval()

	@property
	def callbacks(self) -> 'Optional[MOD]':
		dat = self.callbacksDAT
		if not dat:
			return None
		return dat.module

	def invokeCallback(self, name: str, **kwargs):
		cb = self.callbacks
		if cb and hasattr(cb, name):
			getattr(cb, name)(**kwargs)

def inputHandlerNameAndLabel(inputHandler: 'COMP') -> 'Tuple[str, str]':
	if not inputHandler:
		return '', ''
	dat = inputHandler.inputs[0]
	if not isinstance(dat, inDAT):
		return inputHandler.name.replace('inputDefinitionHandler_', 'definition_in_'), ''
	name = dat.name
	label = ''
	p = dat.par.label  # type: Par
	if not p.isDefault:
		# noinspection PyBroadException
		try:
			label = p.eval()
		except Exception:
			pass
	return name, label

class CategoryInfo:
	category: COMP

	def __init__(self, o: 'Union[OP, str, Cell]'):
		o = op(o)
		if not o:
			return
		self.category = o

	@property
	def categoryName(self):
		return self.category.name if self.category else None

	@property
	def helpDAT(self) -> 'Optional[DAT]':
		return self.category and self.category.op('help')

	@property
	def operators(self) -> 'List[COMP]':
		if not self.category:
			return []
		return list(sorted([
			o
			for o in self.category.findChildren(
				type=COMP, tags=[RaytkTags.raytkOP.name, RaytkTags.raytkComp.name], maxDepth=1)
			if not o.name.startswith('__')], key=lambda o: o.path))

	@property
	def operatorInfos(self) -> 'List[ROPInfo]':
		infos = []
		for rop in self.operators:
			info = ROPInfo(rop)
			if info:
				infos.append(info)
		return infos

def isROP(o: 'OP'):
	return bool(o) and o.isCOMP and RaytkTags.raytkOP.isOn(o)

def _isRComp(o: 'OP'):
	return bool(o) and o.isCOMP and RaytkTags.raytkComp.isOn(o)

def isROPDef(o: 'OP'):
	return bool(o) and o.isCOMP and o.name == 'opDefinition'

def _isRCompDef(o: 'OP'):
	return bool(o) and o.isCOMP and o.name == 'compDefinition'

def _getROP(comp: 'COMP', checkParents=True):
	if not comp or comp is root:
		return None
	if isROP(comp) or _isRComp(comp):
		return comp
	if isROPDef(comp) or _isRCompDef(comp):
		host = comp.par.Hostop.eval()
		if isROP(host) or _isRComp(host):
			return host
	if checkParents:
		return _getROP(comp.parent(), checkParents=checkParents)

def getChildROPs(comp: 'COMP'):
	rops = []
	for o in comp.children:
		if isROP(o) or _isRComp(o):
			rops.append(o)
	return rops

def recloneComp(o: 'COMP'):
	if o and o.par['enablecloningpulse'] is not None:
		o.par.enablecloningpulse.pulse()

_defaultNodeColor = 0.545, 0.545, 0.545
_buildExcludeColor = 0.1, 0.1, 0.1
_fileSyncColor = 0.65, 0.5, 1
_alphaColor = 1, 0.55, 0
_betaColor = 1, 0, 0.5
_buildLockColor = 0, 0.68, 0.543
_validationColor = 1, 0.95, 0.45
_deprecatedColor = 0.2, 0.2, 0.2

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

class _OpStatusTag(Tag):
	def apply(self, o: 'OP', state: bool):
		info = ROPInfo(o)
		if info.opDef:
			self.applyTag(info.opDef, state)
			self.applyColor(info.opDef, state)
		if not state:
			# clear it off the main op if it's there instead of / in addition to on opDef
			self.applyTag(o, False)
		self.applyColor(o, state)
		self.applyUpdate(info.opDef, state)

	def isOn(self, o: 'OP'):
		opDef = ROPInfo(o).opDef
		return super().isOn(o) or super().isOn(opDef)

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
	raytkComp = Tag('raytkComp')
	raytkOutput = Tag('raytkOutput')
	buildExclude = Tag('buildExclude', _buildExcludeColor)
	buildLock = Tag('buildLock', _buildLockColor)
	fileSync = Tag('fileSync', _fileSyncColor, _updateFileSyncPars)
	alpha = _OpStatusTag('raytkAlpha', _alphaColor)
	beta = _OpStatusTag('raytkBeta', _betaColor)
	deprecated = _OpStatusTag('raytkDeprecated', _deprecatedColor)
	validation = Tag('raytkValidation', _validationColor)

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
	functionGraph = 'functionGraph'

	values = [
		none,
		field,
		render2d,
		render3d,
		functionGraph,
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
	float = 'float'
	vec2 = 'vec2'
	vec3 = 'vec3'

	values = [
		float,
		vec2,
		vec3,
	]

class ContextTypes:
	Context = 'Context'
	MaterialContext = 'MaterialContext'
	CameraContext = 'CameraContext'
	LightContext = 'LightContext'
	RayContext = 'RayContext'
	none = 'none'

	values = [
		Context,
		none,
		MaterialContext,
		CameraContext,
		LightContext,
		RayContext,
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

class TypeTableHelper:
	def __init__(self, table: 'DAT'):
		self.table = table

	def getTypeNamesAndLabels(self, filterColumn: str) -> 'Tuple[List[str], List[str]]':
		names = []
		labels = []
		for row in range(1, self.table.numRows):
			if self.table[row, filterColumn] != '1':
				continue
			names.append(self.table[row, 'name'].val)
			labels.append(self.table[row, 'label'].val)
		return names, labels

	def isTypeAvailableForCategory(self, typeName: str, filterColumn: str):
		return self.table[typeName, filterColumn] == '1'

	def updateTypePar(
			self,
			par: 'Par',
			filterColumn: str,
			hasUseInput: Optional[bool] = None):
		currentVal = par.eval()
		if hasUseInput is None:
			hasUseInput = 'useinput' in par.menuNames
		names, labels = self.getTypeNamesAndLabels(filterColumn)
		if hasUseInput:
			names = ['useinput'] + names
			labels = ['Use Input'] + labels
		ui.undo.startBlock(f'Updating type parameter {par.owner} {par.name} hasUseInput: {hasUseInput}')
		par.menuNames = names
		par.menuLabels = labels
		par.val = currentVal
		ui.undo.endBlock()

	def updateCoordTypePar(
			self,
			par: 'Par',
			hasUseInput: Optional[bool] = None):
		self.updateTypePar(par, 'isCoordType', hasUseInput=hasUseInput)

	def updateContextTypePar(
			self,
			par: 'Par',
			hasUseInput: Optional[bool] = None):
		self.updateTypePar(par, 'isContextType', hasUseInput=hasUseInput)

	def updateReturnTypePar(
			self,
			par: 'Par',
			hasUseInput: Optional[bool] = None):
		self.updateTypePar(par, 'isReturnType', hasUseInput=hasUseInput)

	def coordTypes(self):
		types, _ = self.getTypeNamesAndLabels('isCoordType')
		return types

	def contextTypes(self):
		types, _ = self.getTypeNamesAndLabels('isContextType')
		return types

	def returnTypes(self):
		types, _ = self.getTypeNamesAndLabels('isReturnType')
		return types

class RaytkContext:
	@staticmethod
	def toolkit():
		return getToolkit()

	@staticmethod
	def toolkitVersion():
		return getToolkitVersion()

	def operatorsRoot(self):
		return self.toolkit().op('operators')

	@staticmethod
	def activeEditor():
		return getActiveEditor()

	def opTable(self) -> 'Optional[DAT]':
		toolkit = self.toolkit()
		return toolkit and toolkit.op('opTable')

	def opHelpTable(self) -> 'Optional[DAT]':
		toolkit = self.toolkit()
		return toolkit and toolkit.op('opHelpTable')

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
		if not comp:
			return []
		if exclude and exclude(comp):
			return []
		rop = _getROP(comp) or _getROP(comp.currentChild)
		if masterOnly and not _isMaster(rop):
			rop = None
		if rop and primaryOnly:
			return [rop]
		rops = [rop] if rop else []
		for child in comp.selectedChildren:
			rop = _getROP(child, checkParents=False)
			if masterOnly and not _isMaster(rop):
				continue
			if rop and rop not in rops:
				rops.append(rop)
		return rops

	def currentCategories(self):
		pane = getActiveEditor()
		if not pane:
			return None
		comp = pane.owner
		operators = self.operatorsRoot()
		if comp.parent() == operators:
			return [comp]
		if comp != operators:
			return []
		cats = []
		for child in comp.selectedChildren:
			if child.isCOMP:
				cats.append(child)
		return cats

	def allCategories(self):
		return [
			child
			for child in self.operatorsRoot().children
			if child.isCOMP
		]

	def allMasterOperators(self):
		results = []
		for catComp in self.allCategories():
			results += CategoryInfo(catComp).operators
		return results

def _isMaster(o: 'COMP'):
	return o and o.par['clone'] is not None and (o.par.clone.eval() or o.par.clone.expr)

def simplifyNames(fullNames: List[Union[str, 'Cell']]):
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

def _longestCommonPrefix(strs):
	if not strs:
		return []
	for i, letter_group in enumerate(zip(*strs)):
		if len(set(letter_group)) > 1:
			return strs[0][:i]
	else:
		return min(strs)

# see https://forum.derivative.ca/t/active-current-page-of-parameter-comp-as-a-chop-value/10458
def focusCustomParameterPage(o: 'COMP', page: 'Union[str, int, Page]'):
	if not o or not o.customPages:
		return
	customIndex = None
	if isinstance(page, int):
		customIndex = page
	elif isinstance(page, str):
		for pg in o.customPages:
			if pg.name == page:
				customIndex = pg.index
				break
	elif isinstance(page, Page):
		customIndex = page.index
	if customIndex is not None:
		customIndex += len(o.pages)
		o.par.stdswitcher1 = customIndex
		o.cook(force=True)

def detachTox(comp: 'COMP'):
	if not comp or comp.par['externaltox'] is None:
		return
	if not comp.par.externaltox and comp.par.externaltox.mode == ParMode.CONSTANT:
		return
	comp.par.reloadtoxonstart.expr = ''
	comp.par.reloadtoxonstart.val = False
	comp.par.externaltox.expr = ''
	comp.par.externaltox.val = ''

def stripFirstMarkdownHeader(text: str):
	if not text:
		return ''
	if not text.startswith('# '):
		return text
	return text.split('\n', 1)[1].strip()

_headerPattern = re.compile(r'^#', re.MULTILINE)
def incrementMarkdownHeaders(text: str, steps: int):
	if not text:
		return ''
	return _headerPattern.sub('#' + ('#' * steps), text)

def stripFrontMatter(text: str):
	if not text or not text.startswith('---'):
		return text or ''
	return text.split('---\n', maxsplit=2)[-1]

def datText(path: 'Union[str, Cell]'):
	dat = op(path)
	return dat.text.strip() if dat else ''
