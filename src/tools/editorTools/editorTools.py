from typing import Optional
from editorToolsCommon import ActionManager
from editorActions import createActionManager

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class EditorTools:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.actions = None # type: Optional[ActionManager]

	def init(self):
		if not self.actions:
			self.actions = createActionManager()

	def Open(self):
		self.init()
		self.actions.openMenu()
