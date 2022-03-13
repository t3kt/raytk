from dataclasses import dataclass
from typing import List, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

@dataclass
class Conversion:
	fromTypes: List[str]
	toType: str
	expr: str
	name: Optional[str] = None
	label: Optional[str] = None

@dataclass
class Field:
	name: str
	label: Optional[str]
	type: str

@dataclass
class DataType:
	name: str
	label: str
	labelForCoord: Optional[str] = None
	isCoord: bool = False
	isContext: bool = False
	isReturn: bool = False
	isVariable: bool = True
	vectorLength: Optional[int] = None
	fields: List[Field] = None

	@classmethod
	def scalar(cls, name, label, **kwargs):
		return cls(name, label, vectorLength=1, **kwargs)

	@classmethod
	def vector(cls, name, label, partType: str, parts: str, **kwargs):
		return cls(
			name, label,
			vectorLength=len(parts),
			fields=[
				Field(part, part.upper(), partType)
				for part in parts
			],
			**kwargs)

_allTypes = [
	DataType.scalar('float', 'Float', labelForCoord='1D', isCoord=True, isReturn=True),
	DataType.vector('vec2', 'Vector2', labelForCoord='2D', isCoord=True, partType='float', parts='xy'),
	DataType.vector('vec3', 'Vector3', labelForCoord='3D', isCoord=True, partType='float', parts='xyz'),
	DataType.vector('vec4', 'Vector', isReturn=True, partType='float', parts='xyzw'),

	DataType.scalar('int', 'Int'),
	DataType.vector('ivec2', 'IntVector2', partType='int', parts='xy'),
	DataType.vector('ivec3', 'IntVector3', partType='int', parts='xyz'),
	DataType.vector('ivec4', 'IntVector', partType='int', parts='xyzw'),

	DataType.scalar('bool', 'Bool'),
	DataType.vector('bvec2', 'BoolVector2', partType='bool', parts='xy'),
	DataType.vector('bvec3', 'BoolVector3', partType='bool', parts='xyz'),
	DataType.vector('bvec4', 'BoolVector4', partType='bool', parts='xyzw'),

	DataType.scalar('uint', 'UInt'),
	DataType.vector('uvec2', 'UIntVector2', partType='uint', parts='xy'),
	DataType.vector('uvec3', 'UIntVector3', partType='uint', parts='xyz'),
	DataType.vector('uvec4', 'UIntVector', partType='uint', parts='xyzw'),

	DataType.scalar('double', 'Double'),
	DataType.vector('dvec2', 'DVector2', partType='double', parts='xy'),
	DataType.vector('dvec3', 'DVector3', partType='double', parts='xyz'),
	DataType.vector('dvec4', 'DVector', partType='double', parts='xyzw'),

	DataType(
		'Sdf', 'SDF', isReturn=True,
		fields=[
			Field('x', 'Distance', 'float'),
			Field('mat', 'Material', 'vec3'),
			# TODO: sdf fields
		]),
	DataType(
		'Ray', 'Ray', isReturn=True,
		fields=[
			Field('pos', 'Origin', 'vec3'),
			Field('dir', 'Direction', 'vec3'),
		]),
	DataType(
		'Light', 'Light', isReturn=True,
		fields=[
			Field('pos', 'Position', 'vec3'),
			Field('color', 'Color', 'vec3'),
		]),
	DataType(
		'Particle', 'Particle', isReturn=True,
		fields=[
			Field('pos', 'Position', 'vec3'),
			# TODO: particle fields
		]),
	DataType(
		'Context', 'Context', isContext=True, isVariable=False,
		fields=[
			# TODO: context fields
		]),
	DataType(
		'MaterialContext', 'Material Context', isContext=True, isVariable=False,
		fields=[
			# TODO: context fields
		]),
	DataType(
		'CameraContext', 'Camera Context', isContext=True, isVariable=False,
		fields=[
			# TODO: context fields
		]),
	DataType(
		'LightContext', 'Light Context', isContext=True, isVariable=False,
		fields=[
			# TODO: context fields
		]),
	DataType(
		'RayContext', 'Ray Context', isContext=True, isVariable=False,
		fields=[
			# TODO: context fields
		]),
	DataType(
		'ParticleContext', 'Particle Context', isContext=True, isVariable=False,
		fields=[
			# TODO: context fields
		]),
]

_typesByName = {
	dt.name: dt
	for dt in _allTypes
}

def buildCoreTypeTable(dat: 'scriptDAT'):
	dat.clear()
	dat.appendRow(['name', 'isReturnType', 'isCoordType', 'isContextType'])
	def addTypes(types: List[DataType]):
		for dt in types:
			dat.appendRow([
				dt.name, int(dt.isReturn), int(dt.isCoord), int(dt.isContext),
			])
	addTypes([
		_typesByName['float'],
		_typesByName['vec2'], _typesByName['vec3'], _typesByName['vec4'],
		_typesByName['Sdf'], _typesByName['Ray'], _typesByName['Light'], _typesByName['Particle'],
	])
	addTypes([
		dt
		for dt in _allTypes
		if dt.isContext
	])

_allConversions = [
	Conversion(
		fromTypes=['float', 'vec2', 'vec3', 'vec4', 'Sdf'],
		toType='float',
		expr='adaptAsFloat(val)'),
	Conversion(
		fromTypes=['float', 'vec2', 'vec3', 'vec4', 'Sdf'],
		toType='vec2',
		expr='adaptAsVec2(val)'),
	Conversion(
		fromTypes=['float', 'vec2', 'vec3', 'vec4', 'Sdf'],
		toType='vec3',
		expr='adaptAsVec3(val)'),
	Conversion(
		fromTypes=['float', 'vec2', 'vec3', 'vec4', 'Sdf'],
		toType='vec4',
		expr='adaptAsVec4(val)'),
	Conversion(
		fromTypes=['float', 'Sdf'],
		toType='Sdf',
		expr='adaptAsSdf(val)'),
]

def _conversionsFrom(fromType: str):
	return [
		conv
		for conv in _allConversions
		if fromType in conv.fromTypes
	]
