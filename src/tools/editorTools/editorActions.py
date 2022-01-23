from typing import Callable, List, Optional, Union
from editorToolsCommon import Action, ActionContext, ActionGroup, ActionManager, ActionUtils, ROPState
from raytkUtil import showPromptDialog

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

_IsValidFunc = Callable[[ActionContext], bool]
_ExecuteFunc = Callable[[ActionContext], None]
_GetActionsFunc = Callable[[ActionContext], List[Action]]
_OpPredicate = Callable[[OP], bool]

class _SimpleAction(Action):
	def __init__(
			self, text: str,
			isValid: _IsValidFunc,
			execute: _ExecuteFunc,
	):
		super().__init__(text)
		self._isValid = isValid
		self._execute = execute

	def isValid(self, ctx: ActionContext) -> bool: return self._isValid(ctx)
	def execute(self, ctx: ActionContext): self._execute(ctx)

class _SimpleGroup(ActionGroup):
	def __init__(
			self, text: str,
			isValid: _IsValidFunc,
			getActions: _GetActionsFunc,
	):
		super().__init__(text)
		self._isValid = isValid
		self._getActions = getActions

	def isValid(self, ctx: ActionContext) -> bool: return self._isValid(ctx)
	def getActions(self, ctx: ActionContext) -> List[Action]: return self._getActions(ctx)

def _createAppendNull(text: str):
	def execute(ctx: ActionContext):
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

	def isValid(ctx: ActionContext) -> bool:
		return bool(ctx.primaryOp and ctx.primaryOp.outputConnectors)

	return _SimpleAction(text, isValid, execute)

def _createConvertToFloatAction(text: str):
	def isValid(ctx: ActionContext) -> bool:
		state = ctx.primaryRopState
		return bool(state and state.isVectorField or state.isSdf)

	def execute(ctx: ActionContext):
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

	return _SimpleAction(text, isValid, execute)

def _createAddOutputAction(
		text: str,
		isValid: _IsValidFunc,
		ropType: str,
		paramVals: Optional[dict] = None,
):
	def isValidWrapper(ctx: ActionContext):
		if not ActionUtils.isKnownRopType(ropType):
			return False
		return not isValid or isValid(ctx)

	def execute(ctx: ActionContext):
		def init(rop: 'COMP'):
			if paramVals:
				for name, val in paramVals.items():
					rop.par[name] = val
		ActionUtils.createAndAttachFromOutput(
			fromRop=ctx.primaryRop,
			ropType=ropType,
			init=init,
		)
	return _SimpleAction(text, isValidWrapper, execute)

def _createCombineActionGroup(
		text: str, ropType: str, paramName: str,
		modeTable: 'DAT',
		minCount: int, maxCount: Optional[int] = None,
		ignoreNonMatches: bool = True,
		matchPredicate: Optional[_OpPredicate] = None,
):
	def isValid(ctx: ActionContext):
		if not ActionUtils.isKnownRopType(ropType):
			return False
		return ctx.hasSelectedOps(minCount, maxCount, matchPredicate, ignoreNonMatches)
	def createAction(label: str, value: str):
		def execute(ctx: ActionContext):
			inputs = ctx.selectedRops
			if matchPredicate:
				inputs = [o for o in inputs if matchPredicate(o)]
			def init(rop: 'COMP'):
				rop.par[paramName] = value
			ActionUtils.createAndAttachFromMultiOutputs(inputs, ropType, init)
		return _SimpleAction(label, isValid, execute)
	actions = [
		createAction(modeTable[i, 'label'].val, modeTable[i, 'name'].val)
		for i in range(1, modeTable.numRows)
	]
	return _SimpleGroup(text, isValid, lambda _: actions)

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

def _createVarRefGroup(text: str):
	def isValid(ctx: ActionContext) -> bool:
		table = ctx.primaryRopState.info.variableTable
		return table and table.numRows > 1

	def getActions(ctx: ActionContext) -> List[Action]:
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
	return _SimpleGroup(text, isValid, getActions)

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

def _createRenderSelGroup(text: str):
	def isValid(ctx: ActionContext) -> bool:
		return any(ctx.primaryRopState.info.outputBufferNamesAndLabels)

	def getActions(ctx: ActionContext) -> List[Action]:
		return [
			_createRenderSelAction(label, name)
			for name, label in ctx.primaryRopState.info.outputBufferNamesAndLabels
		]
	return _SimpleGroup(text, isValid, getActions)

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
		if not ActionUtils.isKnownRopType(createType):
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

