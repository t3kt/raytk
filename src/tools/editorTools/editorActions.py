from typing import Callable, List
from editorToolsCommon import Action, ActionContext, ActionGroup, ActionManager, ActionUtils

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class _SimpleAction(Action):
	def __init__(
			self, text: str,
			isValid: Callable[[ActionContext], bool],
			execute: Callable[[ActionContext], None],
	):
		super().__init__(text)
		self._isValid = isValid
		self._execute = execute

	def isValid(self, ctx: ActionContext) -> bool: return self._isValid(ctx)
	def execute(self, ctx: ActionContext): self._execute(ctx)

class _AppendNull(Action):
	def execute(self, ctx: ActionContext):
		o = ctx.primaryOp
		conn = o.outputConnectors[0]
		if conn.outOP.isDAT:
			newType = nullDAT
		elif conn.outOP.isTOP:
			newType = nullTOP
		elif conn.outOP.isCHOP:
			newType = nullCHOP
		else:
			raise TypeError(f'Output type not supported {conn.outOP}')
		n = ctx.parentComp.create(newType)
		ActionUtils.moveAfter(n, after=o)
		conn.connect(n)

	def isValid(self, ctx: ActionContext) -> bool:
		return bool(ctx.primaryOp and ctx.primaryOp.outputConnectors)

class _ConvertToFloatAction(Action):
	def isValid(self, ctx: ActionContext) -> bool:
		state = ctx.primaryRopState
		return bool(state and state.isVectorField or state.isSdf)

	def execute(self, ctx: ActionContext):
		state = ctx.primaryRopState
		if state.isVectorField:
			ropType = 'raytk.operators.convert.vectorToFloat'
		elif state.isSdf:
			ropType = 'raytk.operators.field.sdfField'
		else:
			raise Exception('Invalid target')
		ActionUtils.createAndAttachFromOutput(
			fromRop=ctx.primaryRop,
			ropType=ropType)

class _RescaleFieldAction(Action):
	def isValid(self, ctx: ActionContext) -> bool:
		return ctx.primaryRopState.isField

	def execute(self, ctx: ActionContext):
		ActionUtils.createAndAttachFromOutput(
			fromRop=ctx.primaryRop,
			ropType='raytk.operators.filter.rescaleField',
		)

class _RescaleFloatFieldAsVectorAction(Action):
	def isValid(self, ctx: ActionContext) -> bool:
		return ctx.primaryRopState.isFloatField

	def execute(self, ctx: ActionContext):
		def init(rop: 'COMP'):
			rop.par.Returntype = 'vec4'
		ActionUtils.createAndAttachFromOutput(
			fromRop=ctx.primaryRop,
			ropType='raytk.operators.filter.rescaleField',
			init=init,
		)

class _CombineSdfsAction(Action):
	def __init__(self, text: str, mode: str):
		super().__init__(text=text)
		self.mode = mode

	def isValid(self, ctx: ActionContext) -> bool:
		return ctx.hasSelectedSdfs(minCount=2, maxCount=2, ignoreNonSdfs=False)

	def execute(self, ctx: ActionContext):
		def init(combine: 'COMP'):
			combine.par.Combine = self.mode
		ActionUtils.createAndAttachFromMultiOutputs(
			fromRops=ctx.selectedRops,
			ropType='raytk.operators.combine.combine',
			init=init,
		)

class _CombineSdfsGroup(ActionGroup):
	def isValid(self, ctx: ActionContext) -> bool:
		return ctx.hasSelectedSdfs(minCount=2, maxCount=2, ignoreNonSdfs=False)

	def getActions(self, ctx: ActionContext) -> List[Action]:
		table = op('combineModes')  # type: DAT
		return [
			_CombineSdfsAction(
				table[i, 'label'].val,
				table[i, 'name'].val,
			)
			for i in range(1, table.numRows)
		]

class _CreateVarRefAction(Action):
	def __init__(self, text: str, variable: str, dataType: str):
		super().__init__(text=text)
		self.variable = variable
		self.dataType = dataType

	def isValid(self, ctx: ActionContext) -> bool: return True

	def execute(self, ctx: ActionContext):
		def init(refOp: 'COMP'):
			fromOp = ctx.primaryRop
			refOp.nodeCenterY = fromOp.nodeCenterY - 100
			refOp.nodeX = fromOp.nodeX - refOp.nodeWidth - 150
		ActionUtils.createVariableReference(
			ctx.primaryRop, self.variable, self.dataType, init)

class _CreateVarRefGroup(ActionGroup):
	def isValid(self, ctx: ActionContext) -> bool:
		table = ctx.primaryRopState.info.variableTable
		return table and table.numRows > 1

	def getActions(self, ctx: ActionContext) -> List[Action]:
		table = ctx.primaryRopState.info.variableTable
		if not table:
			return []
		return [
			_CreateVarRefAction(
				text=table[i, 'label'].val,
				variable=table[i, 'localName'].val,
				dataType=table[i, 'dataType'].val,
			)
			for i in range(1, table.numRows)
		]

def createActionManager():
	manager = ActionManager()
	manager.addActions(
		_AppendNull('Append Null'),
		_SimpleAction(
			'Inspect',
			isValid=lambda ctx: ctx.primaryRopState.canInspect,
			execute=lambda ctx: ctx.primaryRop.par['Inspect'].pulse(),
		),
		_ConvertToFloatAction('Convert To Float'),
		_RescaleFieldAction('Rescale Field'),
		_RescaleFloatFieldAsVectorAction('Rescale As Vector'),
	)
	manager.addGroups(
		_CombineSdfsGroup('Combine SDFs'),
		_CreateVarRefGroup('Reference Variable'),
	)
	return manager
