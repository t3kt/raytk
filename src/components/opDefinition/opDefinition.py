from dataclasses import dataclass
import json
import math
from raytkState import RopState, Macro, Texture, Reference, Variable, Dispatch, Buffer, ValidationError, Constant
import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import Callable, Dict, List, Optional, Union
	from raytkUtil import OpDefParsT
	from _stubs.PopDialogExt import PopDialogExt


def parentPar() -> 'Union[ParCollection, OpDefParsT]':
	return parent().par

def _host() -> 'Optional[COMP]':
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


# Evaluates a type spec in an OP, expanding wildcards and inheriting input types or using fallback type.
# Produces a list of 1 or more concrete type names, or a `@` reference to another op (for reverse inheritance).
#
# Formats for spec input:
#   `Type1 Type2`
#   `*`
#   `useinput|Type1 Type2`
#   `useinput|*`
#   `@some_op_name`
#
# Output formats:
#    `Type1`
#    `Type1 Type2`
#    `@some_op_name`
# These outputs are what appear in the generated definition tables passed between ops.
def _evalType(category: str, supportedTypes: 'DAT', inputDefs: 'DAT'):
	spec = supportedTypes[category, 'spec'].val
	if spec.startswith('@'):
		return spec
	inputCell = inputDefs[1, category]
	if spec.startswith('useinput|') and inputCell:
		return inputCell
	return supportedTypes[category, 'types']

def buildTypeTable(dat: 'scriptDAT', supportedTypes: 'DAT', inputDefs: 'DAT'):
	dat.clear()
	dat.appendRows([
		['coordType', _evalType('coordType', supportedTypes, inputDefs)],
		['returnType', _evalType('returnType', supportedTypes, inputDefs)],
		['contextType', _evalType('contextType', supportedTypes, inputDefs)],
	])

def _inputDefsFromPar():
	return parentPar().Inputdefs.evalOPs()

def buildInputTable(dat: 'DAT', inDats: 'List[DAT]'):
	dat.clear()
	dat.appendRow([
		'inputFunc', 'name', 'path',
		'coordType', 'contextType', 'returnType',
		'placeholder',
		'vars', 'varInputs',
		'tags',
	])
	for i, inDat in enumerate(inDats + _inputDefsFromPar()):
		if not inDat[1, 'name']:
			continue
		func = str(inDat[1, 'input:alias'] or f'inputOp{i + 1}')
		dat.appendRow([
			func,
			inDat[1, 'name'],
			inDat[1, 'path'],
			inDat[1, 'coordType'],
			inDat[1, 'contextType'],
			inDat[1, 'returnType'],
			('inputOp_' + func) if not func.startswith('inputOp') else func,
			inDat[1, 'input:vars'],
			inDat[1, 'input:varInputs'],
			inDat[1, 'tags'] or '',
		])

def getCombinedTags(inputTable: 'DAT'):
	tags = set()
	for i in range(1, inputTable.numRows):
		tags.update(tdu.split(inputTable[i, 'tags']))
	table = parentPar().Tagtable.eval()
	if table and table.numRows > 1:
		for i in range(1, table.numRows):
			if _isFalseStr(table[i, 'enable']):
				continue
			tags.add(table[i, 'name'].val)
	return list(sorted(tags))

def combineInputDefinitions(
		dat: 'DAT',
		inDats: 'List[DAT]',
		defFields: 'DAT',
):
	dat.clear()
	inDats += _inputDefsFromPar()
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

def processInputDefinitionTypes(dat: 'scriptDAT', supportedTypeTable: 'DAT'):
	_processInputDefTypeCategory(dat, supportedTypeTable, 'coordType')
	_processInputDefTypeCategory(dat, supportedTypeTable, 'contextType')
	_processInputDefTypeCategory(dat, supportedTypeTable, 'returnType')

def _processInputDefTypeCategory(dat: 'scriptDAT', supportedTypeTable: 'DAT', category: 'str'):
	supported = supportedTypeTable[category, 'types'].val.split(' ')
	cells = dat.col(category)
	if not cells:
		return
	errors = []
	ownName = parentPar().Name.eval()
	# TODO: consolidate this and the typeRestrictor
	for cell in cells[1:]:
		inputName = dat[cell.row, 'name']
		inputTypes = cell.val.split(' ')
		supportedInputTypes = [t for t in inputTypes if t in supported]
		if not supportedInputTypes:
			errors.append(f'No supported {category} for {inputName} ({" ".join(inputTypes)}')
		elif len(supportedInputTypes) == 1:
			cell.val = supportedInputTypes[0]
		else:
			# cell.val = ' '.join(supportedInputTypes)
			cell.val = '@' + ownName

