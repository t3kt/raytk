from dataclasses import dataclass, field
import json
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from editorToolsCommon import Action, ActionContext, ActionGroup, ActionManager, ActionUtils, InitFunc, ROPState

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from exposeParamDialog.exposeParamDialog import ExposeParamDialog

_IsValidFunc = Callable[[ActionContext], bool]
_ExecuteFunc = Callable[[ActionContext], None]
_GetActionsFunc = Callable[[ActionContext], List[Action]]
_OpPredicate = Callable[[OP], bool]

class _SimpleAction(Action):
	def __init__(
			self, text: str,
			isValid: Optional[_IsValidFunc],
			execute: _ExecuteFunc,
	):
		super().__init__(text)
		self._isValid = isValid
		self._execute = execute

	def isValid(self, ctx: ActionContext) -> bool: return self._isValid is None or self._isValid(ctx)
	def execute(self, ctx: ActionContext): self._execute(ctx)

class _SimpleGroup(ActionGroup):
	def __init__(
			self, text: str,
			isValid: Optional[_IsValidFunc],
			getActions: Union[_GetActionsFunc, List[Action]],
	):
		super().__init__(text)
		self._isValid = isValid
		if isinstance(getActions, list):
			self._getActions = lambda _: getActions
		else:
			self._getActions = getActions

	def isValid(self, ctx: ActionContext) -> bool: return self._isValid is None or self._isValid(ctx)
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

def _createAddInputActionGroup(
		text: str,
		createType: str,
		paramName: str,
		matchTypes: List[str],
		table: 'DAT',
):
	return _GroupImpl(
		text,
		select=_OpSelect(ropTypes=matchTypes),
		actions=[
			_ActionImpl(
				table[i, 'label'].val,
				ropType=createType,
				select=_OpSelect(ropTypes=matchTypes),
				attach=_AttachIntoExisting(inputIndex=1, useNextInput=True),
				params={paramName: table[i, 'name'].val},
			)
			for i in range(1, table.numRows)
		],
	)

def _createVarRefAction(label: str, variable: str, dataType: str, fieldName: Optional[str] = None):
	def execute(ctx: ActionContext):
		def init(refOp: 'COMP'):
			if fieldName:
				refOp.par.Field = fieldName
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
		execute=execute,
		isValid=None,
	)

def _loadTypeFields():
	typeFields = {}
	table = op('typeFields')  # type: DAT
	for i in range(1, table.numRows):
		typeName = table[i, 'parentType'].val
		fieldName = table[i, 'name'].val
		fieldLabel = table[i, 'label'].val
		if fieldName == 'this':
			continue
		if typeName in typeFields:
			typeFields[typeName].append((fieldName, fieldLabel))
		else:
			typeFields[typeName] = [(fieldName, fieldLabel)]
	return typeFields

_typeFields = _loadTypeFields()

def _createVarRefGroup(text: str):
	def getVariableObjs(ctx: ActionContext) -> List[dict]:
		stateText = ctx.primaryRopState.info.opStateText
		if not stateText:
			return []
		stateObj = json.loads(stateText)
		if not stateObj.get('variables'):
			return []
		return stateObj.get('variables')
	def isValid(ctx: ActionContext) -> bool:
		return bool(getVariableObjs(ctx))

	def getActions(ctx: ActionContext) -> List[Action]:
		actions = []
		for variableObj in getVariableObjs(ctx):
			dataType = variableObj['dataType']
			varName = variableObj['localName']
			actions.append(
				_createVarRefAction(
					label=variableObj['label'],
					variable=varName,
					dataType=dataType,
				)
			)
			for fieldName, fieldLabel in _typeFields.get(dataType) or ():
				actions.append(
					_createVarRefAction(
						label='  ' + fieldLabel,
						variable=varName,
						dataType=dataType,
						fieldName=fieldName,
					)
				)
		return actions
	return _SimpleGroup(text, isValid, getActions)

def _createRenderSelAction(label: str, name: str, enablePar: str):
	def execute(ctx: ActionContext):
		def init(refOp: 'COMP'):
			fromOp = ctx.primaryRop
			refOp.nodeCenterY = fromOp.nodeCenterY - 200
			refOp.nodeX = fromOp.nodeX + refOp.nodeWidth + 100
			if enablePar:
				fromOp.par[enablePar] = True
		ActionUtils.palette().CreateRenderSelect(
			ctx.primaryRop,
			outputName=name,
			postSetup=init,
		)
	return _SimpleAction(
		text=label,
		execute=execute,
		isValid=None,
	)

