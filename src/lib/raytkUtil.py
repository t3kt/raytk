"""
Common utilities for working with the toolkit and related ops.
This can be included in runtime tools.
"""
from functools import total_ordering
from pathlib import Path
import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _typeAliases import *
	from _stubs.PopDialogExt import PopDialogExt
	from typing import Callable, Optional
	from components.opDefinition.opDefinition import OpDefinition

	op.raytk = COMP()

@total_ordering
class Version:
	pattern = re.compile(r'([0-9])+(?:\.([0-9]+))?')

	def __init__(self, majorOrString: str | int | Cell | Par | None = None, minor: int = None):
		if isinstance(majorOrString, (Cell, Par)):
			majorOrString = str(majorOrString)
		if isinstance(majorOrString, str):
			s = majorOrString  # type: str
			if minor is not None:
				raise ValueError('Cannot specify both string and major/minor')
			match = Version.pattern.match(s)
			if not match:
				raise ValueError(f'Invalid version string: {s!r}')
			majorPart = match.group(1)
			minorPart = match.group(2)
			major = int(majorPart)
			minor = int(minorPart) if minorPart else 0
		else:
			major = majorOrString
		if major is None:
			raise ValueError('Must specify either string or `major`')
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

class _OpMetaPars:
	enablecloningpulse: Par
	Raytkoptype: 'StrParamT'
	Raytkopversion: 'IntParamT'
	Raytkopstatus: 'StrParamT'
	Raytkversion: 'StrParamT'
	Lockpars: 'StrParamT'

class CompDefParsT(_OpMetaPars):
	Help: 'DatParamT'
	Helpurl: 'StrParamT'
	Displaycategory: 'StrParamT'
	Keywords: 'StrParamT'
	Shortcuts: 'StrParamT'
	Rops: 'StrParamT'
	Style: 'StrParamT'
	Label: 'StrParamT'

class OpDefParsT(_OpMetaPars):
	Useruntimebypass: 'BoolParamT'
	Hostop: 'OPParamT'
	Paramsop: 'OPParamT'
	Name: 'StrParamT'
	Style: 'StrParamT'
	Label: 'StrParamT'
	Enable: 'BoolParamT'
	Opglobals: 'DatParamT'
	Initcode: 'DatParamT'
	Functemplate: 'DatParamT'
	Materialcode: 'DatParamT'
	Macrotable: 'DatParamT'
	Buffertable: 'DatParamT'
	Texturetable: 'DatParamT'
	Variabletable: 'DatParamT'
	Referencetable: 'DatParamT'
	Tagtable: 'DatParamT'
	Generatedmacrotables: 'StrParamT'
	Paramgrouptable: 'DatParamT'
	Callbacks: 'DatParamT'
	Librarynames: 'StrParamT'
	Help: 'DatParamT'
	Helpurl: 'StrParamT'
	Displaycategory: 'StrParamT'
	Keywords: 'StrParamT'
	Shortcuts: 'StrParamT'
	Disableinspect: 'BoolParamT'
	Typespec: 'CompParamT'
	Inputdefs: 'StrParamT'
	Flags: 'StrParamT'

	def __getitem__(self, item) -> Par | None:
		return getattr(self, item)

class ModuleMetaParsT:
	Modulename: 'StrParamT'
	Optable: 'DatParamT'
	Operatorsroot: 'CompParamT'
	Operatorsfolder: 'StrParamT'
	Testsfolder: 'StrParamT'
	Raytkopversion: 'IntParamT'
	Experimentalbuild: 'BoolParamT'

