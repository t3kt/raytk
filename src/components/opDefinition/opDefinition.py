from typing import Dict, Any

import json
import math
from raytkState import *
import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from raytkUtil import OpDefParsT

def parentPar() -> 'ParCollection | OpDefParsT':
	return parent().par

def _host() -> COMP | None:
	return parentPar().Hostop.eval()

def buildName():
	host = _host()
	if not host:
		return ''
	pathParts = host.path[1:].split('/')
	for i in range(len(pathParts)):
		if pathParts[i].startswith('_'):
			pathParts[i] = 'U' + pathParts[i][1:]
	name = '_'.join(pathParts)
	name = re.sub('_+', '_', name)
	if name.startswith('_'):
		name = 'o_' + name
	return 'RTK_' + name

def _evalType(category: str, supportedTypes: DAT, inputDefs: DAT):
	spec = supportedTypes[category, 'spec'].val
	if spec.startswith('@'):
		return spec
	inputCell = inputDefs[1, category]
	if spec.startswith('useinput|') and inputCell:
		return inputCell
	return supportedTypes[category, 'types']

def buildTypeTable(dat: scriptDAT, supportedTypes: DAT, inputDefs: DAT):
	dat.clear()
	dat.appendRows([
		['coordType', _evalType('coordType', supportedTypes, inputDefs)],
		['returnType', _evalType('returnType', supportedTypes, inputDefs)],
		['contextType', _evalType('contextType', supportedTypes, inputDefs)],
	])

def combineInputDefinitions(dat: scriptDAT, inDats: list[DAT], defFields: DAT, supportedTypeTable: DAT):
	dat.clear()
	inDats += parentPar().Inputdefs.evalOPs()
	if not inDats:
		return
	cols = defFields.col(0) + ['input:handler']
	dat.appendRow(cols)
	inDats = [d for d in inDats if d.numRows > 1]
	if not inDats:
		return
	usedNames = set()
	for d in reversed(inDats):
		insertRow = 0
		for inDatRow in range(1, d.numRows):
			name = d[inDatRow, 'name']
			if not name or name.val in usedNames:
				continue
			usedNames.add(name.val)
			dat.appendRow([d[inDatRow, col] or '' for col in cols], insertRow)
			insertRow += 1
	_processInputDefTypeCategory(dat, supportedTypeTable, 'coordType')
	_processInputDefTypeCategory(dat, supportedTypeTable, 'contextType')
	_processInputDefTypeCategory(dat, supportedTypeTable, 'returnType')

def _processInputDefTypeCategory(dat: scriptDAT, supportedTypeTable: DAT, category: str):
	supported = supportedTypeTable[category, 'types'].val.split(' ')
	cells = dat.col(category)
	if not cells:
		return
	errors = []
	for cell in cells[1:]:
		inputTypes = cell.val.split(' ')
		supportedInputTypes = [t for t in inputTypes if t in supported]
		if not supportedInputTypes:
			errors.append(f'No supported {category} for {dat[cell.row, "name"]} ({" ".join(inputTypes)}')
		elif len(supportedInputTypes) == 1:
			cell.val = supportedInputTypes[0]
		else:
			cell.val = '@' + parentPar().Name.eval()

def _getParamsOp() -> COMP | None:
	return parentPar().Paramsop.eval() or _host()

def _getRegularParams(specs: list[str]) -> list[Par]:
	host = _getParamsOp()
	if not host:
		return []
	paramNames = tdu.expand(str(' '.join(specs)).strip())
	if not paramNames:
		return []
	return [
		p
		for p in host.pars(*[pn.strip() for pn in paramNames])
		if p.isCustom and p.name != 'Inspect'
	]

def _canBeReadOnlyTuplet(pars: list[Par]):
	return all(p.readOnly and p.mode == ParMode.CONSTANT for p in pars)

def _getTupletName(parts: list[str]):
	if len(parts) <= 1 or len(parts[0]) <= 1:
		return None
	prefix = parts[0][:-1]
	for part in parts[1:]:
		if not part.startswith(prefix):
			return None
	return prefix

