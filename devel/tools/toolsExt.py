import popMenu
from raytkTools import RaytkTools
from raytkUtil import RaytkTags, Tag, navigateTo, recloneComp, RaytkContext, Version
from typing import Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from devel.toolkitEditor.toolkitEditor import ToolkitEditor

class Tools:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	def onInit(self):
		self.updateAllROPToolkitVersions()

	@staticmethod
	def IncrementMajor():
		version = RaytkContext().toolkitVersion()
		setToolkitVersion(Version(version.major + 1, 0))

	@staticmethod
	def IncrementMinor():
		context = RaytkContext()
		version = context.toolkitVersion()
		setToolkitVersion(Version(version.major, version.minor + 1))

	@property
	def toolkitVersion(self):
		return RaytkContext().toolkitVersion()

	@staticmethod
	def ShowLibraryParams():
		RaytkContext().toolkit().openParameters()

	def FillMonitorHeight(self, usePrimary=True):
		height = _getMonitorHeight(usePrimary)
		height -= 270
		self.ownerComp.par.h = height

	@staticmethod
	def NavigateTo(comp: COMP):
		navigateTo(comp)

	def GetCurrentROP(self):
		rops = self.getCurrentROPs(primaryOnly=True)
		return rops[0] if rops else None

	def getCurrentROPs(self, primaryOnly=False):
		return RaytkContext().currentROPs(
			primaryOnly=primaryOnly,
			exclude=lambda c: c is self.ownerComp or c.path.startswith(self.ownerComp.path + '/'))

	def OnOperatorsShortcutRightClick(self, button: COMP):
		def goToItem(name, path):
			return popMenu.Item(
				name,
				callback=lambda: self.NavigateTo(op(path)),
			)
		categories = RaytkContext().allCategories()
		categories.sort(key=lambda c: c.name)
		popMenu.fromButton(button, h='Right', v='Top').Show(
			[
				goToItem(o.name, o.path)
				for o in categories
			]
		)

	def setBuildExcludeStateOnSelected(self, state: bool):
		self.applyTagToSelected(RaytkTags.buildExclude, state)

	def setBuildLockOnSelected(self, state: bool):
		self.applyTagToSelected(RaytkTags.buildLock, state)

	def setFileSyncOnSelected(self, state: bool):
		self.applyTagToSelected(RaytkTags.fileSync, state)

	def setValidationOnSelected(self, state: bool):
		self.applyTagToSelected(RaytkTags.validation, state)

	def recloneSelected(self):
		self.forEachSelected(recloneComp)

	def setShowCustomOnlyOnSelected(self, state: bool):
		def _action(o: COMP):
			o.showCustomOnly = state
		self.forEachSelected(_action)

	def DestroySelectedCustomPars(self):
		def _action(o: 'OP'):
			if hasattr(o, 'destroyCustomPars'):
				o.destroyCustomPars()
		self.forEachSelected(_action)

	def applyTagToSelected(self, tag: 'Tag', state: bool):
		self.forEachSelected(lambda o: tag.apply(o, state))

	@staticmethod
	def forEachSelected(action):
		editor = RaytkContext().activeEditor()
		if not editor:
			return
		for o in editor.owner.selectedChildren:
			action(o)

	def organizeCurrentCategory(self):
		categories = RaytkContext().currentCategories()
		for cat in categories:
			self.organizeCategory(cat)

	@staticmethod
	def organizeCategory(comp: COMP):
		RaytkTools().organizeCategory(comp)

	@staticmethod
	def updateAllROPToolkitVersions():
		RaytkTools().updateAllROPToolkitVersions()

	def openToolkitEditor(self):
		self.toolkitEditor().par.Open.pulse()

	@staticmethod
	def toolkitEditor() -> 'Union[ToolkitEditor, COMP]':
		return op('/toolkitEditor')

	def openPrototypeEditor(self):
		self.openEditorWorkspace('devel/prototypes/')

	def openExampleEditor(self):
		self.openEditorWorkspace('examples/')

	def openTestCaseEditor(self):
		self.openEditorWorkspace('tests/testCases/')

	@staticmethod
	def openEditorWorkspace(workspaceFolder: str):
		editor = op('/editor')
		# noinspection PyUnresolvedReferences
		editor.Workspace.LoadWorkspaceFolder(workspaceFolder)
		editor.par.Openwindow.pulse()

def _getMonitorHeight(usePrimary=True):
	if usePrimary:
		return monitors.primary.height
	for m in monitors:
		if not m.isPrimary:
			return m.height
	for m in monitors:
		return m.height

def setToolkitVersion(version: Version):
	context = RaytkContext()
	toolkit = context.toolkit()
	if toolkit.par['Raytkversion'] is None:
		page = toolkit.appendCustomPage('RayTK')
		page.appendStr('Raytkversion', label='RayTK Version')
	par = toolkit.par.Raytkversion
	par.val = str(version)
	par.readOnly = True