class ROPInfo:
	"""
	Information about either a ROP or RComp instance.

	If the OP used to construct the ROPInfo is invalid or missing, this will evaluate
	to False when treated as a boolean.
	"""

	rop: OP | COMP | None
	opDef: COMP | None
	opDefPar: 'ParCollection | OpDefParsT | CompDefParsT | None'

	def __init__(self, o: OP | str | Cell | Par | None):
		o = op(o)
		if not o:
			self.rop = None
			self.opDef = None
			self.opDefPar = None
		elif isROP(o):
			self.rop = o
			self.opDef = o.op('opDefinition')
			# noinspection PyTypeChecker
			self.opDefPar = self.opDef.par
		elif isROPDef(o) and o.par['Hostop'] is not None:
			self.rop = o.par.Hostop.eval()
			self.opDef = o
			# noinspection PyTypeChecker
			self.opDefPar = self.opDef.par
		elif isRComp(o):
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
	def opDefExt(self) -> 'Optional[OpDefinition]':
		if not self.isROP:
			return
		return getattr(self.opDef.ext, 'opDefinition', None)

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
	def opStyle(self):
		return str(self.opDefPar['Style'] or 'default')

	@property
	def opLabel(self):
		return str(self.opDefPar['Label'])

	@property
	def helpUrl(self):
		return str(self.opDefPar.Helpurl or '')

	@helpUrl.setter
	def helpUrl(self, val):
		self.opDefPar.Helpurl = val

	@property
	def paramsOp(self) -> COMP | None:
		if not self.isROP:
			return None
		return self.opDefPar.Paramsop.eval() or self.rop

	@paramsOp.setter
	def paramsOp(self, o: COMP | None):
		if not self.isROP:
			return
		self.opDefPar.Paramsop = o or ''

	@property
	def isROP(self):
		return isROP(self.rop)

	@property
	def isRComp(self):
		return isRComp(self.rop)

	@property
	def _statusInParam(self):
		if not self:
			return ''
		val = str(self.opDefPar['Raytkopstatus'] or '')
		return '' if val == 'unset' else val

	def _checkStatus(self, name: str, tag: 'Tag'):
		if not self:
			return False
		val = self._statusInParam
		if val:
			return val == name
		return tag.isOn(self.rop)

	@property
	def isBeta(self):
		return self._checkStatus('beta', RaytkTags.beta)

	@property
	def isAlpha(self):
		return self._checkStatus('alpha', RaytkTags.alpha)

	@property
	def isDeprecated(self):
		return self._checkStatus('deprecated', RaytkTags.deprecated)

	@property
	def statusLabel(self):
		val = self._statusInParam
		if val:
			return val
		if self.isDeprecated:
			return 'deprecated'
		elif self.isAlpha:
			return 'alpha'
		elif self.isBeta:
			return 'beta'
		else:
			return 'default'

	def setOpStatus(self, status: str | None):
		if not self:
			return
		self.opDefPar.Raytkopstatus = status or 'default'
		# note: since applying with status false resets the color, the false ones have to be done before the true one
		if status == 'alpha':
			RaytkTags.beta.apply(self.rop, False)
			RaytkTags.deprecated.apply(self.rop, False)
			RaytkTags.alpha.apply(self.rop, True)
		elif status == 'beta':
			RaytkTags.alpha.apply(self.rop, False)
			RaytkTags.deprecated.apply(self.rop, False)
			RaytkTags.beta.apply(self.rop, True)
		elif status == 'deprecated':
			RaytkTags.alpha.apply(self.rop, False)
			RaytkTags.beta.apply(self.rop, False)
			RaytkTags.deprecated.apply(self.rop, True)
		else:
			RaytkTags.alpha.apply(self.rop, False)
			RaytkTags.beta.apply(self.rop, False)
			RaytkTags.deprecated.apply(self.rop, False)

	@property
	def isMaster(self):
		if not self.rop:
			return False
		module = getattr(self.rop.parent, 'raytkModule', None)
		if module:
			modDef = module.op('moduleDefinition')
			operators = modDef and op(modDef.par['Operatorsroot'])
			if operators and operators.path in self.rop.parent().path:
				return True
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
	def displayCategoryName(self):
		if not self:
			return None
		p = self.opDefPar['Displaycategory']
		return str(p) if p else None

	@property
	def shortName(self):
		'''
		Short form of the name of the ROP type (not the ROP instance).
		'''
		t = self.opType
		if not t:
			return None
		return t.rsplit('.', 1)[-1]

	@property
	def typeSpec(self) -> COMP | None:
		if not self.isROP:
			return None
		return self.opDefPar.Typespec.eval()

	@property
	def supportedTypeTable(self) -> DAT | None:
		if not self.isROP:
			return None
		return self.opDef.op('supportedTypes')

	@property
	def outputBufferTable(self) -> DAT | None:
		if not self.isOutput:
			return None
		return self.rop.op('outputBuffers')

	@property
	def subROPs(self):
		if not self:
			return []
		if not self.isRComp or self.opDefPar['Rops'] is None:
			return _getChildROPs(self.rop)
		return self.opDefPar.Rops.evalOPs()

	@property
	def helpDAT(self) -> DAT | None:
		dat = op(self.opDefPar.Help)
		if dat:
			return dat
		dat = self.rop.op('help')
		if dat and dat.isDAT:
			return dat

	@helpDAT.setter
	def helpDAT(self, dat: DAT | None):
		self.opDefPar.Help = dat or ''

	@property
	def keywords(self) -> set[str]:
		return set(tdu.split(self.opDefPar['Keywords'] or '')) if self else set()

	@keywords.setter
	def keywords(self, keywords: set[str] | None):
		self.opDefPar.Keywords = ' '.join(sorted(keywords)) if keywords else ''

	@property
	def shortcuts(self) -> set[str]:
		return set(tdu.split(self.opDefPar['Shortcuts'] or '')) if self else set()

	@property
	def hasROPInputs(self):
		for conn in self.opDef.inputConnectors:
			if conn.connections and conn.inOP.isDAT:
				return True
		return False

	@property
	def inputHandlers(self) -> list[COMP]:
		if not self:
			return []
		handlers = self.rop.ops('inputHandler*')
		handlers = [o for o in handlers if o.isCOMP and not o.name.endswith('_typeSpec')]
		handlers.sort(key=lambda o: o.nodeY, reverse=True)
		return handlers

	@property
	def multiInputHandler(self) -> COMP | None:
		if self:
			return self.rop.op('multiInputHandler')

	@property
	def isOutput(self):
		return RaytkTags.raytkOutput.isOn(self.rop)

	@property
	def toxFile(self) -> str | None:
		return self.rop.par.externaltox.eval() or None

	@property
	def supportsInspect(self):
		if not self:
			return False
		if self.isROP:
			return not self.opDefPar['Disableinspect']
		for sub in self.subROPs:
			subInfo = ROPInfo(sub)
			if subInfo.supportsInspect:
				return True
		return False

	@property
	def callbacksDAT(self) -> DAT | None:
		if not self.opDefPar or not self.opDefPar['Callbacks']:
			return None
		return self.opDefPar.Callbacks.eval()

	@property
	def callbacks(self) -> MOD | None:
		dat = self.callbacksDAT
		if not dat:
			return None
		return dat.module

	def invokeCallback(self, name: str, **kwargs):
		cb = self.callbacks
		if cb and hasattr(cb, name):
			getattr(cb, name)(**kwargs)

	@property
	def ropKind(self):
		if not self:
			return
		if self.isOutput:
			return RaytkTags.raytkOutput.name
		if self.isROP:
			return RaytkTags.raytkOP.name
		if self.isRComp:
			return RaytkTags.raytkComp.name

	def moduleRoot(self):
		if not self.isMaster:
			return None
		module = getattr(self.rop.parent, 'raytkModule', None)
		if module:
			return module
		return getattr(self.rop.parent, 'raytk', None)

	def moduleName(self):
		moduleRoot = self.moduleRoot()
		if not moduleRoot:
			return None
		return ModuleInfo(moduleRoot).moduleName

