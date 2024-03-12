from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Union
from raytkUtil import isROP, isRComp, RaytkContext, ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from tools.palette.palette import Palette
	from _stubs.PopMenuExt import PopMenuExt

@dataclass
class ActionContext:
	pane: NetworkEditor
	parentComp: COMP
	selectedOps: List['OP']
	primaryOp: OP | None

	@property
	def primaryComp(self) -> COMP | None:
		return self.primaryOp if self.primaryOp and self.primaryOp.isCOMP else None

	def hasSelectedOps(
			self,
			minCount: int = 1, maxCount: Optional[int] = None,
			predicate: Callable[[OP], bool] = None,
			ignoreNonMatches: bool = True):
		selOps = self.selectedOps
		matches = selOps
		if predicate:
			matches = [o for o in matches if predicate(o)]
		if not ignoreNonMatches and len(matches) != len(selOps):
			return False
		if maxCount is not None and len(matches) > maxCount:
			return False
		if len(matches) < minCount:
			return False
		return True

@dataclass
class _MenuItem:
	text: str
	subItems: List['_MenuItem'] = None
	callback: Callable[[], None] = None

class _Item:
	def isValid(self, ctx: ActionContext) -> bool:
		raise NotImplementedError()

	def createMenuItem(self, ctx: ActionContext) -> _MenuItem:
		raise NotImplementedError()

@dataclass
class Action(_Item, ABC):
	text: str

	def execute(self, ctx: ActionContext):
		raise NotImplementedError()

	def createMenuItem(self, ctx: ActionContext) -> _MenuItem:
		return _MenuItem(
			text=self.text,
			callback=lambda: self.execute(ctx),
		)

@dataclass
class ActionGroup(_Item, ABC):
	text: str

	def getActions(self, ctx: ActionContext) -> List[Action]:
		raise NotImplementedError()

	def createMenuItem(self, ctx: ActionContext) -> _MenuItem:
		return _MenuItem(
			text=self.text,
			subItems=[
				action.createMenuItem(ctx)
				for action in self.getActions(ctx)
				if action.isValid(ctx)
			],
		)

class ActionManager:
	items: List[_Item]

	def __init__(self, *items: _Item):
		self.items = list(items)

	@staticmethod
	def _getEditor():
		pane = ui.panes.current
		if isinstance(pane, NetworkEditor):
			return pane
		for pane in ui.panes:
			if isinstance(pane, NetworkEditor):
				return pane

	def _getContext(self) -> Optional[ActionContext]:
		pane = self._getEditor()
		if not pane:
			return None
		comp = pane.owner
		return ActionContext(
			pane, comp,
			selectedOps=comp.selectedChildren,
			primaryOp=comp.currentChild,
		)

	def openMenu(self, popMenu: 'PopMenuExt'):
		ctx = self._getContext()
		if not ctx:
			return
		items = [
			action.createMenuItem(ctx)
			for action in self.items
			if action.isValid(ctx)
		]
		if not items:
			return
		self._openMenu(popMenu, items, isSubMenu=False)

	def _openMenu(
			self,
			popMenu: 'PopMenuExt',
			items: List[_MenuItem],
			isSubMenu: bool,
	):
		itemNames = [item.text for item in items]

		def getItem(info: dict):
			i = info['index']
			if 0 <= i < len(items):
				return items[i]

		def onSelect(info: dict):
			item = getItem(info)
			if item and item.callback:
				item.callback()
				info['menu'].Close()
				if popMenu != info['menu']:
					popMenu.Close()
			elif item and item.subItems:
				self._openMenu(
					popMenu=info['menu'],
					items=item.subItems,
					isSubMenu=True,
				)

		if isSubMenu:
			popMenu.OpenSubMenu(
				items=itemNames,
				callback=onSelect,
				allowStickySubMenus=False,
				autoClose=True,
			)
		else:
			popMenu.Open(
				items=itemNames,
				callback=onSelect,
				subMenuItems=[item.text for item in items if item.subItems],
				allowStickySubMenus=False,
				autoClose=True,
			)

	def buildTable(self, dat: scriptDAT):
		dat.clear()
		dat.appendRow(['name', 'label'])
		ctx = self._getContext()
		if not ctx:
			return
		for action in self.items:
			if action.isValid(ctx):
				item = action.createMenuItem(ctx)
				dat.appendRow([item.text, item.text])

