from raytkUtil import simplifyNames

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from components.inspectorCore.inspectorCoreExt import InspectorCore
	ext.inspectorCore = InspectorCore(COMP())

	class _StatePar(ParCollection):
		Simplifynames: 'BoolParamT'
	ipar.inspectorState = _StatePar()

class ShaderPanel:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def prepareCode(dat: 'DAT', definition: 'DAT'):
		code = dat.text
		if not ipar.inspectorState.Simplifynames or not code or definition.numRows < 2:
			return
		rawNames = [str(c) for c in definition.col('name')[1:]]
		names = simplifyNames(rawNames)
		for rawName, name in zip(rawNames, names):
			code = code.replace(rawName, name)
		dat.text = code

	@staticmethod
	def buildCodeBlockTable(dat: 'DAT', includes: 'DAT', preparedCode: 'DAT'):
		dat.clear()
		dat.appendRow(['name', 'label', 'path'])
		dat.appendRow(['main', 'main', preparedCode])
		if includes.numRows < 2:
			return
		for row in range(1, includes.numRows):
			name = includes[row, 'name']
			path = includes[row, 'path']
			dat.appendRow([
				name,
				f'{name} ({path})',
				path,
			])