class _InputHandlerParsT:
	Source: 'OPParamT'
	Required: 'BoolParamT'
	Variables: 'StrParamT'
	Variableinputs: 'StrParamT'

class InputInfo:
	"""
	Information about a ROP input and its supported types and requirements.

	This is constructed from an `inputHandler` component, whose parameters
	define the behavior.
	"""

	handler: COMP | None
	rop: COMP | None
	handlerPar: '_InputHandlerParsT | ParCollection'

	def __init__(self, handler: OP | str | Cell | Par):
		handler = op(handler)
		if not handler:
			return
		self.handler = handler
		self.handlerPar = handler.par
		self.rop = handler.parent()

	def __bool__(self):
		return bool(self.handler)

	def _configTableVal(self, name: str) -> str | None:
		table = self.handler and self.handler.op('config')
		if table and table[name, 1] is not None:
			return table[name, 1].val

	@property
	def name(self) -> str | None:
		return self._configTableVal('name')

	@property
	def label(self) -> str | None:
		return self._configTableVal('label')

	@label.setter
	def label(self, val: str | None):
		self.handlerPar.Label = val or ''

	@property
	def multiHandler(self) -> COMP | None:
		"""
		:return: The `multiInputHandler` that this input flows into, if any.
		"""

		if not self.handler or not self.handler.outputs:
			return
		output = self.handler.outputs[0]
		if output.isDAT and output.outputs:
			output = output.outputs[0]
		if output and output.isCOMP and output.name == 'multiInputHandler':
			return output

	@property
	def required(self):
		return bool(self.handler and self.handler.par.Required)

	def _supportedTypeTable(self) -> DAT | None:
		return self.handler and self.handler.op('./supportedTypes')

	@property
	def supportedCoordTypes(self):
		table = self._supportedTypeTable()
		return tdu.split(table['coordType', 'types']) if table else []

	@property
	def supportedContextTypes(self):
		table = self._supportedTypeTable()
		return tdu.split(table['contextType', 'types']) if table else []

	@property
	def supportedReturnTypes(self):
		table = self._supportedTypeTable()
		return tdu.split(table['returnType', 'types']) if table else []

	@property
	def supportedVariables(self):
		return tdu.split(self.handlerPar.Variables) if self.handlerPar.Variables else []

	@property
	def supportedVariableInputs(self):
		return tdu.split(self.handlerPar.Variableinputs) if self.handlerPar.Variableinputs else []

