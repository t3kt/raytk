from raytkTools import RaytkTools

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .ropEditor.ropEditor import ROPEditor
	# noinspection PyTypeHints
	iop.ropEditor = ROPEditor(COMP())  # type: ROPEditor | COMP


class ToolkitEditor:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp
	
	def Open(self, _=None):
		op('window').par.winopen.pulse()

	def EditROP(self, rop: COMP):
		self.Open()
		iop.ropEditor.LoadROP(rop)

	@staticmethod
	def saveAllROPSpecs():
		RaytkTools().saveAllROPSpecs()

	def saveAllROPs(self, incrementVersion):
		RaytkTools().saveAllROPs(incrementVersion)

	def updateAllShaderLibraries(self):
		for area in ops('/raytk', '/devel', '/toolkitEditor'):
			if not area:
				continue
			for comp in area.findChildren(name='shaderLibraries'):
				for dat in comp.findChildren(type=DAT, depth=1):
					if dat.par['syncfile'] or dat.par['loadonstartpulse'] is None:
						continue
					dat.par.loadonstartpulse.pulse()
