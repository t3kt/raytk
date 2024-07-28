from editorToolsCommon import ActionManager
import editorActions

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class EditorTools:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	@staticmethod
	def _createActionManager():
		actions = []
		for d in root.findChildren(tags=['raytkEditorActionModule']):
			if not d.isDAT:
				continue
			try:
				actions += d.module.getActions()
			except Exception as e:
				debug(e)
		return ActionManager(*actions)

	def Open(self, _=None):
		actions = self._createActionManager()
		actions.openMenu(op.TDResources.op('popMenu'))