def _getParamsOp() -> 'Optional[COMP]':
	return parentPar().Paramsop.eval() or _host()

# Builds the primary table from which all other parameter tables are built.
# This table contains regular parameters and special parameters, with both runtime and macro handling.
def buildParamSpecTable(dat: 'scriptDAT', paramGroupTable: 'DAT'):
	dat.clear()
	dat.appendRow([
		'localName',
		'globalName',
		'source',
		'style',
		'tupletName',
		'tupletGlobalName',
		'vecIndex',
		'status',
		'handling',
		'conversion',
	])
	globalPrefix = parentPar().Name.eval() + '_'

	def addPar(p: 'Par', handling: str, skipExisting=False, conversion=''):
		if skipExisting and dat[p.name, 0] is not None:
			# skip params that are already loaded
			return
		dat.appendRow([
			p.name,
			globalPrefix + p.name,
			'param',
			p.style,
			p.tupletName,
			globalPrefix + p.tupletName,
			p.vecIndex,
			'',
			handling,
			conversion,
		])

	def addSpecialPar(name: str):
		dat.appendRow([
			name,
			globalPrefix + name,
			'special', 'Float', '', '', '0', '', 'runtime', '',
		])

	def addFromGroupTable(table: 'DAT'):
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

	addFromGroupTable(paramGroupTable)
	for path in _getOpElementTable().col('paramGroupTable')[1:]:
		addFromGroupTable(op(path))

	# Add runtime bypass
	if parentPar().Useruntimebypass:
		addPar(parentPar().Enable, handling='runtime', skipExisting=True)

	# Update param statuses based on tuplets
	_fillParamStatuses(dat)

	# Group special parameters into tuplets
	_groupSpecialParamsIntoTuplets(dat)

def _getOpElementTable() -> 'DAT':
	return op('opElements')

def _fillParamStatuses(dat: 'DAT'):
	parsByTuplet = {}  # type: Dict[str, List[Par]]
	host = _getParamsOp()
	if not host:
		return
	for i in range(1, dat.numRows):
		if dat[i, 'source'] != 'param':
			continue
		name = dat[i, 'localName']
		tupletName = dat[i, 'tupletName'].val
		par = host.par[name]
		if par is None:
			continue
		if tupletName not in parsByTuplet:
			parsByTuplet[tupletName] = [par]
		else:
			parsByTuplet[tupletName].append(par)
	for tupletName, pars in parsByTuplet.items():
		if _canBeReadOnlyTuplet(pars):
			for par in pars:
				dat[par.name, 'status'] = 'readOnly'

def _groupSpecialParamsIntoTuplets(dat: 'DAT'):
	parts = []
	tupletIndex = 0
	globalPrefix = parentPar().Name.eval() + '_'

	def addTuplet():
		tupletName = _getTupletName(parts) or f'special{tupletIndex}'
		for vecIndex, part in enumerate(parts):
			dat[part, 'tupletName'] = tupletName
			dat[part, 'tupletGlobalName'] = globalPrefix + tupletName
			dat[part, 'vecIndex'] = vecIndex

	for i in range(1, dat.numRows):
		if dat[i, 'source'] != 'special':
			continue
		name = dat[i, 'localName'].val
		parts.append(name)
		if len(parts) == 4:
			addTuplet()
			parts.clear()
			tupletIndex += 1
	if parts:
		addTuplet()

def _getRegularParams(specs: 'List[str]') -> 'List[Par]':
	host = _getParamsOp()
	if not host:
		return []
	# TODO: clean this up. joining and splitting and rejoining, etc.
	paramNames = tdu.expand(str(' '.join(specs)).strip())
	if not paramNames:
		return []
	return [
		p
		for p in host.pars(*[pn.strip() for pn in paramNames])
		if p.isCustom and p.name != 'Inspect'
	]

