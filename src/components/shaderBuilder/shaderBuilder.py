from dataclasses import dataclass
from raytkUtil import RaytkContext, simplifyNames
import re
from typing import Callable, Dict, List, Set, Tuple, Union, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _ConfigPar(ParCollection):
		Parammode: StrParamT
		Inlineparameteraliases: BoolParamT
		Inlinereadonlyparameters: BoolParamT
		Simplifynames: BoolParamT
		Inlinetypedefs: BoolParamT
		Includemode: StrParamT
		Filtermode: StrParamT

	class _OwnerCompPar(_ConfigPar):
		Globalprefix: DatParamT
		Predeclarations: DatParamT
		Textureindexoffset: IntParamT
		Globalmacrotable: DatParamT
		Libraries: StrParamT
		Bodytemplate: DatParamT
		Outputbuffertable: DatParamT
		Supportmaterials: BoolParamT
		Shaderbuilderconfig: CompParamT
		Shadertype: StrParamT

	class _OwnerComp(COMP):
		par: '_OwnerCompPar'

	class _ConfigComp(COMP):
		par: '_ConfigPar'

class ShaderBuilder:
	def __init__(self, ownerComp: 'Union[_OwnerComp, COMP]'):
		self.ownerComp = ownerComp

	def _config(self) -> '_ConfigComp':
		o = self.ownerComp.par.Shaderbuilderconfig.eval()
		# noinspection PyTypeChecker
		return o or self.ownerComp.op('default_shaderBuilderConfig')

	def configPar(self) -> '_ConfigPar':
		return self._config().par

	def Createcustomconfig(self, _=None):
		hostPar = self.ownerComp.par.Shaderbuilderconfig.bindMaster
		if hostPar is None or not isinstance(hostPar, Par):
			raise Exception('Invalid setup for Shaderbuilderconfig par, must be a parameter binding')
		if hostPar.eval():
			msg = f'Operator already has custom Shaderbuilderconfig: {hostPar.owner}'
			print(msg)
			ui.status = msg
			return
		template = self._config()
		host = hostPar.owner
		ui.undo.startBlock('Customize shader config')
		config = host.parent().copy(template, name=host.name + '_shaderConfig')
		config.nodeX = host.nodeX
		config.nodeY = host.nodeY - 150
		config.dock = host
		host.showDocked = True
		for par in config.customPars:
			if par.mode == ParMode.EXPRESSION:
				par.expr = ''
				par.val = template.par[par.name].eval()
		hostPar.val = config.name
		ui.undo.endBlock()

	def preprocessDefinitions(self, dat: 'scriptDAT'):
		# BEFORE definitions are reversed, so a def's inputs are always BELOW it in the table
		pass

	def _definitionTable(self) -> 'DAT':
		# in reverse order (aka declaration order)
		return self.ownerComp.op('definitions')

	def _parameterDetailTable(self) -> 'DAT':
		return self.ownerComp.op('param_details')

	def _outputBufferTable(self) -> 'DAT':
		return self.ownerComp.op('output_buffer_table')

	def _allParamVals(self) -> 'CHOP':
		return self.ownerComp.op('all_param_vals')

	def buildNameReplacementTable(self, dat: 'scriptDAT'):
		dat.clear()
		dat.appendRow(['before', 'after'])
		if not self.configPar().Simplifynames:
			return
		origNames = [c.val for c in self._definitionTable().col('name')[1:]]
		simpleNames = simplifyNames(origNames)
		if simpleNames == origNames:
			return
		dat.clear()
		dat.appendCol(['before'] + origNames)
		dat.appendCol(['after'] + simpleNames)

	def buildGlobalPrefix(self):
		return wrapCodeSection(self.ownerComp.par.Globalprefix.eval(), 'globalPrefix')

	def _createParamProcessor(self) -> '_ParameterProcessor':
		mode = self.configPar().Parammode.eval()
		if mode == 'uniformarray':
			return _VectorArrayParameterProcessor(
				self._parameterDetailTable(),
				self._allParamVals(),
				self.configPar(),
			)
		elif mode == 'separateuniforms':
			return _SeparateUniformsParameterProcessor(
				self._parameterDetailTable(),
				self._allParamVals(),
				self.configPar(),
			)
		else:
			raise NotImplementedError(f'Parameter processor not available for mode: {mode!r}')

	def buildGlobalDeclarations(self):
		defsTable = self._definitionTable()
		if defsTable.numRows < 2:
			code = ['#error No input definition']
		else:
			mainName = defsTable[-1, 'name']
			paramProcessor = self._createParamProcessor()
			code = paramProcessor.globalDeclarations()
			code += [
				f'#define thismap {mainName}'
			]
		return wrapCodeSection(code, 'globals')

	def getOpsFromDefinitionColumn(self, column: str):
		defsTable = self._definitionTable()
		if defsTable.numRows < 2 or not defsTable[0, column]:
			return []
		results = []
		for cell in defsTable.col(column)[1:]:
			if not cell.val.strip():
				continue
			paths = cell.val.strip().split(' ')
			for path in paths:
				o = op(path)
				if o:
					results.append(o)
		return results

	def buildMacroTable(self, dat: 'DAT'):
		dat.clear()
		tables = [self.ownerComp.par.Globalmacrotable.eval()]
		tables += self.getOpsFromDefinitionColumn('macroTable')
		for table in tables:
			if not table or not table.numRows:
				continue
			for row in range(table.numRows):
				if table.numCols == 3:
					if table[row, 0] in ('0', 'False'):
						continue
					name = table[row, 1].val.strip()
					if name:
						dat.appendRow([name, table[row, 2]])
				else:
					name = table[row, 0].val.strip()
					if not name:
						continue
					dat.appendRow([name, table[row, 1] if table.numCols > 1 else ''])
		outputBufferTable = self._outputBufferTable()
		for row in range(1, outputBufferTable.numRows):
			name = outputBufferTable[row, 'macro'].val.strip()
			if name:
				dat.appendRow([name, ''])

	@staticmethod
	def buildMacroBlock(macroTable: 'DAT'):
		decls = [
			f'#define {macroTable[i, 0]} {macroTable[i, 1]}'
			for i in range(macroTable.numRows)
		]
		decls = _uniqueList(decls)
		code = wrapCodeSection(decls, 'macros')
		# if self.configPar().Inlineparameteraliases:
		# 	processor = self._createParamProcessor()
		# 	return processor.processCodeBlock(code)
		return code

	def _getLibraryDats(self, onWarning: Callable[[str], None] = None) -> 'List[DAT]':
		requiredLibNames = self.ownerComp.par.Librarynames.eval().strip().split(' ')  # type: List[str]
		requiredLibNames = [n for n in requiredLibNames if n]
		defsTable = self._definitionTable()
		if defsTable[0, 'libraryNames']:
			for cell in defsTable.col('libraryNames')[1:]:
				if not cell.val:
					continue
				for name in cell.val.split(' '):
					if name not in requiredLibNames:
						requiredLibNames.append(name)
		libraryOps = self.ownerComp.par.Libraries.evalOPs()
		dats = []  # type: List[DAT]
		for libraryOp in libraryOps:
			if libraryOp.isDAT:
				if libraryOp not in dats:
					dats.append(libraryOp)
			elif libraryOp.isCOMP:
				namesToRemove = []
				for name in requiredLibNames:
					if name.startswith('/'):
						# This is a full library DAT path, not a name, so it's handled in the next loop
						continue
					dat = libraryOp.op(name)
					if not dat:
						continue
					dats.append(dat)
					namesToRemove.append(name)
				for name in namesToRemove:
					requiredLibNames.remove(name)
		namesToRemove = []
		for libraryPath in requiredLibNames:
			if not libraryPath.startswith('/'):
				continue
			dat = op(libraryPath)
			if dat:
				dats.append(dat)
				namesToRemove.append(libraryPath)
		for name in namesToRemove:
			requiredLibNames.remove(name)
		if requiredLibNames and onWarning:
			onWarning('Missing libraries: ' + repr(requiredLibNames))
		dedupedDats = []
		libraryTexts = set()
		for dat in dats:
			if dat.text in libraryTexts:
				continue
			libraryTexts.add(dat.text)
			dedupedDats.append(dat)
		dats = dedupedDats
		return dats

	def buildLibraryIncludes(self, onWarning: Callable[[str], None] = None):
		mode = str(self.configPar()['Includemode'] or 'includelibs')
		supportsInclude = self.ownerComp.op('support_table')['include', 1] == '1'
		if mode == 'includelibs' and not supportsInclude:
			inlineAll = True
		else:
			inlineAll = mode == 'inlineall'
		libraries = self._getLibraryDats(onWarning)
		if inlineAll:
			libBlocks = [
				f'// Library: <{lib.path}>\n{lib.text}'
				for lib in libraries
			]
		else:
			libBlocks = [
				f'#include <{lib.path}>'
				for lib in libraries
			]
		return wrapCodeSection(libBlocks, 'libraries')

	def buildOpDataTypedefBlock(self, typeDefMacroTable: 'DAT'):
		inline = self.configPar()['Inlinetypedefs']
		if typeDefMacroTable.numRows:
			typedefs = {}
			macros = {}
			for cells in typeDefMacroTable.rows():
				if cells[2] == 'typedef':
					typedefs[cells[0].val] = cells[1].val
				else:
					macros[cells[0].val] = cells[1].val
			lines = []
			if not inline:
				# Primary typedef macros are not needed when they're being inlined
				lines += [
					f'#define {name}  {val}'
					for name, val in typedefs.items()
				]
			# Macros like FOO_COORD_TYPE_float are always needed
			lines += [
				f'#define {name}'
				for name, val in macros.items()
				if val == ''
			]
			if not inline:
				# Replacement macros like FOO_asCoordT are not needed when they're being inlined
				lines += [
					f'#define {name} {val}'
					for name, val in macros.items()
					if val != ''
				]
		else:
			lines = []
		return wrapCodeSection(lines, 'opDataTypedefs')

	def buildTypedefMacroTable(self, dat: 'scriptDAT'):
		dat.clear()
		defsTable = self._definitionTable()
		coordTypeAdaptFuncs = {
			'float': 'adaptAsFloat',
			'vec2': 'adaptAsVec2',
			'vec3': 'adaptAsVec3',
		}
		returnTypeAdaptFuncs = {
			'float': 'adaptAsFloat',
			'vec4': 'adaptAsVec4',
			'Sdf': 'adaptAsSdf',
		}
		for row in range(1, defsTable.numRows):
			name = str(defsTable[row, 'name'])
			coordType = str(defsTable[row, 'coordType'])
			contextType = str(defsTable[row, 'contextType'])
			returnType = str(defsTable[row, 'returnType'])
			dat.appendRow([name + '_CoordT',  coordType, 'typedef'])
			dat.appendRow([name + '_ContextT',  contextType, 'typedef'])
			dat.appendRow([name + '_ReturnT',  returnType, 'typedef'])
			dat.appendRow([name + '_COORD_TYPE_' + coordType, '', 'macro'])
			dat.appendRow([name + '_CONTEXT_TYPE_' + contextType, '', 'macro'])
			dat.appendRow([name + '_RETURN_TYPE_' + returnType, '', 'macro'])
			if coordType in coordTypeAdaptFuncs:
				dat.appendRow([name + '_asCoordT', coordTypeAdaptFuncs[coordType], 'macro'])
			if returnType in returnTypeAdaptFuncs:
				dat.appendRow([name + '_asReturnT', returnTypeAdaptFuncs[returnType], 'macro'])

	def inlineTypedefs(self, code: str, typeDefMacroTable: 'DAT') -> str:
		if not self.configPar()['Inlinetypedefs']:
			return code
		if not typeDefMacroTable.numRows:
			return code

		replacements = {
			str(cells[0]): str(cells[1])
			for cells in typeDefMacroTable.rows()
		}

		def replace(m: re.Match):
			return replacements.get(m.group(0)) or m.group(0)

		pattern = r'\b[\w_]+_(as)?(CoordT|ContextT|ReturnT)\b'

		code = re.sub(pattern, replace, code)

		return code

	def _createCodeFilter(self, typeDefMacroTable: 'DAT') -> '_CodeFilter':
		mode = self.configPar()['Filtermode']
		if mode == 'filter':
			return _CodeReducerFilter(
				macroTable=self.ownerComp.op('macroTable'),
				typeDefMacroTable=typeDefMacroTable,
			)
		else:  # macroize
			return _CodeMacroizerFilter()

	def filterCode(self, code: str, typeDefMacroTable: 'DAT') -> str:
		if not code:
			return ''
		if '#pragma' not in code:
			return code
		filt = self._createCodeFilter(typeDefMacroTable)
		return filt.processCodeBlock(code)

	def buildPredeclarations(self):
		return wrapCodeSection(self.ownerComp.par.Predeclarations.eval(), 'predeclarations')

	def buildParameterAliases(self):
		paramProcessor = self._createParamProcessor()
		decls = paramProcessor.paramAliases()
		return wrapCodeSection(decls, 'paramAliases')

	def processParametersInCode(self, code: str):
		paramProcessor = self._createParamProcessor()
		return paramProcessor.processCodeBlock(code)

	def buildTextureDeclarations(self):
		textureTable = self.ownerComp.op('texture_table')
		offset = int(self.ownerComp.par.Textureindexoffset)
		indexByType: 'Dict[str, int]' = {
			'2d': offset,
			'3d': 0,
			'cube': 0,
			'2darray': 0,
		}
		arrayByType = {
			'2d': 'sTD2DInputs',
			'3d': 'sTD3DInputs',
			'cube': 'sTDCubeInputs',
			'2darray': 'sTD2DArrayInputs',
		}
		infoByType = {
			'2d': 'uTD2DInfos',
			'3d': 'uTD3DInfos',
			'cube': 'uTDCubeInfos',
			'2darray': 'uTD2DArrayInfos',
		}
		decls = []
		for i in range(1, textureTable.numRows):
			name = str(textureTable[i, 'name'])
			texType = str(textureTable[i, 'type'] or '2d')
			if texType not in indexByType:
				raise Exception(f'Invalid texture type for {name}: {texType!r}')
			index = indexByType[texType]
			decls.append(f'#define {name} {arrayByType[texType]}[{index}]')
			decls.append(f'#define {name}_info {infoByType[texType]}[{index}]')
			indexByType[texType] = index + 1
		return wrapCodeSection(decls, 'textures')

	def buildBufferDeclarations(self):
		bufferTable = self.ownerComp.op('buffer_table')
		decls = []
		for i in range(1, bufferTable.numRows):
			name = bufferTable[i, 'name']
			dataType = bufferTable[i, 'type']
			uniType = bufferTable[i, 'uniformType']
			if uniType == 'uniformarray':
				lengthVal = str(bufferTable[i, 'length'] or '')
				if lengthVal == '':
					c = op(bufferTable[i, 'chop'])
					n = c.numSamples if c else 1
				else:
					n = int(lengthVal)
				decls.append(f'uniform {dataType} {name}[{n}];')
			elif uniType == 'texturebuffer':
				decls.append(f'uniform samplerBuffer {name};')
			else:
				raise Exception(f'Invalid uniform type: {uniType}')
		return wrapCodeSection(decls, 'buffers')

	def buildMaterialDeclarations(self):
		if not self.ownerComp.par.Supportmaterials:
			return ' '
		materialTable = self.ownerComp.op('material_table')
		if materialTable.numRows < 2:
			return ' '
		i = 1001
		decls = []
		for name in materialTable.col('material')[1:]:
			decls.append(f'#define {name} {i}')
			i += 1
		return wrapCodeSection(decls, 'materials')

	def buildOutputBufferDeclarations(self):
		outputBufferTable = self._outputBufferTable()
		if outputBufferTable.numRows <= 1:
			return ' '

		outputBuffers = self._outputBufferTable()
		if outputBuffers.numRows < 2:
			return ' '
		if self.ownerComp.par.Shadertype == 'compute':
			decls = [
				f'#define {outputBufferTable[row, "name"]} mTDComputeOutputs[{row - 1}]'
				for row in range(1, outputBufferTable.numRows)
			]
		else:
			decls = [
				f'layout(location = {row - 1}) out vec4 {outputBufferTable[row, "name"]};'
				for row in range(1, outputBufferTable.numRows)
			]

		return wrapCodeSection(decls, 'outputBuffers')

	def buildOutputInitBlock(self):
		outputBuffers = self._outputBufferTable()
		lines = ['void initOutputs() {']
		if self.ownerComp.par.Shadertype != 'compute':
			lines += [
				f'{cell.val} = vec4(0.);'
				for cell in outputBuffers.col('name')[1:]
			]
		return wrapCodeSection(
			lines + ['}'],
			'outputInit',
		)

	def buildOpGlobalsBlock(self):
		dats = self.getOpsFromDefinitionColumn('opGlobalsPath')
		return wrapCodeSection(dats, 'opGlobals')

	def buildInitBlock(self):
		dats = self.getOpsFromDefinitionColumn('initPath')
		code = _combineCode(dats)
		if not code.strip():
			return ' '
		return wrapCodeSection([
			'#define RAYTK_HAS_INIT',
			'void init() {',
			code,
			'}',
		], 'init')

	def buildStageInitBlock(self):
		dats = self.getOpsFromDefinitionColumn('stageInitPath')
		code = _combineCode(dats)
		if not code.strip():
			return ' '
		return wrapCodeSection([
			'#define RAYTK_HAS_STAGE_INIT',
			'void stageInit(int stage) {',
			code,
			'}',
		], 'stageInit')

	def buildFunctionsBlock(self):
		dats = self.getOpsFromDefinitionColumn('functionPath')
		return wrapCodeSection(dats, 'functions')

	def buildBodyBlock(self, materialTable: 'DAT'):
		bodyDat = self.ownerComp.par.Bodytemplate.eval()
		code = bodyDat.text if bodyDat else ''
		if not code:
			return ' '
		placeholder = '// #include <materialParagraph>'
		if placeholder in code:
			materialBlock = self._buildMaterialBlock(materialTable)
			code = code.replace(placeholder, materialBlock, 1)
		return wrapCodeSection(code, 'body')

	@staticmethod
	def _buildMaterialBlock(materialTable: 'DAT'):
		if materialTable.numRows < 2:
			return ''
		output = ''
		for nameCell, pathCell in materialTable.rows()[1:]:
			if not nameCell:
				continue
			codeDat = op(pathCell)
			materialCode = codeDat.text if codeDat else ''
			output += f'else if(m == {nameCell.val}) {{\n'
			output += materialCode + '\n}'
		return output

	def buildValidationErrors(self, dat: 'DAT'):
		dat.clear()
		if RaytkContext().develMode():
			return
		toolkitVersions = {}  # type: Dict[str, int]
		defsTable = self._definitionTable()
		if defsTable.numRows < 2 or not defsTable[0, 'toolkitVersion']:
			return
		for i in range(1, defsTable.numRows):
			version = str(defsTable[i, 'toolkitVersion'] or '')
			if version != '':
				toolkitVersions[version] = 1 + toolkitVersions.get(version, 0)
		if len(toolkitVersions) > 1:
			error = f'Toolkit version mismatch ({", ".join(list(toolkitVersions.keys()))})'
			dat.appendRow(['path', 'level', 'message'])
			dat.appendRow([parent().path, 'warning', error])

	def V2_writeShader(
			self,
			dat: 'scriptDAT',
			macroTable: 'DAT',
			typeDefMacroTable: 'DAT',
			textureTable: 'DAT',
			bufferTable: 'DAT',
			materialTable: 'DAT',
			outputBufferTable: 'DAT',
	):
		writer = _V2_Writer(
			sb=self,
			out=dat,
			defTable=self._definitionTable(),
			paramProc=self._createParamProcessor(),
			codeFilter=self._createCodeFilter(typeDefMacroTable=typeDefMacroTable),
			macroTable=macroTable,
			typeDefMacroTable=typeDefMacroTable,
			libraryDats=self._getLibraryDats(),
			textureTable=textureTable,
			bufferTable=bufferTable,
			materialTable=materialTable,
			outputBufferTable=outputBufferTable,
		)
		writer.run()