def _createRenderSelGroup(text: str):
	def isValid(ctx: ActionContext) -> bool:
		table = ctx.primaryRopState.info.outputBufferTable
		return bool(table and table.numRows > 1)

	def getActions(ctx: ActionContext) -> List[Action]:
		table = ctx.primaryRopState.info.outputBufferTable
		if not table:
			return []
		return [
			_createRenderSelAction(
				str(table[i, 'label']),
				str(table[i, 'name']),
				str(table[i, 'enablePar'] or ''))
			for i in range(1, table.numRows)
			if table[i, 'available'] != 'False'
		]
	return _SimpleGroup(text, isValid, getActions)

def _createAnimateParamAction(
		text: str,
		parOrTuplet: Union['Par', 'ParTupletT'],
		ropType: str, nameSuffix: str):
	def getPars():
		if isinstance(parOrTuplet, Par):
			return [parOrTuplet]
		return list(parOrTuplet)
	def isValid(_):
		return ActionUtils.isKnownRopType(ropType) and bool(getPars())
	def execute(ctx: ActionContext):
		o = ctx.primaryOp
		pars = getPars()
		if not pars:
			return
		if len(pars) == 1:
			parOrTupletName = pars[0].name
		else:
			parOrTupletName = pars[0].tupletName
		undoInfo = {}
		def init(gen: 'COMP'):
			gen.name = f'{o.name}_{parOrTupletName}_{nameSuffix}'
			chop = gen.parent().create(nullCHOP, f'{o.name}_{parOrTupletName}_vals')
			undoInfo['chop'] = chop
			gen.par.Name = ' '.join(p.name for p in pars)
			chop.inputConnectors[0].connect(gen.outputConnectors[0])
			gen.nodeCenterY = o.nodeCenterY - 100
			gen.nodeX = o.nodeX - gen.nodeWidth - 300
			chop.nodeCenterY = gen.nodeCenterY
			chop.nodeX = gen.nodeX + gen.nodeWidth + 100
			chop.viewer = True
			parStates = []
			for par in pars:
				parStates.append({
					'name': par.name,
					'mode': par.mode,
					'val': par.val,
					'expr': par.expr,
					'bindExpr': par.bindExpr,
				})
				par.expr = f"op('{chop.name}')['{par.name}']"
			undoInfo['parStates'] = parStates
		def undo():
			chop = undoInfo.get('chop')
			if chop:
				try:
					chop.destroy()
				except:
					pass
			parStates = undoInfo.get('parStates')
			if parStates:
				for i, par in enumerate(pars):
					state = parStates[i]
					par.val = state['val']
					par.expr = state['expr']
					par.bindExpr = state['bindExpr']
					par.mode = state['mode']
		ActionUtils.createROP(ropType, init, undo=undo)
	return _SimpleAction(text, isValid, execute)

def _createAnimateParamsGroup(text: str, ropType: str, nameSuffix: str):
	def getActions(ctx: ActionContext) -> List[Action]:
		o = ctx.primaryOp
		if not o:
			return []
		actions = []
		tuplets = o.customTuplets
		if not tuplets:
			for par in o.builtinPars:
				if par.tuplet not in tuplets:
					tuplets.append(par.tuplet)
			tuplets.sort(key=lambda t: t[0].tupletName)
		for t in tuplets:
			if not t[0].isNumber:
				continue
			actions.append(_createAnimateParamAction(t[0].label, t, ropType, nameSuffix))
			if len(t) > 1:
				for p in t:
					actions.append(_createAnimateParamAction(
						f'{t[0].label} ({p.name[-1]})', p, ropType, nameSuffix))
		return actions
	return _SimpleGroup(text, lambda _: True, getActions)

def _createExposeParamGroup(text: str):
	def isValid(ctx: ActionContext):
		o = ctx.primaryOp
		return bool(o and o.customTuplets)

	ignorePars = ['Inspect', 'Updateop', 'Help']

	def getActions(ctx: ActionContext):
		o = ctx.primaryOp
		if not o:
			return []
		actions = []
		for parTuplet in o.customTuplets:
			if parTuplet[0].name in ignorePars:
				continue
			if len(parTuplet) > 1:
				actions.append(_createExposeParamOrTupletAction(parTuplet))
			for par in parTuplet:
				actions.append(_createExposeParamOrTupletAction(par))
		return actions

	return _SimpleGroup(text, isValid, getActions)