class CategoryInfo:
	"""
	Information about a category of ROPs.

	This can be used by tools that show lists of available ROP types.
	"""

	category: COMP

	def __init__(self, o: OP | str | Cell):
		o = op(o)
		if not o:
			return
		self.category = o

	def __bool__(self):
		return bool(self.category)

	@property
	def categoryName(self):
		return self.category.name if self.category else None

	@property
	def helpDAT(self) -> DAT | None:
		return self.category and self.category.op('help')

	@property
	def operators(self) -> list[COMP]:
		if not self.category:
			return []
		return list(sorted([
			o
			for o in _getChildROPs(self.category)
			if not o.name.startswith('__')], key=lambda o: o.path))

	@property
	def templateComp(self) -> COMP | None:
		return self.category.op('__template')

class ModuleInfo:
	module: COMP | None
	modDef: COMP | None
	modDefPar: 'ParCollection | ModuleMetaParsT | None'

	def __init__(self, o: OP | str | Cell, modDef: COMP | None = None):
		o = op(o)
		if not o:
			self.module = None
			self.modDef = None
			self.modDefPar = None
			return
		self.module = o
		self.modDef = modDef or o.op('moduleDefinition')
		self.modDefPar = self.modDef and self.modDef.par

	def __bool__(self):
		return bool(self.modDef)

	@property
	def moduleName(self):
		return self.modDefPar.Modulename.eval() if self else None

	def operatorsRoot(self) -> COMP | None:
		if not self:
			return None
		return self.modDefPar.Operatorsroot.eval()

	def allCategories(self):
		return [
			child
			for child in self.operatorsRoot().children
			if child.isCOMP
		]

	def categoryInfo(self, category: str) -> 'CategoryInfo | None':
		comp = self.operatorsRoot().op(category)
		if comp:
			return CategoryInfo(comp)


def isROP(o: OP):
	return bool(o) and o.isCOMP and RaytkTags.raytkOP.isOn(o)

def isRComp(o: OP):
	return bool(o) and o.isCOMP and RaytkTags.raytkComp.isOn(o)

def isROPDef(o: OP):
	return bool(o) and o.isCOMP and o.name == 'opDefinition' and o.par['Hostop'] is not None

def _isRCompDef(o: OP):
	return bool(o) and o.isCOMP and o.name == 'compDefinition' and o.par['Hostop'] is not None

def _getROP(comp: COMP, checkParents=True):
	if not comp or comp is root:
		return None
	if isROP(comp) or isRComp(comp):
		return comp
	if isROPDef(comp) or _isRCompDef(comp):
		host = op(comp.par['Hostop'])
		if isROP(host) or isRComp(host):
			return host
	if checkParents:
		return _getROP(comp.parent(), checkParents=checkParents)

def _getChildROPs(comp: COMP, maxDepth=1):
	return comp.findChildren(type=COMP, tags=[RaytkTags.raytkOP.name, RaytkTags.raytkComp.name], maxDepth=maxDepth)

