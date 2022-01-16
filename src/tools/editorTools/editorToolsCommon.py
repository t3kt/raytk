from abc import ABC
from dataclasses import dataclass
from typing import List, Optional, Callable
from raytkUtil import isROP, isRComp, RaytkContext, ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from tools.palette.palette import Palette
	from _stubs.PopMenuExt import PopMenuExt

@dataclass
class ActionContext:
	pane: 'NetworkEditor'
	parentComp: 'COMP'
	selectedOps: List['OP']
	primaryOp: Optional['OP']
	allRops: List['OP']

	@property
	def selectedRops(self):
		return [o for o in self.selectedOps if _isRopOrComp(o)]

	@property
	def selectedRopStates(self):
		return [ROPState(o) for o in self.selectedOps if _isRopOrComp(o)]

	@property
	def primaryRop(self):
		return self.primaryOp if _isRopOrComp(self.primaryOp) else None

	@property
	def primaryRopState(self): return ROPState(self.primaryRop)

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

def _getPopMenu() -> 'PopMenuExt':
	return op.TDResources.op('popMenu')

class ActionManager:
	actions: List[Action]
	groups: List[ActionGroup]

	def __init__(self):
		self.actions = []
		self.groups = []

	def addActions(self, *actions: Action):
		self.actions += actions

	def addGroups(self, *groups: ActionGroup):
		self.groups += groups

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
			allRops=RaytkContext().ropChildrenOf(comp),
		)

	def openMenu(self, popMenu: 'PopMenuExt'):
		ctx = self._getContext()
		if not ctx:
			return
		items = [
			action.createMenuItem(ctx)
			for action in self.actions
			if action.isValid(ctx)
		]
		items += [
			group.createMenuItem(ctx)
			for group in self.groups
			if group.isValid(ctx)
		]
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

def _isRopOrComp(o: 'OP'):
	return isROP(o) or isRComp(o)

class ROPState:
	rop: Optional['OP']
	info: ROPInfo

	def __init__(self, rop: Optional['OP']):
		self.rop = rop
		self.info = ROPInfo(rop)

	def __bool__(self):
		return bool(self.rop and self.info)

	@property
	def currentDefTable(self) -> Optional['DAT']:
		return self.rop.op('definition') if self.rop and self.info.isROP else None

	def _defTypes(self, col: str) -> List[str]:
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

	def getParam(self, parName: str):
		if self.rop:
			return self.rop.par[parName]

InitFunc = Optional[Callable[['COMP'], None]]

class ActionUtils:
	@staticmethod
	def palette() -> 'Palette': return op.raytk.op('tools/palette')

	@staticmethod
	def createROP(ropType: str, *inits: InitFunc):
		def init(rop: 'COMP'):
			for fn in inits:
				if fn:
					fn(rop)
		ActionUtils.palette().CreateItem(ropType, postSetup=init)

	@staticmethod
	def moveAfter(o: 'OP', after: 'OP'):
		if not after:
			return
		o.nodeCenterY = after.nodeCenterY
		o.nodeX = after.nodeX + after.nodeWidth + 100

	@staticmethod
	def moveAfterMultiple(o: 'OP', after: List['OP']):
		if not after:
			return
		o.nodeCenterY = sum(a.nodeCenterY for a in after) / len(after)
		o.nodeX = max(a.nodeX + a.nodeWidth for a in after) + 100

	@staticmethod
	def createAndAttachFromOutput(
			fromRop: 'OP',
			ropType: str,
			init: InitFunc = None,
			inputIndex: int = 0,
			outputIndex: int = 0,
	):
		def placeAndAttach(rop: 'COMP'):
			ActionUtils.moveAfter(rop, after=fromRop)
			rop.inputConnectors[inputIndex].connect(fromRop.outputConnectors[outputIndex])
		ActionUtils.createROP(ropType, placeAndAttach, init)

	@staticmethod
	def createAndAttachToInput(
			fromRop: 'OP',
			ropType: str,
			init: InitFunc = None,
			inputIndex: int = 0,
			outputIndex: int = 0,
	):
		def placeAndAttach(rop: 'COMP'):
			rop.nodeCenterY = fromRop.nodeCenterY - 100
			rop.nodeX = fromRop.nodeX - rop.nodeWidth - 150
			rop.outputConnectors[outputIndex].connect(fromRop.inputConnectors[inputIndex])
		ActionUtils.createROP(ropType, placeAndAttach, init)

	@staticmethod
	def createAndAttachFromMultiOutputs(
			fromRops: List['OP'],
			ropType: str,
			init: InitFunc = None,
			outputIndex: int = 0,
	):
		fromRops.sort(key=lambda r: r.nodeCenterY, reverse=True)
		def placeAndAttach(combine: 'COMP'):
			ActionUtils.moveAfterMultiple(combine, fromRops)
			for i, fromRop in enumerate(fromRops):
				if i >= len(combine.inputConnectors):
					break
				combine.inputConnectors[i].connect(fromRop.outputConnectors[outputIndex])
		ActionUtils.createROP(ropType, placeAndAttach, init)

	@staticmethod
	def isKnownRopType(pathOrOpType: str):
		return ActionUtils.palette().IsKnownType(pathOrOpType)
