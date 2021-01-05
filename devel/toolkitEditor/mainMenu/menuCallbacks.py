# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .mainMenu import MainMenu

	ext.mainMenu = MainMenu(COMP())

"""
TopMenu callbacks

Callbacks always take a single argument, which is a dictionary
of values relevant to the callback. Print this dictionary to see what is
being passed. The keys explain what each item is.

TopMenu info keys:
	'widget': the TopMenu widget
	'item': the item label in the menu list
	'index': either menu index or -1 for none
	'indexPath': list of parent menu indexes leading to this item
	'define': TopMenu define DAT definition info for this menu item
	'menu': the popMenu component inside topMenu
"""

def getMenuItems(info):
	items = ext.mainMenu.getMenuItems(**info)
	print('getMenuItems produced', items)
	return items


def onItemTrigger(info):
	ext.mainMenu.onMenuTrigger(**info)

# standard menu callbacks

def onSelect(info):
	"""
	User selects a menu option
	"""
	# debug(info)

def onRollover(info):
	"""
	Mouse rolled over an item
	"""

def onOpen(info):
	"""
	Menu opened
	"""

def onClose(info):
	"""
	Menu closed
	"""

def onMouseDown(info):
	"""
	Item pressed
	"""

def onMouseUp(info):
	"""
	Item released
	"""

def onClick(info):
	"""
	Item pressed and released
	"""

def onLostFocus(info):
	"""
	Menu lost focus
	"""