"""
Utilities for processing (coord/context/return) types within ROPs and in shader construction.
"""

from typing import Dict, List, Optional, Tuple

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class TypeSpec:
	"""
	A specification for a category of types (such as coordinate types) that an operator/input/etc supports using.
	Each ROP has 3 of these:
	* Coordinate type spec
	* Context type spec
	* Return type spec

	A type spec is either:
	* A single type (e.g. 'vec2')
	* A set of several types (e.g. 'vec2|vec3')
	* All available types ('*')
	"""
	useInput: bool = False
	supportsAll: bool = False
	supported: 'Optional[List[str]]' = None

	def __init__(self, useInput=False, supportsAll=False, supported: Optional[List[str]] = None):
		self.useInput = useInput
		self.supportsAll = supportsAll
		self.supported = supported

	def expandedTypes(self, allTypes: List[str]) -> List[str]:
		if self.supportsAll:
			return list(allTypes)
		return [
			t
			for t in allTypes
			if self.supported and t in self.supported
		]

	def formatSpec(self, allTypes: List[str]) -> str:
		types = self.expandedTypes(allTypes)
		if self.supportsAll:
			spec = '*'
		else:
			spec = ' '.join(types)
		if self.useInput:
			return f'useinput|{spec}'
		return spec

	def formatTypes(self, allTypes: List[str]) -> str:
		types = self.expandedTypes(allTypes)
		return ' '.join(types)

	@classmethod
	def parseSpec(cls, spec: str):
		if not spec:
			return cls()
		useInput, spec = _parseUseInput(spec)
		return cls(
			useInput=useInput,
			supportsAll=spec == '*',
			supported=None if spec == '*' else spec.split(' '),
		)

def _parseUseInput(spec: str) -> Tuple[bool, str]:
	useInput = spec.startswith('useinput|')
	if useInput:
		spec = spec[9:]  # len('useinput|')
	return useInput, spec

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
def evalSpecInOp(spec: str, expandedTypes: str, inputCell: Optional['Cell']) -> str:
	if spec.startswith('@'):
		return spec
	useInput, spec = _parseUseInput(spec)
	if useInput and inputCell:
		return str(inputCell)
	return expandedTypes

def restrictExpandedTypes(expandedTypes: str, supportedTypes: List[str]) -> str:
	return ' '.join([t for t in expandedTypes.split(' ') if t in supportedTypes])

def getCommonTypesFromCells(cells: List['Cell']) -> List[str]:
	cells = [
		cell for cell in cells if cell
	]
	if not cells:
		return []
	typeCounts = {}  # type: Dict[str, int]
	for cell in cells:
		for part in cell.val.split(' '):
			if not part:
				continue
			typeCounts[part] = typeCounts.get(part, 0) + 1
	n = len(cells)
	return [
		t
		for t, count in typeCounts.items()
		if count == n
	]