def onCook(dat):
	# noinspection PyUnreachableCode
	if False:
		ext.shaderBuilder = ShaderBuilder(COMP())
	ext.shaderBuilder.V2_writeShader(
		dat,
		macroTable=dat.inputs[0],
		typeDefMacroTable=dat.inputs[1],
		textureTable=dat.inputs[2],
		bufferTable=dat.inputs[3],
		materialTable=dat.inputs[4],
		outputBufferTable=dat.inputs[5],
	)

@dataclass
class _V2_Writer:
	sb: 'ShaderBuilder'
	out: 'scriptDAT'
	defTable: 'DAT'
	paramProc: '_ParameterProcessor'
	codeFilter: '_CodeFilter'
	macroTable: 'DAT'
	typeDefMacroTable: 'DAT'
	libraryDats: 'List[DAT]'
	textureTable: 'DAT'
	bufferTable: 'DAT'
	materialTable: 'DAT'
	outputBufferTable: 'DAT'

	inlineTypedefRepls: 'Optional[Dict[str, str]]' = None
	inlineTypedefPattern: 'Optional[re.Pattern]' = None

	def __post_init__(self):
		self.configPar = self.sb.configPar()
		self.ownerComp = self.sb.ownerComp
		if self.configPar['Inlinetypedefs'] and self.typeDefMacroTable.numRows > 1:
			self.inlineTypedefRepls = {
				str(cells[0]): str(cells[1])
				for cells in self.typeDefMacroTable.rows()
				if cells[1]
			}
			self.inlineTypedefPattern = re.compile(r'\b[\w_]+_(as)?(CoordT|ContextT|ReturnT)\b')

	def run(self):
		self.out.clear()
		if self.defTable.numRows < 2:
			self._write('#error No input definition\n')
			return
		self._writeCodeDat('globalPrefix', self.ownerComp.par.Globalprefix.eval())
		self._writeGlobalDecls()
		self._writeOpDataTypedefs()
		self._writeMacroBlock()
		self._writeLibraryIncludes()
		self._writeCodeDat('predeclarations', self.ownerComp.par.Predeclarations.eval())
		self._writeParameterAliases()
		self._writeTextureDeclarations()
		self._writeBufferDeclarations()
		self._writeMaterialDeclarations()
		self._writeOutputBufferDeclarations()


		self._writeOutputInit()
		self._writeOpGlobals()
		self._writeInit()
		self._writeStageInit()
		self._writeFunctions()
		self._writeBody()

	def _writeGlobalDecls(self):
		mainName = self.defTable[-1, 'name']
		self._startBlock('globals')
		self._writeLines(self.paramProc.globalDeclarations())
		self._write(f'#define thismap {mainName}\n')
		self._endBlock('globals')

	def _writeOpDataTypedefs(self):
		inline = self.configPar['Inlinetypedefs']
		if not self.typeDefMacroTable.numRows:
			return
		self._startBlock('opDataTypedefs')
		macros = {}
		for cells in self.typeDefMacroTable.rows():
			if cells[2] == 'typedef':
				if not inline:
					# Primary typedef macros are not needed when they're being inlined
					self._writeMacro(cells[0], cells[1])
			else:
				macros[cells[0].val] = cells[1].val
		# Macros like FOO_COORD_TYPE_float are always needed
		for name, val in macros.items():
			if val == '':
				self._writeMacro(name)
			elif not inline:
				# Replacement macros like FOO_asCoordT are not needed when they're being inlined
				self._writeMacro(name, val)
		self._endBlock('opDataTypedefs')

	def _writeMacroBlock(self):
		if not self.macroTable.numRows:
			return
		self._startBlock('macros')
		decls = set()
		for name, val in self.macroTable.rows():
			nameVal = name.val, val.val
			if nameVal in decls:
				continue
			decls.add(nameVal)
			self._writeMacro(name, val)
		self._endBlock('macros')

	def _writeLibraryIncludes(self):
		if not self.libraryDats:
			return
		self._startBlock('libraries')
		mode = str(self.configPar['Includemode'] or 'includelibs')
		supportsInclude = self.ownerComp.op('support_table')['include', 1] == '1'
		if mode == 'includelibs' and not supportsInclude:
			inlineAll = True
		else:
			inlineAll = mode == 'inlineall'
		if inlineAll:
			for lib in self.libraryDats:
				self._write(f'/// Library: <{lib.path}>\n', lib.text, '\n')
		else:
			for lib in self.libraryDats:
				self._write(f'#include <{lib.path}>\n')
		self._endBlock('libraries')

	def _writeParameterAliases(self):
		decls = self.paramProc.paramAliases()
		if not decls:
			return
		self._startBlock('paramAliases')
		self._writeLines(decls)
		self._endBlock('paramAliases')

	def _writeTextureDeclarations(self):
		if self.textureTable.numRows < 2:
			return
		offset = int(self.ownerComp.par.Textureindexoffset)
		indexByType: 'Dict[str, int]' = {
			'2d': offset,
			'3d': 0,
			'cube': 0,
			'2darray': 0,
		}
		arrayByType = {
			'2d': 'sTD2DInputs',
			'3d': 'sTD3DInputs',
			'cube': 'sTDCubeInputs',
			'2darray': 'sTD2DArrayInputs',
		}
		infoByType = {
			'2d': 'uTD2DInfos',
			'3d': 'uTD3DInfos',
			'cube': 'uTDCubeInfos',
			'2darray': 'uTD2DArrayInfos',
		}
		self._startBlock('textures')
		for name, path, texType in self.textureTable.rows()[1:]:
			texType = texType.val or '2d'
			if texType not in indexByType:
				raise Exception(f'Invalid texture type for {name}: {texType!r}')
			index = indexByType[texType]
			indexByType[texType] = index + 1
			self._writeMacro(name, f'{arrayByType[texType]}[{index}]')
			self._writeMacro(name + '_info', f'{infoByType[texType]}[{index}]')
		self._endBlock('textures')

	def _writeBufferDeclarations(self):
		if self.bufferTable.numRows < 2:
			return
		self._startBlock('buffers')
		for i in range(1, self.bufferTable.numRows):
			name = self.bufferTable[i, 'name']
			dataType = self.bufferTable[i, 'type']
			uniType = self.bufferTable[i, 'uniformType']
			if uniType == 'uniformarray':
				lengthVal = str(self.bufferTable[i, 'length'] or '')
				if lengthVal == '':
					c = op(self.bufferTable[i, 'chop'])
					n = c.numSamples if c else 1
				else:
					n = int(lengthVal)
				self._write(f'uniform {dataType} {name}[{n}];\n')
			elif uniType == 'texturebuffer':
				self._write(f'uniform samplerBuffer {name};\n')
		self._endBlock('buffers')

	def _writeMaterialDeclarations(self):
		if not self.ownerComp.par.Supportmaterials or self.materialTable.numRows < 2:
			return
		self._startBlock('materials')
		for name in self.materialTable.col('material')[1:]:
			self._writeMacro(name, 1001 + (name.row - 1))
		self._endBlock('materials')

	def _writeOutputBufferDeclarations(self):
		if self.outputBufferTable.numRows < 2:
			return
		self._startBlock('outputBuffers')
		if self.ownerComp.par.Shadertype == 'compute':
			for name in self.outputBufferTable.col('name')[1:]:
				self._writeMacro(name, f'mTDComputeOutputs[{name.row}]')
		else:
			for name in self.outputBufferTable.col('name')[1:]:
				self._write(f'layout(location = {name.row - 1}) out vec4 {name};\n')
		self._endBlock('outputBuffers')

	def _writeOutputInit(self):
		if self.ownerComp.par.Shadertype == 'compute' or self.outputBufferTable.numRows < 2:
			return
		self._startBlock('outputInit')
		self._write('void initOutputs() {\n')
		for name in self.outputBufferTable.col('name')[1:]:
			self._write(f'{name} = vec4(0.);\n')
		self._endBlock('outputInit')

	def _writeOpGlobals(self):
		self._writeCodeDatsFromCol('opGlobals', col='opGlobals')

	def _writeInit(self):
		self._writeCodeDatsFromCol(
			'init', col='initPath',
			prefixes=[
				'#define RAYTK_HAS_INIT',
				'void init() {',
			],
			suffixes=['}'],
		)

	def _writeStageInit(self):
		self._writeCodeDatsFromCol(
			'stageInit', col='stageInitPath',
			prefixes=[
				'#define RAYTK_HAS_STAGE_INIT',
				'void stageInit(int stage) {',
			],
			suffixes=['}'],
		)

	def _writeFunctions(self):
		self._writeCodeDatsFromCol('functions', col='functionPath')

	def _writeBody(self):
		dat = self.ownerComp.par.Bodytemplate.eval()
		if not dat:
			return
		self._startBlock('body')
		code = self._inlineTypedefs(dat.text)
		code = self.codeFilter.processCodeBlock(code)
		for line in code.splitlines(keepends=True):
			if line.endswith('// #include <materialParagraph>\n'):
				self._writeMaterialBody()
			else:
				self._write(line)
		self._endBlock('body')

	def _writeMaterialBody(self):
		if self.materialTable.numRows < 2:
			return
		for name, path in self.materialTable.rows()[1:]:
			if not name:
				continue
			self._write(f'else if(m == {name}) {{\n')
			dat = op(path)
			if dat:
				# Intentionally skipping typedef inlining and code filtering for these since no materials need it.
				self._write(dat.text, '\n}')

	def _write(self, *args):
		self.out.write(*args)

	def _writeLines(self, lines: 'Optional[List[str]]'):
		if lines:
			for line in lines:
				self._write(line, '\n')

	def _writeMacro(self, name: 'Union[str, Cell]', val: 'Union[str, Cell, None, int]' = None):
		if val == '' or val is None:
			self._write('#define ', name, '\n')
		else:
			self._write('#define ', name, ' ', val, '\n')

	def _startBlock(self, name: str):
		self._write(f'///----BEGIN {name}\n')

	def _endBlock(self, name: str):
		self._write(f'///----END {name}\n')

	def _writeCodeDat(self, blockName: str, dat: 'Optional[DAT]'):
		if not dat or not dat.text:
			return
		self._startBlock(blockName)
		code = self._inlineTypedefs(dat.text)
		code = self.codeFilter.processCodeBlock(code)
		self._write(code, '\n')
		self._endBlock(blockName)

	def _writeCodeDatsFromCol(
			self, blockName: str, col: str,
			prefixes: 'Optional[List[str]]' = None,
			suffixes: 'Optional[List[str]]' = None,
	):
		dats = self.sb.getOpsFromDefinitionColumn(col)
		if not dats:
			return
		self._startBlock(blockName)
		self._writeLines(prefixes)
		for dat in dats:
			code = self._inlineTypedefs(dat.text)
			code = self.codeFilter.processCodeBlock(code)
			self._write(code, '\n')
		self._writeLines(suffixes)
		self._endBlock(blockName)

	def _replaceInlineTypedefMatch(self, m: 're.Match'):
		return self.inlineTypedefRepls.get(m.group(0)) or m.group(0)

	def _inlineTypedefs(self, code: 'str'):
		if not self.inlineTypedefRepls:
			return code
		return self.inlineTypedefPattern.sub(self._replaceInlineTypedefMatch, code)

	# def _processCodeBlock(self, code: str):
	# 	pass