# Builds a table that lists global names of runtime-based parameters.
def buildParamTable(dat: 'DAT', paramSpecTable: 'DAT'):
	dat.clear()
	foundNames = set()
	for i in range(1, paramSpecTable.numRows):
		if paramSpecTable[i, 'handling'] != 'runtime':
			continue
		name = paramSpecTable[i, 'globalName'].val
		if name not in foundNames:
			dat.appendRow([name])
			foundNames.add(name)

# Builds a table of parameters organized into tuplets.
def buildParamDetailTable(dat: 'DAT', paramSpecTable: 'DAT'):
	dat.clear()
	dat.appendRow([
		'tuplet', 'tupletLocalName',
		'source', 'size',
		'part1', 'part2', 'part3', 'part4',
		'status', 'conversion', 'localNames', 'handling',
	])
	namesByTupletName = {}  # type: Dict[str, List[str]]
	for i in range(1, paramSpecTable.numRows):
		tupletName = paramSpecTable[i, 'tupletName'].val
		vecIndex = int(paramSpecTable[i, 'vecIndex'] or 0)
		if not tupletName:
			continue
		if tupletName not in namesByTupletName:
			namesByTupletName[tupletName] = ['', '', '', '']
		namesByTupletName[tupletName][vecIndex] = paramSpecTable[i, 'localName'].val

	for tupletName, parts in namesByTupletName.items():
		size = 0
		for part in parts:
			if part:
				size += 1
			else:
				break
		dat.appendRow([
			paramSpecTable[parts[0], 'tupletGlobalName'],
			paramSpecTable[parts[0], 'tupletName'],
			paramSpecTable[parts[0], 'source'],
			size,
			paramSpecTable[parts[0], 'globalName'] or '',
			paramSpecTable[parts[1], 'globalName'] or '',
			paramSpecTable[parts[2], 'globalName'] or '',
			paramSpecTable[parts[3], 'globalName'] or '',
			paramSpecTable[parts[0], 'status'],
			paramSpecTable[parts[0], 'conversion'],
			' '.join(p for p in parts if p),
			paramSpecTable[parts[0], 'handling'],
		])


def _canBeReadOnlyTuplet(pars: 'List[Par]'):
	return all(p.readOnly and p.mode == ParMode.CONSTANT for p in pars)

def _getTupletName(parts: 'List[str]'):
	if len(parts) <= 1 or len(parts[0]) <= 1:
		return None
	prefix = parts[0][:-1]
	for part in parts[1:]:
		if not part.startswith(prefix):
			return None
	return prefix

def buildParamTupletAliases(dat: 'DAT', paramTable: 'DAT'):
	dat.clear()
	for i in range(1, paramTable.numRows):
		size = int(paramTable[i, 'size'])
		if size > 1:
			dat.appendRow([
				'#define {} vec{}({})'.format(paramTable[i, 'tuplet'].val, size, ','.join([
					paramTable[i, f'part{j + 1}'].val
					for j in range(size)
				]))
			])

# Builds a table with lists of parameter local names, for use in CHOP parameter expressions.
def buildParamChopNamesTable(dat: 'DAT', paramSpecTable: 'DAT'):
	dat.clear()
	regularNames = []
	specialNames = []
	angleNames = []
	constantNames = []
	for i in range(1, paramSpecTable.numRows):
		handling = paramSpecTable[i, 'handling']
		if handling == 'macro':
			continue
		name = paramSpecTable[i, 'localName'].val
		source = paramSpecTable[i, 'source']
		if handling == 'constant':
			if source != 'param':
				raise Exception(f'Constants must come from parameters {name} {source}')
			else:
				constantNames.append(name)
		elif source == 'param':
			regularNames.append(name)
		elif source == 'special':
			specialNames.append(name)
		if paramSpecTable[i, 'conversion'] == 'angle':
			angleNames.append(name)
	dat.appendRow(['regular', ' '.join(regularNames)])
	dat.appendRow(['special', ' '.join(specialNames)])
	dat.appendRow(['angle', ' '.join(angleNames)])
	dat.appendRow(['constant', ' '.join(constantNames)])

def updateLibraryMenuPar(libsComp: 'COMP'):
	p = parentPar().Librarynames  # type: Par
	libs = libsComp.findChildren(type=DAT, maxDepth=1, tags=['library'])
	libs.sort(key=lambda l: -l.nodeY)
	p.menuNames = [lib.name for lib in libs]

