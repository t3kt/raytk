import json
import popMenu
from raytkShader import simplifyNames
from raytkUtil import ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from components.inspectorCore.inspectorCoreExt import InspectorCore
	ext.inspectorCore = InspectorCore(COMP())

	class _InspectorStatePar:
		Simplifynames: BoolParamT
	ipar.inspectorState = _InspectorStatePar()

	class _ShaderPanelPar:
		Codeblock: StrParamT
	ipar.shaderPanelState = _ShaderPanelPar()

class ShaderPanel:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	@staticmethod
	def _processCode(code: str, definition: DAT):
		if not code:
			return ''
		if not ipar.inspectorState.Simplifynames or definition.numRows < 2:
			return code
		rawNames = [str(c) for c in definition.col('name')[1:]]
		names = simplifyNames(rawNames)
		for rawName, name in zip(rawNames, names):
			code = code.replace(rawName, name)
		return code

	@staticmethod
	def buildCodeBlockTable(dat: DAT, includes: DAT, mainCode: DAT, definition: DAT):
		dat.clear()
		dat.appendRow(['name', 'label', 'path', 'category'])
		dat.appendRow(['main', 'main', mainCode, 'main'])
		for row in range(1, includes.numRows):
			name = includes[row, 'name']
			path = includes[row, 'path']
			dat.appendRow([
				name,
				f'include {name} ({path})',
				path,
				'include',
			])
		for row in range(1, definition.numRows):
			info = ROPInfo(op(definition[row, 'path']))
			if not info.isROP:
				continue
			opDefExt = info.opDefExt
			if not opDefExt:
				continue
			state = opDefExt.getRopState()
			if state.functionCode:
				opName = definition[row, 'name'].val
				dat.appendRow([
					opName + '_functionCode',
					f'ROP Function: {opName}',
					info.rop.path,
					'opFunction',
				])

	def fillPreparedCode(self, dat: DAT, codeBlocks: DAT, selectedName: str, definition: DAT):
		dat.clear()
		category = codeBlocks[selectedName, 'category']
		srcOp = op(codeBlocks[selectedName, 'path'])
		if not category or not srcOp:
			dat.write(' ')
			return
		if category == 'opFunction':
			info = ROPInfo(srcOp)
			if not info.isROP:
				code = None
			else:
				code = info.opDefExt.getRopState().functionCode
		else:
			code = srcOp.text
		if category in ('main', 'opFunction'):
			code = self._processCode(code, definition)
		dat.write(code or ' ')

	def showCodeBlockMenu(self):
		popMenu.fromButton(self.ownerComp.op('codeBlock_drop_button')).Show(
			popMenu.ParEnumItems(ipar.shaderPanelState.Codeblock, noCheckboxes=True))