def _isRopOrComp(o: OP):
	return isROP(o) or isRComp(o)

class EditorROPState:
	rop: OP | None
	info: ROPInfo

	def __init__(self, rop: OP | None):
		self.rop = rop
		self.info = ROPInfo(rop)

	def __bool__(self):
		return bool(self.rop and self.info)

	@property
	def currentDefTable(self) -> Optional[DAT]:
		return self.rop.op('definition') if self.rop and self.info.isROP else None

	def _defTypes(self, col: str) -> list[str]:
		dat = self.currentDefTable
		cell = dat[1, col] if dat else None
		return str(cell or '').split()

	@property
	def returnTypes(self): return self._defTypes('returnType')

	@property
	def coordTypes(self): return self._defTypes('coordType')

	@property
	def isField(self): return bool({'float', 'vec4'} & set(self.returnTypes))

	@property
	def isVectorField(self): return bool(self and 'vec4' in self.returnTypes)

	@property
	def isFloatField(self): return bool(self and 'float' in self.returnTypes)

	@property
	def isSdf(self): return bool(self and self.returnTypes == ['Sdf'])

	@property
	def is2d(self): return 'vec2' in self.coordTypes

	@property
	def is3d(self): return 'vec3' in self.coordTypes

	def hasCoordType(self, *types: str):
		return any([t in self.coordTypes for t in types])

	def hasReturnType(self, *types: str):
		return any([t in self.returnTypes for t in types])

	def getParam(self, parName: str):
		if self.rop:
			return self.rop.par[parName]

InitFunc = Callable[[COMP], None] | None

class ActionUtils:
	@staticmethod
	def palette() -> 'Palette': return op.raytk.op('tools/palette')

	@staticmethod
	def createROP(ropType: str, *inits: InitFunc, undo: 'Optional[Callable[[], None]]' = None):
		def init(rop: COMP):
			for fn in inits:
				if fn:
					fn(rop)
		ActionUtils.palette().CreateItem(ropType, postSetup=init, undoSetup=undo)

	@staticmethod
	def moveAfter(o: OP, after: OP):
		if not after:
			return
		o.nodeCenterY = after.nodeCenterY
		o.nodeX = after.nodeX + after.nodeWidth + 100

	@staticmethod
	def moveAfterMultiple(o: OP, after: List['OP']):
		if not after:
			return
		o.nodeCenterY = sum(a.nodeCenterY for a in after) / len(after)
		o.nodeX = max(a.nodeX + a.nodeWidth for a in after) + 100

	@staticmethod
	def createAndAttachFromOutput(
			fromRop: OP,
			ropType: str,
			init: InitFunc = None,
			inputIndex: int = 0,
			outputIndex: int = 0,
	):
		def placeAndAttach(rop: COMP):
			ActionUtils.moveAfter(rop, after=fromRop)
			rop.inputConnectors[inputIndex].connect(fromRop.outputConnectors[outputIndex])
		ActionUtils.createROP(ropType, placeAndAttach, init)

	@staticmethod
	def createAndAttachToInput(
			fromRop: OP,
			ropType: str,
			inits: List[InitFunc] = None,
			inputIndex: int = 0,
			outputIndex: int = 0,
	):
		def placeAndAttach(rop: COMP):
			rop.nodeCenterY = fromRop.nodeCenterY - 100
			rop.nodeX = fromRop.nodeX - rop.nodeWidth - 150
			rop.outputConnectors[outputIndex].connect(fromRop.inputConnectors[inputIndex])
		ActionUtils.createROP(ropType, placeAndAttach, *(inits or []))

	@staticmethod
	def createAndAttachFromMultiOutputs(
			fromRops: List['OP'],
			ropType: str,
			init: InitFunc = None,
			outputIndex: int = 0,
	):
		fromRops.sort(key=lambda r: r.nodeCenterY, reverse=True)
		def placeAndAttach(combine: COMP):
			ActionUtils.moveAfterMultiple(combine, fromRops)
			for i, fromRop in enumerate(fromRops):
				if i >= len(combine.inputConnectors):
					break
				combine.inputConnectors[i].connect(fromRop.outputConnectors[outputIndex])
		ActionUtils.createROP(ropType, placeAndAttach, init)

	@staticmethod
	def isKnownRopType(pathOrOpType: str):
		return ActionUtils.palette().IsKnownType(pathOrOpType)

