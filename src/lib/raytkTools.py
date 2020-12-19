from raytkDocs import OpDocManager
from raytkUtil import RaytkContext, ROPInfo, focusCustomParameterPage

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class RaytkTools(RaytkContext):
	def generateROPType(self, comp: 'COMP'):
		info = ROPInfo(comp)
		if not info.isMaster:
			raise Exception('ROP is not proper master')
		path = self.toolkit().relativePath(comp)
		if path.startswith('./'):
			path = path[2:]
		return 'raytk.' + path.replace('/', '.')

	def updateROPMetadata(self, rop: 'COMP', incrementVersion=False):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		info.opDefPar.enablecloningpulse.pulse()
		currentOpType = info.opType
		currentOpVersion = info.opVersion
		newType = self.generateROPType(rop)
		info.opType = newType
		if not currentOpVersion or not currentOpType or currentOpType != newType:
			versionVal = 0
		else:
			versionVal = currentOpVersion
			if incrementVersion:
				versionVal = int(versionVal) + 1
		info.opVersion = versionVal
		info.toolkitVersion = self.toolkitVersion()
		info.helpUrl = f'https://t3kt.github.io/raytk/reference/opType/{info.opType}/'

	@staticmethod
	def updateROPParams(rop: 'COMP'):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			return
		if rop.customPages:
			page = rop.customPages[0]
		else:
			page = rop.appendCustomPage('Settings')

		# Set up Enable par
		if info.isROP and info.hasROPInputs and not info.isOutput:
			enablePar = rop.par['Enable']
			if enablePar is None:
				enablePar = page.appendToggle('Enable')[0]
				enablePar.val = True
			enablePar.order = -1
			enablePar.default = True
			if info.opDefPar and not info.opDefPar.Enable.expr:
				info.opDefPar.Enable.expr = "op('..').par.Enable"

		# Set up inspect par
		inspectPar = rop.par['Inspect']
		if info.supportsInspect:
			if inspectPar is None:
				inspectPar = page.appendPulse('Inspect')[0]
			inspectPar.startSection = True
			inspectPar.order = 888
		elif inspectPar is not None:
			inspectPar.destroy()

		# Set up help trigger par
		helpPar = rop.par['Help']
		if info.helpUrl:
			if helpPar is None:
				helpPar = page.appendPulse('Help')[0]
			helpPar.startSection = True
			helpPar.order = 999
		elif helpPar is not None:
			helpPar.destroy()

	def saveROP(self, rop: 'COMP', incrementVersion=False):
		info = ROPInfo(rop)
		if not info or not info.isMaster:
			# TODO: warning?
			return
		self.updateROPMetadata(rop, incrementVersion)
		self.updateROPParams(rop)
		OpDocManager(info).pushToParamsAndInputs()
		focusCustomParameterPage(rop, 0)
		tox = info.toxFile
		rop.save(tox)
		ui.status = f'Saved TOX {tox} (version: {info.opVersion})'


