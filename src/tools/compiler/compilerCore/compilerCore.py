from dataclasses import dataclass, field
from enum import Enum
from raytkUtil import ROPInfo
from typing import List, Union, Optional

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

	def _originalShaderBuilderPar(self, name: str) -> 'Optional[Par]':
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
	def _analyzeROP(rop: 'COMP'):
		info = ROPInfo(rop)
		result = _ROPCompileInfo(ropInfo=info)

		paramTupletTable = info.opDef.op('param_tuplets')
		# tuplet,  source (param|special),  size,  part1, part2, part3, part4, status (readOnly|''), conversion (angle|'')
		name = info.opDefPar.Name.eval()
		prefix = name + '_'
		for i in range(1, paramTupletTable.numRows):
			tupletName = str(paramTupletTable[i, 'tuplet']).replace(prefix, '')
			if paramTupletTable[i, 'source'] != 'param':
				result.errors.append(f'Special parameter not supported: {tupletName}')
			else:
				par1 = rop.par[paramTupletTable[i, 'part1']]
				if paramTupletTable[i, 'status'] == 'readOnly':
					result.constantPars += par1.tuplet
				else:
					result.variablePars += par1.tuplet
				if par1.isMenu:
					result.menuPars.append(par1)
				if paramTupletTable[i, 'convesrion'] == 'angle':
					result.anglePars += par1.tuplet
			pass

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
	constantPars: List[Par] = field(default_factory=list)
	menuPars: List[Par] = field(default_factory=list)
	variablePars: List[Par] = field(default_factory=list)
	anglePars: List[Par] = field(default_factory=list)
	errors: List[str] = field(default_factory=list)
