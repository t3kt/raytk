from typing import Union, Optional, List
from raytkUtil import ROPInfo, navigateTo, RaytkTags

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from components.inspectorCore.inspectorCoreExt import InspectorCore
	# noinspection PyTypeHints
	iop.inspectorCore = InspectorCore(COMP())  # type: Union[COMP, InspectorCore]

class ROPEditor:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@property
	def _statusDropMenu(self) -> 'widgetCOMP':
		return self.ownerComp.op('status_dropmenu')

	def LoadROP(self, o: 'Union[OP, DAT, COMP, str]'):
		iop.inspectorCore.Inspect(o)
		info = self.ROPInfo
		self._statusDropMenu.par.Value0 = info.statusLabel or 'default'

	def onStatusDropMenuChange(self):
		info = self.ROPInfo
		if not info:
			return
		status = self._statusDropMenu.par.Value0.eval()
		# note: since applying with status false resets the color, the false ones have to be done before the true one
		if status == 'alpha':
			RaytkTags.beta.apply(info.rop, False)
			RaytkTags.deprecated.apply(info.rop, False)
			RaytkTags.alpha.apply(info.rop, True)
		elif status == 'beta':
			RaytkTags.alpha.apply(info.rop, False)
			RaytkTags.deprecated.apply(info.rop, False)
			RaytkTags.beta.apply(info.rop, True)
		elif status == 'deprecated':
			RaytkTags.alpha.apply(info.rop, False)
			RaytkTags.beta.apply(info.rop, False)
			RaytkTags.deprecated.apply(info.rop, True)
		else:
			RaytkTags.alpha.apply(info.rop, False)
			RaytkTags.beta.apply(info.rop, False)
			RaytkTags.deprecated.apply(info.rop, False)

	@property
	def ROP(self) -> 'Optional[COMP]':
		return iop.inspectorCore.TargetComp

	@property
	def ROPInfo(self):
		return ROPInfo(self.ROP)

	def ShowInEditor(self, popup=False):
		rop = self.ROP
		if rop:
			navigateTo(rop, goInto=True, popup=popup)

	def CustomizeParameters(self):
		rop = self.ROP
		if rop:
			ui.openCOMPEditor(rop)