@dataclass
class _ParamTupletSpec:
	tuplet: str
	parts: Tuple[str]
	isReadOnly: bool

	def isPresentInChop(self, chop: 'CHOP'):
		return any([chop[part] is not None for part in self.parts])

	@classmethod
	def fromRow(cls, dat: 'DAT', row: int):
		parts = []
		for i in range(1, 5):
			cell = dat[row, 'part' + str(i)]
			if not cell.val:
				break
			parts.append(cell.val)
		return cls(
			tuplet=str(dat[row, 'tuplet']),
			parts=tuple(parts),
			isReadOnly='readOnly' in str(dat[row, 'status'] or ''),
		)

	@classmethod
	def fromTableRows(cls, dat: 'DAT') -> 'List[_ParamTupletSpec]':
		if not dat or dat.numRows < 2:
			return []
		return [
			cls.fromRow(dat, row)
			for row in range(1, dat.numRows)
		]

@dataclass
class _ParamExpr:
	name: str
	expr: Union[str, float]
	type: str

@dataclass
class _UniformSpec:
	name: str
	dataType: str  # float | vec2 | vec3 | vec4
	uniformType: str  # vector | uniformarray
	arrayLength: int = 1
	chop: Optional[str] = None
	expr1: Optional[str] = None
	expr2: Optional[str] = None
	expr3: Optional[str] = None
	expr4: Optional[str] = None

	def declaration(self):
		if self.uniformType == 'vector':
			return f'uniform {self.dataType} {self.name};'
		elif self.uniformType == 'uniformarray':
			return f'uniform {self.dataType} {self.name}[{self.arrayLength}];'
		else:
			raise Exception(f'Invalid uniformType: {self.uniformType!r}')

