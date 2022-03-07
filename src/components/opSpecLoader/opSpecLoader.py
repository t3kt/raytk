from raytkModel import ROPSpec, ROPDef, ROPMeta
from raytkUtil import ROPInfo
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Pars:
		Hostop: OPParamT
		Specfile: StrParamT
		Enable: BoolParamT
		Enablepush: BoolParamT
		Enablepull: BoolParamT

	class _Comp(COMP):
		par: _Pars

class OpSpecLoader:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _Comp

	def _parseSpec(self) -> Optional[ROPSpec]:
		text = self.ownerComp.op('spec').text
		if not text:
			return None
		return ROPSpec.parseFromText(text)

	def pushToOps(self):
		ropInfo = ROPInfo(self.ownerComp.par.Hostop.eval())
		if not ropInfo:
			debug(f'Unable to push with invalid host: {self.ownerComp.par.Hostop.eval()!r}')
			return
		spec = self._parseSpec()
		if not spec:
			debug('Unable to push with missing/invalid spec')
			return
		if spec.opDef:
			spec.opDef.applyToComp(ropInfo.opDef)
		if spec.meta:
			spec.meta.applyToRopInfo(ropInfo)
		# TODO: inputs, params, etc.

	def pullFromOps(self):
		ropInfo = ROPInfo(self.ownerComp.par.Hostop.eval())
		if not ropInfo:
			debug(f'Unable to pull with invalid host: {self.ownerComp.par.Hostop.eval()!r}')
			return
		spec = self._parseSpec() or ROPSpec()
		if not spec.opDef:
			spec.opDef = ROPDef()
		spec.opDef.updateFromComp(ropInfo.opDef)
		if not spec.meta:
			spec.meta = ROPMeta()
		spec.meta.updateFromRopInfo(ropInfo)
		# TODO: inputs, params, etc.
		dat = self.ownerComp.op('spec')
		dat.clear()
		dat.write(spec.toYamlText())

	def Push(self, _=None):
		if not self.ownerComp.par.Enable or not self.ownerComp.par.Enablepush:
			return
		self.pushToOps()

	def Pull(self, _=None):
		if not self.ownerComp.par.Enable or not self.ownerComp.par.Enablepull:
			return
		self.pullFromOps()
