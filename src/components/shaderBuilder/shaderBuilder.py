from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple, Union
from raytkUtil import RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

	class _ConfigPar(ParCollection):
		Parammode: 'Union[str, Par]'
		Inlineparameteraliases: 'Union[bool, Par]'
		Inlinereadonlyparameters: 'Union[bool, Par]'
		Simplifynames: 'Union[bool, Par]'
		Generatetypedefs: 'Union[bool, Par]'
		Includemode: 'Union[str, Par]'

	class _OwnerCompPar(_ConfigPar):
		Globalprefix: 'Union[DAT, str, Par]'
		Predeclarations: 'Union[DAT, str, Par]'
		Textureindexoffset: 'Union[int, Par]'
		Globalmacrotable: 'Union[DAT, str, Par]'
		Libraries: 'Union[str, Par]'
		Bodytemplate: 'Union[DAT, str, Par]'
		Outputbuffertable: 'Union[DAT, str, Par]'
		Supportmaterials: 'Union[bool, Par]'
		Shaderbuilderconfig: 'Union[COMP, str, Par]'

	class _OwnerComp(COMP):
		par: '_OwnerCompPar'

	class _ConfigComp(COMP):
		par: '_ConfigPar'

class ShaderBuilder:
	def __init__(self, ownerComp: '_OwnerComp'):
		self.ownerComp = ownerComp

	def configPar(self) -> '_ConfigPar':
		p = self.ownerComp.par['Shaderbuilderconfig']
		if p:
			o = op(p)
			if o:
				# noinspection PyTypeChecker
				return o.par
		return self.ownerComp.par

	def preprocessDefinitions(self, dat: 'scriptDAT'):
		# BEFORE definitions are reversed, so a def's inputs are always BELOW it in the table
		pass

	def definitionTable(self) -> 'DAT':
		# in reverse order (aka declaration order)
		return self.ownerComp.op('definitions')

	def parameterDetailTable(self) -> 'DAT':
		return self.ownerComp.op('param_details')

	def outputBufferTable(self) -> 'DAT':
		return self.ownerComp.op('output_buffer_table')

	def allParamVals(self) -> 'CHOP':
		return self.ownerComp.op('all_param_vals')

	def buildGlobalPrefix(self):
		return wrapCodeSection(self.ownerComp.par.Globalprefix.eval(), 'globalPrefix')

	def _createParamProcessor(self) -> '_ParameterProcessor':
		mode = self.configPar().Parammode.eval()
		if mode == 'uniformarray':
			return _VectorArrayParameterProcessor(
				self.parameterDetailTable(),
				self.allParamVals(),
				self.configPar(),
			)
		elif mode == 'separateuniforms':
			return _SeparateUniformsParameterProcessor(
				self.parameterDetailTable(),
				self.allParamVals(),
				self.configPar(),
			)
		else:
			raise NotImplementedError(f'Parameter processor not available for mode: {mode!r}')

	def buildGlobalDeclarations(self):
		defsTable = self.definitionTable()
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
		defsTable = self.definitionTable()
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
		outputBuffers = self.outputBufferTable()
		if outputBuffers.numRows > 1 and outputBuffers.col('macro'):
			for cell in outputBuffers.col('macro')[1:]:
				if cell.val:
					namesAndVals.append((cell.val, ''))
		return namesAndVals

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
		defsTable = self.definitionTable()
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
					dat = libraryOp.op(name)
					if not dat:
						continue
					dats.append(dat)
					namesToRemove.append(name)
				for name in namesToRemove:
					requiredLibNames.remove(name)
		if requiredLibNames and onWarning:
			onWarning('Missing libraries: ' + repr(requiredLibNames))
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
		defsTable = self.definitionTable()
		typedefs = []
		macros = []
		coordTypeAdaptFuncs = {
			'float': 'adaptAsFloat',
			'vec2': 'adaptAsVec2',
			'vec3': 'adaptAsVec3',
		}
		returnTypeAdaptFuncs = {
			'float': 'adaptAsFloat',
			'vec4': 'adaptAsVec4',
		}
		for row in range(1, defsTable.numRows):
			name = str(defsTable[row, 'name'])
			coordType = str(defsTable[row, 'coordType'])
			contextType = str(defsTable[row, 'contextType'])
			returnType = str(defsTable[row, 'returnType'])
			typedefs += [
				f'#define {name}_CoordT    {coordType}',
				f'#define {name}_ContextT  {contextType}',
				f'#define {name}_ReturnT   {returnType}',
			]
			macros += [
				f'#define {name}_COORD_TYPE_{coordType}',
				f'#define {name}_CONTEXT_TYPE_{contextType}',
				f'#define {name}_RETURN_TYPE_{returnType}',
				f'#define {name}_asCoordT {coordTypeAdaptFuncs[coordType]}',
			]
			if returnType in returnTypeAdaptFuncs:
				macros.append(f'#define {name}_asReturnT {returnTypeAdaptFuncs[returnType]}')
		if typedefs:
			lines = typedefs + [''] + macros
		else:
			lines = []
		return wrapCodeSection(lines, 'opDataTypedefs')

	def buildPredeclarations(self):
		return wrapCodeSection(self.ownerComp.par.Predeclarations.eval(), 'predeclarations')

	def _buildParameterExprs(self) -> 'List[Tuple[str, Union[str, float]]]':
		paramDetails = self.parameterDetailTable()
		if paramDetails.numRows < 2:
			return []
		suffixes = 'xyzw'
		partAliases = []  # type: List[Tuple[str, Union[str, float]]]
		mainAliases = []  # type: List[Tuple[str, Union[str, float]]]
		inlineReadOnly = bool(self.configPar()['Inlinereadonlyparameters'])
		paramVals = self.allParamVals()
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
		}
		arrayByType = {
			'2d': 'sTD2DInputs',
			'3d': 'sTD3DInputs',
			'cube': 'sTDCubeInputs',
		}
		decls = []
		for i in range(1, textureTable.numRows):
			name = str(textureTable[i, 'name'])
			texType = str(textureTable[i, 'type'] or '2d')
			if texType not in indexByType:
				raise Exception(f'Invalid texture type for {name}: {texType!r}')
			index = indexByType[texType]
			decls.append(f'#define {name} {arrayByType[texType]}[{index}]')
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
		outputBuffers = self.outputBufferTable()
		if outputBuffers.numRows < 2:
			return ' '
		decls = [
			f'layout(location = {cell.row - 1}) out vec4 {cell.val};'
			for cell in outputBuffers.col('name')[1:]
		]
		return wrapCodeSection(decls, 'outputBuffers')

	def buildOutputInitBlock(self):
		outputBuffers = self.outputBufferTable()
		return wrapCodeSection(
			[
				'void initOutputs() {'
			] +
			[
				f'{cell.val} = vec4(0.);'
				for cell in outputBuffers.col('name')[1:]
			] + [
				'}'
			],
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
		defsTable = self.definitionTable()
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
		# if self.inlineAliases:
		# 	return []
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
			code = code.replace(paramExpr.name, paramExpr.expr)
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
	return f'///----BEGIN {name}\n{code}\n///----END {name}'

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