class _ParameterProcessor:
	def __init__(
			self,
			paramDetailTable: 'DAT',
			paramVals: 'CHOP',
			configPar: '_ConfigPar',
	):
		self.paramDetailTable = paramDetailTable
		self.hasParams = paramDetailTable.numRows > 1
		self.useConstantReadOnly = configPar.Inlinereadonlyparameters
		self.inlineAliases = configPar.Inlineparameteraliases
		self.paramVals = paramVals
		self.aliasMode = str(configPar['Paramaliasmode'] or 'macro')
		self.paramExprs = None  # type: Optional[List[_ParamExpr]]

	def globalDeclarations(self) -> List[str]:
		raise NotImplementedError()

	def paramAliases(self) -> List[str]:
		if not self.hasParams:
			return []
		if self.inlineAliases:
			return []
		self._initParamExprs()
		if self.aliasMode == 'globalvar':
			return [
				f'{paramExpr.type} {paramExpr.name} = {paramExpr.expr};'
				for paramExpr in self.paramExprs
			]
		else:  # self.aliasMode == 'macro'
			return [
				f'#define {paramExpr.name} {paramExpr.expr}'
				for paramExpr in self.paramExprs
			]

	def processCodeBlock(self, code: str) -> str:
		if not self.inlineAliases or not code:
			return code
		self._initParamExprs()
		for paramExpr in self.paramExprs:
			code = re.sub(r'\b' + re.escape(paramExpr.name) + r'\b', paramExpr.expr, code)
		return code

	def _initParamExprs(self):
		if self.paramExprs is not None:
			return
		self.paramExprs = []  # type: List[_ParamExpr]
		suffixes = 'xyzw'
		paramTuplets = _ParamTupletSpec.fromTableRows(self.paramDetailTable)
		for i, paramTuplet in enumerate(paramTuplets):
			useConstant = self.useConstantReadOnly and paramTuplet.isReadOnly and paramTuplet.isPresentInChop(self.paramVals)
			size = len(paramTuplet.parts)
			paramRef = self._paramReference(i, paramTuplet)
			if size == 1:
				name = paramTuplet.parts[0]
				self.paramExprs.append(_ParamExpr(
					name,
					repr(float(self.paramVals[name])) if useConstant else f'{paramRef}.x',
					'float'
				))
			else:
				if useConstant:
					partVals = [float(self.paramVals[part]) for part in paramTuplet.parts]
					valsExpr = ','.join(str(v) for v in partVals)
					parType = f'vec{size}'
					self.paramExprs.append(_ParamExpr(paramTuplet.tuplet, f'{parType}({valsExpr})', parType))
					for partI, partVal in enumerate(partVals):
						self.paramExprs.append(_ParamExpr(paramTuplet.parts[partI], partVal, 'float'))
				else:
					if size == 4:
						self.paramExprs.append(_ParamExpr(paramTuplet.tuplet, paramRef, 'vec4'))
					else:
						parType = f'vec{size}'
						self.paramExprs.append(_ParamExpr(
							paramTuplet.tuplet,
							f'{parType}({paramRef}.{suffixes[:size]})',
							parType
						))
					for partI, partName in enumerate(paramTuplet.parts):
						self.paramExprs.append(_ParamExpr(partName, f'{paramRef}.{suffixes[partI]}', 'float'))

	def _paramReference(self, i: int, paramTuplet: _ParamTupletSpec) -> str:
		raise NotImplementedError()

