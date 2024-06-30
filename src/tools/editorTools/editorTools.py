from editorToolsCommon import ActionManager
import editorActions

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class EditorTools:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	def _createActionManager(self):
		table = self.ownerComp.op('editorActionModules')
		actions = []
		for path in table.col('path')[1:]:
			d = op(path)
			if not d or not d.isDAT:
				continue
			try:
				actions += d.module.getActions()
			except Exception as e:
				debug(e)
		return ActionManager(*actions)

	def Open(self, _=None):
		actions = self._createActionManager()
		actions.openMenu(op.TDResources.op('popMenu'))
