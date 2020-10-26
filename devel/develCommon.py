from typing import List, Union
import re
from pathlib import Path
from raytkUtil import getToolkit

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
	for page in comp.customPages:
		if page.name == 'Metadata':
			page.destroy()
			break

def generateROPType(comp: 'COMP'):
	if not comp:
		return
	toolkit = getToolkit()
	path = toolkit.relativePath(comp)
	if path.startswith('./'):
		path = path[2:]
	return 'raytk.' + path.replace('/', '.')

class AutoLoader:
	def __init__(self, folderComp: 'COMP'):
		self.folderComp = folderComp

	def setUpParameters(self):
		if not self.folderComp.par.externaltox:
			ui.status = f'Component does not have a tox, so auto-load does not apply: {self.folderComp}'
			return
		ui.undo.startBlock(f'Add auto-load parameters to {self.folderComp}')
		page = self.folderComp.appendCustomPage('Auto Load')
		if not self.folderComp.par['Autoloadfolder']:
			p = page.appendFolder('Autoloadfolder', label='Auto Load Folder')[0]
			toxPath = self.folderComp.par.externaltox.eval()
			if toxPath:
				p.val = Path(toxPath).parent.as_posix() + '/'
		if self.folderComp.par['Autoloaddeletemissing'] is None:
			page.appendToggle('Autoloaddeletemissing', label='Delete Missing Components')
		if self.folderComp.par['Autoloadalwaysreloadall'] is None:
			page.appendToggle('Autoloadalwaysreloadall', label='Always Reload All')
		ui.undo.endBlock()

	def applyAutoLoad(self):
		print(f'Applying auto load to {self.folderComp}')
		if not self.folderComp.par['Autoloadfolder']:
			return
		folder = self.folderComp.par.Autoloadfolder.eval()
		folderPath = Path(folder)
		if not folderPath.exists() or not folderPath.is_dir():
			raise Exception(f'Invalid auto-load folder: {folder!r}')
		parentToxPath = Path(self.folderComp.par.externaltox.eval()).as_posix()
		deleteMissing = bool(self.folderComp.par['Autoloaddeletemissing'])
		alwaysReload = bool(self.folderComp.par['Autoloadalwaysreloadall'])

		currentCompsByTox = {
			Path(c.par.externaltox.eval()).as_posix(): c
			for c in self.folderComp.findChildren(type=COMP, maxDepth=1)
			if c.par.externaltox
		}

		toxPaths = [
			p.as_posix()
			for p in sorted(folderPath.glob('*.tox'))
			if p.as_posix() != parentToxPath
		]
		print(f'Auto load found current comps:')
		for t, c in currentCompsByTox.items():
			print(f'   {c} : {t}')
		print(f'Auto load found toxes:')
		for t in toxPaths:
			print(f'   {t}')

		toDelete = []  # type: List[COMP]
		toxsToLoad = []  # type: List[str]

		if alwaysReload:
			toDelete = list(currentCompsByTox.values())
			toxsToLoad = list(toxPaths)
		else:
			if deleteMissing:
				toDelete = [
					comp
					for tox, comp in currentCompsByTox.items()
					if tox not in toxPaths
				]
			toxsToLoad = [
				tox
				for tox in toxPaths
				if tox not in currentCompsByTox
			]

		# print(f'Auto load for {self.folderComp} will destroy:')
		# print('\n'.join([c.name for c in toDelete]))
		# print('and will load:')
		# print('\n'.join(toxsToLoad))

		for child in toDelete:
			print(f'Auto load is removing {child}')
			try:
				child.destroy()
			except:
				pass

		for i, tox in enumerate(toxsToLoad):
			print(f'Auto load is loading {tox}')
			comp = self.folderComp.loadTox(tox)
			comp.nodeY = 500 - i * 150