def _getChildOutputROPs(comp: COMP, maxDepth=1):
	return comp.findChildren(type=COMP, tags=[RaytkTags.raytkOutput.name], maxDepth=maxDepth)

def recloneComp(o: COMP):
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
_guideColor = 0.0477209, 0.816, 0.816


class IconColors:
	defaultBgColor = 0.0477209, 0.111349, 0.114
	defaultFgColor = 0.135166, 0.816, 0.816
	alphaBgColor = 0.24, 0.306, 0.405
	alphaFgColor = defaultFgColor
	betaBgColor = 0.1, 0.155, 0.238
	betaFgColor = defaultFgColor
	deprecatedBgColor = 0.185, 0.21, 0.21
	deprecatedFgColor = 0.635, 0.816, 0.816
	experimentalBgColor = 0.1, 0.238, 0.1368
	experimentalFgColor = defaultFgColor


class Tag:
	"""
	A tag that can be applied to OPs which tools use to apply various types of behaviors.
	"""
	def __init__(
			self,
			name: str,
			color: tuple[float, float, float] = None,
			update: 'Callable[[OP, bool], None]' = None):
		"""
		:param name: the tag name
		:param color: Optional RGB color applied to OPs that use the tag.
		:param update: Optional function that applies tag-specific behavior to OPs.
		"""
		self.name = name
		self.color = color
		self.update = update

	def apply(self, o: OP, state: bool):
		"""
		Add/remove the tag on an OP, and update the color (if applicable), and apply the update function (if applicable)
		"""
		self.applyTag(o, state)
		self.applyColor(o, state)
		self.applyUpdate(o, state)

	def applyUpdate(self, o: OP, state: bool):
		"""
		Apply the tag's update function to an OP, performing tag-specific changes.
		"""
		if o and self.update:
			self.update(o, state)

	def applyTag(self, o: OP, state: bool):
		"""
		Add/remove the tag on an OP
		"""
		if not o:
			return
		if state:
			o.tags.add(self.name)
		elif self.name in o.tags:
			o.tags.remove(self.name)

	def applyColor(self, o: OP, state: bool):
		"""
		If applicable, set the color of an OP to either the tag's color or the default color.
		"""
		if self.color:
			o.color = self.color if state else _defaultNodeColor

	def __str__(self):
		return self.name

	def isOn(self, o: OP):
		return bool(o) and self.name in o.tags

class _OpStatusTag(Tag):
	def apply(self, o: OP, state: bool):
		info = ROPInfo(o)
		if info.opDef:
			self.applyTag(info.opDef, state)
			self.applyColor(info.opDef, state)
		if not state:
			# clear it off the main op if it's there instead of / in addition to on opDef
			self.applyTag(o, False)
		self.applyColor(o, state)
		self.applyUpdate(info.opDef, state)

	def isOn(self, o: OP):
		opDef = ROPInfo(o).opDef
		return super().isOn(o) or super().isOn(opDef)

def _getRelPathBehavior(o: OP):
	p = o.par['relpath']
	if p == 'project':
		return 'project'
	if p == 'externaltox':
		return 'externaltox'
	po = o.parent()
	if not po:
		return 'project'
	return _getRelPathBehavior(po)

def _resolveFilePath(o: OP, file: str):
	if not file:
		return ''
	rule = _getRelPathBehavior(o)
	if rule == 'externaltox':
		return o.parent().fileFolder + '/' + file
	return file

