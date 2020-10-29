from typing import Callable, List, Tuple, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

	class _OwnerCompPar:
		Globalprefix: 'Union[DAT, str, Par]'
		Predeclarations: 'Union[DAT, str, Par]'
		Textureindexoffset: 'Union[int, Par]'
		Globalmacrotable: 'Union[DAT, str, Par]'
		Libraries: 'Union[str, Par]'
		Bodytemplate: 'Union[DAT, str, Par]'
		Outputbuffertable: 'Union[DAT, str, Par]'
		Supportmaterials: 'Union[bool, Par]'
		Parammode: 'Union[str, Par]'
		Inlineparameteraliases: 'Union[bool, Par]'
		Simplifynames: 'Union[bool, Par]'
		Generatetypedefs: 'Union[bool, Par]'

	class _OwnerComp(COMP):
		par: '_OwnerCompPar'

class ShaderBuilder:
	def __init__(self, ownerComp: '_OwnerComp'):
		self.ownerComp = ownerComp

	def definitionTable(self) -> 'DAT':
		# in reverse order (aka declaration order)
		return self.ownerComp.op('definitions')

	def parameterDetailTable(self) -> 'DAT':
		return self.ownerComp.op('param_details')

	def outputBufferTable(self) -> 'DAT':
		return self.ownerComp.op('output_buffer_table')

	def buildGlobalPrefix(self):
		return wrapCodeSection(self.ownerComp.par.Globalprefix.eval(), 'globalPrefix')

	def buildGlobalDeclarations(self):
		defsTable = self.definitionTable()
		if defsTable.numRows < 2:
			code = ['#error No input definition']
		else:
			paramDetailTable = self.parameterDetailTable()
			paramCount = max(1, paramDetailTable.numRows - 1)
			mainName = defsTable[defsTable.numRows - 1, 'name']
			code = [
				f'uniform vec4 vecParams[{paramCount}];',
				f'#define thismap {mainName}'
			]
		return wrapCodeSection(code, 'globals')

	def getOpsFromDefinitionColumn(self, column: str):
		defsTable = self.definitionTable()
		if defsTable.numRows < 2 or not defsTable[1, column]:
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

	def buildMacroBlock(self):
		tables = [self.ownerComp.par.Globalmacrotable.eval()]
		tables += self.getOpsFromDefinitionColumn('macroTable')
		decls = []
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
				if name.startswith('#define'):
					decls.append(name + value)
				else:
					decls.append(f'#define {name} {value}')
		outputBuffers = self.outputBufferTable()
		if outputBuffers.numRows > 1 and outputBuffers.col('macro'):
			for cell in outputBuffers.col('macro')[1:]:
				if cell.val:
					decls.append(f'#define {cell.val}')
		decls = _uniqueList(decls)
		return wrapCodeSection(decls, 'macros')

	def getLibraryDats(self, onWarning: Callable[[str], None] = None):
		requiredLibNames = parent().par.Librarynames.eval().strip().split(' ')  # type: List[str]
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
		libraries = self.getLibraryDats(onWarning)
		includes = [
			f'#include <{lib.path}>'
			for lib in libraries
		]
		return wrapCodeSection(includes, 'libraries')

	def buildOpDataTypedefBlock(self):
		if not self.ownerComp.par.Generatetypedefs:
			return ' '
		defsTable = self.definitionTable()
		typedefs = []
		macros = []
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
			]
		if typedefs:
			lines = typedefs + [''] + macros
		else:
			lines = []
		return wrapCodeSection(lines, 'opDataTypedefs')

	def buildPredeclarations(self):
		return wrapCodeSection(self.ownerComp.par.Predeclarations.eval(), 'predeclarations')

	def buildParameterAliases(self):
		paramDetailTable = self.parameterDetailTable()
		decls = []
		for name, expr in _getParamAliases(paramDetailTable):
			decls.append(f'#define {name} {expr}')
		return wrapCodeSection(decls, 'paramAliases')

	def buildTextureDeclarations(self):
		textureTable = self.ownerComp.op('texture_table')
		offset = int(self.ownerComp.par.Textureindexoffset)
		decls = [
			f'#define {cell.val} sTD2DInputs[{offset + cell.row - 1}]'
			for cell in textureTable.col('name')[1:]
		]
		return wrapCodeSection(decls, 'textures')

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

def buildParamAliasTable(dat: 'DAT', paramDetails: 'DAT'):
	dat.clear()
	dat.appendRow(['before', 'after'])
	for name, expr in _getParamAliases(paramDetails):
		dat.appendRow([name, expr])

def _getParamAliases(paramDetails: 'DAT') -> List[Tuple[str, str]]:
	suffixes = 'xyzw'
	partAliases = []
	mainAliases = []
	for i in range(paramDetails.numRows - 1):
		tupletName = paramDetails[i + 1, 'tuplet']
		size = int(paramDetails[i + 1, 'size'])
		if size == 1:
			name = paramDetails[i + 1, 'part1']
			mainAliases.append((str(name), f'vecParams[{i}].x'))
		else:
			if size == 4:
				mainAliases.append((str(tupletName), f'vecParams[{i}]'))
			else:
				mainAliases.append((str(tupletName), f'vec{size}(vecParams[{i}].{suffixes[:size]})'))
			for partI in range(1, 5):
				name = paramDetails[i + 1, f'part{partI}']
				if name:
					suffix = suffixes[partI - 1]
					partAliases.append((str(name), f'vecParams[{i}].{suffix}'))
	return partAliases + mainAliases

def buildMaterialBlock(materialTable: 'DAT'):
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

def _stringify(val: 'Union[str, DAT]'):
	if val is None:
		return ''
	if isinstance(val, DAT):
		return val.text
	return str(val)

def wrapCodeSection(code: 'Union[str, DAT, List[Union[str, DAT]]]', name: str):
	if isinstance(code, list):
		code = '\n'.join(_stringify(s) for s in code)
	else:
		code = _stringify(code)
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
