from raytkTools import RaytkTools
from raytkUtil import ROPInfo, navigateTo, RaytkModuleContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from components.inspectorCore.inspectorCoreExt import InspectorCore
	from ..testEditor.testEditor import TestEditor
	from .specPanel.specPanel import SpecPanel
	# noinspection PyTypeHints
	iop.inspectorCore = InspectorCore(COMP())  # type: COMP | InspectorCore
	# noinspection PyTypeChecker,PyTypeHints
	iop.testEditor = TestEditor(COMP())  # type: COMP | TestEditor
	# noinspection PyTypeChecker,PyTypeHints
	iop.specPanel = SpecPanel(COMP())  # type: COMP | SpecPanel

class ROPEditor:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp
		picker = self.ownerComp.op('opPicker2')
		picker.ExpandAll()
		# why is this needed?
		def _fix():
			picker.allowCooking = False
			picker.allowCooking = True
		run(_fix, delayFrames=5)

	def _tools(self):
		info = self.ROPInfo
		if not info:
			return None
		modRoot = info.moduleRoot()
		return RaytkTools(RaytkModuleContext(modRoot))

	@property
	def _statusDropMenu(self) -> widgetCOMP:
		return self.ownerComp.op('status_dropmenu')

	def LoadROP(self, o: OP | DAT | COMP | str):
		print('Loading ROP:', o)
		iop.inspectorCore.Inspect(o)
		info = self.ROPInfo
		self._statusDropMenu.par.Value0 = info.statusLabel or 'default'
		iop.testEditor.Unload()
		iop.specPanel.Update()

	def onStatusDropMenuChange(self):
		info = self.ROPInfo
		if not info:
			return
		status = self._statusDropMenu.par.Value0.eval()
		self._tools().setROPStatus(info.rop, status)

	@property
	def ROP(self) -> COMP | None:
		return iop.inspectorCore.TargetComp

	@property
	def ROPInfo(self):
		return ROPInfo(self.ROP)

	@property
	def ROPType(self):
		info = self.ROPInfo
		if info:
			return info.opType

	@property
	def ModuleName(self):
		info = self.ROPInfo
		if info:
			return info.moduleName()

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
			self._tools().setUpHelp(info.rop)

	def reloadHelp(self):
		info = self.ROPInfo
		if info:
			self._tools().reloadHelp(info.rop)

	def saveROP(self, incrementVersion: bool):
		info = self.ROPInfo
		if info:
			self._tools().saveROP(info.rop, incrementVersion)

	def onEditItem(self, path: str):
		if not path:
			return
		self.LoadROP(path)

	def onKeyboardShortcut(self, shorcutName: str):
		pass

	def updateCoordTypeParMenu(self):
		self._tools().updateCoordTypeParMenu(self.ROPInfo)

	def updateContextTypeParMenu(self):
		self._tools().updateContextTypeParMenu(self.ROPInfo)

	def updateReturnTypeParMenu(self):
		self._tools().updateReturnTypeParMenu(self.ROPInfo)

	def buildRopInfoTable(self, dat: scriptDAT):
		dat.clear()
		info = self.ROPInfo
		if info:
			dat.appendRow(['opType', info.opType])
			dat.appendRow(['module', info.moduleName()])
		else:
			dat.appendRow(['opType', ''])
			dat.appendRow(['module', ''])
