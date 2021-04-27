from raytkUtil import ROPInfo, InputInfo
from raytkModel import extractOpSpec
from typing import Optional
import yaml

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _InspectorCorePars(ParCollection):
		Hastarget: 'BoolParamT'
		Definitiontable: 'DatParamT'
		Targetcomp: 'CompParamT'
	ipar.inspectorCore = _InspectorCorePars()

	class _StatePar(ParCollection):
		Includeparams: 'BoolParamT'
	ipar.specPanelState = _StatePar()

class SpecPanel:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def generateSpec(self) -> Optional[str]:
		info = ROPInfo(ipar.inspectorCore.Targetcomp)
		if not info:
			return None
		spec = extractOpSpec(info.rop, skipParams=not ipar.specPanelState.Includeparams)
		return yaml.dump(spec, default_style='')

	def Update(self):
		self.ownerComp.op('generateSpec').cook(force=True)