def _createConvertFrom2dSdfAction(text: str, ropType: str):
	def isValid(ctx: ActionContext):
		return ctx.primaryRopState.isSdf and ctx.primaryRopState.is2d
	return _createAddOutputAction(text, isValid, ropType)

def _createAnimateParamAction(
		text: str,
		parOrTuplet: Union['Par', 'ParTupletT'],
		ropType: str, nameSuffix: str):
	def getPars(ctx: ActionContext):
		if isinstance(parOrTuplet, Par):
			return [parOrTuplet]
		return list(parOrTuplet)
	def isValid(ctx: ActionContext):
		if not ActionUtils.isKnownRopType(ropType):
			return False
		return bool(getPars(ctx))
	def execute(ctx: ActionContext):
		rop = ctx.primaryRop
		pars = getPars(ctx)
		if not pars:
			return
		if len(pars) == 1:
			parOrTupletName = pars[0].name
		else:
			parOrTupletName = pars[0].tupletName
		def init(gen: 'COMP'):
			gen.name = f'{rop.name}_{parOrTupletName}_{nameSuffix}'
			chop = gen.parent().create(nullCHOP, f'{rop.name}_{parOrTupletName}_vals')
			gen.par.Name = ' '.join(p.name for p in pars)
			chop.inputConnectors[0].connect(gen.outputConnectors[0])
			gen.nodeCenterY = rop.nodeCenterY - 100
			gen.nodeX = rop.nodeX - gen.nodeWidth - 300
			chop.nodeCenterY = gen.nodeCenterY
			chop.nodeX = gen.nodeX + gen.nodeWidth + 100
			chop.viewer = True
			for par in pars:
				par.expr = f"op('{chop.name}')['{par.name}']"
		ActionUtils.createROP(ropType, init)
	return _SimpleAction(text, isValid, execute)

def _createAnimateParamsGroup(text: str, ropType: str, nameSuffix: str):
	def isValid(ctx: ActionContext) -> bool:
		rop = ctx.primaryRop
		return bool(rop and rop.current and ActionUtils.isKnownRopType(ropType))

	def getActions(ctx: ActionContext) -> List[Action]:
		rop = ctx.primaryRop
		if not rop:
			return []
		actions = []
		for t in rop.customTuplets:
			if not t[0].isNumber:
				continue
			actions.append(_createAnimateParamAction(t[0].label, t, ropType, nameSuffix))
			if len(t) > 1:
				for p in t:
					actions.append(_createAnimateParamAction(
						f'{t[0].label} ({p.name[-1]})', p, ropType, nameSuffix))
		return actions
	return _SimpleGroup(text, isValid, getActions)

def _createExposeParamGroup(text: str):
	def isValid(ctx: ActionContext):
		o = ctx.primaryOp
		return bool(o and o.customTuplets)
	def createAction(parTuplet: 'ParTupletT'):
		def execute(ctx: ActionContext):
			scene = ctx.parentComp
			showPromptDialog(
				'Parameter Name Prefix',
				'Provide a prefix for the exposed parameters',
				ok=lambda prefix: _exposeParamTuplet(scene, parTuplet, prefix),
			)
		return _SimpleAction(parTuplet[0].label, isValid, execute)
	def getActions(ctx: ActionContext):
		o = ctx.primaryOp
		if not o:
			return []
		return [createAction(t) for t in o.customTuplets]
	return _SimpleGroup(text, isValid, getActions)

def _exposeParamTuplet(
		scene: 'COMP', parTuplet: 'ParTupletT', prefix: str):
	ui.undo.startBlock(f'Exposing parameter {parTuplet[0].tupletName}')
	scenePage = scene.customPages[0] if scene.customPages else scene.appendCustomPage(parTuplet[0].page.name)
	label = (prefix + ' ' if prefix else '') + parTuplet[0].label
	par = parTuplet[0]
	if parTuplet[0].isMenu:
		newPars = scenePage.appendMenu((prefix + par.name).capitalize(), label=label)
		newPars[0].menuSource = scene.shortcutPath(parTuplet[0].owner, toParName=parTuplet[0].name)
	elif len(parTuplet) == 1:
		newPars = scenePage.appendPar(prefix + par.name, par=par, label=label)
	else:
		newPars = scenePage.appendPar(prefix + par.tupletName, par=par, label=label)
	for i, newPar in enumerate(newPars):
		par = parTuplet[i]
		newPar.val = par.eval()
		par.bindExpr = par.owner.shortcutPath(scene, toParName=newPar.name)
	ui.undo.endBlock()