class _VectorArrayParameterProcessor(_ParameterProcessor):
	def _paramReference(self, i: int, paramTuplet: _ParamTupletSpec) -> str:
		return f'vecParams[{i}]'

	def globalDeclarations(self) -> List[str]:
		paramCount = max(1, self.paramDetailTable.numRows - 1)
		return [
			f'uniform vec4 vecParams[{paramCount}];',
		]

class _SeparateUniformsParameterProcessor(_ParameterProcessor):
	def globalDeclarations(self) -> List[str]:
		if not self.hasParams:
			return []
		decls = []
		for row in range(1, self.paramDetailTable.numRows):
			name = self.paramDetailTable[row, 'tuplet'].val
			size = int(self.paramDetailTable[row, 'size'])
			if size == 1:
				decls.append(f'uniform float {name};')
			else:
				decls.append(f'uniform vec{size} {name};')
		return decls

	def _paramReference(self, i: int, paramTuplet: _ParamTupletSpec) -> str:
		return paramTuplet.tuplet

_filterLinePattern = re.compile(r'^\s*#pragma r:(if|elif|else|endif)([ \t]+(.+))?$', re.MULTILINE)

class _CodeFilter:
	def processCodeBlock(self, code: str) -> str:
		return code

class _CodeMacroizerFilter(_CodeFilter):
	def processCodeBlock(self, code: str) -> str:
		if not code:
			return ''
		return _filterLinePattern.sub(self._replacement, code)

	@staticmethod
	def _replacement(m: 're.Match'):
		command = m.group(1)
		condition = _ReducerCondition.parse(m.group(3))
		if command == 'if':
			return f'#if {condition.asExpr()}'
		elif command == 'elif':
			return f'#elif {condition.asExpr()}'
		elif command == 'else':
			return '#else'
		elif command == 'endif':
			return '#endif'
		else:
			return m.group()


