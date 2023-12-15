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

	def _renderTop(self) -> glslmultiTOP | None:
		return self.ownerComp.par.Rendertop.eval()

	def onInit(self):
		self.resetInfoParams()
		self.updateParamSequences()

	def onUniformsChange(self):
		self.updateParamSequences()

	def resetInfoParams(self):
		host = self._host()
		if not host:
			return
		for par in host.customPars:
			if par.page == 'Info' and not par.readOnly and not par:
				par.val = par.default

	def updateParamSequences(self):
		renderTop = self._renderTop()
		if not renderTop:
			return
		table = self.ownerComp.op('uniforms')
		if table.numRows < 2:
			return
		constCount = 0
		arrayCount = 0
		for i in range(1, table.numRows):
			if table[i, 'uniformType'] == 'constant':
				constCount += 1
			elif table[i, 'uniformType'] == 'uniformarray':
				arrayCount += 1
		sequence = renderTop.par.const0name.sequence  # type: Sequence
		if constCount > sequence.numBlocks:
			sequence.numBlocks = constCount
		sequence = renderTop.par.chop0uniname.sequence
		if arrayCount > sequence.numBlocks:
			sequence.numBlocks = arrayCount