def _createCustomizeShaderConfigAction(text: str):
	def getTriggerPars(ctx: ActionContext):
		pars = []
		for rop in ctx.selectedRops:
			if rop.par['Shaderbuilderconfig']:
				continue
			builder = rop.op('shaderBuilder')
			if builder and builder.par['Createcustomconfig'] is not None:
				pars.append(builder.par.Createcustomconfig)
		return pars
	def isValid(ctx: ActionContext):
		return bool(getTriggerPars(ctx))
	def execute(ctx: ActionContext):
		pars = getTriggerPars(ctx)
		for par in pars:
			par.pulse()
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
	combine = 'raytk.operators.combine.combine'
	combineFields = 'raytk.operators.combine.combineFields'
	modularMat = 'raytk.operators.material.modularMat'
	rescaleField = 'raytk.operators.filter.rescaleField'
	raymarchRender3d = 'raytk.operators.output.raymarchRender3D'
	render2d = 'raytk.operators.output.render2D'
	speedGenerator = 'raytk.operators.utility.speedGenerator'
	lfoGenerator = 'raytk.operators.utility.lfoGenerator'

def createActionManager():
	manager = ActionManager(
		_createAppendNull('Append Null'),
		_SimpleAction(
			'Inspect',
			isValid=lambda ctx: _primaryRopHasParam(ctx, 'Inspect'),
			execute=lambda ctx: _pulsePrimaryRopParam(ctx, 'Inspect')),
		_SimpleAction(
			'Update OPs',
			isValid=lambda ctx: _anySelectedRopHasParam(ctx, 'Updateop'),
			execute=lambda ctx: _pulseSelectedRopParams(ctx, 'Updateop')),
		_createConvertToFloatAction('Convert To Float'),
		_createAddOutputAction(
			'Rescale Field',
			isValid=lambda ctx: ctx.primaryRopState.isField,
			ropType=_RopTypes.rescaleField),
		_createAddOutputAction(
			'Rescale As Vector',
			isValid=lambda ctx: ctx.primaryRopState.isFloatField,
			ropType=_RopTypes.rescaleField,
			paramVals={'Returntype': 'vec4'}),
		_createAddInputAction(
			'Add Diffuse',
			[_RopTypes.modularMat],
			'raytk.operators.material.diffuseContrib',
			firstInput=1),
		_createAddInputAction(
			'Add Specular',
			[_RopTypes.modularMat],
			'raytk.operators.material.specularContrib',
			firstInput=1),
		_createAddInputAction(
			'Add Look At Camera',
			[_RopTypes.raymarchRender3d],
			'raytk.operators.camera.lookAtCamera',
			firstInput=1, lastInput=1),
		_createAddInputAction(
			'Add Point Light',
			[_RopTypes.raymarchRender3d],
			'raytk.operators.light.pointLight',
			firstInput=2, lastInput=2),
		_createConvertFrom2dSdfAction('Extrude', 'raytk.operators.convert.extrude'),
		_createConvertFrom2dSdfAction('Revolve', 'raytk.operators.convert.revolve'),
		_createConvertFrom2dSdfAction('Colorize 2D SDF', 'raytk.operators.material.colorizeSdf2d'),
		_createCombineActionGroup(
			'Combine SDFs', _RopTypes.combine, 'Combine', op('sdfCombineModes'),
			minCount=2, maxCount=2,
			matchPredicate=lambda o: ROPState(o).isSdf),
		_createCombineActionGroup(
			'Combine Fields', _RopTypes.combineFields, 'Operation', op('fieldCombineModes'),
			minCount=2, maxCount=2,
			matchPredicate=lambda o: ROPState(o).isField),
		_createVarRefGroup('Reference Variable'),
		_createRenderSelGroup('Select Output Buffer'),
		_createAnimateParamsGroup(
			'Animate With Speed', _RopTypes.speedGenerator, 'speedGen'),
		_createAnimateParamsGroup(
			'Animate With LFO', _RopTypes.lfoGenerator, 'lfoGen'),
		_createExposeParamGroup('Expose Parameter'),
		_createCustomizeShaderConfigAction('Customize Shader Config'),
		_createAddOutputAction(
			'Add render2D',
			lambda ctx: ctx.primaryRopState.is2d,
			_RopTypes.render2d,
		),
	)
	return manager
