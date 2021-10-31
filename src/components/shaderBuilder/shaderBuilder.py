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
	def __init__(self, ownerComp: '_OwnerComp'):
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
			mainName = defsTable[defsTable.numRows - 1, 'name']
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

	def _getMacros(self) -> 'List[Tuple[str, str]]':
		tables = [self.ownerComp.par.Globalmacrotable.eval()]
		tables += self.getOpsFromDefinitionColumn('macroTable')
		namesAndVals = []
		for table in tables:
			if not table:
				continue
			for row in range(table.numRows):
				if table.numCols == 3:
					if table[row, 0].val in ('0', 'False'):
						continue
					name = table[row, 1].val
					value = table[row, 2].val
				else:
					name = table[row, 0].val
					if table.numCols > 1:
						value = table[row, 1].val
					else:
						value = ''
				if value:
					value = ' ' + value
				if not name.strip():
					continue
				namesAndVals.append((name, value))
		for outputBuffer in self._getOutputBufferSpecs():
			if outputBuffer.macro:
				namesAndVals.append((outputBuffer.macro, ''))
		return namesAndVals

	def _getOutputBufferSpecs(self) -> 'List[_OutputBufferSpec]':
		table = self._outputBufferTable()
		if table.numRows <= 1:
			return []
		return [
			_OutputBufferSpec(
				name=table[row, 'name'].val,
				label=table[row, 'label'].val,
				macro=table[row, 'macro'].val,
				index=row - 1,
			)
			for row in range(1, table.numRows)
		]

	def buildMacroTable(self, dat: 'DAT'):
		dat.clear()
		dat.appendRows([
			[name, value]
			for name, value in self._getMacros()
		])

	def buildMacroBlock(self):
		decls = []
		for name, value in self._getMacros():
			if name.startswith('#define'):
				decls.append(name + value)
			else:
				decls.append(f'#define {name} {value}')
		decls = _uniqueList(decls)
		code = wrapCodeSection(decls, 'macros')
		# if self.configPar().Inlineparameteraliases:
		# 	processor = self._createParamProcessor()
		# 	return processor.processCodeBlock(code)
		return code

	def getLibraryDats(self, onWarning: Callable[[str], None] = None) -> 'List[DAT]':
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
		libraries = self.getLibraryDats(onWarning)
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

	def buildOpDataTypedefBlock(self):
		inline = self.configPar()['Inlinetypedefs']
		typedefs, macros = self._buildTypedefs()
		if typedefs:
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

	def _buildTypedefs(self) -> 'Tuple[Dict[str, str], Dict[str, str]]':
		defsTable = self._definitionTable()
		typedefs = {}
		macros = {}
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
			typedefs.update({
				name + '_CoordT': coordType,
				name + '_ContextT': contextType,
				name + '_ReturnT': returnType,
			})
			macros.update({
				f'{name}_COORD_TYPE_{coordType}': '',
				f'{name}_CONTEXT_TYPE_{contextType}': '',
				f'{name}_RETURN_TYPE_{returnType}': '',
			})
			if coordType in coordTypeAdaptFuncs:
				macros[name + '_asCoordT'] = coordTypeAdaptFuncs[coordType]
			if returnType in returnTypeAdaptFuncs:
				macros[name + '_asReturnT'] = returnTypeAdaptFuncs[returnType]
		return typedefs, macros

	def inlineTypedefs(self, code: str) -> str:
		if not self.configPar()['Inlinetypedefs']:
			return code
		typedefs, macros = self._buildTypedefs()
		if not typedefs:
			return code

		replacements = dict(typedefs)
		replacements.update({
			k: v
			for k, v in macros.items()
			if v != ''
		})

		def replace(m: re.Match):
			return replacements.get(m.group(0)) or m.group(0)

		pattern = r'\b[\w_]+_(as)?(CoordT|ContextT|ReturnT)\b'

		code = re.sub(pattern, replace, code)

		return code

	def _createCodeFilter(self) -> '_CodeFilter':
		mode = self.configPar()['Filtermode']
		if mode == 'filter':
			_, typeDefMacros = self._buildTypedefs()
			return _CodeReducerFilter(
				macroTable=self.ownerComp.op('macroTable'),
				typeDefMacros=typeDefMacros,
			)
		else:  # macroize
			return _CodeMacroizerFilter()

	def filterCode(self, code: str) -> str:
		if not code:
			return ''
		if '#pragma' not in code:
			return code
		filt = self._createCodeFilter()
		return filt.processCodeBlock(code)

	def buildPredeclarations(self):
		return wrapCodeSection(self.ownerComp.par.Predeclarations.eval(), 'predeclarations')

	def _buildParameterExprs(self) -> 'List[Tuple[str, Union[str, float]]]':
		paramDetails = self._parameterDetailTable()
		if paramDetails.numRows < 2:
			return []
		suffixes = 'xyzw'
		partAliases = []  # type: List[Tuple[str, Union[str, float]]]
		mainAliases = []  # type: List[Tuple[str, Union[str, float]]]
		inlineReadOnly = bool(self.configPar()['Inlinereadonlyparameters'])
		paramVals = self._allParamVals()
		paramTuplets = _ParamTupletSpec.fromTableRows(paramDetails)
		for i, paramTuplet in enumerate(paramTuplets):
			shouldInline = inlineReadOnly and paramTuplet.isReadOnly and paramTuplet.isPresentInChop(paramVals)
			size = len(paramTuplet.parts)
			if size == 1:
				if shouldInline:
					mainAliases.append((paramTuplet.parts[0], float(paramVals[paramTuplet.parts[0]])))
				else:
					mainAliases.append((paramTuplet.parts[0], f'vecParams[{i}].x'))
			else:
				if shouldInline:
					partVals = [float(paramVals[part]) for part in paramTuplet.parts]
					valsExpr = ','.join(str(v) for v in partVals)
					mainAliases.append((paramTuplet.tuplet, f'vec{size}({valsExpr})'))
					for partI, partVal in enumerate(partVals):
						partAliases.append((paramTuplet.parts[partI], partVal))
				else:
					if size == 4:
						mainAliases.append((paramTuplet.tuplet, f'vecParams[{i}]'))
					else:
						mainAliases.append((paramTuplet.tuplet, f'vec{size}(vecParams[{i}].{suffixes[:size]})'))
					for partI, partName in enumerate(paramTuplet.parts):
						partAliases.append((partName, f'vecParams[{i}].{suffixes[partI]}'))
		return partAliases + mainAliases

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
		indexByType = {
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
		outputBuffers = self._outputBufferTable()
		if outputBuffers.numRows < 2:
			return ' '
		specs = self._getOutputBufferSpecs()
		if self.ownerComp.par.Shadertype == 'compute':
			decls = [
				spec.computeOutputDeclaration()
				for spec in specs
			]
		else:
			decls = [
				spec.fragmentOutputDeclaration()
				for spec in specs
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
		if _materialParagraphPlaceholder in code:
			materialBlock = self._buildMaterialBlock(materialTable)
			code = code.replace(_materialParagraphPlaceholder, materialBlock, 1)
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

	def buildUniformTable(self, dat: 'scriptDAT'):
		pass

_materialParagraphPlaceholder = '// #include <materialParagraph>'

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
class _OutputBufferSpec:
	name: str
	index: int
	label: Optional[str] = None
	macro: Optional[str] = None

	def fragmentOutputDeclaration(self):
		return f'layout(location = {self.index}) out vec4 {self.name};'

	def computeOutputDeclaration(self):
		return f'#define {self.name} mTDComputeOutputs[{self.index}]'

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

	def globalDeclarations(self) -> List[str]:
		raise NotImplementedError()

	def paramAliases(self) -> List[str]:
		if not self.hasParams:
			return []
		if self.inlineAliases:
			return []
		if self.aliasMode == 'globalvar':
			return [
				f'{paramExpr.type} {paramExpr.name} = {paramExpr.expr};'
				for paramExpr in self._generateParamExprs()
			]
		else:  # self.aliasMode == 'macro'
			return [
				f'#define {paramExpr.name} {paramExpr.expr}'
				for paramExpr in self._generateParamExprs()
			]

	def processCodeBlock(self, code: str) -> str:
		if not self.inlineAliases or not code:
			return code
		for paramExpr in self._generateParamExprs():
			code = re.sub(r'\b' + re.escape(paramExpr.name) + r'\b', paramExpr.expr, code)
		return code

	def _generateParamExprs(self) -> List[_ParamExpr]:
		paramExprs = []  # type: List[_ParamExpr]
		suffixes = 'xyzw'
		paramTuplets = _ParamTupletSpec.fromTableRows(self.paramDetailTable)
		for i, paramTuplet in enumerate(paramTuplets):
			useConstant = self.useConstantReadOnly and paramTuplet.isReadOnly and paramTuplet.isPresentInChop(self.paramVals)
			size = len(paramTuplet.parts)
			paramRef = self._paramReference(i, paramTuplet)
			if size == 1:
				name = paramTuplet.parts[0]
				paramExprs.append(_ParamExpr(
					name,
					repr(float(self.paramVals[name])) if useConstant else f'{paramRef}.x',
					'float'
				))
			else:
				if useConstant:
					partVals = [float(self.paramVals[part]) for part in paramTuplet.parts]
					valsExpr = ','.join(str(v) for v in partVals)
					parType = f'vec{size}'
					paramExprs.append(_ParamExpr(paramTuplet.tuplet, f'{parType}({valsExpr})', parType))
					for partI, partVal in enumerate(partVals):
						paramExprs.append(_ParamExpr(paramTuplet.parts[partI], partVal, 'float'))
				else:
					if size == 4:
						paramExprs.append(_ParamExpr(paramTuplet.tuplet, paramRef, 'vec4'))
					else:
						parType = f'vec{size}'
						paramExprs.append(_ParamExpr(
							paramTuplet.tuplet,
							f'{parType}({paramRef}.{suffixes[:size]})',
							parType
						))
					for partI, partName in enumerate(paramTuplet.parts):
						paramExprs.append(_ParamExpr(partName, f'{paramRef}.{suffixes[partI]}', 'float'))
		return paramExprs

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

_filterLinePattern = re.compile(r'^\s*#pragma r:(if|elif|else|endif)(\s+(\w+))?$', re.MULTILINE)

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
		symbol = m.group(3)
		if command == 'if':
			return f'#ifdef {symbol}'
		elif command == 'elif':
			return f'#elif defined({symbol})'
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
			typeDefMacros: 'Dict[str, str]',
	):
		cells = macroTable.col(0)
		self.macros = set(c.val for c in cells) if cells else set()  # type: Set[str]
		self.macros |= typeDefMacros.keys()

	def processCodeBlock(self, code: str) -> str:
		if not code:
			return ''
		if not self.macros:
			return code
		lines = []
		state = _ReducerState()
		for line in code.splitlines():
			m = _filterLinePattern.fullmatch(line)
			if m:
				command = m.group(1)
				symbol = m.group(3)
				if command == 'endif':
					if symbol:
						raise AssertionError('Invalid endif')
					state.handleEndif()
					continue
				elif command == 'if':
					state.handleIf(symbol in self.macros)
					continue
				elif command == 'elif':
					state.handleElif(symbol in self.macros)
					continue
				elif command == 'else':
					if symbol:
						raise AssertionError('Invalid else')
					state.handleElse()
					continue
			if state.isMatching():
				lines.append(line)
		return '\n'.join(lines)

@dataclass
class _ReducerFrame:
	nowMatching: bool
	hasMatched: bool = False

class _ReducerState:
	def __init__(self):
		self._stack = []  # type: List[_ReducerFrame]

	def handleIf(self, matching: bool):
		self._stack.append(_ReducerFrame(nowMatching=matching, hasMatched=matching))

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

	def handleElse(self):
		if not self._stack:
			raise AssertionError('Invalid else without if')
		frame = self._stack[-1]
		if frame.hasMatched:
			frame.nowMatching = False
		else:
			frame.nowMatching = True
			frame.hasMatched = True

	def handleEndif(self):
		if not self._stack:
			raise AssertionError('Invalid endif without if')
		self._stack.pop()

	def isMatching(self):
		if not self._stack:
			return True
		return all(f.nowMatching for f in self._stack)

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

def updateLibraryMenuPar(libsComp: 'COMP'):
	p = parent().par.Librarynames  # type: Par
	libs = libsComp.findChildren(type=DAT, maxDepth=1, tags=['library'])
	libs.sort(key=lambda l: -l.nodeY)
	p.menuNames = [lib.name for lib in libs]

def _uniqueList(items: list):
	results = []
	for item in items:
		if item not in results:
			results.append(item)
	return results
