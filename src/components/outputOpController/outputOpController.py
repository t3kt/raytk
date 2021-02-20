from typing import List

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
		host = self.ownerComp.par.Hostop.eval()
		if not host:
			raise Exception('No host attached to output op controller')
		return host

	def _opDef(self) -> 'Optional[COMP]':
		return self.ownerComp.par.Opdef.eval()

	def _renderTop(self) -> 'Optional[glslmultiTOP]':
		return self.ownerComp.par.Rendertop.eval()

	def onInit(self):
		self.updateTextureInputs()
		self.resetInfoParams()

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
		for conn in renderTop.inputConnectors:
			while conn.connections:
				conn.disconnect()
		fixedInputs = self.ownerComp.par.Fixedtexinputs.evalOPs()  # type: List[TOP]
		if fixedInputs:
			for inputTop in fixedInputs:
				if inputTop:
					inputTop.outputConnectors[0].connect(renderTop)
		host = self._host()
		host.clearScriptErrors(error='texerr*')
		texSources = self.ownerComp.op('textureSources')  # type: DAT
		selectors = self.ownerComp.par.Texselectors.evalOPs()  # type: List[TOP]
		for i in range(texSources.numRows):
			if i >= len(selectors):
				host.addScriptError(f'texerr: Too many texture sources (failed on #{i})')
				return
			select = selectors[i]
			while select.outputConnectors[0].connections:
				select.outputConnectors[0].disconnect()
			select.outputConnectors[0].connect(renderTop)