def _createExposeParamOrTupletAction(parOrTuplet: 'Union[Par, ParTupletT]'):
	def execute(ctx: ActionContext):
		dialog = op('exposeParamDialog')  # type: Union[COMP, ExposeParamDialog]
		scene = ctx.parentComp
		if isinstance(parOrTuplet, Par):
			dialog.ShowForParam(parOrTuplet, scene)
		else:
			dialog.ShowForTuplet(parOrTuplet, scene)
	if isinstance(parOrTuplet, Par):
		suffix = parOrTuplet.name.replace(parOrTuplet.tupletName, '').upper()
		text = f'{parOrTuplet.label} ({suffix})'
	else:
		text = parOrTuplet[0].label
	return _SimpleAction(text, execute=execute, isValid=None)

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

def _createTableBasedGroup(
		text: str, table: 'DAT',
		ropType: str,
		paramName: str,
		select: '_OpSelect',
		attach: '_OpAttach',
):
	return _GroupImpl(
		text,
		select,
		[
			_ActionImpl(
				str(table[i, 'label']),
				ropType=ropType,
				select=select,
				attach=attach,
				params={paramName: str(table[i, 'name'])},
			)
			for i in range(1, table.numRows)
		])

def _createTypeListGroup(
		text: str,
		typesAndLabels: List[Tuple[str, str]],
		select: '_OpSelect',
		attach: '_OpAttach',
):
	return _GroupImpl(
		text,
		select,
		[
			_ActionImpl(
				label,
				ropType=ropType,
				select=select,
				attach=attach
			)
			for ropType, label in typesAndLabels
		]
	)

def _createGoToAction(text: str, getTargets: Callable[[ActionContext], List[OP]]):
	def isValid(ctx: ActionContext):
		return bool(getTargets(ctx))
	def execute(ctx: ActionContext):
		targets = getTargets(ctx)
		if not targets:
			return
		targets[0].current = True
		if len(targets) == 1:
			ctx.pane.home(zoom=True, op=targets[0])
		else:
			for o in list(ctx.parentComp.selectedChildren):
				if o not in targets:
					o.selected = False
			for o in targets:
				o.selected = True
			ctx.pane.homeSelected(zoom=True)
	return _SimpleAction(text, isValid, execute)

def _createGoToGroup(text: str):
	def _getVariableSource(ctx: ActionContext):
		if not ctx.primaryRopState or ctx.primaryRopState.info.opType != _RopTypes.variableReference:
			return []
		source = ctx.primaryRop.par.Source.eval()
		return [source] if source else []
	def _getVariableReferences(ctx: ActionContext):
		sources = ctx.selectedRops
		return [
			ropState.rop
			for ropState in ctx.allRopStates
			if ropState.info.opType == _RopTypes.variableReference and ropState.rop.par.Source.eval() in sources
		]
	actions = [
		_createGoToAction('Variable Source', getTargets=_getVariableSource),
		_createGoToAction('Variable References', getTargets=_getVariableReferences),
	]
	def isValid(ctx: ActionContext):
		return any([action.isValid(ctx) for action in actions])
	return _SimpleGroup(
		text,
		isValid=isValid,
		getActions=lambda _: actions,
	)

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
	return any(rop.par[par] is not None for rop in ctx.selectedRops)