class _CodeReducerFilter(_CodeFilter):
	def __init__(
			self,
			macroTable: 'DAT',
			typeDefMacroTable: 'DAT',
	):
		cells = macroTable.col(0)
		self.macros = set(c.val for c in cells) if cells else set()  # type: Set[str]
		for cells in typeDefMacroTable.rows():
			n = cells[0]
			self.macros.add(str(n))

	def processCodeBlock(self, code: str) -> str:
		if not code:
			return ''
		if not self.macros:
			return code
		lines = []
		state = _ReducerState()
		for line in code.splitlines():
			cleaned = line.lstrip()
			if cleaned.startswith('#pragma r:'):
				cleaned = cleaned[10:]
				parts = cleaned.split(' ', maxsplit=1)
				command = parts[0]
				conditionExpr = parts[1] if len(parts) > 1 else None
				condition = _ReducerCondition.parse(conditionExpr)
				if command == 'endif':
					if condition:
						raise AssertionError(f'Invalid endif: {line}')
					state.handleEndif()
					continue
				elif command == 'if':
					if not condition:
						raise AssertionError(f'Missing condition: {line}')
					state.handleIf(condition.eval(self.macros))
					continue
				elif command == 'elif':
					if not condition:
						raise AssertionError(f'Missing condition: {line}')
					state.handleElif(condition.eval(self.macros))
					continue
				elif command == 'else':
					if condition:
						raise AssertionError('Invalid else')
					state.handleElse()
					continue
				else:
					raise AssertionError(f'Invalid pragma: {line}')
			if state.matching:
				lines.append(line)
		if state.hasOpenBlock():
			raise AssertionError('Unmatched if block, missing endif')
		return '\n'.join(lines)

