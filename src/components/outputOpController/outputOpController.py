from typing import List, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Par:
		Hostop: 'OPParamT'
		Opdef: 'OPParamT'
		Rendertop: 'OPParamT'
		Shaderbuilder: 'OPParamT'

	class _COMP(COMP):
		par: _Par

class OutputOp:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	def _host(self) -> COMP | None:
		return self.ownerComp.par.Hostop.eval()

	def _opDef(self) -> COMP | None:
		return self.ownerComp.par.Opdef.eval()

	def _renderTop(self) -> 'Optional[glslmultiTOP]':
		return self.ownerComp.par.Rendertop.eval()

	def onInit(self):
		self.resetInfoParams()
		self.updateConstantParams()

	def resetInfoParams(self):
		host = self._host()
		if not host:
			return
		for par in host.customPars:
			if par.page == 'Info' and not par.readOnly and not par:
				par.val = par.default

	def updateConstantParams(self):
		renderTop = self._renderTop()
		if not renderTop:
			return
		table = self.ownerComp.op('uniforms')
		if table.numRows < 2:
			return
		count = 0
		for i in range(1, table.numRows):
			if table[i, 'uniformType'] == 'constant':
				count += 1
		sequence = renderTop.par.const0name.sequence  # type: Sequence
		if count > sequence.numBlocks:
			sequence.numBlocks = count