def _updateFileSyncPars(o: OP | DAT, state: bool):
	if o.isDAT:
		filePar = o.par['file']
		if filePar and state:
			o.save(_resolveFilePath(o, filePar.eval()))
		if o.par['defaultreadencoding'] is not None:
			o.par.defaultreadencoding = 'utf8'
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
	"""
	The collection of tags used by RayTK infrastructure and tools.
	"""

	raytkOP = Tag('raytkOP')
	"""Indicates that a comp is a ROP."""

	raytkComp = Tag('raytkComp')
	"""Indicates that a comp is a RComp (a component treated similarly to ROPs)."""

	raytkOutput = Tag('raytkOutput')
	"""Indicates that a comp is an output ROP that generates and runs a shared."""

	buildExclude = Tag('buildExclude', _buildExcludeColor)
	"""Indicates that an OP should be removed during the build process."""

	buildLock = Tag('buildLock', _buildLockColor)
	"""Indicates that an OP should be locked during the build process."""

	fileSync = Tag('fileSync', _fileSyncColor, _updateFileSyncPars)
	"""Indicates that a DAT is synced with an external file (when in development mode)."""

	alpha = _OpStatusTag('raytkAlpha')
	"""Status applied to the `opDefinition` within a ROP to indicate that the ROP has alpha status
	(not yet ready for use).
	"""

	beta = _OpStatusTag('raytkBeta')
	"""Status applied to the `opDefinition` within a ROP to indicate that the ROP has beta status
	(experimental and may be unreliable)."""

	deprecated = _OpStatusTag('raytkDeprecated')
	"""Status applied to the `opDefinition` within a ROP to indicate that the ROP has deprecated status
	(should no longer be used and may be removed in future versions)."""

	validation = Tag('raytkValidation', _validationColor)
	"""Indicates that a DAT is a table of validation errors/warnings for related components."""

	guide = Tag('raytkGuide', _guideColor)
	guideHeader = Tag('raytkGuideHeader', _guideColor)
	guideContent = Tag('raytkGuideContent', _guideColor)
	generated = Tag('raytkGenerated')

def getActiveEditor() -> NetworkEditor:
	pane = ui.panes.current
	if pane and pane.type == PaneType.NETWORKEDITOR:
		return pane
	for pane in ui.panes:
		if pane.type == PaneType.NETWORKEDITOR:
			return pane

def _getPaneByName(name: str):
	for pane in ui.panes:
		if pane.name == name:
			return pane

def _getEditorPane(name: str | None = None, popup=False):
	if name:
		pane = _getPaneByName(name)
	else:
		pane = getActiveEditor()
	if pane:
		if popup:
			return pane.floatingCopy()
		return pane
	else:
		return ui.panes.createFloating(type=PaneType.NETWORKEDITOR, name=name)

def navigateTo(o: OP | COMP, name: str | None = None, popup=False, goInto=True) -> NetworkEditor | None:
	if not o:
		return
	pane = _getEditorPane(name, popup)
	if not pane:
		return
	if goInto and o.isCOMP:
		pane.owner = o
	else:
		pane.owner = o.parent()
		o.current = True
		o.selected = True
		pane.homeSelected(zoom=False)
	return pane

class ReturnTypes:
	Sdf = 'Sdf'
	vec4 = 'vec4'
	float = 'float'
	Ray = 'Ray'
	Light = 'Light'
	Volume = 'Volume'

	values = [
		Sdf,
		vec4,
		float,
		Ray,
		Light,
		Volume,
	]

class CoordTypes:
	float = 'float'
	vec2 = 'vec2'
	vec3 = 'vec3'
	vec4 = 'vec4'

	values = [
		float,
		vec2,
		vec3,
		vec4,
	]