IsValidFunc = Callable[[ActionContext], bool]
ExecuteFunc = Callable[[ActionContext], None]
GetActionsFunc = Callable[[ActionContext], List[Action]]

class SimpleAction(Action):
	def __init__(
			self, text: str,
			isValid: Optional[IsValidFunc],
			execute: ExecuteFunc,
	):
		super().__init__(text)
		self._isValid = isValid
		self._execute = execute

	def isValid(self, ctx: ActionContext) -> bool: return self._isValid is None or self._isValid(ctx)
	def execute(self, ctx: ActionContext): self._execute(ctx)

class SimpleGroup(ActionGroup):
	def __init__(
			self, text: str,
			isValid: Optional[IsValidFunc],
			getActions: Union[GetActionsFunc, List[Action]],
	):
		super().__init__(text)
		self._isValid = isValid
		if isinstance(getActions, list):
			self._getActions = lambda _: getActions
		else:
			self._getActions = getActions

	def isValid(self, ctx: ActionContext) -> bool: return self._isValid is None or self._isValid(ctx)
	def getActions(self, ctx: ActionContext) -> List[Action]: return self._getActions(ctx)

@dataclass
class OpSelect:
	test: Optional[Callable[['OP'], bool]] = None
	multi: bool = False
	minCount: int = 1
	maxCount: Optional[int] = None
	all: bool = False

	def matches(self, o: OP) -> bool:
		if not o:
			return False
		if self.all:
			return True
		if self.test and not self.test(o):
			return False
		return True

	def getOps(self, ctx: ActionContext) -> 'Optional[List[OP]]':
		matches = []
		primary = ctx.primaryOp
		if primary and self.matches(primary):
			matches.append(primary)
		if self.multi:
			for o in ctx.selectedOps:
				if o not in matches and self.matches(o):
					matches.append(o)
		if len(matches) < self.minCount:
			return None
		if self.maxCount is not None and len(matches) > self.maxCount:
			return None
		return matches

@dataclass
class RopSelect(OpSelect):
	ropTypes: Optional[List[str]] = None
	coordTypes: Optional[List[str]] = None
	returnTypes: Optional[List[str]] = None

	def matches(self, o: OP) -> bool:
		if not o:
			return False
		if self.all:
			return True
		opState = EditorROPState(o)
		if not opState:
			return False
		if self.ropTypes and opState.info.opType not in self.ropTypes:
			return False
		if self.coordTypes and not opState.hasCoordType(*self.coordTypes):
			return False
		if self.returnTypes and not opState.hasReturnType(*self.returnTypes):
			return False
		if self.test and not self.test(o):
			return False
		return True

@dataclass
class OpAttach:
	def placeAndAttach(self, newOp: COMP, fromOps: list[COMP]):
		raise NotImplementedError()

@dataclass
class AttachIntoExisting(OpAttach):
	inputIndex: int = 0
	outputIndex: int = 0
	useNextInput: bool = False

	def _nextInput(self, fromOp: COMP):
		inIndex = self.inputIndex
		if not self.useNextInput:
			return inIndex
		for conn in fromOp.inputConnectors[inIndex:]:
			if not conn.connections:
				return conn.index

	def placeAndAttach(self, newOp: COMP, fromOps: list[COMP]):
		for fromOp in fromOps:
			i = self._nextInput(fromOp)
			if i is None:
				raise Exception('No input connector available')
			newOp.nodeCenterY = fromOp.nodeCenterY - (150 * i)
			newOp.nodeX = fromOp.nodeX - newOp.nodeWidth - 150
			newOp.outputConnectors[self.outputIndex].connect(fromOp.inputConnectors[i])

@dataclass
class AttachOutFromExisting(OpAttach):
	inputIndex: int = 0
	outputIndex: int = 0

	def placeAndAttach(self, newOp: COMP, fromOps: list[COMP]):
		newOp.nodeX = max(o.nodeX + o.nodeWidth for o in fromOps) + 100
		newOp.nodeCenterY = sum(o.nodeCenterY for o in fromOps) / len(fromOps)
		inputIndex = self.inputIndex
		for i, fromOp in enumerate(sorted(fromOps, key=lambda r: r.nodeCenterY, reverse=True)):
			newOp.inputConnectors[inputIndex].connect(fromOp.outputConnectors[self.outputIndex])
			inputIndex += 1