class _RopTypes:
	crossSection = 'raytk.operators.convert.crossSection'
	modularMat = 'raytk.operators.material.modularMat'
	pointMapRender = 'raytk.operators.output.pointMapRender'
	projectPlane = 'raytk.operators.convert.projectPlane'
	rescaleField = 'raytk.operators.filter.rescaleField'
	raymarchRender3d = 'raytk.operators.output.raymarchRender3D'
	render2d = 'raytk.operators.output.render2D'
	speedGenerator = 'raytk.operators.utility.speedGenerator'
	lfoGenerator = 'raytk.operators.utility.lfoGenerator'
	vectorToFloat = 'raytk.operators.convert.vectorToFloat'
	variableReference = 'raytk.operators.utility.variableReference'

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
		_ActionImpl(
			'Convert To Float',
			'raytk.operators.field.sdfField',
			select=_OpSelect(returnTypes=['Sdf']),
			attach=_AttachOutFromExisting(),
		),
		_ActionImpl(
			'Convert To SDF',
			'raytk.operators.field.floatToSdf',
			select=_OpSelect(returnTypes=['float']),
			attach=_AttachOutFromExisting(),
		),
		_createTableBasedGroup(
			'To Vector Part', op('vectorToFloatParts'), _RopTypes.vectorToFloat, 'Usepart',
			select=_OpSelect(returnTypes=['vec4']),
			attach=_AttachOutFromExisting(),
		),
		_ActionImpl(
			'Rescale Field',
			_RopTypes.rescaleField,
			select=_OpSelect(returnTypes=['float', 'vec4']),
			attach=_AttachOutFromExisting(),
		),
		_ActionImpl(
			'Rescale As Vector',
			_RopTypes.rescaleField,
			select=_OpSelect(returnTypes=['float']),
			attach=_AttachOutFromExisting(),
			params={'Returntype': 'vec4'},
		),
		_createTableBasedGroup(
			'Project Plane', op('projectPlanes'), _RopTypes.projectPlane, 'Plane',
			select=_OpSelect(coordTypes=['vec2']),
			attach=_AttachOutFromExisting(),
		),
		_createTableBasedGroup(
			'Cross Section', op('crossSectionAxes'), _RopTypes.crossSection, 'Axes',
			select=_OpSelect(coordTypes=['vec3']),
			attach=_AttachOutFromExisting(),
		),
		_createAddInputActionGroup(
			'Add Diffuse',
			'raytk.operators.material.diffuseContrib',
			paramName='Method',
			matchTypes=[_RopTypes.modularMat],
			table=op('diffuseContribMethods')),
		_createAddInputActionGroup(
			'Add Specular',
			'raytk.operators.material.specularContrib',
			paramName='Method',
			matchTypes=[_RopTypes.modularMat],
			table=op('specularContribMethods')),
		_createTypeListGroup(
			'Add Camera',
			typesAndLabels=[
				('raytk.operators.camera.basicCamera', 'Basic Camera'),
				('raytk.operators.camera.fisheyeCamera', 'Fisheye Camera'),
				('raytk.operators.camera.linkedCamera', 'Linked Camera'),
				('raytk.operators.camera.lookAtCamera', 'Look At Camera'),
			],
			select=_OpSelect(ropTypes=[_RopTypes.raymarchRender3d, _RopTypes.pointMapRender]),
			attach=_AttachIntoExisting(inputIndex=1),
		),
		_createTypeListGroup(
			'Add Light',
			typesAndLabels=[
				('raytk.operators.light.axisLight', 'Axis Light'),
				('raytk.operators.light.directionalLight', 'Directional Light'),
				('raytk.operators.light.linkedLight', 'Linked Light'),
				('raytk.operators.light.pointLight', 'Point Light'),
				('raytk.operators.light.spotLight', 'Spot Light'),
			],
			select=_OpSelect(ropTypes=[_RopTypes.raymarchRender3d, _RopTypes.pointMapRender]),
			attach=_AttachIntoExisting(inputIndex=2),
		),
		_ActionImpl(
			'Extrude',
			'raytk.operators.convert.extrude',
			select=_OpSelect(coordTypes=['vec2'], returnTypes=['Sdf']),
			attach=_AttachOutFromExisting(),
		),
		_ActionImpl(
			'Revolve',
			'raytk.operators.convert.revolve',
			select=_OpSelect(coordTypes=['vec2'], returnTypes=['Sdf']),
			attach=_AttachOutFromExisting(),
		),
		_ActionImpl(
			'Colorize 2D SDF',
			'raytk.operators.material.colorizeSdf2d',
			select=_OpSelect(coordTypes=['vec2'], returnTypes=['Sdf']),
			attach=_AttachOutFromExisting(),
		),
		_createTableBasedGroup(
			'Combine SDFs',
			ropType='raytk.operators.combine.combine',
			paramName='Combine',
			table=op('sdfCombineModes'),
			select=_OpSelect(
				returnTypes=['Sdf'],
				multi=True, minCount=2, maxCount=2),
			attach=_AttachOutFromExisting()),
		_createTableBasedGroup(
			'Arrange SDFs',
			ropType='raytk.operators.combine.arrange',
			paramName='Combine',
			table=op('sdfCombineModes'),
			select=_OpSelect(
				returnTypes=['Sdf'],
				multi=True, minCount=2, maxCount=None),
			attach=_AttachOutFromExisting()),
		_ActionImpl(
			'Switch OPs',
			ropType='raytk.operators.combine.switch',
			select=_OpSelect(multi=True, minCount=2, maxCount=None),
			attach=_AttachOutFromExisting()),
		_ActionImpl(
			'Blend OPs',
			ropType='raytk.operators.combine.switch',
			select=_OpSelect(multi=True, minCount=2, maxCount=None),
			attach=_AttachOutFromExisting(),
			params={'Blend': True}),
		_createTableBasedGroup(
			'Combine Fields',
			ropType='raytk.operators.combine.combineFields',
			paramName='Operation',
			table=op('fieldCombineModes'),
			select=_OpSelect(
				returnTypes=['float', 'vec4'],
				multi=True, minCount=True, maxCount=None),
			attach=_AttachOutFromExisting()),
		_createTableBasedGroup(
			'Composite Fields',
			ropType='raytk.operators.combine.compositeFields',
			paramName='Blendmode',
			table=op('compositeModes'),
			select=_OpSelect(
				returnTypes=['vec4'],
				multi=True, minCount=True, maxCount=None),
			attach=_AttachOutFromExisting()),
		_ActionImpl(
			'Combine Lights',
			ropType='raytk.operators.light.multiLight',
			select=_OpSelect(
				returnTypes=['Light'],
				multi=True, minCount=True, maxCount=None),
			attach=_AttachOutFromExisting()),
		_createVarRefGroup('Reference Variable'),
		_createRenderSelGroup('Select Output Buffer'),
		_ActionImpl(
			'Select Depth Map',
			ropType='raytk.operators.post.depthMap',
			select=_OpSelect(ropTypes=[_RopTypes.raymarchRender3d]),
			attach=_AttachOutFromExisting(inputIndex=0, outputIndex=2),
		),
		_ActionImpl(
			'Select Object Id Mask',
			ropType='raytk.operators.post.objectIdMask',
			select=_OpSelect(ropTypes=[_RopTypes.raymarchRender3d]),
			attach=_AttachOutputSelector(),
			inits=[
				_LinkPrimaryToParam('Outputop'),
				_SetParamOnPrimaryRop('Enableobjectidoutput', True),
			]
		),
		_createAnimateParamsGroup(
			'Animate With Speed', _RopTypes.speedGenerator, 'speedGen'),
		_createAnimateParamsGroup(
			'Animate With LFO', _RopTypes.lfoGenerator, 'lfoGen'),
		_createExposeParamGroup('Expose Parameter'),
		_createCustomizeShaderConfigAction('Customize Shader Config'),
		_ActionImpl(
			'Add render2D',
			ropType=_RopTypes.render2d,
			select=_OpSelect(coordTypes=['vec2']),
			attach=_AttachOutFromExisting(),
		),
		_ActionImpl(
			'Add raymarchRender3d',
			ropType=_RopTypes.raymarchRender3d,
			select=_OpSelect(coordTypes=['vec3'], returnTypes=['Sdf']),
			attach=_AttachOutFromExisting(),
		),
		_createGoToGroup('Go to'),
	)
	return manager