class ContextTypes:
	Context = 'Context'
	MaterialContext = 'MaterialContext'
	CameraContext = 'CameraContext'
	LightContext = 'LightContext'
	RayContext = 'RayContext'
	PopContext = 'PopContext'

	values = [
		Context,
		MaterialContext,
		CameraContext,
		LightContext,
		RayContext,
		PopContext,
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
	"""
	Utility that accesses various parts of the toolkit and the current project.
	"""

	@staticmethod
	def toolkit():
		if hasattr(parent, 'raytk'):
			return parent.raytk
		if hasattr(op, 'raytk'):
			return op.raytk

	def moduleRoot(self):
		return self.toolkit()

	def moduleName(self):
		return 'raytk'

	def toolkitVersion(self):
		toolkit = self.toolkit()
		par = toolkit.par['Raytkversion']
		return Version(str(par or '0.1'))

	def develMode(self):
		toolkit = self.toolkit()
		return bool(toolkit and toolkit.par['Devel'])

	def experimentalMode(self):
		toolkit = self.toolkit()
		return bool(toolkit and toolkit.par['Experimentalbuild'])

	def operatorsRoot(self):
		return self.toolkit().op('operators')

	def operatorsFolder(self):
		operatorsRoot = self.operatorsRoot()
		if not operatorsRoot:
			return None
		tox = operatorsRoot.par.externaltox.eval()
		if not tox:
			return None
		return Path(tox).parent.as_posix()

	@staticmethod
	def activeEditor():
		return getActiveEditor()

	def opTable(self) -> DAT | None:
		toolkit = self.toolkit()
		return toolkit and toolkit.op('opTable')

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

	@staticmethod
	def ropChildrenOf(comp: COMP, maxDepth=1):
		return _getChildROPs(comp, maxDepth=maxDepth) if comp else []

	@staticmethod
	def ropOutputChildrenOf(comp: COMP, maxDepth=1):
		return _getChildOutputROPs(comp, maxDepth=maxDepth) if comp else []

	def libraryImage(self) -> COMP | None:
		toolkit = self.toolkit()
		return toolkit and toolkit.op('./libraryImage')

	def categoryInfo(self, category: str) -> 'CategoryInfo | None':
		comp = self.operatorsRoot().op(category)
		if comp:
			return CategoryInfo(comp)

class RaytkModuleContext(RaytkContext):
	module: COMP
	modInfo: ModuleInfo

	def __init__(self, module: COMP):
		self.module = module
		self.modInfo = ModuleInfo(module)

	def moduleRoot(self):
		return self.module

	def moduleName(self):
		return self.modInfo.moduleName

	def moduleDefinition(self):
		return self.modInfo.modDef

	def operatorsRoot(self):
		return self.modInfo.operatorsRoot()

	def operatorsFolder(self):
		folder = self.modInfo.modDefPar.Operatorsfolder.eval()
		if folder:
			return folder
		return super().operatorsFolder()

	def experimentalMode(self):
		return self.modInfo.modDefPar.Experimentalbuild.eval()

	def opTable(self) -> DAT | None:
		return self.modInfo.modDefPar.Optable.eval()

def _isMaster(o: COMP):
	return o and o.par['clone'] is not None and (o.par.clone.eval() or o.par.clone.expr)

def focusFirstCustomParameterPage(o: COMP):
	if o and o.customPages:
		o.currentPage = o.customPages[0]

def detachTox(comp: COMP):
	if not comp or comp.par['externaltox'] is None:
		return
	if not comp.par.externaltox and comp.par.externaltox.mode == ParMode.CONSTANT:
		return
	if comp.par['reloadtoxonstart'] is not None:
		comp.par.reloadtoxonstart.expr = ''
		comp.par.reloadtoxonstart.val = False
	else:
		comp.par.enableexternaltox.expr = ''
		comp.par.enableexternaltox.val = False
	comp.par.externaltox.expr = ''
	comp.par.externaltox.val = ''

def _popDialog() -> 'PopDialogExt':
	# noinspection PyUnresolvedReferences
	return op.TDResources.op('popDialog')

def showPromptDialog(
		title=None,
		text=None,
		default='',
		textEntry=True,
		okText='OK',
		cancelText='Cancel',
		ok: callable = None,
		cancel: callable = None,
):
	def _callback(info: dict):
		if info['buttonNum'] == 1:
			if ok:
				if not textEntry:
					ok()
				else:
					ok(info.get('enteredText'))
		elif info['buttonNum'] == 2:
			if cancel:
				cancel()
	dialog = op.TDResources.op('popDialog')  # type: PopDialogExt
	dialog.Open(
		title=title,
		text=text,
		textEntry=False if not textEntry else (default or ''),
		buttons=[okText, cancelText],
		enterButton=1, escButton=2, escOnClickAway=True,
		callback=_callback)

def showMessageDialog(
		title=None,
		text=None,
		escOnClickAway=True,
		**kwargs):
	dialog = _popDialog()
	dialog.Open(
		title=title,
		text=text,
		escOnClickAway=escOnClickAway,
		**kwargs)

def cleanDict(d):
	if not d:
		return None
	result = {}
	for key, val in d.items():
		if val is None:
			continue
		if isinstance(val, dict):
			val = cleanDict(val)
		if isinstance(val, (str, list, dict, tuple)) and len(val) == 0:
			continue
		result[key] = val
	return result

def mergeDicts(*parts):
	x = {}
	for part in parts:
		if part:
			x.update(part)
	return x