class _ReducerCondition:
	def eval(self, macros: 'Set[str]') -> bool: pass
	def asExpr(self) -> str: pass

	@classmethod
	def parse(cls, expr: str):
		expr = expr.strip() if expr else None
		if not expr:
			return None

		posSyms = set()
		negSyms = set()
		isOr = False
		isAnd = False

		for token in expr.split():
			if token == '||':
				if isAnd:
					raise AssertionError(f'Invalid expression (multiple operators): {expr!r}')
				isOr = True
			elif token == '&&':
				if isOr:
					raise AssertionError(f'Invalid expression (multiple operators): {expr!r}')
				isAnd = True
			else:
				neg = token.startswith('!')
				if neg:
					token = token[1:]
				# if not re.fullmatch(r'\w+', token):
				# 	raise AssertionError(f'Invalid expression (bad token): {expr!r}')
				# else:
				if neg:
					negSyms.add(token)
				else:
					posSyms.add(token)
		if not posSyms and not negSyms:
			if isOr or isAnd:
				raise AssertionError(f'Invalid expression (operator but no symbols): {expr!r}')
			return None
		if isOr:
			return _ReducerConditionOr(posSyms, negSyms)
		elif isAnd:
			return _ReducerConditionAnd(posSyms, negSyms)
		else:
			if (len(posSyms) + len(negSyms)) > 1:
				raise AssertionError(f'Invalid expression (missing operator): {expr!r}')
			else:
				if posSyms:
					return _ReducerConditionSingle(posSyms.pop(), neg=False)
				else:
					return _ReducerConditionSingle(negSyms.pop(), neg=True)

