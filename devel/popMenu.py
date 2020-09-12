from typing import List, Union

# noinspection PyUnreachableCode
if False:
	from _stubs import *
	from _stubs.PopMenuExt import PopMenuExt

class Item:
	def __init__(
			self,
			text,
			callback=None,
			disabled=False,
			dividerafter=False,
			highlighted=False,
			checked=None,
			hassubmenu=False):
		self.text = text
		self.disabled = disabled
		self.dividerafter = dividerafter
		self.highlighted = highlighted
		self.checked = checked
		self.hassubmenu = hassubmenu
		self.callback = callback

def ParToggleItem(
		par,
		text=None,
		callback=None,
		**kwargs):
	def _callback():
		par.val = not par
		if callback:
			callback()
	return Item(
		text or par.label,
		checked=par.eval(),
		callback=_callback,
		**kwargs)

def ParEnumItems(par):
	def _valitem(value, label):
		return Item(
			label,
			checked=par == value,
			callback=lambda: setattr(par, 'val', value))
	return [
		_valitem(v, l)
		for v, l in zip(par.menuNames, par.menuLabels)
	]

def ViewOpItem(
		o: 'OP',
		text,
		unique=True,
		borders=True,
		**kwargs):
	return Item(
		text,
		callback=lambda: o.openViewer(unique=unique, borders=borders),
		**kwargs)

class Divider:
	pass

def _PreprocessItems(rawitems: List[Union[Item, Divider]]):
	if not rawitems:
		return []
	processeditems = []
	previtem = None
	for item in rawitems:
		if not item:
			continue
		if isinstance(item, Divider):
			if previtem:
				previtem.dividerafter = True
			previtem = None
		else:
			previtem = item
			processeditems.append(item)
	return processeditems


class _Opener:
	def __init__(self, applyPosition):
		self.applyPosition = applyPosition

	def Show(
			self,
			items: List[Union[Item, Divider]],
			callback=None,
			callbackDetails=None,
			autoClose=None,
			rolloverCallback=None,
			allowStickySubMenus=None):
		items = _PreprocessItems(items)
		if not items:
			return

		popmenu = _getPopMenu()

		if not callback:
			def _callback(info):
				i = info['index']
				if i < 0 or i >= len(items):
					return
				item = items[i]
				if not item or item.disabled or not item.callback:
					return
				item.callback()
			callback = _callback

		if self.applyPosition:
			self.applyPosition(popmenu)

		popmenu.Open(
			items=[item.text for item in items],
			highlightedItems=[
				item.text for item in items if item.highlighted],
			disabledItems=[
				item.text for item in items if item.disabled],
			dividersAfterItems=[
				item.text for item in items if item.dividerafter],
			checkedItems={
				item.text: item.checked
				for item in items
				if item.checked is not None
			},
			subMenuItems=[
				item.text for item in items if item.hassubmenu],
			callback=callback,
			callbackDetails=callbackDetails,
			autoClose=autoClose,
			rolloverCallback=rolloverCallback,
			allowStickySubMenus=allowStickySubMenus)

def _getPopMenu():
	popmenu = op.TDResources.op('popMenu')  # type: PopMenuExt
	return popmenu

def fromMouse(h='Left', v='Top', offset=(0, 0)):
	def _applyPosition(
			popmenu  # type: PopMenuExt
	):
		popmenu.SetPlacement(hAlign=h, vAlign=v, alignOffset=offset, matchWidth=False)
	return _Opener(_applyPosition)

def fromButton(buttonComp, h='Left', v='Bottom', matchWidth=False, offset=(0, 0)):
	if not buttonComp:
		return fromMouse(h=h, v=v, offset=offset)

	def _applyPosition(
			popmenu  # type: PopMenuExt
	):
		popmenu.SetPlacement(
			buttonComp=buttonComp,
			hAttach=h, vAttach=v, matchWidth=matchWidth, alignOffset=offset)
	return _Opener(_applyPosition)