@dataclass
class _OpSelect:
	ropTypes: Optional[List[str]] = None
	coordTypes: Optional[List[str]] = None
	returnTypes: Optional[List[str]] = None
	multi: bool = False
	test: Optional[Callable[[ROPState], bool]] = None
	minCount: int = 1
	maxCount: Optional[int] = None
	all: bool = False

	def _matches(self, opState: ROPState) -> bool:
		if not opState:
			return False
		if self.all:
			return True
		if self.ropTypes and opState.info.opType not in self.ropTypes:
			return False
		if self.coordTypes and not opState.hasCoordType(*self.coordTypes):
			return False
		if self.returnTypes and not opState.hasReturnType(*self.returnTypes):
			return False
		if self.test and not self.test(opState):
			return False
		return True

	def getOps(self, ctx: ActionContext):
		matches = []
		primaryRopState = ctx.primaryRopState
		if primaryRopState and self._matches(primaryRopState):
			matches.append(ctx.primaryRopState.rop)
		if self.multi:
			for opState in ctx.selectedRopStates:
				if opState.rop not in matches and self._matches(opState):
					matches.append(opState.rop)
		if len(matches) < self.minCount:
			return None
		if self.maxCount is not None and len(matches) > self.maxCount:
			return None
		return matches

@dataclass
class _OpAttach:
	def placeAndAttach(self, newOp: 'COMP', fromOps: 'List[COMP]'):
		raise NotImplementedError()

