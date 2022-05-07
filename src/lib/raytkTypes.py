import itertools
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
	accessExpr: Optional[str] = None
	macros: Optional[str] = None

@dataclass
class DataType:
	name: str
	label: str
	labelForCoord: Optional[str] = None
	isCoord: bool = False
	isContext: bool = False
	isReturn: bool = False
	returnConversion: Optional[Conversion] = None
	isVariable: bool = True
	vectorLength: Optional[int] = None
	fields: List[Field] = None
	defaultExpr: Optional[str] = None
	conversionFromParam: Optional[Conversion] = None
	macros: Optional[str] = None

	@property
	def returnAsType(self):
		return self.returnConversion.toType if self.returnConversion else self.name

	@property
	def returnExpr(self):
		return self.returnConversion.expr if self.returnConversion else 'val'

	@property
	def paramExpr(self):
		return self.conversionFromParam.expr if self.conversionFromParam else ''

	@classmethod
	def scalar(cls, name, label, **kwargs):
		return cls(
			name, label,
			vectorLength=1,
			**kwargs)

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

class _Conversions:
	adaptAsFloat = Conversion(
		name='adaptAsFloat',
		fromTypes=tdu.expand('float bool int uint vec[2-4] [biu]vec[2-4] Sdf'),
		toType='float',
		expr='adaptAsFloat(val)')
	adaptAsVec2 = Conversion(
		name='adaptAsVec2',
		fromTypes=tdu.expand('float vec[2-4]'),
		toType='vec2',
		expr='adaptAsVec2(val)')
	adaptAsVec3 = Conversion(
		name='adaptAsVec3',
		fromTypes=tdu.expand('float vec[2-4]'),
		toType='vec3',
		expr='adaptAsVec3(val)')
	adaptAsVec4 = Conversion(
		name='adaptAsVec4',
		fromTypes=tdu.expand('float bool int uint vec[2-4] [biu]vec[2-4]'),
		toType='vec4',
		expr='adaptAsVec4(val)')
	adaptAsSdf = Conversion(
		name='adaptAsSdf',
		fromTypes=['float', 'Sdf'],
		toType='Sdf',
		expr='adaptAsSdf(val)')

_allConversions = [
	_Conversions.adaptAsFloat,
	_Conversions.adaptAsVec2,
	_Conversions.adaptAsVec3,
	_Conversions.adaptAsVec4,
	_Conversions.adaptAsSdf,
]

def _createScalarAndVector(scalarName: str, vectorPrefix: str, label: str, defaultVal: str):
	return [
		DataType.scalar(
			scalarName, label,
			returnConversion=_Conversions.adaptAsFloat,
			defaultExpr=defaultVal,
			conversionFromParam=Conversion(fromTypes=['vec4'], toType=scalarName, expr=f'{scalarName}(val.x)'),
		)
	] + [
		DataType.vector(
			f'{vectorPrefix}{i}', f'{label}Vector{i}', partType=scalarName, parts='xyzw'[:i],
			returnConversion=_Conversions.adaptAsVec4,
			defaultExpr=f'{vectorPrefix}{i}({defaultVal})',
			conversionFromParam=Conversion(
				fromTypes=['vec4'], toType=f'{vectorPrefix}{i}',
				expr=f'{vectorPrefix}{i}(val.{"xyzw"[:i]})' if i < 4 else f'{vectorPrefix}4(val)',
			),
		)
		for i in range(2, 5)
	]

