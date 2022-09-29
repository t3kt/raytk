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
		Fixedtexinputs: 'StrParamT'
		Texselectors: 'StrParamT'

	class _COMP(COMP):
		par: _Par

class OutputOp:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	def _host(self) -> 'Optional[COMP]':
		return self.ownerComp.par.Hostop.eval()

	def _opDef(self) -> 'Optional[COMP]':
		return self.ownerComp.par.Opdef.eval()

	def _renderTop(self) -> 'Optional[glslmultiTOP]':
		return self.ownerComp.par.Rendertop.eval()

	def onInit(self):
		self.updateTextureInputs()
		self.resetInfoParams()
		self.updateConstantParams()

	def resetInfoParams(self):
		host = self._host()
		if not host:
			return
		for par in host.customPars:
			if par.page == 'Info' and not par.readOnly and not par:
				par.val = par.default

	def updateTextureInputs(self):
		renderTop = self._renderTop()
		if not renderTop:
			return
		inputs = self.ownerComp.par.Fixedtexinputs.evalOPs()  # type: List[TOP]
		host = self._host()
		host.clearScriptErrors(error='texerr*')
		texSources = self.ownerComp.op('textureSources')  # type: DAT
		selectors = self.ownerComp.par.Texselectors.evalOPs()  # type: List[TOP]
		for i in range(texSources.numRows):
			if i >= len(selectors):
				host.addScriptError(f'texerr: Too many texture sources (failed on #{i})')
				return
			inputs.append(selectors[i])
		renderTop.setInputs(inputs)

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
		sequence = renderTop.par.constname0.sequence  # type: Sequence
		if count > sequence.numBlocks:
			sequence.numBlocks = count
