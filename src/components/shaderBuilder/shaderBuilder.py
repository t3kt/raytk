from dataclasses import dataclass
import json
from raytkShader import simplifyNames
from raytkState import RopState, Texture, Buffer, Macro, Reference, Variable, ValidationError, Constant, \
	InputState, SurfaceAttribute
import re
from io import StringIO
from typing import Callable, Dict, Union, Optional
try:
	from opDefinition import OpDefinition
except ImportError:
	from components.opDefinition.opDefinition import OpDefinition

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _ConfigPar(ParCollection):
		Inlinereadonlyparameters: BoolParamT
		Simplifynames: BoolParamT
		Inlinetypedefs: BoolParamT
		Includemode: StrParamT

	class _OwnerCompPar(_ConfigPar):
		Predeclarations: DatParamT
		Textureindexoffset: IntParamT
		Texture3dindexoffset: IntParamT
		Texture2darrayindexoffset: IntParamT
		Libraries: StrParamT
		Bodytemplate: DatParamT
		Outputbuffertable: DatParamT
		Supportmaterials: BoolParamT
		Shaderbuilderconfig: CompParamT
		Shadertype: StrParamT
		Limitcodetonames: StrParamT

	class _OwnerComp(COMP):
		par: '_OwnerCompPar'

	class _ConfigComp(COMP):
		par: '_ConfigPar'

# @dataclass
# class _ShaderTargetConfig:
# 	hasPrimaryRopFunction: bool
# 	hasOutputBuffers: bool
#
# _topShaderConfig = _ShaderTargetConfig(
# 	hasPrimaryRopFunction=True,
# 	hasOutputBuffers=True,
# )
# _matShaderConfig = _ShaderTargetConfig(
# 	hasPrimaryRopFunction=False,
# 	hasOutputBuffers=False,
# )