_allTypes = [
	DataType.scalar(
		'float', 'Float', labelForCoord='1D', isCoord=True, isReturn=True, defaultExpr='0.',
		conversionFromParam=Conversion(fromTypes=['vec4'], toType='float', expr='val.x'),
	),
	DataType.vector(
		'vec2', 'Vector2', labelForCoord='2D', isCoord=True,
		partType='float', parts='xy',
		returnConversion=_Conversions.adaptAsVec4,
		defaultExpr='vec2(0.)',
		conversionFromParam=Conversion(fromTypes=['vec4'], toType='vec2', expr='val.xy'),
	),
	DataType.vector(
		'vec3', 'Vector3', labelForCoord='3D', isCoord=True,
		partType='float', parts='xyz',
		returnConversion=_Conversions.adaptAsVec4,
		defaultExpr='vec3(0.)',
		conversionFromParam=Conversion(fromTypes=['vec4'], toType='vec3', expr='val.xyz'),
	),
	DataType.vector(
		'vec4', 'Vector', isReturn=True,
		partType='float', parts='xyzw',
		defaultExpr='vec4(0.)',
		conversionFromParam=Conversion(fromTypes=['vec4'], toType='vec4', expr='val'),
	),
]

_allTypes += _createScalarAndVector('bool', 'bvec', 'Bool', 'false')
_allTypes += _createScalarAndVector('int', 'ivec', 'Int', '0')
_allTypes += _createScalarAndVector('uint', 'uvec', 'UInt', '0')

_allTypes += [
	DataType(
		'Sdf', 'SDF', isReturn=True,
		fields=[
			Field('x', 'Distance', 'float'),
			Field('mat', 'Material', 'vec3'),
			Field('uv', 'Primary UV', 'vec4', macros='RAYTK_USE_UV'),
			Field('uv.x', 'Primary UV (X)', 'float', macros='RAYTK_USE_UV'),
			Field('uv.y', 'Primary UV (Y)', 'float', macros='RAYTK_USE_UV'),
			Field('uv.z', 'Primary UV (Z)', 'float', macros='RAYTK_USE_UV'),
			Field('uv2', 'Secondary UV', 'vec4', macros='RAYTK_USE_UV'),
			Field('uv2.x', 'Secondary UV (X)', 'float', macros='RAYTK_USE_UV'),
			Field('uv2.y', 'Secondary UV (Y)', 'float', macros='RAYTK_USE_UV'),
			Field('uv2.z', 'Secondary UV (Z)', 'float', macros='RAYTK_USE_UV'),
			Field('color', 'Surface Color', 'vec4', macros='RAYTK_USE_SURFACE_COLOR'),
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

def _getType(name: str) -> Optional[DataType]:
	return _typesByName.get(name)

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

def buildVariableTypeTable(dat: 'scriptDAT'):
	dat.clear()
	dat.appendRow(['name', 'label', 'returnAs', 'defaultExpr', 'paramExpr'])
	for dt in _allTypes:
		if not dt.isVariable:
			continue
		dat.appendRow([
			dt.name,
			dt.label,
			dt.returnAsType,
			dt.defaultExpr or '',
			dt.paramExpr or '',
		])

def buildVariableTypeFieldTable(dat: 'scriptDAT'):
	dat.clear()
	dat.appendRow([
		'parentType', 'name', 'label', 'type',
		'accessExpr', 'returnAs', 'returnExpr', 'defaultExpr', 'paramExpr',
		'macros',
	])
	for dt in _allTypes:
		if not dt.isVariable:
			continue
		dat.appendRow([
			dt.name, 'this', '(value)',
			dt.name,
			'val',
			dt.returnAsType,
			dt.returnExpr,
			dt.defaultExpr or '',
			dt.paramExpr or '',
			dt.macros or '',
		])
		if not dt.fields:
			continue
		for field in dt.fields:
			fieldType = _getType(field.type)
			if not fieldType or not fieldType.isReturn:
				pass
			macros = dt.macros or ''
			if field.macros:
				if macros:
					macros += ' ' + field.macros
				else:
					macros = field.macros
			dat.appendRow([
				dt.name, field.name, field.label,
				field.type,
				field.accessExpr or f'val.{field.name}',
				fieldType.returnAsType,
				fieldType.returnExpr,
				fieldType.defaultExpr or '',
				fieldType.paramExpr or '',
				macros,
			])

def _conversionsFrom(fromType: str):
	return [
		conv
		for conv in _allConversions
		if fromType in conv.fromTypes
	]