class _ReducerConditionOr(_ReducerCondition):
	def __init__(self, posSyms: 'Set[str]', negSyms: 'Set[str]'):
		self.posSyms = posSyms
		self.negSyms = negSyms

	def eval(self, macros: 'Set[str]') -> bool:
		if self.posSyms and _anyIn(self.posSyms, macros):
			return True
		if self.negSyms and not _allIn(self.negSyms, macros):
			return True
		return False

	def asExpr(self) -> str:
		return ' || '.join([f'defined({s})' for s in self.posSyms] + [f'!defined({s})' for s in self.negSyms])

class _ReducerConditionAnd(_ReducerCondition):
	def __init__(self, posSyms: 'Set[str]', negSyms: 'Set[str]'):
		self.posSyms = posSyms
		self.negSyms = negSyms

	def eval(self, macros: 'Set[str]') -> bool:
		if self.posSyms and not _allIn(self.posSyms, macros):
			return False
		if self.negSyms and _anyIn(self.posSyms, macros):
			return False
		return True

	def asExpr(self) -> str:
		return ' && '.join([f'defined({s})' for s in self.posSyms] + [f'!defined({s})' for s in self.negSyms])

class _ReducerConditionSingle(_ReducerCondition):
	def __init__(self, sym: str, neg: bool):
		self.sym = sym
		self.neg = neg

	def eval(self, macros: 'Set[str]') -> bool:
		if self.neg:
			return self.sym not in macros
		else:
			return self.sym in macros

	def asExpr(self) -> str:
		if self.neg:
			return f'!defined({self.sym})'
		else:
			return f'defined({self.sym})'

def _anyIn(s1: 'Set[str]', s2: 'Set[str]'):
	return s1.intersection(s2)
def _allIn(s1: 'Set[str]', s2: 'Set[str]'):
	return s1.issubset(s2)

@dataclass
class _ReducerFrame:
	nowMatching: bool
	hasMatched: bool = False

class _ReducerState:
	def __init__(self):
		self._stack = []  # type: List[_ReducerFrame]
		self.matching = True

	def handleIf(self, matching: bool):
		self._stack.append(_ReducerFrame(nowMatching=matching, hasMatched=matching))
		self._updateState()

	def handleElif(self, matching: bool):
		if not self._stack:
			raise AssertionError('Invalid elif without if')
		frame = self._stack[-1]
		if matching:
			if not frame.hasMatched:
				frame.nowMatching = True
				frame.hasMatched = True
		else:
			frame.nowMatching = False
		self._updateState()

	def handleElse(self):
		if not self._stack:
			raise AssertionError('Invalid else without if')
		frame = self._stack[-1]
		if frame.hasMatched:
			frame.nowMatching = False
		else:
			frame.nowMatching = True
			frame.hasMatched = True
		self._updateState()

	def handleEndif(self):
		if not self._stack:
			raise AssertionError('Invalid endif without if')
		self._stack.pop()
		self._updateState()

	def _updateState(self):
		if not self._stack:
			self.matching = True
		else:
			self.matching = all(f.nowMatching for f in self._stack)

	def hasOpenBlock(self):
		return bool(self._stack)

def _stringify(val: 'Union[str, DAT]'):
	if val is None:
		return ''
	if isinstance(val, DAT):
		return val.text
	return str(val)

def _combineCode(code: 'Union[str, DAT, List[Union[str, DAT]]]'):
	if isinstance(code, list):
		combined = ''
		for item in code:
			val = _stringify(item)
			if val:
				combined += val + '\n'
		return combined
	else:
		return _stringify(code)

def wrapCodeSection(code: 'Union[str, DAT, List[Union[str, DAT]]]', name: str):
	code = _combineCode(code)
	if not code:
		# return a non-empty string in order to force DATs to be text when using dat.write()
		return ' '
	return f'///----BEGIN {name}\n{code.strip()}\n///----END {name}\n'

def _uniqueList(items: list):
	results = []
	for item in items:
		if item not in results:
			results.append(item)
	return results
