from develCommon import *
from datetime import datetime
from typing import List

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
		self.queueMethodCall('runBuild_stage', 0)

	def runBuild_stage(self, stage: int):
		toolkit = getToolkit()
		if stage == 0:
			components = toolkit.op('components')
			self.processComponents(components, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 1:
			operators = toolkit.op('operators')
			self.processOperators(operators, thenRun='runBuild_stage', runArgs=[stage + 1])
		elif stage == 2:
			self.freezeOperatorTable(toolkit)
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 3:
			version = getToolkitVersion()
			text = f'RayTK v{version}\nBuilt {datetime.now().isoformat(sep=" ")}'
			toolkit.op('version').text = text
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 4:
			toolkit.par.Devel = False
			toolkit.par.Devel.readOnly = True
			toolkit.par.externaltox = ''
			toolkit.par.enablecloning = False
			toolkit.par.savebackup = True
			toolkit.par.reloadtoxonstart = True
			toolkit.par.reloadcustom = True
			toolkit.par.reloadbuiltin = True
			self.queueMethodCall('runBuild_stage', stage + 1)
		elif stage == 5:
			version = getToolkitVersion()
			toxFile = f'build/RayTK-{version}.tox'
			self.log('Exporting TOX to ' + toxFile)
			toolkit.save(toxFile)
			self.log('Build completed!')
			ui.messageBox('Build completed!', f'Exported tox file: {toxFile}!')

	def processComponents(self, components: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing components {components}')
		self.detachTox(components)
		comps = getChildComps(components)
		self.queueMethodCall('processComponents_stage', comps, thenRun, runArgs)

	def processComponents_stage(self, components: List['COMP'], thenRun: str = None, runArgs: list = None):
		if components:
			comp = components.pop()
			self.detachTox(comp)
			self.detachDats(comp)
			if components:
				self.queueMethodCall('processComponents_stage', components, thenRun, runArgs)
				return
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperators(self, comp: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing operators {comp}')
		self.detachTox(comp)
		categories = comp.findChildren(type=baseCOMP)
		self.queueMethodCall('processOperatorCategories_stage', categories, thenRun, runArgs)

	def freezeOperatorTable(self, toolkit: 'COMP'):
		self.log('Freezing operator table')
		table = toolkit.op('opTable')
		if table:
			table.lock = True

	def processOperatorCategories_stage(self, categories: List['COMP'], thenRun: str = None, runArgs: list = None):
		if categories:
			category = categories.pop()
			self.processOperatorCategory(category, thenRun='processOperatorCategories_stage', runArgs=[categories, thenRun, runArgs])
		elif thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def processOperatorCategory(self, category: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Processing operator category {category.name}')
		comps = category.findChildren(type=baseCOMP)
		self.queueMethodCall('processOperatorCategory_stage', comps, thenRun, runArgs)

	def processOperatorCategory_stage(self, components: List['COMP'], thenRun: str = None, runArgs: list = None):
		if components:
			comp = components.pop()
			self.processOperator(comp)
			if components:
				self.queueMethodCall('processOperatorCategory_stage', components, thenRun, runArgs)
				return
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

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
		if not dat.par.file and dat.par.file.mode == ParMode.CONSTANT:
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

	def queueMethodCall(self, method: str, *args):
		if '.' in method:
			run(method, *args, delayFrames=5, delayRef=root)
		else:
			run(f'args[0].{method}(*(args[1:]))', self, *args, delayFrames=5, delayRef=root)

def getChildComps(comp: 'COMP'):
	return comp.findChildren(type=COMP, maxDepth=1) if comp else []
