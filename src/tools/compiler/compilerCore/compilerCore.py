from dataclasses import dataclass, field
from enum import Enum
from raytkUtil import ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from src.components.inspectorCore.inspectorCoreExt import InspectorCore

	class _CompilerCorePars:
		Sceneconfig: OPParamT

	class _SceneConfigPars:
		Paramsop: OPParamT
		Renderer: OPParamT

	iop.inspectorCore = InspectorCore(COMP())
	ipar.inspectorCore = InspectorCore(COMP()).state

class CompilerCore:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp
		# noinspection PyUnreachableCode
		if False:
			self.ownerComp.par = _SceneConfigPars()
		self.inspectorCore = iop.inspectorCore  # type: InspectorCore | COMP

	def Reset(self, _=None):
		self.inspectorCore.Reset()

	def Load(self, o: OP):
		self.inspectorCore.Inspect(o)

	@property
	def OutputOP(self) -> COMP | None:
		return self.inspectorCore.TargetComp

	@property
	def OutputOPInfo(self):
		return ROPInfo(self.OutputOP)

	def _originalShaderBuilderPar(self, name: str) -> Par | None:
		o = self.OutputOP
		builder = o and o.op('shaderBuilder')
		return builder and builder.par[name]

	def originalShaderBuilderPar(self, name: str):
		p = self._originalShaderBuilderPar(name)
		return None if p is None else p.eval()

	def originalShaderBuilderParOPs(self, name: str):
		p = self._originalShaderBuilderPar(name)
		return None if p is None else p.evalOPs()

	def processShaderCode(self, code: str) -> str:
		# TODO: EVERYTHING!
		return code

	@staticmethod
	def _analyzeROP(rop: COMP):
		info = ROPInfo(rop)
		result = _ROPCompileInfo(ropInfo=info)

		# TODO: check for CHOP-based parameters
		# TODO: check for textures
		# TODO: check for buffer CHOPs
		# TODO: check for problematic macros
		# TODO: ...??
		return result

# class _ParamMappingType(Enum):
# 	single = 'single'
# 	expanded = 'expanded'
#
# @dataclass
# class _ParamCompileInfo:
# 	globalName: str
# 	par: Optional[Par]
# 	tuplet: Optional[ParTuple]
# 	isAngle: bool = False
# 	readOnly: bool = False
# 	supported: bool = True

@dataclass
class _ROPCompileInfo:
	ropInfo: ROPInfo
	constantPars: list[Par] = field(default_factory=list)
	menuPars: list[Par] = field(default_factory=list)
	variablePars: list[Par] = field(default_factory=list)
	anglePars: list[Par] = field(default_factory=list)
	errors: list[str] = field(default_factory=list)
