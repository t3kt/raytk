from raytkUtil import ROPInfo
from typing import Union

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
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		# noinspection PyUnreachableCode
		if False:
			self.ownerComp.par = _SceneConfigPars()
		self.inspectorCore = iop.inspectorCore  # type: Union[InspectorCore, COMP]

	def Reset(self, _=None):
		self.inspectorCore.Reset()

	def Load(self, o: 'OP'):
		self.inspectorCore.Inspect(o)

	@property
	def OutputOP(self) -> 'Optional[COMP]':
		return self.inspectorCore.TargetComp

	@property
	def OutputOPInfo(self):
		return ROPInfo(self.OutputOP)

	def originalShaderBuilderPar(self, name: str):
		o = self.OutputOP
		builder = o and o.op('shaderBuilder')
		p = builder and builder.par[name]
		return None if p is None else p.eval()

	def originalShaderBuilderParOPs(self, name: str):
		o = self.OutputOP
		builder = o and o.op('shaderBuilder')
		p = builder and builder.par[name]
		return None if p is None else p.evalOPs()

	def processShaderCode(self, code: str) -> str:
		# TODO: EVERYTHING!
		return code
