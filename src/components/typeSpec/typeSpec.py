from raytkUtil import TypeTableHelper
from raytkModel import TypeSpec, FunctionSignature
from typing import List

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def updateTypeParMenus():
	helper = _typeHelper()
	helper.updateCoordTypePar(parent().par.Supportcoordtypes)
	helper.updateReturnTypePar(parent().par.Supportreturntypes)
	helper.updateContextTypePar(parent().par.Supportcontexttypes)

def _typeHelper():
	return TypeTableHelper(op('typeTable'))

def _getTypeSpec(paramPrefix: str, allTypes: List[str]):
	supported = tdu.split(parent().par[paramPrefix + 's'] or '')
	if '*' in supported:
		return TypeSpec.all()
	return TypeSpec(
		types=[
			typeName
			for typeName in allTypes
			if parent().par[paramPrefix + typeName.lower()] or typeName in supported
		]
	)

def _getFunctionSignature():
	helper = _typeHelper()
	return FunctionSignature(
		coordType=_getTypeSpec('Supportcoordtype', helper.coordTypes()),
		contextType=_getTypeSpec('Supportcontexttype', helper.contextTypes()),
		returnType=_getTypeSpec('Supportreturntype', helper.returnTypes()),
	)

def buildVariationsTable(dat: 'DAT'):
	signature = _getFunctionSignature()
	dat.clear()
	dat.appendRow(['coordType', 'contextType', 'returnType'])
	for sig in signature.expandAll():
		dat.appendRow([sig.coordType, sig.contextType, sig.returnType])