# Builds table with parameter local names, for select CHOPs.
def buildParamChopNamesTable(dat: DAT):
	dat.clear()
	regularNames = []
	specialNames = []
	angleNames = []
	constantNames = []
	state = _parseOpState()
	for paramSpec in state.params:
		if paramSpec.handling == 'macro':
			continue
		name = paramSpec.localName
		source = paramSpec.source
		if paramSpec.handling == 'constant':
			if source != 'param':
				raise Exception(f'Constants must come from parameters {name} {source}')
			else:
				constantNames.append(name)
		elif source == 'param':
			regularNames.append(name)
		elif source == 'special':
			specialNames.append(name)
		if paramSpec.conversion == 'angle':
			angleNames.append(name)
	dat.appendRow(['regular', ' '.join(regularNames)])
	dat.appendRow(['special', ' '.join(specialNames)])
	dat.appendRow(['angle', ' '.join(angleNames)])
	dat.appendRow(['constant', ' '.join(constantNames)])
	part1Names = []
	part2Names = []
	part3Names = []
	part4Names = []
	for paramTuplet in state.paramTuplets:
		if paramTuplet.handling != 'runtime':
			continue
		part1Names.append(paramTuplet.part1 or '_')
		part2Names.append(paramTuplet.part2 or '_')
		part3Names.append(paramTuplet.part3 or '_')
		part4Names.append(paramTuplet.part4 or '_')
	dat.appendRow(['regularPart1', ' '.join(part1Names)])
	dat.appendRow(['regularPart2', ' '.join(part2Names)])
	dat.appendRow(['regularPart3', ' '.join(part3Names)])
	dat.appendRow(['regularPart4', ' '.join(part4Names)])

def buildValidationErrors(
		errorDat: scriptDAT,
		inputDefinitions: DAT,
		elementValidationErrors: list[DAT]):
	errorDat.clear()
	errorDat.appendRow(['path', 'level', 'message'])
	_validateReferences(errorDat)
	_validateInputs(errorDat, inputDefinitions)
	for dat in elementValidationErrors:
		errorDat.appendRows(dat.rows()[1:])

def _validateReferences(errorDat: scriptDAT):
	path = parent().path
	table = parentPar().Referencetable.eval()
	if not table or table.numRows < 2:
		return []
	for i in range(1, table.numRows):
		localName = str(table[1, 'name'])
		if localName == 'none' or not localName:
			continue
		sourcePath = table[i, 'sourcePath']
		if not sourcePath:
			continue
		sourceOp = op(sourcePath)
		if not sourceOp:
			errorDat.appendRow([path, 'error', f'Invalid source path for reference {localName}'])

def _validateInputs(dat: scriptDAT, inputDefinitions: DAT):
	if hasattr(parent, 'raytk'):
		return
	for handlerPath in inputDefinitions.col('input:handler')[1:]:
		handler = op(handlerPath)
		if not handler:
			continue
		errors, warnings = _validateInput(handler)
		for error in errors:
			if error:
				dat.appendRow([handlerPath, 'error', error])
		for warning in warnings:
			if warning:
				dat.appendRow([handlerPath, 'warning', warning])

def _validateInput(handler: COMP):
	inputDef = handler.op('inputDefinition')
	errors = [
		_checkInputType(handler, str(inputDef[1, 'coordType'] or ''), 'coordType'),
		_checkInputType(handler, str(inputDef[1, 'contextType'] or ''), 'contextType'),
		_checkInputType(handler, str(inputDef[1, 'returnType'] or ''), 'returnType'),
		'Required input is missing' if handler.par.Required and inputDef.numRows < 2 else None,
	]
	warnings = [
		'Input is not supported due to current operator settings and/or other connected inputs' if handler.par.Prohibited and inputDef.numRows > 1 else None,
	]
	return errors, warnings

