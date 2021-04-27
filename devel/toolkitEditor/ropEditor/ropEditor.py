from typing import Union, Optional

from raytkTools import RaytkTools
from raytkUtil import ROPInfo, navigateTo, RaytkTags

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from components.inspectorCore.inspectorCoreExt import InspectorCore
	from components.opPicker.opPicker import PickerItem
	from ..testEditor.testEditor import TestEditor
	from .specPanel.specPanel import SpecPanel
	# noinspection PyTypeHints
	iop.inspectorCore = InspectorCore(COMP())  # type: Union[COMP, InspectorCore]
	# noinspection PyTypeChecker,PyTypeHints
	iop.testEditor = TestEditor(COMP())  # type: Union[COMP, TestEditor]
	# noinspection PyTypeChecker,PyTypeHints
	iop.specPanel = SpecPanel(COMP())  # type: Union[COMP, SpecPanel]

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
		iop.testEditor.UnloadTest()
		iop.specPanel.Update()

	def onStatusDropMenuChange(self):
		info = self.ROPInfo
		if not info:
			return
		status = self._statusDropMenu.par.Value0.eval()
		RaytkTools().setROPStatus(info.rop, status)

	@property
	def ROP(self) -> 'Optional[COMP]':
		return iop.inspectorCore.TargetComp

	@property
	def ROPInfo(self):
		return ROPInfo(self.ROP)

	@property
	def ROPType(self):
		info = self.ROPInfo
		if info:
			return info.opType

	def showInEditor(self, popup=False):
		rop = self.ROP
		if rop:
			navigateTo(rop, goInto=True, popup=popup)

	def customizeParameters(self):
		rop = self.ROP
		if rop:
			ui.openCOMPEditor(rop)

	def setUpHelp(self):
		info = self.ROPInfo
		if info:
			RaytkTools().setUpHelp(info.rop)

	def reloadHelp(self):
		info = self.ROPInfo
		if info:
			RaytkTools().reloadHelp(info.rop)

	def saveROP(self, incrementVersion: bool):
		info = self.ROPInfo
		if info:
			RaytkTools().saveROP(info.rop, incrementVersion)

	def onEditItem(self, item: 'PickerItem'):
		if not item or not item.isOP:
			return
		self.LoadROP(item.path)

	def onKeyboardShortcut(self, shorcutName: str):
		pass

	def updateCoordTypeParMenu(self):
		RaytkTools().updateCoordTypeParMenu(self.ROPInfo)

	def updateContextTypeParMenu(self):
		RaytkTools().updateContextTypeParMenu(self.ROPInfo)

	def updateReturnTypeParMenu(self):
		RaytkTools().updateReturnTypeParMenu(self.ROPInfo)
