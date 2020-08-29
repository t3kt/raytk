import re
from typing import Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class Version:
	pattern = re.compile(r'([0-9])+(?:\.([0-9]+))?')

	def __init__(self, majorOrString: Union[str, int] = None, minor: int = None):
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

class Tools:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def getToolkit() -> 'COMP':
		return op.raytk

	def getToolkitVersion(self):
		toolkit = self.getToolkit()
		par = toolkit.par['Raytkversion']
		return Version(str(par or '0.1'))

	def setToolkitVersion(self, version: Version):
		toolkit = self.getToolkit()
		toolkit.par.Raytkversion = str(version)

	def UpdateOpType(self, comp: 'COMP' = None):
		if comp is None:
			comp = self.GetCurrentROP()
		if not comp:
			return
		opDef = getOpDef(comp)
		opDef.par.Optype = self.generateROPType(comp)

	def generateROPType(self, comp: 'COMP'):
		if not comp:
			return
		toolkit = self.getToolkit()
		path = toolkit.relativePath(comp)
		if path.startswith('./'):
			path = path[2:]
		return 'raytk.' + path.replace('/', '.')

	def UpdateROPMetadata(self, comp: 'COMP' = None):
		if comp is None:
			comp = self.GetCurrentROP()
		if not comp:
			return
		page = comp.appendCustomPage('Metadata')
		p = page.appendStr('Raytkoptype', label='OP Type')[0]
		p.default = p.val = self.generateROPType(comp)
		p.readOnly = True
		versionPar = comp.par['Raytkopversion']
		currentVersion = int(versionPar) if versionPar is not None else 0
		p = page.appendStr('Raytkopversion', label='OP Version')[0]
		p.default = p.val = currentVersion
		p.readOnly = True
		p = page.appendStr('Raytkversion', label='RayTK Version')[0]
		p.default = p.val = str(self.getToolkitVersion())
		p.readOnly = True

	def FillMonitorHeight(self, usePrimary=True):
		height = _getMonitorHeight(usePrimary)
		height -= 270
		self.ownerComp.par.h = height

	def NavigateTo(self, comp: 'COMP'):
		if not comp:
			return
		pane = self.GetActiveEditor()
		if not pane:
			return
		pane.owner = comp

	@staticmethod
	def GetActiveEditor():
		pane = ui.panes.current
		if pane.type == PaneType.NETWORKEDITOR:
			return pane
		for pane in ui.panes:
			if pane.type == PaneType.NETWORKEDITOR:
				return pane

	def GetCurrentROP(self):
		pane = self.GetActiveEditor()
		if not pane:
			return None
		comp = pane.owner
		if comp is self.ownerComp or comp.path.startswith(self.ownerComp.path + '/'):
			return None
		rop = _getROP(comp) or _getROP(comp.currentChild)
		if rop:
			return rop
		for child in comp.selectedChildren:
			rop = _getROP(child, checkParents=False)
			if rop:
				return rop

	def SaveROP(self, incrementVersion=False):
		rop = self.GetCurrentROP()
		if not rop:
			# TODO: warning?
			return
		self.UpdateROPMetadata(rop)
		if incrementVersion:
			rop.par.Raytkopversion += 1
		tox = rop.par.externaltox.eval()
		rop.save(tox)
		ui.status = f'Saved TOX {tox} (version: {rop.par.Raytkopversion})'

def _getROP(comp: 'COMP', checkParents=True):
	if not comp or comp is root:
		return None
	if 'raytkOP' in comp.tags:
		return comp
	if comp.name == 'opDefinition':
		host = comp.par.Hostop.eval()
		if host and 'raytkOP' in host.tags:
			return host
	if checkParents:
		return _getROP(comp.parent())

def _getMonitorHeight(usePrimary=True):
	if usePrimary:
		return monitors.primary.height
	for m in monitors:
		if not m.isPrimary:
			return m.height
	for m in monitors:
		return m.height

def getOpDef(comp: 'COMP'):
	return comp and comp.op('opDefinition')


