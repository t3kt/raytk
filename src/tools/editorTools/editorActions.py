from typing import List
from editorToolsCommon import Action, ActionContext, ActionGroup, ActionManager, ActionUtils, ROPState

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

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
		table = op('combine_combineModes')  # type: DAT
		return [
			_CombineSdfsAction(
				table[i, 'label'].val,
				table[i, 'name'].val,
			)
			for i in range(1, table.numRows)
		]

def createActionManager():
	manager = ActionManager()
	manager.addActions(
		_AppendNull('Append Null'),
		_ConvertToFloatAction('Convert To Float'),
		_RescaleFieldAction('Rescale Field'),
		_RescaleFloatFieldAsVectorAction('Rescale As Vector'),
	)
	manager.addGroups(
		_CombineSdfsGroup('Combine SDFs'),
	)
	return manager