def _checkInputType(handler: COMP, typeName: str, typeCategory: str):
	if not typeName:
		return
	supported = tdu.split(handler.op('supportedTypes')[typeCategory, 'types'] or '')
	if ' ' in typeName:
		if any(t in supported for t in typeName.split(' ')):
			return
	elif typeName in supported:
		return
	return f'Input does not support {typeCategory} {typeName}'

def onValidationChange(dat: DAT):
	host = _host()
	if not host or host.par.clone == host:
		return
	host.clearScriptErrors()
	if dat.numRows < 2:
		return
	cells = dat.col('message')
	if not cells:
		return
	err = '\n'.join([c.val for c in cells])
	host.addScriptError(err)

def onHostNameChange():
	# See issue #295
	op('sel_funcTemplate').cook(force=True)

def _createBuilder():
	return _Builder(parent())

def buildOpState():
	builder = _createBuilder()
	builder.load()
	return builder.opState

class _Builder:
	defPar: 'OpDefParsT'
	hostOp: COMP
	paramsOp: COMP
	inDats: list[DAT]
	opName: str
	namePrefix: str
	opState: RopState
	replacements: dict[str, str]
	elementReplacements: dict[str, str]

	def __init__(self, opDefComp: COMP):
		# noinspection PyTypeChecker
		self.defPar = opDefComp.par  # type: OpDefParsT
		self.hostOp = self.defPar.Hostop.eval()
		self.paramsOp = self.defPar.Paramsop.eval() or self.hostOp
		self.inDats = opDefComp.ops('input_def_[0-9]*')
		fullOpType = self.defPar.Raytkoptype.eval()
		opType = fullOpType
		if opType and '.' in opType:
			opType = opType.rsplit('.', maxsplit=1)[1]
		self.opState = RopState(
			name=self.defPar.Name.eval(),
			path=self.hostOp.path if self.hostOp else None,
			ropType=opType,
			ropFullType=fullOpType,
		)
		self.opName = self.opState.name
		self.namePrefix = self.opName + '_'
		if self.defPar.Materialcode:
			self.opState.materialId = 'MAT_' + self.opState.name
		self.replacements = {'thismap': self.opName, 'THIS_': self.namePrefix}
		if opType:
			self.replacements['THISTYPE_'] = opType + '_'
		if self.opState.materialId:
			self.replacements['THISMAT'] = self.opState.materialId
		self.elementReplacements = {}

	def load(self):
		self.loadInputs()
		self.loadTags()
		self.loadOpElements()
		self.loadParams()
		self.loadCode()
		self.loadMacros()
		self.loadConstants()
		self.loadTextures()
		self.loadBuffers()
		self.loadReferences()
		self.loadVariablesAndAttributes()

	def loadInputs(self):
		self.opState.inputStates = []
		for i, inDat in enumerate(self.inDats + self.defPar.Inputdefs.evalOPs()):
			if not inDat[1, 'name']:
				continue
			func = str(inDat[1, 'input:alias'] or f'inputOp{i + 1}')
			placeholder = f'inputOp_{func}' if not func.startswith('inputOp') else func
			name = str(inDat[1, 'name'])
			inputState = InputState(
				functionName=func,
				sourceName=name,
				placeholder=placeholder,
				varNames=tdu.split(inDat[1, 'input:vars']),
				varInputNames=tdu.split(inDat[1, 'input:varInputs']),
				tags=tdu.split(inDat[1, 'tags'] or ''),
				coordType=tdu.split(inDat[1, 'coordType']),
				contextType=tdu.split(inDat[1, 'contextType']),
				returnType=tdu.split(inDat[1, 'returnType']),
			)
			self.replacements[placeholder] = name
			self.opState.inputStates.append(inputState)

	def loadTags(self):
		tags = set()
		for inputState in self.opState.inputStates:
			if inputState.tags:
				tags.update(inputState.tags)
		table = parentPar().Tagtable.eval()
		if table and table.numRows > 1:
			for i in range(1, table.numRows):
				if _isFalseStr(table[i, 'enable']):
					continue
				tags.add(table[i, 'name'].val)
		self.opState.tags = list(sorted(tags))

	def loadOpElements(self):
		if not self.hostOp:
			return
		elements = self.hostOp.ops('*/opElement')
		if not elements:
			return
		self.opState.opElements = []
		elements.sort(key=lambda e: e.path)
		for element in elements:
			elementRoot = op(element.par['Elementroot'] or element.parent())
			codeReplacements = {}
			def replace(placeholderPar: Par, codePar: Par):
				if not placeholderPar:
					return
				placeholder = placeholderPar.eval()
				codeDat = codePar.eval()
				code = codeDat.text if codeDat else ''
				codeReplacements[placeholder] = code
				self.elementReplacements[placeholder] = code
			replace(element.par['Placeholder1'], element.par['Code1'])
			replace(element.par['Placeholder2'], element.par['Code2'])
			replace(element.par['Placeholder3'], element.par['Code3'])
			replace(element.par['Placeholder4'], element.par['Code4'])
			elementState = OpElementState(
				elementRoot=elementRoot.path,
				isNested=elementRoot is not element.parent(),
				paramGroupTable=str(element.par['Paramgrouptable'] or ''),
				macroTable=str(element.par['Macrotable'] or ''),
				codeReplacements=codeReplacements,
			)

			self.opState.opElements.append(elementState)

	def loadParams(self):
		self.opState.paramTuplets = []
		self.opState.params = []
		globalPrefix = self.opState.name + '_'
		knownParNames = set()
		def addPar(p: Par, handling: str, skipExisting=False, conversion=''):
			if skipExisting and p.name in knownParNames:
				return
			self.opState.params.append(ParamSpec(
				name=globalPrefix + p.name,
				localName=p.name,
				source='param',
				style=p.style,
				tupletName=globalPrefix + p.tupletName,
				tupletLocalName=p.tupletName,
				vecIndex=p.vecIndex,
				status=None,
				handling=handling,
				conversion=conversion,
			))

		def addSpecialPar(name: str):
			self.opState.params.append(ParamSpec(
				name=globalPrefix + name,
				localName=name,
				source='special',
				style='Float',
				tupletName=None,
				tupletLocalName=None,
				vecIndex=0,
				status=None,
				handling='runtime',
				conversion=None,
			))

		def addFromGroupTable(table: DAT):
			if not table:
				return
			for row in range(1, table.numRows):
				if table[row, 'enable'] in ('0', 'False'):
					continue
				source = table[row, 'source'] or 'param'
				if source == 'special':
					for name in tdu.expand(table[row, 'names'].val):
						addSpecialPar(name)
				else:  # if source == 'param':
					for par in _getRegularParams([table[row, 'names'].val]):
						handling = table[row, 'handling']
						if par.readOnly:
							handling = table[row, 'readOnlyHandling'] or handling
						addPar(par, handling=handling.val, skipExisting=False, conversion=table[row, 'conversion'].val)

		addFromGroupTable(self.defPar.Paramgrouptable.eval())
		if self.opState.opElements:
			for element in self.opState.opElements:
				addFromGroupTable(op(element.paramGroupTable))

		if self.defPar.Useruntimebypass:
			addPar(self.defPar.Enable, handling='runtime', skipExisting=True)

		self._fillParamStatuses()
		self._groupSpecialParamsIntoTuplets()
		self._prepareParamTupletSpecs()

	def _fillParamStatuses(self):
		parsByTuplet = {}  # type: dict[str, list[Par]]
		paramSpecsByName = {}  # type: dict[str, ParamSpec]
		host = _getParamsOp()
		if not host:
			return
		for paramSpec in self.opState.params:
			if paramSpec.source != 'param':
				continue
			par = host.par[paramSpec.localName]
			if par is None:
				continue
			paramSpecsByName[paramSpec.localName] = paramSpec
			if paramSpec.tupletLocalName not in parsByTuplet:
				parsByTuplet[paramSpec.tupletLocalName] = [par]
			else:
				parsByTuplet[paramSpec.tupletLocalName].append(par)
		for tupletName, pars in parsByTuplet.items():
			if _canBeReadOnlyTuplet(pars):
				for par in pars:
					paramSpecsByName[par.name].status = 'readOnly'

	def _groupSpecialParamsIntoTuplets(self):
		parts = []
		tupletIndex = 0
		globalPrefix = self.opState.name + '_'
		paramSpecsByName = {
			p.localName: p
			for p in self.opState.params
		}

		def addTuplet():
			tupletName = _getTupletName(parts) or f'special{tupletIndex}'
			for vecIndex, part in enumerate(parts):
				partSpec = paramSpecsByName[part]
				partSpec.tupletName = globalPrefix + tupletName
				partSpec.tupletLocalName = tupletName
				partSpec.vecIndex = vecIndex

		for paramSpec in self.opState.params:
			if paramSpec.source != 'special':
				continue
			name = paramSpec.localName
			parts.append(name)
			if len(parts) == 4:
				addTuplet()
				parts.clear()
				tupletIndex += 1
		if parts:
			addTuplet()

	def _prepareParamTupletSpecs(self):
		self.opState.paramTuplets = []
		namesByTuplet = {}  # type: dict[str, list[str]]
		paramSpecsByName = {}  # type: dict[str, ParamSpec]
		for paramSpec in self.opState.params:
			if not paramSpec.tupletLocalName:
				continue
			paramSpecsByName[paramSpec.localName] = paramSpec
			vecIndex = paramSpec.vecIndex or 0
			if paramSpec.tupletLocalName not in namesByTuplet:
				namesByTuplet[paramSpec.tupletLocalName] = ['', '', '', '']
			namesByTuplet[paramSpec.tupletLocalName][vecIndex] = paramSpec.localName
		if self.opState.path:
			sourceVectorPath = self.opState.path + '/param_vector_vals'
		else:
			sourceVectorPath = ''  # only for master opDefinition
		sourceVectorIndex = 0
		for tupletName, partNames in namesByTuplet.items():
			localNames = []
			for partName in partNames:
				if partName:
					localNames.append(partName)
				else:
					break
			part0Spec = paramSpecsByName[partNames[0]]
			self.opState.paramTuplets.append(ParamTupletSpec(
				name=part0Spec.tupletName,
				localName=part0Spec.tupletLocalName,
				source=part0Spec.source,
				size=len(localNames),
				style=part0Spec.style,
				part1=paramSpecsByName[partNames[0]].name,
				part2=paramSpecsByName[partNames[1]].name if partNames[1] else None,
				part3=paramSpecsByName[partNames[2]].name if partNames[2] else None,
				part4=paramSpecsByName[partNames[3]].name if partNames[3] else None,
				status=part0Spec.status,
				conversion=part0Spec.conversion,
				handling=part0Spec.handling,
				localNames=localNames,
				sourceVectorPath=sourceVectorPath if part0Spec.handling == 'runtime' else None,
				sourceVectorIndex=sourceVectorIndex if part0Spec.handling == 'runtime' else None,
			))
			if part0Spec.handling == 'runtime':
				sourceVectorIndex += 1

	def addError(self, message: str, path: str | None = None, level: str = 'error'):
		self.opState.validationErrors.append(ValidationError(
			path=path or parent(2).path, level=level, message=message))

	def replaceNames(self, val: str):
		if not val:
			return ''
		for k, v in self.replacements.items():
			val = val.replace(k, v)
		return val

	def loadCode(self):
		self.opState.functionCode = self.processCode(self.defPar.Functemplate.eval())
		self.opState.materialCode = self.processCode(self.defPar.Materialcode.eval())
		self.opState.initCode = self.processCode(self.defPar.Initcode.eval())
		self.opState.opGlobals = self.processCode(self.defPar.Opglobals.eval())

	def getFunctionCode(self):
		return self.processCode(self.defPar.Functemplate.eval())

	def getMaterialCode(self):
		return self.processCode(self.defPar.Materialcode.eval())

	def getInitCode(self):
		return self.processCode(self.defPar.Initcode.eval())

	def getOpGlobalsCode(self):
		return self.processCode(self.defPar.Opglobals.eval())

	def processCode(self, codeDat: DAT):
		if not codeDat or not codeDat.text:
			return ''
		code = codeDat.text
		for placeholder, val in self.elementReplacements.items():
			code = code.replace(placeholder, val)
		code = _typePattern.sub(_typeRepl, code)
		return self.replaceNames(code)

	def loadMacros(self):
		macros = []
		def addMacro(m: Macro):
			if not m.name:
				return
			m.name = self.replaceNames(m.name)
			if isinstance(m.value, str):
				m.value = self.replaceNames(m.value)
			macros.append(m)
		for inputState in self.opState.inputStates:
			addMacro(Macro(_getHasInputMacroName(inputState.functionName)))
		for tag in self.opState.tags:
			addMacro(Macro(f'THIS_HAS_TAG_{tag}'))
		macroParams = []
		angleParamNames = []
		for paramSpec in self.opState.params:
			if paramSpec.handling != 'macro':
				continue
			par = self.paramsOp.par[paramSpec.localName]
			if par is None:
				continue
			macroParams.append(par)
			if paramSpec.conversion == 'angle':
				angleParamNames.append(par.name)
		macroParamVals = {}
		for par in macroParams:
			name = par.name
			val = par.eval()
			if name in angleParamNames:
				val = math.radians(val)
			macroParamVals[name] = val
			style = par.style
			if style in ('Menu', 'Str', 'StrMenu'):
				addMacro(Macro(f'{self.namePrefix}{name}_{val}'))
				addMacro(Macro(self.namePrefix + name, val))
			elif style == 'Toggle':
				if val:
					addMacro(Macro(self.namePrefix + name, 1))
			else:
				addMacro(Macro(self.namePrefix + name, val))
		for paramTupletSpec in self.opState.paramTuplets:
			if paramTupletSpec.handling != 'macro':
				continue
			if paramTupletSpec.size < 2:
				continue
			parts = [
				repr(macroParamVals[p])
				for p in paramTupletSpec.localNames
			]
			partsJoined = ','.join(parts)
			addMacro(Macro(self.namePrefix + paramTupletSpec.localName, f'vec{paramTupletSpec.size}({partsJoined})'))
		tables = [self.defPar.Macrotable.eval()] + self.defPar.Generatedmacrotables.evalOPs()
		if self.opState.opElements:
			for elementState in self.opState.opElements:
				if elementState.macroTable:
					tables.append(op(elementState.macroTable))
		for table in tables:
			if not table or not table.numCols or not table.numRows:
				continue
			if table.numCols == 3:
				for row in table.rows():
					addMacro(Macro(row[1].val, row[2].val, not _isFalseStr(row[0])))
			elif table.numCols == 1:
				for cell in table.col(0):
					addMacro(Macro(cell.val))
			elif table.numCols == 2:
				for row in table.rows():
					addMacro(Macro(row[0].val, row[1].val))
			else:
				for row in table.rows():
					addMacro(Macro(row[1].val, ' '.join([c.val or '' for c in row[2:]]), not _isFalseStr(row[0])))
		self.opState.macros = macros

	def loadConstants(self):
		self.opState.constants = []
		for paramSpec in self.opState.params:
			if paramSpec.handling != 'constant':
				continue
			globalName = paramSpec.name
			localName = paramSpec.localName
			style = paramSpec.style
			if style == 'Int':
				self.opState.constants.append(Constant(
					globalName, localName, 'int'
				))
			elif style == 'Float':
				self.opState.constants.append(Constant(
					globalName, localName, 'float'
				))
			elif style == 'Toggle':
				self.opState.constants.append(Constant(
					globalName, localName, 'bool'
				))
			elif style == 'Menu':
				par = self.paramsOp.par[paramSpec.localName]
				self.opState.constants.append(Constant(
					globalName, localName, 'int',
					menuOptions=par.menuNames
				))
			else:
				raise Exception(f'Invalid constant style {globalName} {style}')

	def loadTextures(self):
		self.opState.textures = []
		table = self.defPar.Texturetable.eval()
		if not table or table.numRows < 2:
			return
		for i in range(1, table.numRows):
			if _isFalseStr(table[i, 'enable']):
				continue
			name = table[i, 'name']
			path = table[i, 'path']
			if not name or not path:
				continue
			self.opState.textures.append(Texture(
				name=self.namePrefix + name.val,
				path=path.val,
				type=str(table[i, 'type'] or '2d')
			))

	def loadBuffers(self):
		self.opState.buffers = []
		table = self.defPar.Buffertable.eval()
		if not table or table.numRows < 2:
			return
		for i in range(1, table.numRows):
			if _isFalseStr(table[i, 'enable']):
				continue
			name = str(table[i, 'name'] or '')
			path = str(table[i, 'chop'] or '')
			expr1 = str(table[i, 'expr1'] or '')
			expr2 = str(table[i, 'expr2'] or '')
			expr3 = str(table[i, 'expr3'] or '')
			expr4 = str(table[i, 'expr4'] or '')
			if not name:
				continue
			if not path and not expr1 and not expr2 and not expr3 and not expr4:
				continue
			self.opState.buffers.append(Buffer(
				name=self.namePrefix + name,
				type=str(table[i, 'type'] or 'vec4'),
				chop=path,
				uniformType=str(table[i, 'uniformType'] or 'uniformarray'),
				length=int(table[i, 'length']) if table[i, 'length'] != '' else None,
				expr1=expr1,
				expr2=expr2,
				expr3=expr3,
				expr4=expr4,
			))

	def loadReferences(self):
		self.opState.references = []
		table = self.defPar.Referencetable.eval()
		if not table or table.numRows < 2:
			return
		for i in range(1, table.numRows):
			localName = str(table[1, 'name'])
			if localName == 'none':
				continue
			if table[i, 'category'] == 'attribute':
				self.opState.references.append(Reference(
					name=self.namePrefix + localName,
					localName=localName,
					sourcePath=None,
					sourceName=str(table[i, 'sourceName']),
					dataType=str(table[i, 'dataType']),
					owner=self.opName,
					category='attribute',
				))
			else:
				sourcePath = str(table[1, 'sourcePath'])
				if not localName or not sourcePath:
					continue
				sourceOp = op(sourcePath)
				if not sourceOp:
					self.addError(f'Invalid source path for reference {localName}')
					continue
				self.opState.references.append(Reference(
					name=self.namePrefix + localName,
					localName=localName,
					sourcePath=sourcePath,
					sourceName=str(table[i, 'sourceName']),
					dataType=str(table[i, 'dataType']),
					owner=self.opName,
					category='variable',
				))

	def loadVariablesAndAttributes(self):
		self.opState.variables = []
		self.opState.attributes = []
		table = self.defPar.Variabletable.eval()
		if not table or table.numRows < 2:
			return
		for i in range(1, table.numRows):
			if _isFalseStr(table[i, 'enable']):
				continue
			if table[i, 'category'] == 'attribute':
				self.opState.attributes.append(SurfaceAttribute(
					name=table[i, 'name'].val,
					label=table[i, 'label'].val or table[i, 'name'].val,
					dataType=table[i, 'dataType'].val,
					macros=str(table[i, 'macros'] or ''),
				))
			else:
				localName = table[i, 'name'].val
				self.opState.variables.append(Variable(
					name=self.namePrefix + localName,
					localName=localName,
					label=table[i, 'label'].val or localName,
					dataType=table[i, 'dataType'].val,
					owner=self.opName,
					macros=str(table[i, 'macros'] or ''),
				))