def validateReferences(dat: 'scriptDAT'):
	dat.clear()
	dat.appendRow(['path', 'level', 'message'])
	path = parent().path
	def onError(err):
		dat.appendRow([path, 'error', err])
	_prepareReferences(onError=onError)

def _prepareReferences(
		dat: 'Optional[scriptDAT]' = None,
		onError: 'Optional[Callable[[str], None]]' = None,
):
	table = parentPar().Referencetable.eval()
	if not table or table.numRows < 2:
		return []
	hostName = parentPar().Name.eval()
	namePrefix = hostName + '_'
	for i in range(1, table.numRows):
		localName = str(table[1, 'name'])
		if localName == 'none' or not localName:
			continue
		sourcePath = table[i, 'sourcePath']
		if not sourcePath:
			continue
		sourceOp = op(sourcePath)
		if not sourceOp:
			if onError:
				onError(f'Invalid source path for reference {localName}')
			continue
		dataType = table[i, 'dataType']
		if dat:
			globalName = namePrefix + localName
			dat.appendRow([
				globalName,
				localName,
				sourcePath,
				table[i, 'sourceName'],
				dataType,
				hostName,
			])

def validateInputs(dat: 'scriptDAT', inputDefinitions: 'DAT'):
	dat.clear()
	dat.appendRow(['path', 'level', 'message'])
	if hasattr(parent, 'raytk'):
		return
	for handlerPath in inputDefinitions.col('input:handler')[1:]:
		handler = op(handlerPath)
		if not handler:
			continue
		for error in _validateInput(handler):
			if error:
				dat.appendRow([handlerPath, 'error', error])

def _validateInput(handler: 'COMP'):
	inputDef = handler.op('inputDefinition')
	return [
		_checkInputType(handler, str(inputDef[1, 'coordType'] or ''), 'coordType'),
		_checkInputType(handler, str(inputDef[1, 'contextType'] or ''), 'contextType'),
		_checkInputType(handler, str(inputDef[1, 'returnType'] or ''), 'returnType'),
		'Required input is missing' if handler.par.Required and inputDef.numRows < 2 else None,
	]

def _checkInputType(handler: 'COMP', typeName: str, typeCategory: str):
	if not typeName:
		return
	supported = tdu.split(handler.op('supportedTypes')[typeCategory, 'types'] or '')
	if ' ' in typeName:
		if any(t in supported for t in typeName.split(' ')):
			return
	else:
		if typeName in supported:
			return
	return f'Input does not support {typeCategory} {typeName}'

def _isMaster():
	host = _host()
	return host and host.par.clone == host

def onValidationChange(dat: 'DAT'):
	if _isMaster():
		return
	host = _host()
	if not host:
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
	# Workaround for dependency update issue (#295) when the host is renamed.
	op('sel_funcTemplate').cook(force=True)

def buildOpState():
	builder = _Builder()
	builder.loadInputs(ops('input_def_*'))
	builder.loadOpElements(op('opElements'))
	builder.loadCode()
	builder.loadMacros(
		paramSpecTable=op('paramSpecTable'),
		paramTupletTable=op('param_tuplets'),
		opElementTable=op('opElements'),
		inputTable=op('input_table'),
	)
	builder.loadConstants(
		paramSpecTable=op('paramSpecTable'),
	)
	builder.loadTextures()
	builder.loadBuffers()
	builder.loadReferences()
	builder.loadVariables()
	builder.loadDispatchBlocks()

	return builder.opState