class ShaderBuilder:
	def __init__(self, ownerComp: 'Union[_OwnerComp, COMP]'):
		self.ownerComp = ownerComp

	def _config(self) -> '_ConfigComp':
		o = self.ownerComp.par.Shaderbuilderconfig.eval()
		# noinspection PyTypeChecker
		return o or self.ownerComp.op('default_shaderBuilderConfig')

	def configValid(self):
		o = self._config()
		try:
			return bool(o is not None and o.valid)
		except:
			return False

	def configPar(self) -> '_ConfigPar':
		return self._config().par

	def Createcustomconfig(self, _=None):
		hostPar = self.ownerComp.parent().par['Shaderbuilderconfig']
		if hostPar is None:
			raise Exception('Unable to locate Shaderbuilderconfig par')
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

	def preprocessDefinitions(self, dat: scriptDAT):
		# BEFORE definitions are reversed, so a def's inputs are always BELOW it in the table
		knownCols = [c.val for c in dat.row(0)]
		skipCols = ['name', 'path', 'coordType', 'contextType', 'returnType', 'definitionPath']
		for row in range(1, dat.numRows):
			defPath = str(dat[row, 'definitionPath'] or '')
			defTable = op(defPath)
			if not defTable or defTable.numRows < 2:
				continue
			if defTable.numRows > 2:
				raise Exception(f'Invalid single-op definition table, too many rows: {defTable}')
			for col, val in defTable.cols():
				if col in skipCols:
					continue
				if col.val not in knownCols:
					knownCols.append(col.val)
					dat.appendCol([col])
				dat[row, col].val = val
		self._resolveTypes(dat, 'coordType')
		self._resolveTypes(dat, 'contextType')
		self._resolveTypes(dat, 'returnType')

	@staticmethod
	def _resolveTypes(dat: scriptDAT, column: str):
		# BEFORE definitions are reversed, so a def's inputs are always BELOW it in the table
		typesByName = {}  # type: Dict[str, str]
		cells = dat.col(column)
		if not cells:
			return
		for cell in cells[1:]:
			name = dat[cell.row, 'name'].val
			if cell.val.startswith('@'):
				refName = cell.val.replace('@', '', 1)
				if refName not in typesByName:
					raise Exception(f'Type resolution error for {name}: {cell.val!r}')
				cell.val = typesByName[refName]
			typesByName[name] = cell.val

	def _definitionTable(self) -> DAT:
		# in reverse order (aka declaration order)
		return self.ownerComp.op('definitions')

	def _parameterDetailTable(self) -> DAT:
		return self.ownerComp.op('param_details')

	def _outputBufferTable(self) -> DAT:
		return self.ownerComp.op('output_buffer_table')

	def _variableTable(self) -> DAT:
		return self.ownerComp.op('variable_table')

	def _referenceTable(self) -> DAT:
		return self.ownerComp.op('reference_table')

	def _allParamVals(self) -> 'CHOP':
		return self.ownerComp.op('all_param_vals')

	def buildNameReplacementTable(self, dat: scriptDAT):
		dat.clear()
		dat.appendRow(['before', 'after'])
		if not self.configValid():
			return
		if not self.configPar().Simplifynames:
			return
		origNames = [c.val for c in self._definitionTable().col('name')[1:]]
		simpleNames = simplifyNames(origNames)
		if simpleNames == origNames:
			return
		dat.clear()
		dat.appendCol(['before'] + origNames)
		dat.appendCol(['after'] + simpleNames)

	def _createParamProcessor(self) -> '_ParameterProcessor':
		configPar = self.configPar() if self.configValid() else None
		if configPar and configPar['Parammode'] == 'separateuniformarrays':
			return _SeparateArrayParameterProcessor(
				self._parameterDetailTable(),
				self._allParamVals(),
				configPar,
				self._getOpStates(),
				self.ownerComp.par.Shadertype.eval(),
			)
		return _SingleArrayParameterProcessor(
			self._parameterDetailTable(),
			self._allParamVals(),
			configPar,
			self._getOpStates(),
			self.ownerComp.par.Shadertype.eval(),
		)

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

	def buildMacroTable(self, dat: DAT):
		dat.clear()
		states = self._getOpStates()
		for state in states:
			if not state.macros:
				continue
			for m in state.macros:
				if m.enable:
					dat.appendRow([m.name, m.value if m.value is not None else ''])
		outputBufferTable = self._outputBufferTable()
		for row in range(1, outputBufferTable.numRows):
			name = outputBufferTable[row, 'macro'].val.strip()
			if name:
				dat.appendRow([name, ''])
		varTable = self._variableTable()
		for row in range(1, varTable.numRows):
			ownerName = varTable[row, 'owner']
			localName = varTable[row, 'localName']
			dat.appendRow([f'{ownerName}_EXPOSE_{localName}', ''])
			for part in tdu.split(varTable[row, 'macros']):
				dat.appendRow([part, ''])
		refTable = self._referenceTable()
		for row in range(1, refTable.numRows):
			ownerName = refTable[row, 'owner']
			localName = refTable[row, 'localName']
			dat.appendRow([refTable[row, 'name'], refTable[row, 'source']])
			dat.appendRow([f'{ownerName}_HAS_REF_{localName}', ''])
		for state in states:
			if not state.constants:
				continue
			for const in state.constants:
				if const.menuOptions:
					for i, opt in enumerate(const.menuOptions):
						dat.appendRow([f'{state.ropType}_{const.localName}_{opt}', i])

	def _getLibraryDats(self, onWarning: Callable[[str], None] = None) -> list[DAT]:
		requiredLibNames = self.ownerComp.par.Librarynames.eval().strip().split(' ')  # type: list[str]
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
		dats = []  # type: list[DAT]
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

	def buildTypedefMacroTable(self, dat: scriptDAT):
		dat.clear()
		defsTable = self._definitionTable()
		typeAdaptFuncs = {
			'float': 'adaptAsFloat',
			'vec2': 'adaptAsVec2',
			'vec3': 'adaptAsVec3',
			'vec4': 'adaptAsVec4',
			'Sdf': 'adaptAsSdf',
			'int': 'adaptAsInt',
			'Ray': 'adaptAsRay',
			'Light': 'adaptAsLight',
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
			if coordType in typeAdaptFuncs:
				dat.appendRow([name + '_asCoordT', typeAdaptFuncs[coordType], 'macro'])
			if returnType in typeAdaptFuncs:
				dat.appendRow([name + '_asReturnT', typeAdaptFuncs[returnType], 'macro'])
		varTable = self._variableTable()
		for row in range(1, varTable.numRows):
			name = str(varTable[row, 'name'])
			dataType = str(varTable[row, 'dataType'])
			dat.appendRow([name + '_VarT', dataType, 'typedef'])
			dat.appendRow([name + '_TYPE_' + dataType, '', 'macro'])
			if dataType in typeAdaptFuncs:
				dat.appendRow([name + '_asVarT', typeAdaptFuncs[dataType], 'macro'])

	def processReferenceTable(self, dat: scriptDAT):
		dat.clear()
		dat.appendRow(['name', 'owner', 'localName', 'source', 'dataType', 'category'])
		defTable = self._definitionTable()
		varNames = {}
		attrNames = set()
		states = self._getOpStates()
		for state in states:
			if state.variables:
				for variable in state.variables:
					varOwnerName = variable.owner
					pathCell = defTable[varOwnerName, 'path']
					if not pathCell:
						continue
					varOwnerPath = pathCell.val
					varNames[(varOwnerPath, variable.localName)] = variable.name
			if state.attributes:
				for attribute in state.attributes:
					attrNames.add(attribute.name)
		for state in states:
			if not state.references:
				continue
			for reference in state.references:
				if reference.category == 'attribute':
					if not reference.name or reference.sourceName not in attrNames:
						# TODO: report invalid ref
						continue
					# TODO: validate dataType match
					dat.appendRow([
						reference.name,
						reference.owner,
						reference.localName,
						reference.sourceName,
						reference.dataType,
						'attribute',
					])
				else:
					if not reference.sourcePath or not reference.sourceName:
						continue
					sourceName = varNames.get((reference.sourcePath, reference.sourceName), None)
					if not sourceName:
						# TODO: report invalid ref
						continue
					# TODO: validate dataType match
					dat.appendRow([
						reference.name,
						reference.owner,
						reference.localName,
						sourceName,
						reference.dataType,
						'variable',
					])

	def processVariableTable(
			self,
			dat: scriptDAT,
			procRefTable: DAT,
	):
		dat.clear()
		dat.appendRow(['name', 'owner', 'localName', 'dataType', 'macros'])
		refNames = set(
			procRefTable[i, 'source'].val
			for i in range(1, procRefTable.numRows)
			if procRefTable[i, 'category'] == 'variable'
		)
		states = self._getOpStates()
		for state in states:
			if not state.variables:
				continue
			for variable in state.variables:
				if variable.name in refNames:
					dat.appendRow([
						variable.name,
						variable.owner,
						variable.localName,
						variable.dataType,
						variable.macros or '',
					])

	def buildParamUniformTable(self, dat: DAT):
		dat.clear()
		dat.appendRow(['name', 'type', 'chop', 'uniformType', 'expr1', 'expr2', 'expr3', 'expr4'])
		paramProcessor = self._createParamProcessor()
		specs = paramProcessor.paramUniforms()
		for spec in specs:
			dat.appendRow([
				spec.name, spec.dataType, spec.chop or '',
				spec.uniformType,
				spec.expr1 or '', spec.expr2 or '', spec.expr3 or '', spec.expr4 or ''
			])

	def buildRuntimeParamDetailTable(self, dat: DAT):
		dat.clear()
		dat.appendRow([
			'tuplet', 'source', 'size',
			'part1', 'part2', 'part3', 'part4',
			'status', 'handling', 'ownerName',
			'sourceVectorPath', 'sourceVectorIndex'])
		states = self._getOpStates()
		for state in states:
			if not state.paramTuplets:
				continue
			for paramTuplet in state.paramTuplets:
				if paramTuplet.handling != 'runtime':
					continue
				dat.appendRow([
					paramTuplet.name, paramTuplet.source, paramTuplet.size,
					paramTuplet.part1 or '', paramTuplet.part2 or '', paramTuplet.part3 or '', paramTuplet.part4 or '',
					paramTuplet.status or '', paramTuplet.handling or '', state.name,
					paramTuplet.sourceVectorPath or '',
					paramTuplet.sourceVectorIndex if paramTuplet.sourceVectorIndex is not None else '',
				])

	def processLibraryIncludes(self, code: str):
		mode = str((self.configPar() and self.configPar()['Includemode']) or 'includelibs')
		if mode != 'inlineall':
			return code

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

	def buildBufferUniformTable(self, dat: DAT):
		dat.clear()
		dat.appendRow(['name', 'type', 'chop', 'uniformType', 'expr1', 'expr2', 'expr3', 'expr4'])
		for state in self._getOpStates():
			if not state.buffers:
				continue
			for buffer in state.buffers:
				dat.appendRow([
					buffer.name, buffer.type, buffer.chop or '', buffer.uniformType,
					buffer.expr1 or '', buffer.expr2 or '', buffer.expr3 or '', buffer.expr4 or '',
				])

	def buildValidationErrors(self, dat: DAT):
		dat.clear()
		def addError(path, level, message):
			if dat.numRows == 0:
				dat.appendRow(['path', 'level', 'message'])
			dat.appendRow([path, level, message])
		self._validateVariableReferences(addError)
		self._validateDefTypes(addError)
		if _isInDevelMode() and hasattr(parent, 'raytk'):
			return
		self._validateToolkitVersions(addError)

	def _validateDefTypes(self, addError: 'Callable[[str, str, str], None]'):
		defsTable = self._definitionTable()
		if defsTable.numRows < 2:
			return
		for row in range(1, defsTable.numRows):
			path = defsTable[row, 'path'].val
			for category in ('coordType', 'contextType', 'returnType'):
				val = defsTable[row, category].val
				if not val:
					addError(path, 'error', f'Internal error: No {category} defined in {path}')
				elif ' ' in val and len(val.split()) > 1:
					addError(path, 'error', f'Internal error: Multiple {category} defined: {val} in {path}')

	def _validateToolkitVersions(self, addError: 'Callable[[str, str, str], None]'):
		defsTable = self._definitionTable()
		if defsTable.numRows < 2 or not defsTable[0, 'toolkitVersion']:
			return
		toolkitVersions = {}  # type: dict[str, int]
		for i in range(1, defsTable.numRows):
			version = str(defsTable[i, 'toolkitVersion'] or '')
			if version != '':
				toolkitVersions[version] = 1 + toolkitVersions.get(version, 0)
		if len(toolkitVersions) > 1:
			error = f'Toolkit version mismatch ({", ".join(list(toolkitVersions.keys()))})'
			addError(self.ownerComp.path, 'warning', error)

	def _validateVariableReferences(self, addError: 'Callable[[str, str, str], None]'):
		#  addError params (path, level, message)
		refTable = self._referenceTable()
		if refTable.numRows < 2:
			return
		defTable = self._definitionTable()
		if defTable.numRows < 2:
			return
		checker = _VarRefChecker(self._getOpStates(), defTable, addError)
		checker.loadGraph()
		checker.validateRefs()

	def _getOpStates(self):
		return [
			opDef.getRopState()
			for opDef in self._getOpDefinitions()
		]

	def _getOpDefinitions(self):
		return [
			_getOpDefinitionExt(dat.parent())
			for dat in self.getOpsFromDefinitionColumn('definitionPath')
		]

	def buildTextureTable(self, dat: DAT):
		dat.clear()
		dat.appendRow(['name', 'path', 'type'])
		states = self._getOpStates()
		for state in states:
			if not state.textures:
				continue
			for t in state.textures:
				dat.appendRow([t.name, t.path, t.type])

	def writeShader(
			self,
			dat: scriptDAT,
			macroTable: DAT,
			typeDefMacroTable: DAT,
			outputBufferTable: DAT,
			variableTable: DAT,
			referenceTable: DAT,
	):
		dat.clear()
		dat.write(' ')
		writer = _Writer(
			sb=self,
			rops=[
				_RopContent(opDef, opDef.getRopState())
				for opDef in self._getOpDefinitions()
			],
			defTable=self._definitionTable(),
			paramProc=self._createParamProcessor(),
			macroTable=macroTable,
			typeDefMacroTable=typeDefMacroTable,
			libraryDats=self._getLibraryDats(),
			outputBufferTable=outputBufferTable,
			variableTable=variableTable,
			referenceTable=referenceTable,
		)
		# import cProfile
		# cProfile.runctx('writer.run(dat)', globals(), locals())
		writer.run(dat)

class _VarRefChecker:
	def __init__(
			self,
			opStates: list[RopState],
			definitionTable: DAT,
			addError: 'Callable[[str, str, str], None]'):
		self.opStates = opStates
		self.definitionTable = definitionTable  # used to look up paths by rop name
		self._addError = addError
		self.nodesByName = {}  # type: Dict[str, _GraphROP]
		self.nodesByPath = {}  # type: Dict[str, _GraphROP]

	def addError(self, path, level, message):
		self._addError(path, level, message)

	def loadGraph(self):
		self.nodesByName = {}
		self.nodesByPath = {}
		if not self.opStates:
			return
		# build lookup with a node for each ROP in the graph, without yet filling in full info
		for opState in self.opStates:
			node = _GraphROP(
				opState, inputs={}, outputs=[],
				ownVarGlobalNames={
					v.localName: v.name
					for v in opState.variables
				} if opState.variables else {})
			self.nodesByName[opState.name] = node
			self.nodesByPath[opState.path] = node
		# for each node, fill out the input lookups
		for node in self.nodesByName.values():
			opState = node.state
			# fill out input states for the node
			if opState.inputStates:
				for inputState in opState.inputStates:
					inputNode = _GraphROPInput(
						inputState,
						owner=node,
						ownVarGlobalNames=[],
						varInputs=[],
						source=self.nodesByName.get(inputState.sourceName),
					)
					node.inputs[inputState.functionName] = inputNode
					# fill out the global names of variables from the ROP itself which this input supports
					if inputState.varNames:
						if '*' in inputState.varNames:
							inputNode.ownVarGlobalNames = list(node.ownVarGlobalNames.values())
						else:
							inputNode.ownVarGlobalNames = [
								node.ownVarGlobalNames[localName]
								for localName in inputState.varNames
								if localName in node.ownVarGlobalNames
							]
				# after building the lookup of input nodes, attach the var input sources
				for inputNode in node.inputs.values():
					if inputNode.inputState.varInputNames:
						if '*' in inputNode.inputState.varInputNames:
							inputNode.varInputs = [
								i
								for i in node.inputs.values()
								if i != inputNode
							]
						else:
							varInputNames = []
							for name in inputNode.inputState.varInputNames:
								varInputNames += tdu.expand(name)
							inputNode.varInputs = [
								node.inputs[functionName]
								for functionName in varInputNames
								if functionName != inputNode.inputState.functionName and functionName in node.inputs
							]
		# for each node, fill output lists
		for toNode in self.nodesByName.values():
			if not toNode.inputs:
				continue
			for inputNode in toNode.inputs.values():
				if inputNode.source:
					inputNode.source.outputs.append(inputNode)

	def validateRefs(self):
		for node in self.nodesByName.values():
			self._validateRefsFromNode(node)

	def _validateRefsFromNode(self, node: '_GraphROP'):
		if not node.state.references:
			return
		# print(f'Checking references from {node.state.name}')
		# for each outgoing reference, check the graph along the ROPs outputs for a source
		for reference in node.state.references:
			if reference.category != 'category':
				continue
			# print(f' Checking reference {reference.name}')
			refSourceNode = self.nodesByPath.get(reference.sourcePath)
			if not refSourceNode:
				refSourceGlobalName = None
			else:
				refSourceGlobalName = refSourceNode.ownVarGlobalNames.get(reference.sourceName)
			if not self._validateRefFromNode(
				refOwnerNode=node, reference=reference,
				refSourceGlobalName=refSourceGlobalName):
				path = self.definitionTable[node.state.name, 'path'].val
				self.addError(
					path=path,
					level='error',
					message=f'Variable {reference.sourceName} is not available to {path}')
			# print(' ------ ')

	def _validateRefFromNode(
			self, refOwnerNode: '_GraphROP', reference: Reference, refSourceGlobalName: str) -> bool:
		if not refSourceGlobalName:
			return False
		# Walk downstream from the node to the renderer (tree root)
		# At each stop, it's checking through an input on a node.
		#   Check whether that node provides the variable to that input, if so, done.
		#   For each other input on the node that can provide variables to the target input,
		#     Check that input node and all of its inputs for the variable
		for outInput in refOwnerNode.outputs:
			if self._walkDownstreamForRef(
				refOwnerNode, reference, refSourceGlobalName,
				throughInput=outInput,
				checkedSourceNodes=[]):
				return True

	def _walkDownstreamForRef(
			self,
			refOwnerNode: '_GraphROP', reference: Reference, refSourceGlobalName: str,
			throughInput: '_GraphROPInput',
			checkedSourceNodes: 'list[_GraphROP]') -> bool:
		# print(f'   Walking downstream on {throughInput.source.state.name} looking for {refSourceGlobalName}')
		sourceNode = throughInput.owner
		if sourceNode in checkedSourceNodes:
			# print(f'     Already checked node {sourceNode.state.name}')
			return False
		# print(f'    Own input names to check: {throughInput.ownVarGlobalNames}')
		# print(f'      looking for {refSourceGlobalName}')
		if refSourceGlobalName in throughInput.ownVarGlobalNames:
			# print(
			# 	f'     Node {sourceNode.state.name} input {throughInput.inputState.functionName} \n'
			# 	f'       provides variable {refSourceGlobalName}!!')
			return True
		# print(f'     Inputs to check: ', [i.inputState.functionName for i in throughInput.varInputs] or '---')
		for neighborInput in throughInput.varInputs:
			if not neighborInput.source:
				continue
			if self._walkUpstreamForRef(refOwnerNode, reference, refSourceGlobalName, neighborInput.source, checkedSourceNodes):
				return True
		for outInput in sourceNode.outputs:
			if self._walkDownstreamForRef(refOwnerNode, reference, refSourceGlobalName, outInput, checkedSourceNodes):
				return True
		return False

	def _walkUpstreamForRef(
			self,
			refOwnerNode: '_GraphROP', reference: Reference, refSourceGlobalName: str,
			sourceNode: '_GraphROP',
			checkedSourceNodes: 'list[_GraphROP]') -> bool:
		# print(f'    Walking upstream on {sourceNode.state.name} looking for {refSourceGlobalName}')
		if sourceNode in checkedSourceNodes:
			# print(f'     Already checked node {sourceNode.state.name}')
			return False
		if refSourceGlobalName in sourceNode.ownVarGlobalNames.values():
			# print(
			# 	f'     Node {sourceNode.state.name} provides variable {refSourceGlobalName}!!')
			return True
		for sourceInput in sourceNode.inputs.values():
			if not sourceInput.source:
				continue
			if self._walkUpstreamForRef(
					refOwnerNode, reference, refSourceGlobalName,
					sourceInput.source, checkedSourceNodes):
				return True
		return False

@dataclass
class _GraphROP:
	state: RopState
	inputs: 'Dict[str, _GraphROPInput]' = None
	outputs: 'list[_GraphROPInput]' = None
	ownVarGlobalNames: Dict[str, str] = None  # local name -> global name

@dataclass
class _GraphROPInput:
	inputState: InputState
	owner: '_GraphROP'
	ownVarGlobalNames: list[str]
	varInputs: 'list[_GraphROPInput]'
	source: 'Optional[_GraphROP]' = None

@dataclass
class _Writer:
	sb: 'ShaderBuilder'
	rops: 'list[_RopContent]'
	defTable: DAT
	paramProc: '_ParameterProcessor'
	macroTable: DAT
	typeDefMacroTable: DAT
	libraryDats: list[DAT]
	outputBufferTable: DAT
	variableTable: DAT
	referenceTable: DAT

	inlineTypedefRepls: 'Optional[Dict[str, str]]' = None
	inlineTypedefPattern: 'Optional[re.Pattern]' = None
	textures: 'Optional[list[Texture]]' = None
	buffers: 'Optional[list[Buffer]]' = None
	attributes: 'Optional[list[SurfaceAttribute]]' = None
	onlyNames: set[str] | None = None
	out: 'Optional[StringIO]' = None

	def __post_init__(self):
		self.out = StringIO()
		self.configPar = self.sb.configPar() if self.sb.configValid() else None
		self.ownerComp = self.sb.ownerComp
		if self.configPar and self.configPar['Inlinetypedefs'] and self.typeDefMacroTable.numRows > 1:
			self.inlineTypedefRepls = {
				str(cells[0]): str(cells[1])
				for cells in self.typeDefMacroTable.rows()
				if cells[1]
			}
			self.inlineTypedefPattern = re.compile(r'\b[\w_]+_(as)?(CoordT|ContextT|ReturnT|VarT)\b')
		self.textures = []
		self.buffers = []
		names = tdu.split(self.ownerComp.par.Limitcodetonames)
		self.onlyNames = set(names) if names else None
		attrNames = set()
		attrRefNames = [
			self.referenceTable[i, 'source'].val
			for i in range(1, self.referenceTable.numRows)
			if self.referenceTable[i, 'category'] == 'attribute' and
					self._shouldIncludeOp(self.referenceTable[i, 'owner'].val)
		]
		self.attributes = []
		for rop in self.rops:
			rop.included = self._shouldIncludeOp(rop.definition.name)
			if not rop.included:
				continue
			state = rop.state
			if state.textures:
				self.textures += state.textures
			if state.buffers:
				self.buffers += state.buffers
			if state.attributes:
				for attribute in state.attributes:
					if attribute.name not in attrRefNames or attribute.name in attrNames:
						continue
					attrNames.add(attribute.name)
					self.attributes.append(attribute)

	def _shouldIncludeOp(self, name: str):
		if not self.onlyNames:
			return True
		return name in self.onlyNames

	def run(self, dat: scriptDAT):
		if self.defTable.numRows < 2:
			self._writeLine('#error No input definition')
			return
		self._writeGlobalDecls()
		self._writeOpDataTypedefs()
		self._writeMacroBlock()
		self._writeAttributesBlock()
		self._writeLibraryIncludes()
		self._writeCodeDat('predeclarations', self.ownerComp.par.Predeclarations.eval())
		self._writeParameterAliases()
		self._writeTextureDeclarations()
		self._writeBufferDeclarations()
		self._writeMaterialDeclarations()
		self._writeOutputBufferDeclarations()
		self._writeVariableDeclarations()

		self._writeOutputInit()
		self._writeOpGlobals()
		self._writeInit()
		self._writeFunctions()
		self._writeBody()

		dat.clear()
		dat.write(self.out.getvalue())
	def _writeGlobalDecls(self):
		self._startBlock('globals')
		shaderType = self.ownerComp.par.Shadertype.eval()
		if shaderType != 'glslpop':
			self._writeLines(self.paramProc.globalDeclarations())
		if shaderType == 'vertexstage' or shaderType == 'pixelstage':
			pass
		else:
			mainName = self.defTable[-1, 'name']
			self._writeLine(f'#define thismap {mainName}')
		self._endBlock('globals')

	def _writeOpDataTypedefs(self):
		inline = self.configPar and self.configPar['Inlinetypedefs']
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

	def _writeAttributesBlock(self):
		self._startBlock('attributes')
		if self.attributes:
			self._writeMacro('RAYTK_HAS_ATTRS')
			for attr in self.attributes:
				self._writeMacro(f'RAYTK_HAS_ATTR_{attr.name}')
			self._writeLine('struct Attrs {')
			for attr in self.attributes:
				self._writeLine(f'  {attr.dataType} {attr.name};')
			self._writeLine('};')
			self._writeLine('void initAttrs(inout Attrs a) {')
			for attr in self.attributes:
				self._writeLine(f'  a.{attr.name} = {attr.dataType}(0.);')
			self._writeLine('}')
			self._writeLine('void mixAttrs(inout Attrs a, in Attrs b, float amt) {')
			for attr in self.attributes:
				self._writeLine(f'  a.{attr.name} = mix(a.{attr.name}, b.{attr.name}, amt);')
			self._writeLine('}')
		self._endBlock('attributes')

	def _writeLibraryIncludes(self):
		if not self.libraryDats:
			return
		self._startBlock('libraries')
		mode = str((self.configPar and self.configPar['Includemode']) or 'includelibs')
		if mode == 'inlineall':
			for lib in self.libraryDats:
				self._writeLine(f'/// Library: <{lib.path}>')
				self._writeLine(lib.text)
		else:
			for lib in self.libraryDats:
				self._writeLine(f'#include <{lib.path}>')
		self._endBlock('libraries')

	def _writeParameterAliases(self):
		decls = self.paramProc.paramAliases()
		if not decls:
			return
		self._startBlock('paramAliases')
		self._writeLines(decls)
		self._endBlock('paramAliases')

	def _writeTextureDeclarations(self):
		if not self.textures:
			return
		indexByType: 'dict[str, int]' = {
			'2d': int(self.ownerComp.par.Textureindexoffset),
			'3d': int(self.ownerComp.par.Texture3dindexoffset),
			'cube': 0,
			'2darray': int(self.ownerComp.par.Texture2darrayindexoffset),
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
		for texture in self.textures:
			texType = texture.type or '2d'
			if texType not in indexByType:
				raise Exception(f'Invalid texture type for {texture.name}: {texType!r}')
			index = indexByType[texType]
			indexByType[texType] = index + 1
			self._writeMacro(texture.name, f'{arrayByType[texType]}[{index}]')
			self._writeMacro(texture.name + '_info', f'{infoByType[texType]}[{index}]')
		self._endBlock('textures')

	def _writeBufferDeclarations(self):
		if not self.buffers:
			return
		self._startBlock('buffers')
		for buffer in self.buffers:
			if buffer.uniformType == 'uniformarray':
				if buffer.length is None:
					c = op(buffer.chop)
					n = c.numSamples if c else 1
				else:
					n = buffer.length
				self._writeLine(f'uniform {buffer.type} {buffer.name}[{n}];')
			elif buffer.uniformType == 'texturebuffer':
				self._writeLine(f'uniform samplerBuffer {buffer.name};')
		self._endBlock('buffers')

	def _writeMaterialDeclarations(self):
		if not self.ownerComp.par.Supportmaterials:
			return
		self._startBlock('materials')
		i = 1001
		for rop in self.rops:
			state = rop.state
			if state.materialId:
				self._writeMacro(state.materialId, i)
				i += 1
		self._endBlock('materials')

	def _writeOutputBufferDeclarations(self):
		if self.outputBufferTable.numRows < 2:
			return
		self._startBlock('outputBuffers')
		if self.ownerComp.par.Shadertype == 'compute':
			for name in self.outputBufferTable.col('name')[1:]:
				self._writeMacro(name, f'mTDComputeOutputs[{name.row - 1}]')
		else:
			for name in self.outputBufferTable.col('name')[1:]:
				self._writeLine(f'layout(location = {name.row - 1}) out vec4 {name};')
		self._endBlock('outputBuffers')

	def _writeVariableDeclarations(self):
		if self.variableTable.numRows < 2:
			return
		self._startBlock('variables')
		for i in range(1, self.variableTable.numRows):
			name = self.variableTable[i, 'name']
			dataType = self.variableTable[i, 'dataType']
			self._writeLine(f'{dataType} {name};')
		self._endBlock('variables')

	def _writeOutputInit(self):
		if self.ownerComp.par.Shadertype == 'compute' or self.outputBufferTable.numRows < 2:
			return
		self._startBlock('outputInit')
		self._writeLine('void initOutputs() {')
		for name in self.outputBufferTable.col('name')[1:]:
			self._writeLine(f'{name} = vec4(0.);')
		self._writeLine('}')
		self._endBlock('outputInit')

	def _writeOpGlobals(self):
		self._writeCodeBlocks('opGlobals', [
			rop.definition.getOpGlobals()
			for rop in self.rops
			if rop.included
		])

	def _writeInit(self):
		self._writeCodeBlocks(
			'init',
			[
				rop.definition.getInitCode()
				for rop in self.rops
				if rop.included
			],
			prefixes=[
				'#define RAYTK_HAS_INIT',
				'void init() {',
			],
			suffixes=['}'])

	def _writeFunctions(self):
		self._writeCodeBlocks('functions', [
			rop.definition.getFunctionCode()
			for rop in self.rops
			if rop.included
		])

	def _writeCodeBlocks(
			self, section: str, blocks: list[str],
			prefixes: list[str] = None, suffixes: list[str] = None
	):
		if not blocks:
			return
		self._startBlock(section)
		if prefixes:
			self._writeLines(prefixes)
		for block in blocks:
			if not block:
				continue
			self._writeLine(self._processCode(block))
		if suffixes:
			self._writeLines(suffixes)
		self._endBlock(section)

	def _writeBody(self):
		dat = self.ownerComp.par.Bodytemplate.eval()
		if not dat:
			return
		self._startBlock('body')
		code = self._inlineTypedefs(dat.text)
		for line in code.splitlines(keepends=True):
			if line.endswith('// #include <materialParagraph>\n'):
				self._writeMaterialBody()
			else:
				self._write(line)
		self._endBlock('body')

	def _writeMaterialBody(self):
		for rop in self.rops:
			state = rop.state
			if not state.materialId or not rop.included:
				continue
			self._writeLine(f'else if(m == {state.materialId}) {{')
			# Intentionally skipping typedef inlining for these since no materials need it.
			self._writeLine(rop.definition.getMaterialCode() + '\n}')

	def _write(self, arg):
		self.out.write(arg)

	def _writeLine(self, line: str):
		self.out.write(line)
		self.out.write('\n')

	def _writeLines(self, lines: list[str] | None):
		if lines:
			for line in lines:
				self.out.write(line)
				self.out.write('\n')

	def _writeMacro(self, name: 'Union[str, Cell]', val: 'Union[str, Cell, None, int]' = None):
		if val == '' or val is None:
			self._writeLine(f'#define {name}')
		else:
			self._writeLine(f'#define {name} {val}')

	def _startBlock(self, name: str):
		self._writeLine(f'///----BEGIN {name}')

	def _endBlock(self, name: str):
		self._writeLine(f'///----END {name}')

	def _writeCodeDat(self, blockName: str, dat: DAT | None):
		if not dat or not dat.text:
			return
		self._startBlock(blockName)
		self._writeLine(self._processCode(dat.text))
		self._endBlock(blockName)

	def _replaceInlineTypedefMatch(self, m: 're.Match'):
		return self.inlineTypedefRepls.get(m.group(0)) or m.group(0)

	def _inlineTypedefs(self, code: 'str'):
		if not self.inlineTypedefRepls:
			return code
		return self.inlineTypedefPattern.sub(self._replaceInlineTypedefMatch, code)

	def _processCode(self, code: str):
		return self._inlineTypedefs(code)

@dataclass
class _RopContent:
	definition: 'OpDefinition'
	state: RopState
	included: bool = True

@dataclass
class _ParamTupletSpec:
	tuplet: str
	parts: tuple[str]
	ownerName: str
	isReadOnly: bool
	isSpecial: bool = False
	isSpecializationConstant: bool = False
	isRuntime: bool = True
	sourceVectorPath: str | None = None
	sourceVectorIndex: int | None = None

	def isPresentInChop(self, chop: 'CHOP'):
		return any([chop[part] is not None for part in self.parts])

	@classmethod
	def fromRow(cls, dat: DAT, row: int):
		parts = []
		for i in range(1, 5):
			cell = dat[row, 'part' + str(i)]
			if not cell.val:
				break
			parts.append(cell.val)
		handling = dat[row, 'handling']
		vecPath = dat[row, 'sourceVectorPath']
		vecIndex = dat[row, 'sourceVectorIndex']
		if handling == 'runtime' and vecPath != '' and vecIndex != '':
			vecPath = str(vecPath)
			vecIndex = int(vecIndex)
		else:
			vecPath = None
			vecIndex = None
		return cls(
			tuplet=str(dat[row, 'tuplet']),
			parts=tuple(parts),
			ownerName=str(dat[row, 'ownerName']),
			isReadOnly='readOnly' in str(dat[row, 'status'] or ''),
			isSpecial=dat[row, 'source'] == 'special',
			isSpecializationConstant=handling == 'constant',
			isRuntime=handling == 'runtime',
			sourceVectorPath=vecPath,
			sourceVectorIndex=vecIndex,
		)

	@classmethod
	def fromTableRows(cls, dat: DAT, handlingTypes: list[str]) -> 'list[_ParamTupletSpec]':
		if not dat or dat.numRows < 2:
			return []
		return [
			cls.fromRow(dat, row)
			for row in range(1, dat.numRows)
			if dat[row, 'handling'].val in handlingTypes
		]

@dataclass
class _ParamExpr:
	expr: Union[str, float]
	type: str

@dataclass
class _UniformSpec:
	name: str
	dataType: str  # float | vec2 | vec3 | vec4 | int | bool
	uniformType: str  # vector | uniformarray | constant
	arrayLength: int = 1
	chop: str | None = None
	expr1: str | None = None
	expr2: str | None = None
	expr3: str | None = None
	expr4: str | None = None
	constIndex: int = 0

	def declaration(self):
		if self.uniformType == 'vector':
			return f'uniform {self.dataType} {self.name};'
		elif self.uniformType == 'uniformarray':
			return f'uniform {self.dataType} {self.name}[{self.arrayLength}];'
		elif self.uniformType == 'constant':
			if self.dataType == 'int':
				defVal = '0'
			elif self.dataType == 'float':
				defVal = '0.0'
			elif self.dataType == 'bool':
				defVal = 'false'
			else:
				raise Exception(f'Invalid data type for specialization constant: {self.dataType}')
			return f'layout(constant_id = {self.constIndex}) const {self.dataType} {self.name} = {defVal};'
		else:
			raise Exception(f'Invalid uniformType: {self.uniformType!r}')

_paramAliasPattern = re.compile(r'\bRTK_\w+\b')

class _ParameterProcessor:
	def __init__(
			self,
			paramDetailTable: DAT,
			paramVals: 'CHOP',
			configPar: 'Optional[_ConfigPar]',
			opStates: 'list[RopState]',
			shaderType: str,
	):
		self.paramDetailTable = paramDetailTable
		self.hasParams = paramDetailTable.numRows > 1
		self.paramVals = paramVals
		self.useConstantReadOnly = configPar.Inlinereadonlyparameters if configPar else False
		self.aliasMode = str(configPar['Paramaliasmode'] or 'macro') if configPar else 'macro'
		self.paramExprs = None  # type: Optional[Dict[str, _ParamExpr]]
		self.opStates = opStates
		self.shaderType = shaderType

	def globalDeclarations(self) -> list[str]:
		return [
			spec.declaration()
			for spec in self.paramUniforms()
		]

	def _initParamExprs(self):
		if self.paramExprs is not None:
			return
		paramTuplets = _ParamTupletSpec.fromTableRows(
			self.paramDetailTable,
			handlingTypes=['runtime', 'macro'])
		self.paramExprs = {}
		self._addParamExprs(paramTuplets)

	def _shouldUseConstant(self, paramTuplet: _ParamTupletSpec):
		return self.useConstantReadOnly and paramTuplet.isReadOnly and paramTuplet.isPresentInChop(self.paramVals)

	def _addParamExprs(self, paramTuplets: list[_ParamTupletSpec]):
		raise NotImplementedError()

	def paramAliases(self) -> list[str]:
		if not self.hasParams:
			return []
		self._initParamExprs()
		if self.aliasMode == 'globalvar':
			return [
				f'{paramExpr.type} {name} = {paramExpr.expr};'
				for name, paramExpr in self.paramExprs.items()
			]
		else:  # self.aliasMode == 'macro'
			return [
				f'#define {name} {expr.expr}'
				for name, expr in self.paramExprs.items()
			]

	def paramUniforms(self) -> list[_UniformSpec]:
		raise NotImplementedError()

	def _constantParamUniforms(self) -> list[_UniformSpec]:
		uniforms = []
		constCount = 0
		constPath = 'constant_param_vals'
		for opState in self.opStates:
			if opState.constants:
				for const in opState.constants:
					uniforms.append(_UniformSpec(
						name=const.name,
						dataType=const.type,
						uniformType='constant',
						expr1=f'op("{constPath}")["{const.name}"]',
						constIndex=constCount
					))
					constCount += 1
		return uniforms

class _SingleArrayParameterProcessor(_ParameterProcessor):
	def _addParamExprs(self, paramTuplets: list[_ParamTupletSpec]):
		suffixes = 'xyzw'
		for paramTupletIndex, paramTuplet in enumerate(paramTuplets):
			useConstant = self._shouldUseConstant(paramTuplet)
			size = len(paramTuplet.parts)
			if self.shaderType == 'glslpop':
				paramRef = f'texelFetch(vecParams, {paramTupletIndex})'
			else:
				paramRef = f'vecParams[{paramTupletIndex}]'
			if size == 1:
				name = paramTuplet.parts[0]
				self.paramExprs[name] = _ParamExpr(
					repr(float(self.paramVals[name])) if useConstant else f'{paramRef}.x',
					'float'
				)
			else:
				if useConstant:
					partVals = [float(self.paramVals[part]) for part in paramTuplet.parts]
					valsExpr = ','.join(str(v) for v in partVals)
					parType = f'vec{size}'
					self.paramExprs[paramTuplet.tuplet] = _ParamExpr(f'{parType}({valsExpr})', parType)
					for partI, partName in enumerate(paramTuplet.parts):
						self.paramExprs[partName] = _ParamExpr(f'{paramTuplet.tuplet}.{suffixes[partI]}', 'float')
				else:
					if size == 4:
						self.paramExprs[paramTuplet.tuplet] = _ParamExpr(paramRef, 'vec4')
					else:
						parType = f'vec{size}'
						self.paramExprs[paramTuplet.tuplet] = _ParamExpr(
							f'{parType}({paramRef}.{suffixes[:size]})',
							parType
						)
					for partI, partName in enumerate(paramTuplet.parts):
						self.paramExprs[partName] = _ParamExpr(f'{paramRef}.{suffixes[partI]}', 'float')

	def paramUniforms(self) -> list[_UniformSpec]:
		paramCount = max(1, self.paramDetailTable.numRows - 1)
		uniforms = [
			_UniformSpec(
				'vecParams', 'vec4',
				'uniformarray' if self.shaderType != 'glslpop' else 'texturebuffer',
				paramCount,
				'merged_vector_param_vals'
			)
		]
		uniforms += self._constantParamUniforms()
		return uniforms

class _SeparateArrayParameterProcessor(_ParameterProcessor):
	opRuntimeTupletsByName: dict[str, '_OpRuntimeTupletSpecs'] | None = None

	def _addParamExprs(self, paramTuplets: list[_ParamTupletSpec]):
		self._loadRuntimeTuplets(paramTuplets)
		suffixes = 'xyzw'
		for paramTuplet in paramTuplets:
			useConstant = self._shouldUseConstant(paramTuplet)
			if not useConstant and paramTuplet.isRuntime:
				# these are handled below with opRuntimeTupletsByName
				continue
			size = len(paramTuplet.parts)
			if size == 1:
				name = paramTuplet.parts[0]
				self.paramExprs[name] = _ParamExpr(
					repr(float(self.paramVals[name])),
					'float')
			else:
				partVals = [float(self.paramVals[part]) for part in paramTuplet.parts]
				valsExpr = ','.join(str(v) for v in partVals)
				parType = f'vec{size}'
				self.paramExprs[paramTuplet.tuplet] = _ParamExpr(f'{parType}({valsExpr})', parType)
				for partI, partName in enumerate(paramTuplet.parts):
					self.paramExprs[partName] = _ParamExpr(f'{paramTuplet.tuplet}.{suffixes[partI]}', 'float')
		for opState in self.opStates:
			opTupletSpecs = self.opRuntimeTupletsByName.get(opState.name)
			if opTupletSpecs is None:
				continue
			for paramTuplet in opTupletSpecs.tuplets:
				size = len(paramTuplet.parts)
				if size == 1:
					name = paramTuplet.parts[0]
					if self.shaderType == 'glslpop':
						self.paramExprs[name] = _ParamExpr(
							f'texelFetch({opTupletSpecs.uniformName}, {paramTuplet.sourceVectorIndex}).x',
							'float')
					else:
						self.paramExprs[name] = _ParamExpr(
							f'{opTupletSpecs.uniformName}[{paramTuplet.sourceVectorIndex}].x',
							'float')
				else:
					parType = f'vec{size}'
					if self.shaderType == 'glslpop':
						self.paramExprs[paramTuplet.tuplet] = _ParamExpr(
							f'{parType}(texelFetch({opTupletSpecs.uniformName}, {paramTuplet.sourceVectorIndex}).{suffixes[:size]})',
							parType)

					else:
						self.paramExprs[paramTuplet.tuplet] = _ParamExpr(
							f'{parType}({opTupletSpecs.uniformName}[{paramTuplet.sourceVectorIndex}].{suffixes[:size]})',
							parType)
						for partI, partName in enumerate(paramTuplet.parts):
							self.paramExprs[partName] = _ParamExpr(
								f'{opTupletSpecs.uniformName}[{paramTuplet.sourceVectorIndex}].{suffixes[partI]}',
								'float')

	def _loadRuntimeTuplets(self, paramTuplets: list[_ParamTupletSpec]):
		self.opRuntimeTupletsByName = {}
		for paramTuplet in paramTuplets:
			if not paramTuplet.isRuntime:
				continue
			useConstant = self._shouldUseConstant(paramTuplet)
			if useConstant:
				continue
			opTupletSpecs = self.opRuntimeTupletsByName.get(paramTuplet.ownerName)
			if not opTupletSpecs:
				opTupletSpecs = _OpRuntimeTupletSpecs(
					opName=paramTuplet.ownerName,
					sourcePath=paramTuplet.sourceVectorPath,
					uniformName=paramTuplet.ownerName + '_vecParams',
					tuplets=[],
				)
				self.opRuntimeTupletsByName[paramTuplet.ownerName] = opTupletSpecs
			opTupletSpecs.tuplets.append(paramTuplet)
		for opTupletSpecs in self.opRuntimeTupletsByName.values():
			opTupletSpecs.arrayLength = 1 + max(pt.sourceVectorIndex for pt in opTupletSpecs.tuplets)

	def paramUniforms(self) -> list[_UniformSpec]:
		self._initParamExprs()
		uniforms = []
		for opState in self.opStates:
			opTupleSpecs = self.opRuntimeTupletsByName.get(opState.name)
			if opTupleSpecs is None:
				continue
			uniforms.append(_UniformSpec(
				name=opTupleSpecs.uniformName,
				dataType='vec4',
				uniformType='uniformarray' if self.shaderType != 'glslpop' else 'texturebuffer',
				arrayLength=opTupleSpecs.arrayLength,
				chop=opTupleSpecs.sourcePath,
			))
		uniforms += self._constantParamUniforms()
		return uniforms

@dataclass
class _OpRuntimeTupletSpecs:
	opName: str
	sourcePath: str
	tuplets: list[_ParamTupletSpec]
	uniformName: str | None = None
	arrayLength: int | None = None

def _stringify(val: 'Union[str, DAT]'):
	if val is None:
		return ''
	if isinstance(val, DAT):
		return val.text
	return str(val)

def _combineCode(code: str | DAT | list[str | DAT]):
	if isinstance(code, list):
		combined = ''
		for item in code:
			val = _stringify(item)
			if val:
				combined += val + '\n'
		return combined
	else:
		return _stringify(code)

def wrapCodeSection(code: str | DAT | list[str | DAT], name: str):
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

def _isInDevelMode():
	return hasattr(op, 'raytk') and bool(op.raytk.par['Devel'])

def _getOpDefinitionExt(opDefComp: COMP):
	if hasattr(opDefComp.ext, 'opDefinition'):
		return opDefComp.ext.opDefinition
	opDefComp.par.reinitextensions.pulse()
	if hasattr(opDefComp.ext, 'opDefinition'):
		return opDefComp.ext.opDefinition
	debug(f'UNABLE TO ACCESS OPDEF EXT: {opDefComp}')
	return OpDefinition(opDefComp)