@dataclass
class AttachOutputSelector(OpAttach):
	def placeAndAttach(self, newOp: COMP, fromOps: list[COMP]):
		newOp.nodeX = fromOps[0].nodeX + newOp.nodeWidth + 100
		newOp.nodeCenterY = fromOps[0].nodeCenterY - 200

@dataclass
class AttachReplacement(OpAttach):
	def placeAndAttach(self, newOp: COMP, fromOps: list[COMP]):
		origOp = fromOps[0]
		newOp.nodeX = origOp.nodeX
		newOp.nodeY = origOp.nodeY
		newInputCount = len(newOp.inputConnectors)
		for i, origConn in enumerate(origOp.inputConnectors):
			if i >= newInputCount:
				break
			if origConn.connections:
				newOp.inputConnectors[i].connect(origConn.connections[0])
		newOutputCount = len(newOp.outputConnectors)
		for i, origConn in enumerate(origOp.outputConnectors):
			if i >= newOutputCount:
				break
			for targetConn in origConn.connections:
				newOp.outputConnectors[i].connect(targetConn)

class OpInit:
	def init(self, o: COMP, ctx: ActionContext):
		raise NotImplementedError()

@dataclass
class InitSetParamOnPrimaryRop(OpInit):
	name: str
	val: Any

	def init(self, o: COMP, ctx: ActionContext):
		par = ctx.primaryOp.par[self.name]
		if par is not None:
			par.val = self.val

@dataclass
class InitAddToParamOnPrimaryRop(OpInit):
	name: str

	def init(self, o: COMP, ctx: ActionContext):
		par = ctx.primaryOp.par[self.name]
		if par is not None:
			if par.val:
				par.val += ' '
			par.val += ctx.primaryOp.relativePath(o)

@dataclass
class InitLinkPrimaryToParam(OpInit):
	paramName: str

	def init(self, o: COMP, ctx: ActionContext):
		o.par[self.paramName] = ctx.primaryOp

@dataclass
class InitBindParamsToPrimary(OpInit):
	paramNames: Dict[str, str]

	def init(self, o: COMP, ctx: ActionContext):
		primary = ctx.primaryOp
		exprBase = f"op('{o.relativePath(primary)}').par."
		for srcName, destName in self.paramNames.items():
			srcPar = primary.par[srcName]
			destPar = o.par[destName]
			if srcPar is not None and destPar is not None:
				destPar.bindExpr = exprBase + srcName

@dataclass
class ActionImpl(Action):
	ropType: str
	select: OpSelect
	attach: Optional[OpAttach] = None
	params: Dict[str, Any] = field(default_factory=dict)
	inits: List[Union[InitFunc, OpInit]] = field(default_factory=list)

	def isValid(self, ctx: ActionContext) -> bool:
		return ActionUtils.isKnownRopType(self.ropType) and bool(self.select.getOps(ctx))

	def execute(self, ctx: ActionContext):
		fromOps = self.select.getOps(ctx)
		def init(o: COMP):
			if self.attach:
				self.attach.placeAndAttach(o, fromOps or [])
			for name, val in self.params.items():
				o.par[name] = val
			for initFn in self.inits:
				if isinstance(initFn, OpInit):
					initFn.init(o, ctx)
				else:
					initFn(o)
		ActionUtils.createROP(self.ropType, init)

@dataclass
class GroupImpl(ActionGroup):
	select: RopSelect
	actions: Union[GetActionsFunc, List[Action]]

	def isValid(self, ctx: ActionContext) -> bool:
		return bool(self.select.getOps(ctx))

	def getActions(self, ctx: ActionContext) -> List[Action]:
		if isinstance(self.actions, list):
			return self.actions
		else:
			return self.actions(ctx)

class RopActionUtils:
	@staticmethod
	def getSelectedRops(ctx: ActionContext):
		return [
			o
			for o in ctx.selectedOps
			if _isRopOrComp(o)
		]

	@staticmethod
	def getAllRopStates(ctx: ActionContext):
		return [
			EditorROPState(o)
			for o in RaytkContext().ropChildrenOf(ctx.parentComp)
		]
