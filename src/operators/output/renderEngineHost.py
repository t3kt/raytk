import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class RenderEngineController:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp
		self.engine = op('engine')  # type: COMP
		self.host = parent()  # type: COMP

	def renderer(self) -> COMP | None:
		return self.host.par.Renderer.eval()

	def Attach(self):
		rnd = self.renderer()
		if not rnd:
			self.Detach()
			return
		self.engine.par.reload.pulse()

	def InitializeEngine(self):
		print(f'Initializing engine: {self.engine}')
		sourceNames = (
			'shaderCode', 'uniforms', 'textureSources',
			'vectorParamVals', 'constantParamVals',
			'primaryImage',
			'testCode',
		)
		for conn in self.engine.inputConnectors:
			name = conn.inOP.name.removesuffix('_in')
			if name in sourceNames:
				conn.connect(op(name))
		self.engine.par.Outputbuffercount.expr = "op('outputBuffers').numRows - 1"
		self.engine.par.Resolution1.expr = "parent().par.Renderer.eval().par.Resx if parent().par.Renderer else 256"
		self.engine.par.Resolution2.expr = "parent().par.Renderer.eval().par.Resy if parent().par.Renderer else 256"
		self.engine.par.Formatindex.expr = "int(parent().par.Renderer.eval().par.Format) if parent().par.Renderer else 0"
		self.engine.par.Useinputresolution.expr = "parent().par.Renderer.eval().op('shaderExecutor').par.Useinputresolution if parent().par.Renderer else 0"
		self.engine.par.Inputfiltertypeindex.expr = "parent().par.Renderer.eval().op('shaderExecutor').par.Inputfiltertype if parent().par.Renderer else 0"
		self.engine.par.Filtertypeindex.expr = "parent().par.Renderer.eval().op('shaderExecutor').par.Filtertype if parent().par.Renderer else 0"

	def Detach(self):
		self.engine.par.unload.pulse()
		pass

	def InlineLibraryIncludes(self, code: str):
		if not code:
			return ''

		def replacer(m: re.Match):
			path = m.group(1)
			dat = op(path)
			result = f'/// Library: <{path}>\n'
			if dat:
				result += dat.text
			else:
				# TODO: report missing library
				result += '/////// MISSING!!!! /////'
			return result + '\n'

		return re.sub(r'#include\s+<([^>]+)>', replacer, code)