@dataclass
class _AttachIntoExisting(_OpAttach):
	inputIndex: int = 0
	outputIndex: int = 0
	useNextInput: bool = False

	def _nextInput(self, fromOp: 'COMP'):
		inIndex = self.inputIndex
		if not self.useNextInput:
			return inIndex
		for conn in fromOp.inputConnectors[inIndex:]:
			if not conn.connections:
				return conn.index

	def placeAndAttach(self, newOp: 'COMP', fromOps: 'List[COMP]'):
		for fromOp in fromOps:
			i = self._nextInput(fromOp)
			if i is None:
				raise Exception('No input connector available')
			newOp.nodeCenterY = fromOp.nodeCenterY - (150 * i)
			newOp.nodeX = fromOp.nodeX - newOp.nodeWidth - 150
			newOp.outputConnectors[self.outputIndex].connect(fromOp.inputConnectors[i])

@dataclass
class _AttachOutFromExisting(_OpAttach):
	inputIndex: int = 0
	outputIndex: int = 0

	def placeAndAttach(self, newOp: 'COMP', fromOps: 'List[COMP]'):
		newOp.nodeX = max(o.nodeX + o.nodeWidth for o in fromOps) + 100
		newOp.nodeCenterY = sum(o.nodeCenterY for o in fromOps) / len(fromOps)
		inputIndex = self.inputIndex
		for i, fromOp in enumerate(sorted(fromOps, key=lambda r: r.nodeCenterY, reverse=True)):
			newOp.inputConnectors[inputIndex].connect(fromOp.outputConnectors[self.outputIndex])
			inputIndex += 1

@dataclass
class _AttachOutputSelector(_OpAttach):
	def placeAndAttach(self, newOp: 'COMP', fromOps: 'List[COMP]'):
		newOp.nodeX = fromOps[0].nodeX + newOp.nodeWidth + 100
		newOp.nodeCenterY = fromOps[0].nodeCenterY - 200

class _OpInit:
	def init(self, rop: 'COMP', ctx: ActionContext):
		raise NotImplementedError()

@dataclass
class _SetParamOnPrimaryRop(_OpInit):
	name: str
	val: Any

	def init(self, rop: 'COMP', ctx: ActionContext):
		par = ctx.primaryRop.par[self.name]
		if par is not None:
			par.val = self.val

@dataclass
class _LinkPrimaryToParam(_OpInit):
	paramName: str

	def init(self, rop: 'COMP', ctx: ActionContext):
		rop.par[self.paramName] = ctx.primaryRop

@dataclass
class _ActionImpl(Action):
	ropType: str
	select: _OpSelect
	attach: Optional[_OpAttach] = None
	params: Dict[str, Any] = field(default_factory=dict)
	inits: List[Union[InitFunc, _OpInit]] = field(default_factory=list)

	def isValid(self, ctx: ActionContext) -> bool:
		return ActionUtils.isKnownRopType(self.ropType) and bool(self.select.getOps(ctx))

	def execute(self, ctx: ActionContext):
		fromOps = self.select.getOps(ctx)
		def init(o: 'COMP'):
			if self.attach:
				self.attach.placeAndAttach(o, fromOps)
			for name, val in self.params.items():
				o.par[name] = val
			for initFn in self.inits:
				if isinstance(initFn, _OpInit):
					initFn.init(o, ctx)
				else:
					initFn(o)
		ActionUtils.createROP(self.ropType, init)

@dataclass
class _GroupImpl(ActionGroup):
	select: _OpSelect
	actions: Union[_GetActionsFunc, List[Action]]

	def isValid(self, ctx: ActionContext) -> bool:
		return bool(self.select.getOps(ctx))

	def getActions(self, ctx: ActionContext) -> List[Action]:
		if isinstance(self.actions, list):
			return self.actions
		else:
			return self.actions(ctx)