class _Builder:
	def __init__(self):
		# noinspection PyTypeChecker
		self.defPar = parent().par  # type: OpDefParsT
		self.hostOp = self.defPar.Hostop.eval()
		self.paramsOp = self.defPar.Paramsop.eval() or self.hostOp
		opType = self.defPar.Raytkoptype.eval()
		if opType and '.' in opType:
			opType = opType.rsplit('.', maxsplit=1)[1]
		self.opState = RopState(
			name=self.defPar.Name.eval(),
			ropType=opType,
		)
		self.opName = self.opState.name
		self.namePrefix = self.opName + '_'
		if self.defPar.Materialcode:
			self.opState.materialId = 'MAT_' + self.opState.name
		self.inputs = []  # type: List[_InputInfo]
		self.replacements = {
			'thismap': self.opName,
			'THIS_': self.namePrefix,
		}  # type: Dict[str, str]
		if opType:
			self.replacements['THISTYPE_'] = opType + '_'
		if self.opState.materialId:
			self.replacements['THISMAT'] = self.opState.materialId
		self.elementReplacements = {}

	def loadInputs(self, inDats: 'List[DAT]'):
		self.opState.inputNames = []
		for i, inDat in enumerate(inDats + self.defPar.Inputdefs.evalOPs()):
			if not inDat[1, 'name']:
				continue
			func = str(inDat[1, 'input:alias'] or f'inputOp{i + 1}')
			placeholder = f'inputOp_{func}' if not func.startswith('inputOp') else func
			name = str(inDat[1, 'name'])
			self.inputs.append(_InputInfo(
				inputFunc=func,
				name=name,
				path=str(inDat[1, 'path']),
				coordType=str(inDat[1, 'coordType']),
				contextType=str(inDat[1, 'contextType']),
				returnType=str(inDat[1, 'returnType']),
				placeholder=placeholder,
				vars=str(inDat[1, 'input:vars']),
				varInputs=str(inDat[1, 'input:varInputs']),
			))
			self.replacements[placeholder] = name
			self.opState.inputNames.append(name)

	def loadOpElements(self, elementTable: 'DAT'):
		for phCol in elementTable.cells(0, 'placeholder*'):
			i = tdu.digits(phCol.val)
			for row in range(1, elementTable.numRows):
				placeholder = elementTable[row, phCol].val
				if not placeholder:
					continue
				codeDat = op(elementTable[row, f'code{i}'])
				self.elementReplacements[placeholder] = codeDat.text if codeDat else ''

	def addError(self, message: str, path: 'Optional[str]' = None, level: str = 'error'):
		self.opState.validationErrors.append(ValidationError(
			path=path or parent(2).path, level=level, message=message))

	def replaceNames(self, val: str):
		# TODO: there must be a more efficent way to handle this
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

	def processCode(self, codeDat: 'DAT'):
		if not codeDat or not codeDat.text:
			return ''
		code = codeDat.text
		for placeholder, val in self.elementReplacements.items():
			code = code.replace(placeholder, val)
		code = _typePattern.sub(_typeRepl, code)
		return self.replaceNames(code)

	def loadMacros(self, paramSpecTable: 'DAT', paramTupletTable: 'DAT', opElementTable: 'DAT', inputTable: 'DAT'):
		macros = []
		def addMacro(m: Macro):
			if not m.name:
				return
			m.name = self.replaceNames(m.name)
			if isinstance(m.value, str):
				m.value = self.replaceNames(m.value)
			macros.append(m)
		for inputInfo in self.inputs:
			addMacro(Macro(_getHasInputMacroName(inputInfo.inputFunc)))
		tags = getCombinedTags(inputTable)
		for tag in tags:
			addMacro(Macro(f'THIS_HAS_TAG_{tag}'))
		macroParams = []
		angleParamNames = []
		for i in range(1, paramSpecTable.numRows):
			if paramSpecTable[i, 'handling'] != 'macro':
				continue
			par = self.paramsOp.par[paramSpecTable[i, 'localName']]
			if par is None:
				continue
			macroParams.append(par)
			if paramSpecTable[i, 'conversion'] == 'angle':
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
		for i in range(1, paramTupletTable.numRows):
			if paramTupletTable[i, 'handling'] != 'macro':
				continue
			size = int(paramTupletTable[i, 'size'])
			if size < 2:
				continue
			tuplet = paramTupletTable[i, 'tupletLocalName'].val
			parts = [
				repr(macroParamVals[p])
				for p in paramTupletTable[i, 'localNames'].val.split(' ')
			]
			partsJoined = ','.join(parts)
			addMacro(Macro(self.namePrefix + tuplet, f'vec{size}({partsJoined})'))
		tables = [self.defPar.Macrotable.eval()] + self.defPar.Generatedmacrotables.evalOPs() + [
			op(c) for c in opElementTable.col('macroTable')[1:]
		]
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

	def loadConstants(self, paramSpecTable: 'DAT'):
		self.opState.constants = []
		if paramSpecTable.numRows < 2:
			return
		for i in range(1, paramSpecTable.numRows):
			if paramSpecTable[i, 'handling'] != 'constant':
				continue
			globalName = paramSpecTable[i, 'globalName'].val
			localName = paramSpecTable[i, 'localName'].val
			style = paramSpecTable[i, 'style']
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
				par = self.paramsOp.par[paramSpecTable[i, 'localName']]
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
			sourcePath = str(table[1, 'sourcePath'])
			if localName == 'none' or not localName or not sourcePath:
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
			))

	def loadVariables(self):
		self.opState.variables = []
		table = self.defPar.Variabletable.eval()
		if not table or table.numRows < 2:
			return
		for i in range(1, table.numRows):
			if _isFalseStr(table[i, 'enable']):
				continue
			localName = table[i, 'name'].val
			self.opState.variables.append(Variable(
				name=self.namePrefix + localName,
				localName=localName,
				label=table[i, 'label'].val or localName,
				dataType=table[i, 'dataType'].val,
				owner=self.opName,
				macros=str(table[i, 'macros'] or ''),
			))

	def loadDispatchBlocks(self):
		self.opState.dispatchBlocks = []
		table = self.defPar.Dispatchtable.eval()
		if not table or table.numRows < 2:
			return
		for i in range(1, table.numRows):
			name = str(table[i, 'name'] or '')
			if not name or _isFalseStr(table[i, 'enable']):
				continue
			self.opState.dispatchBlocks.append(Dispatch(
				name=self.namePrefix + name,
				category=table[i, 'category'].val,
				code=self.replaceNames(table[i, 'code'].val),
			))

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

