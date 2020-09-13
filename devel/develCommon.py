from typing import Union
import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	op.raytk = COMP()

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


def getToolkit() -> 'COMP':
	return op.raytk

def getToolkitVersion():
	toolkit = getToolkit()
	par = toolkit.par['Raytkversion']
	return Version(str(par or '0.1'))

def updateROPMetadata(comp: 'COMP', incrementVersion=False):
	opDef = comp.op('opDefinition')
	opDef.par.enablecloningpulse.pulse()
	currentOpType = str(opDef.par['Raytkoptype'] or '')
	currentOpVersion = str(opDef.par['Raytkopversion'] or '')
	page = opDef.appendCustomPage('Metadata')
	newType = generateROPType(comp)
	# don't update op type if this is not the master of the ROP
	if comp.par.clone.eval() != comp:
		newType = currentOpType
	p = page.appendStr('Raytkoptype', label='OP Type')[0]
	p.default = p.val = newType
	p.readOnly = True
	if not currentOpVersion or not currentOpType or currentOpType != newType:
		versionVal = 0
	else:
		versionVal = currentOpVersion
		if incrementVersion:
			versionVal = int(versionVal) + 1
	p = page.appendStr('Raytkopversion', label='OP Version')[0]
	p.default = p.val = versionVal
	p.readOnly = True
	p = page.appendStr('Raytkversion', label='RayTK Version')[0]
	p.default = p.val = str(getToolkitVersion())
	p.readOnly = True

def generateROPType(comp: 'COMP'):
	if not comp:
		return
	toolkit = getToolkit()
	path = toolkit.relativePath(comp)
	if path.startswith('./'):
		path = path[2:]
	return 'raytk.' + path.replace('/', '.')
