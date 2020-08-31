from develCommon import *
from datetime import datetime

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class BuildManager:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.logTable = ownerComp.op('log')

	@staticmethod
	def GetToolkitVersion():
		return getToolkitVersion()

	def RunBuild(self):
		self.logTable.clear()
		self.log('Starting build')
		toolkit = getToolkit()
		toolkit.par.Devel = False
		toolkit.par.Devel.readOnly = True
		toolkit.par.externaltox = ''
		toolkit.par.enablecloning = False
		toolkit.par.savebackup = True
		toolkit.par.reloadtoxonstart = True
		toolkit.par.reloadcustom = True
		toolkit.par.reloadbuiltin = True
		components = toolkit.op('components')
		self.processComponents(components)
		operators = toolkit.op('operators')
		self.processOperators(operators)
		version = getToolkitVersion()
		text = f'RayTK v{version}\nBuilt {datetime.now().isoformat(sep=" ")}'
		toolkit.op('version').text = text
		toxFile = f'build/RayTK-{version}.tox'
		self.log('Exporting TOX to ' + toxFile)
		toolkit.save(toxFile)
		self.log('Build completed!')

	def processComponents(self, components: 'COMP'):
		self.log(f'Processing components {components}')
		self.detachTox(components)
		comps = getChildComps(components)
		for comp in comps:
			self.detachTox(comp)
			self.detachDats(comp)

	def processOperators(self, comp: 'COMP'):
		self.log(f'Processing operators {comp}')
		self.detachTox(comp)
		for child in comp.findChildren(type=COMP):
			self.processOperator(child)

	def processOperator(self, comp: 'COMP'):
		self.log(f'Processing operator {comp}')
		self.detachTox(comp)
		self.detachDats(comp)
		updateROPMetadata(comp)

	def detachTox(self, comp: 'COMP'):
		if not comp.par.externaltox and comp.par.externaltox.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching tox from {comp}')
		comp.par.reloadtoxonstart.expr = ''
		comp.par.reloadtoxonstart.val = False
		comp.par.externaltox.expr = ''
		comp.par.externaltox.val = ''

	def detachDats(self, comp: 'COMP'):
		self.log(f'Detaching DATs in {comp}')
		for dat in comp.findChildren(type=textDAT):
			self.detachDat(dat)
		for dat in comp.findChildren(type=tableDAT):
			self.detachDat(dat)

	def detachDat(self, dat: 'DAT'):
		if not dat.par.file and dat.par.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching DAT {dat}')
		dat.par.syncfile = False
		dat.par.loadonstart = False
		dat.par.write = False
		dat.par.file.expr = ''
		dat.par.file.val = ''

	def processRopCategory(self, comp: 'COMP'):
		self.log(f'Processing ROP category {comp}')
		self.removeTestingOps(comp)

		pass

	def removeTestingOps(self, comp: 'COMP'):
		self.log(f'Removing testing ops from {comp}')
		toRemove = list(comp.ops('__test_*'))
		for o in toRemove:
			o.destroy()

	def log(self, message: str):
		print(message)
		self.logTable.appendRow([message])

def getChildComps(comp: 'COMP'):
	return comp.findChildren(type=COMP, maxDepth=1) if comp else []