@dataclass
class _InputInfo:
	inputFunc: str
	name: str
	path: str
	coordType: str
	contextType: str
	returnType: str
	placeholder: str
	vars: str
	varInputs: str

def _popDialog() -> 'PopDialogExt':
	# noinspection PyUnresolvedReferences
	return op.TDResources.op('popDialog')

def inspect(rop: 'COMP'):
	if hasattr(op, 'raytk'):
		inspector = op.raytk.op('tools/inspector')
		if inspector and hasattr(inspector, 'Inspect'):
			inspector.Inspect(rop)
			return
	_popDialog().Open(
		title='Warning',
		text='The RayTK inspector is only available when the main toolkit tox has been loaded.',
		escOnClickAway=True,
	)

def _useLocalHelp():
	return hasattr(op, 'raytk') and bool(op.raytk.par['Devel'])

def launchHelp():
	url = parentPar().Helpurl.eval()
	if not url:
		return
	if _useLocalHelp():
		url = url.replace('https://t3kt.github.io/raytk/', 'http://localhost:4000/raytk/')
	url += '?utm_source=raytkLaunch'
	ui.viewFile(url)

def updateOP():
	if not hasattr(op, 'raytk'):
		_popDialog().Open(
			title='Warning',
			text='Unable to update OP because RayTK toolkit is not available.',
			escOnClickAway=True,
		)
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
		_popDialog().Open(
			title='Warning',
			text=msg,
			escOnClickAway=True,
		)
		return
	if host and host.par.clone:
		host.par.enablecloningpulse.pulse()

def _getPalette():
	if not hasattr(op, 'raytk'):
		_popDialog().Open(
			title='Warning',
			text='Unable to create reference because RayTK toolkit is not available.',
			escOnClickAway=True,
		)
		return
	return op.raytk.op('tools/palette')

def createVarRef(name: str):
	palette = _getPalette()
	if not palette:
		return
	host = _host()
	stateText = op('opState').text
	stateObj = json.loads(stateText)
	variableObjs = stateObj.get('variables') or []
	for variableObj in variableObjs:
		if variableObj['localName'].lower() == name:
			palette.CreateVariableReference(host, variableObj['localName'], variableObj['dataType'])
			return
	raise Exception(f'Variable not found: {name}')

def createRenderSel(name: str):
	palette = _getPalette()
	if not palette:
		return
	host = _host()
	bufTable = op('../output_buffers')
	if bufTable:
		name = name.lower()
		for i in range(1, bufTable.numRows):
			if bufTable[i, 'name'].val.lower() == name:
				palette.CreateRenderSelect(host, bufTable[i, 'name'].val)
				return
	raise Exception(f'Output buffer not found: {name}')
