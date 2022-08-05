from dataclasses import dataclass
import math
from raytkState import RopState, Macro, Texture, Reference, Variable, Dispatch, Buffer, ValidationError
import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from raytkUtil import OpDefParsT
	from typing import Dict, List, Optional

class _Builder:
	def __init__(
			self,
			typeTable: 'DAT',
	):
		# noinspection PyTypeChecker
		self.defPar = parent().par  # type: OpDefParsT
		self.hostOp = self.defPar.Hostop.eval()
		self.paramsOp = self.defPar.Paramsop.eval() or self.hostOp
		self.opState = RopState(
			opType=self.defPar.Raytkoptype.eval(),
			toolkitVersion=self.defPar.Raytkversion.eval(),
			name=self.defPar.Name.eval(),

			coordType=typeTable['coordType', 1].val,
			contextType=typeTable['contextType', 1].val,
			returnType=typeTable['returnType', 1].val,
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
		if self.opState.materialId:
			self.replacements['THISMAT'] = self.opState.materialId

	def loadInputs(self, inDats: 'List[DAT]'):
		for i, inDat in enumerate(inDats + self.defPar.Inputdefs.evalOPs()):
			if not inDat[1, 'name']:
				continue
			func = str(inDat[1, 'input:alias'] or f'inputOp{i + 1}')
			placeholder = f'inputOp_{func}' if not func.startswith('inputOp') else func
			name = str(inDat[i, 'name'])
			self.inputs.append(_InputInfo(
				inputFunc=func,
				name=name,
				path=str(inDat[i, 'path']),
				coordType=str(inDat[i, 'coordType']),
				contextType=str(inDat[i, 'contextType']),
				returnType=str(inDat[i, 'returnType']),
				placeholder=placeholder,
				vars=str(inDat[i, 'input:vars']),
				varInputs=str(inDat[i, 'input:varInputs']),
			))
			self.replacements[placeholder] = name

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

	def loadCode(
			self,
			functionCode: 'DAT',
			materialCode: 'DAT',
			initCode: 'DAT',
			opGlobals: 'DAT',
	):
		self.opState.functionCode = functionCode.text
		self.opState.materialCode = materialCode.text
		self.opState.initCode = initCode.text
		self.opState.opGlobals = opGlobals.text

	def loadMacros(self, paramSpecTable: 'DAT', paramTupletTable: 'DAT', opElementTable: 'DAT'):
		macros = []
		def addMacro(m: Macro):
			m.name = self.replaceNames(m.name)
			if isinstance(m.value, str):
				m.value = self.replaceNames(m.value)
			macros.append(m)
		for inputInfo in self.inputs:
			addMacro(Macro(_getHasInputMacroName(inputInfo.inputFunc)))
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
					addMacro(Macro(row[1].val, ' '.join([c.val for c in row[2:]]), not _isFalseStr(row[0])))
		self.opState.macros = macros

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
				length=int(table[i, 'length']),
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
				code=table[i, 'code'].val,
			))

	def loadInputNames(self, definition: 'DAT'):
		self.opState.inputNames = tdu.split(definition[1, 'inputNames'])

	# def prepareReplacements(
	# 		self,
	# 		inputTable: 'DAT',
	# 		elementTable: 'DAT',
	# ):
	# 	self.replacements = {
	# 		'thismap': self.opState.name,
	# 		'THIS_': self.opState.name + '_',
	# 	}
	# 	if self.opState.materialId:
	# 		self.replacements['THISMAT'] = self.opState.materialId
	# 	if inputTable.numRows > 1:
	# 		for i in range(1, inputTable.numRows):
	# 			self.replacements[inputTable[i, 'placeholder'].val] = inputTable[i, 'name'].val
	# 	if elementTable.numRows > 1:
	# 		for phCol in elementTable.cells(0, 'placeholder*'):
	# 			i = tdu.digits(phCol.val)
	# 			for row in range(1, elementTable.numRows):
	# 				placeholder = elementTable[row, phCol].val
	# 				if not placeholder:
	# 					continue
	# 				codeDat = op(elementTable[row, f'code{i}'])
	# 				self.replacements[placeholder] = codeDat.text if codeDat else ''

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

def onSetupParameters(dat: 'scriptDAT'):
	page = dat.appendCustomPage('Custom')
	page.appendToggle('Pretty')

def onCook(dat: 'DAT'):
	dat.clear()
	builder = _Builder(
		typeTable=op('types'),
	)
	builder.loadInputs(ops('input_def_*'))
	# builder.loadCode(
	# 	functionCode=op('function'),
	# 	materialCode=op('materialCode'),
	# 	initCode=op('initCode'),
	# 	opGlobals=op('opGlobals'),
	# )
	builder.loadMacros(
		paramSpecTable=op('paramSpecTable'),
		paramTupletTable=op('param_tuplets'),
		opElementTable=op('opElements'),
	)
	builder.loadTextures()
	builder.loadBuffers()
	builder.loadReferences()
	builder.loadVariables()
	builder.loadDispatchBlocks()
	builder.loadInputNames(op('definition'))

	dat.write(builder.opState.toJson(pretty=dat.par.Pretty.eval()))
	# dat.write(repr(builder.opState))
