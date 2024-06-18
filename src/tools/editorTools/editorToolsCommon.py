# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _stubs.PopMenuExt import PopMenuExt

from raytkActions import ActionContext, MenuItem, ItemBase

class ActionManager:
	items: list[ItemBase]

	def __init__(self, *items: ItemBase):
		self.items = list(items)

	@staticmethod
	def _getEditor():
		pane = ui.panes.current
		if isinstance(pane, NetworkEditor):
			return pane
		for pane in ui.panes:
			if isinstance(pane, NetworkEditor):
				return pane

	def _getContext(self) -> ActionContext | None:
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
			items: list[MenuItem],
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
