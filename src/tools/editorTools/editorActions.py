from typing import Callable, List, Optional
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
		ui.undo.startBlock('Append null')
		n = ctx.parentComp.create(newType)
		ActionUtils.moveAfter(n, after=o)
		conn.connect(n)
		ui.undo.endBlock()

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
			ropType=_RopTypes.rescaleField,
		)

class _RescaleFloatFieldAsVectorAction(Action):
	def isValid(self, ctx: ActionContext) -> bool:
		return ctx.primaryRopState.isFloatField

	def execute(self, ctx: ActionContext):
		def init(rop: 'COMP'):
			rop.par.Returntype = 'vec4'
		ActionUtils.createAndAttachFromOutput(
			fromRop=ctx.primaryRop,
			ropType=_RopTypes.rescaleField,
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

def _createVarRefAction(label: str, variable: str, dataType: str):
	def execute(ctx: ActionContext):
		def init(refOp: 'COMP'):
			fromOp = ctx.primaryRop
			refOp.nodeCenterY = fromOp.nodeCenterY - 100
			refOp.nodeX = fromOp.nodeX - refOp.nodeWidth - 150
		ActionUtils.palette().CreateVariableReference(
			ctx.primaryRop,
			variable=variable,
			dataType=dataType,
			postSetup=init)
	return _SimpleAction(
		text=label,
		isValid=lambda ctx: True,
		execute=execute,
	)

class _CreateVarRefGroup(ActionGroup):
	def isValid(self, ctx: ActionContext) -> bool:
		table = ctx.primaryRopState.info.variableTable
		return table and table.numRows > 1

	def getActions(self, ctx: ActionContext) -> List[Action]:
		table = ctx.primaryRopState.info.variableTable
		if not table:
			return []
		return [
			_createVarRefAction(
				label=table[i, 'label'].val,
				variable=table[i, 'localName'].val,
				dataType=table[i, 'dataType'].val,
			)
			for i in range(1, table.numRows)
		]

def _createRenderSelAction(label: str, name: str):
	def execute(ctx: ActionContext):
		def init(refOp: 'COMP'):
			fromOp = ctx.primaryRop
			refOp.nodeCenterY = fromOp.nodeCenterY - 200
			refOp.nodeX = fromOp.nodeX + refOp.nodeWidth + 100
		ActionUtils.palette().CreateRenderSelect(
			ctx.primaryRop,
			outputName=name,
			postSetup=init,
		)
	return _SimpleAction(
		text=label,
		isValid=lambda ctx: True,
		execute=execute,
	)

class _CreateRenderSelGroup(ActionGroup):
	def isValid(self, ctx: ActionContext) -> bool:
		return any(ctx.primaryRopState.info.outputBufferNamesAndLabels)

	def getActions(self, ctx: ActionContext) -> List[Action]:
		return [
			_createRenderSelAction(label, name)
			for name, label in ctx.primaryRopState.info.outputBufferNamesAndLabels
		]

def _createAddInputAction(
		text: str,
		matchTypes: List[str],
		createType: str,
		firstInput: int = 0,
		lastInput: Optional[int] = None,
		outputIndex: int = 0,
):
	def getConn(rop: 'OP'):
		if lastInput is None:
			return _firstOpenConnector(rop.inputConnectors[firstInput:])
		return _firstOpenConnector(rop.inputConnectors[firstInput:(lastInput + 1)])

	def isValid(ctx: ActionContext):
		if not ctx.primaryRop:
			return False
		if ctx.primaryRopState.info.opType not in matchTypes:
			return False
		return bool(getConn(ctx.primaryRop))

	def execute(ctx: ActionContext):
		rop = ctx.primaryRop
		conn = getConn(rop)
		ActionUtils.createAndAttachToInput(
			rop,
			createType,
			inputIndex=conn.index,
			outputIndex=outputIndex,
		)

	return _SimpleAction(text, isValid, execute)

def _firstOpenConnector(conns: List['Connector']):
	for conn in conns:
		if not conn.connections:
			return conn

def _createConvertFrom2dSdfAction(
		text: str, ropType: str):
	def isValid(ctx: ActionContext):
		return ctx.primaryRopState.isSdf and ctx.primaryRopState.is2d
	def execute(ctx: ActionContext):
		ActionUtils.createAndAttachFromOutput(ctx.primaryRop, ropType)
	return _SimpleAction(text, isValid, execute)

def _pulsePrimaryRopParam(ctx: ActionContext, par: str):
	rop = ctx.primaryRop
	p = rop.par[par] if rop else None
	if p is not None:
		p.pulse()

def _pulseSelectedRopParams(ctx: ActionContext, par: str):
	for rop in ctx.selectedRops:
		p = rop.par[par]
		if p is not None:
			p.pulse()

def _primaryRopHasParam(ctx: ActionContext, par: str):
	rop = ctx.primaryRop
	return rop and rop.par[par] is not None

def _anySelectedRopHasParam(ctx: ActionContext, par: str):
	for rop in ctx.selectedRops:
		if rop.par[par] is not None:
			return True
	return False

class _RopTypes:
	modularMat = 'raytk.operators.material.modularMat'
	rescaleField = 'raytk.operators.filter.rescaleField'
	raymarchRender3d = 'raytk.operators.output.raymarchRender3D'

def createActionManager():
	manager = ActionManager()
	manager.addActions(
		_AppendNull('Append Null'),
		_SimpleAction(
			'Inspect',
			isValid=lambda ctx: _primaryRopHasParam(ctx, 'Inspect'),
			execute=lambda ctx: _pulsePrimaryRopParam(ctx, 'Inspect'),
		),
		_SimpleAction(
			'Update OPs',
			isValid=lambda ctx: _anySelectedRopHasParam(ctx, 'Updateop'),
			execute=lambda ctx: _pulseSelectedRopParams(ctx, 'Updateop'),
		),
		_ConvertToFloatAction('Convert To Float'),
		_RescaleFieldAction('Rescale Field'),
		_RescaleFloatFieldAsVectorAction('Rescale As Vector'),
		_createAddInputAction(
			'Add Diffuse',
			[_RopTypes.modularMat],
			'raytk.operators.material.diffuseContrib',
			firstInput=1,
		),
		_createAddInputAction(
			'Add Specular',
			[_RopTypes.modularMat],
			'raytk.operators.material.specularContrib',
			firstInput=1,
		),
		_createAddInputAction(
			'Add Look At Camera',
			[_RopTypes.raymarchRender3d],
			'raytk.operators.camera.lookAtCamera',
			firstInput=1, lastInput=1,
		),
		_createAddInputAction(
			'Add Point Light',
			[_RopTypes.raymarchRender3d],
			'raytk.operators.light.pointLight',
			firstInput=2, lastInput=2,
		),
		_createConvertFrom2dSdfAction(
			'Extrude',
			'raytk.operators.convert.extrude'
		),
		_createConvertFrom2dSdfAction(
			'Revolve',
			'raytk.operators.convert.revolve'
		),
	)
	manager.addGroups(
		_CombineSdfsGroup('Combine SDFs'),
		_CreateVarRefGroup('Reference Variable'),
		_CreateRenderSelGroup('Select Output Buffer'),
	)
	return manager