def _parseOpState():
	return RopState.fromJson(op('opState').text)

def buildDefinitionTable(dat: scriptDAT):
	dat.clear()
	state = _parseOpState()
	typeTable = op('types')
	defPath = parent().path
	dat.appendCols([
		['name', state.name],
		['path', state.path],
		['opType', state.ropFullType],
		['coordType', typeTable['coordType', 1]],
		['contextType', typeTable['contextType', 1]],
		['returnType', typeTable['returnType', 1]],
		['opVersion', parentPar().Raytkopversion or 0],
		['toolkitVersion', parentPar().Raytkversion or ''],
		['paramSource', defPath + '/param_vals'],
		['constantParamSource', defPath + '/constant_param_vals'],
		['paramVectors', defPath + '/param_vector_vals'],
		['libraryNames', parentPar().Librarynames],
		['definitionPath', defPath + '/definition'],
		['tags', ' '.join(state.tags or [])],
	])

_typePattern = re.compile(r'\b[CR][a-z]+T\b')
_typeRepls = {'CoordT': 'THIS_CoordT', 'ContextT': 'THIS_ContextT', 'ReturnT': 'THIS_ReturnT'}
def _typeRepl(m): return _typeRepls.get(m.group(0), m.group(0))

def _isFalseStr(val):
	return val in ('0', 'False')

