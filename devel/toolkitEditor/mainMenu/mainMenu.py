from dataclasses import dataclass
from typing import Callable, Dict, List, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from ..ropEditor.ropEditor import ROPEditor
	from ..createRopDialog.createRopDialog import CreateRopDialog
	ext.ropEditor = ROPEditor(COMP())

	class _UiStatePar(ParCollection):
		Showroppicker: 'BoolParamT'
		Showscenepicker: 'BoolParamT'
		Showsceneeditor: 'BoolParamT'
		Showropeditor: 'BoolParamT'

	class _UiStateComp(COMP):
		par: _UiStatePar

	iop.uiState = _UiStateComp()
	ipar.uiState = _UiStatePar()
	iop.createRopDialog = CreateRopDialog(COMP())

class MainMenu:
	menus: 'Dict[str, List[_MenuItem]]'

	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.menus = {
			'File': [
					_MenuItem(
						'saveSameVersion',
						'Save Same Version',
						menuName='File',
						action=lambda: ext.ropEditor.saveROP(incrementVersion=False),
					),
					_MenuItem(
						'saveNewVersion',
						'Save New Version',
						menuName='File',
						action=lambda: ext.ropEditor.saveROP(incrementVersion=True),
						dividerAfter=True,
					),
					_MenuItem(
						'createNewRopType',
						'Create New ROP Type',
						menuName='File',
						action=lambda: iop.createRopDialog.Open(),
					),
				],
			'View': [
				_parToggler(
					'showRopPicker',
					'ROP Picker',
					menuName='View',
					checked='ipar.uiState.Showroppicker',
					getPar=lambda: ipar.uiState.Showroppicker,
				),
				_parToggler(
					'showRopEditor',
					'ROP Editor',
					menuName='View',
					checked='ipar.uiState.Showropeditor',
					getPar=lambda: ipar.uiState.Showropeditor,
				),
				_parToggler(
					'showSceneEditor',
					'Scene Editor',
					menuName='View',
					checked='ipar.uiState.Showsceneeditor',
					getPar=lambda: ipar.uiState.Showsceneeditor,
				),
				_parToggler(
					'showScenePicker',
					'Scene Picker',
					menuName='View',
					checked='ipar.uiState.Showscenepicker',
					getPar=lambda: ipar.uiState.Showscenepicker,
				),
			],
		}

	def getMenuItems(self, rowDict: dict, **kwargs):
		print(self.ownerComp, 'getMenuItems', dict(rowDict))
		depth = rowDict.get('itemDepth', '')
		if depth == '':
			depth = 1
		menuName = rowDict.get('menuName', '')
		if not menuName or menuName not in self.menus:
			return []

		items = self.menus[menuName]
		return [
			item.toMenuItemObj()
			for item in items
		]

	def onMenuTrigger(self, define: dict = None, **kwargs):
		print(self.ownerComp, 'onMenuTrigger', kwargs)
		if not define:
			return
		menuName = define.get('menuName', '')
		itemName = define.get('itemName', '')
		if menuName not in self.menus:
			msg = f'ERROR: menu not supported: {menuName!r} (item: {itemName!r})'
			ui.status = msg
			raise Exception(msg)
		menuItems = self.menus[menuName]
		for item in menuItems:
			if item.name == itemName:
				item.action()
				return
		msg = f'ERROR: menu item not supported: {menuName!r} (item: {itemName!r})'
		ui.status = msg
		raise Exception(msg)

def _parToggler(
		name: str,
		label: str,
		getPar: 'Callable[[], Par]',
		checked: str,
		**kwargs):
	def action():
		par = getPar()
		par.val = not par.val

	return _MenuItem(
		name,
		label,
		checked=checked,
		action=action,
		**kwargs,
	)

@dataclass
class _MenuItem:
	name: str
	label: str
	menuName: str
	depth: int = 1
	checked: 'Optional[str]' = None
	itemValue: 'Optional[str]' = None
	dividerAfter: bool = False
	action: 'Callable[[], None]' = None

	def toMenuItemObj(self):
		nameKey = f'item{self.depth}'
		return {
			nameKey: self.label,
			'checked': self.checked,
			'dividerAfter': self.dividerAfter,
			'menuName': self.menuName,
			'itemName': self.name,
			'callback': 'onItemTrigger',
			'disable': '',
			'highlight': '',
			'shortcut': '',
			'name': self.label,
		}