def _getHasInputMacroName(inputAlias: str):
	if tdu.base(inputAlias) == 'inputOp':
		i = tdu.digits(inputAlias)
		if i is not None:
			return f'THIS_HAS_INPUT_{i}'
	return f'THIS_HAS_INPUT_{inputAlias}'

def _showWarning(msg: str):
	dlg = op.TDResources.op('popDialog')
	dlg.Open(title='Warning', text=msg, escOnClickAway=True)

def inspect(rop: COMP):
	if hasattr(op, 'raytk'):
		inspector = op.raytk.op('tools/inspector')
		if inspector and hasattr(inspector, 'Inspect'):
			inspector.Inspect(rop)
			return
	_showWarning('The RayTK inspector is only available when the main toolkit tox has been loaded.')

def launchHelp():
	url = parentPar().Helpurl.eval()
	if not url:
		return
	url += '?utm_source=raytkLaunch'
	ui.viewFile(url)

def updateOP():
	if not hasattr(op, 'raytk'):
		_showWarning('Unable to update OP because RayTK toolkit is not available.')
		return
	host = _host()
	if not host:
		return
	toolkit = op.raytk
	updater = toolkit.op('tools/updater')
	if updater and hasattr(updater, 'UpdateOP'):
		updater.UpdateOP(host)
		return
	if not host.par.clone:
		msg = 'Unable to update OP because master is not found in the loaded toolkit.'
		if parentPar().Raytkopstatus == 'deprecated':
			msg += '\nNOTE: This OP has been marked as "Deprecated", so it may have been removed from the toolkit.'
		_showWarning(msg)
		return
	if host and host.par.clone:
		host.par.enablecloningpulse.pulse()

def _getPalette():
	if not hasattr(op, 'raytk'):
		_showWarning('Unable to create reference because RayTK toolkit is not available.')
		return
	return op.raytk.op('tools/palette')

class OpDefinition:
	def __init__(self, opDefComp: COMP):
		self.opDefComp = opDefComp
		self.hostRop = opDefComp.par.Hostop.eval()

	def createVarRef(self, name: str):
		palette = _getPalette()
		if not palette:
			return
		state = self.getRopState()
		for variable in state.variables or []:
			if variable.localName.lower() == name:
				palette.CreateVariableReference(self.hostRop, variable.localName, variable.dataType)
				return
		raise Exception(f'Variable not found: {name}')
	
	@property
	def name(self):
		return self.opDefComp.par.Name.eval()

	def getRopState(self) -> RopState:
		return RopState.fromJson(self.opDefComp.op('opState').text)

	def getInitCode(self) -> str | None:
		return self.getRopState().initCode

	def getOpGlobals(self) -> str | None:
		return self.getRopState().opGlobals

	def getFunctionCode(self) -> str:
		return self.getRopState().functionCode

	def getMaterialCode(self) -> str | None:
		state = self.getRopState()
		if not state.materialId:
			return None
		return state.materialCode
