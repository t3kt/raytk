# This file and all related intellectual property rights are
# owned by Derivative Inc. ("Derivative").  The use and modification
# of this file is governed by, and only permitted under, the terms
# of the Derivative [End-User License Agreement]
# [https://www.derivative.ca/Agreements/UsageAgreementTouchDesigner.asp]
# (the "License Agreement").  Among other terms, this file can only
# be used, and/or modified for use, with Derivative's TouchDesigner
# software, and only by employees of the organization that has licensed
# Derivative's TouchDesigner software by [accepting] the License Agreement.
# Any redistribution or sharing of this file, with or without modification,
# to or with any other person is strictly prohibited [(except as expressly
# permitted by the License Agreement)].
#
# Version: 099.2017.30440.28Sep
#
# _END_HEADER_

# SimplePopMenuExt

TDFunctions = op.TDModules.mod.TDFunctions


# Note that selection style is currently locked to "Click" because of Windows
# issues. Setting to "Press" can cause problems when clicking on a menu that is
# floating above a non-TouchDesigner area.

class PopMenuExt:
	"""
	An easy to use pop up menu. See the Open method for instructions or set up
	using parameters.
	"""

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.configComp = ownerComp.par.Configcomp.eval()
		self.itemsTable = ownerComp.op('itemsIn')
		self.layoutTable = ownerComp.op('itemsLayout')
		self.buttonFormat = self.configComp.op('buttonPress')
		self.Window = ownerComp.par.Windowcomp.eval()
		self.Lister = ownerComp.op('lister')
		self.mouseMonitorChan = \
			op.TDDevices.op('mouse/deviceOut').chan('monitor')
		self.mouseXChan = op.TDDevices.op('mouse/deviceOut').chan('abs_mouse_x')
		self.mouseYChan = op.TDDevices.op('mouse/deviceOut').chan('abs_mouse_y')
		self.LastCell = self.SubMenuCell = None
		self.CallbackDetails = None

		# offset for size
		TDFunctions.createProperty(self, 'OffsetX', 0, dependable=True)
		TDFunctions.createProperty(self, 'OffsetY', 0, dependable=True)
		# offset for keeping on screen
		TDFunctions.createProperty(self, 'ScreenAdjustX', 0, dependable=True)
		TDFunctions.createProperty(self, 'ScreenAdjustY', 0, dependable=True)
		# list of submenu type cells
		TDFunctions.createProperty(self, 'SubMenuItems', [], dependable=True)
		# store parent menu if this is a submenu
		TDFunctions.createProperty(self, 'ParentMenu', None, dependable=True)
		# selection value for output
		TDFunctions.createProperty(self, 'Selected', -1, dependable=True)
		# optimal menu height
		TDFunctions.createProperty(self, 'OptimalHeight', 23, dependable=True,
		                           readOnly=True)
		# optimal menu width
		TDFunctions.createProperty(self, 'OptimalWidth', 23, dependable=True,
		                           readOnly=True)
		# item column width
		TDFunctions.createProperty(self, 'ColumnWidth', 23, dependable=True,
		                           readOnly=True)
		# item column width
		TDFunctions.createProperty(self, 'ShortcutWidth', 23, dependable=True,
		                           readOnly=True)
		# if True, show scrollbar
		TDFunctions.createProperty(self, 'ShowScrollbar', False,
		                           dependable=True, readOnly=True)
		# checked items list or dict
		TDFunctions.createProperty(self, 'CheckedItems', [], dependable=True,
		                           readOnly=True)

		self._openDelay = None  # run ob for delay before opening

		self.setAttachPars()

		self.Window.par.winclose.pulse()
		run('op(' + str(ownerComp.id) + ').ext.PopMenuExt.refresh() if '
		                                'op(' + str(ownerComp.id) + ') else None',
		    delayFrames=1, delayRef=op.TDResources)
		run('op(' + str(self.Lister.id) + ').Refresh() if '
		                                  'op(' + str(self.Lister.id) + ') else None',
		    delayFrames=1, delayRef=op.TDResources)

	# IMPORTANT! Any changes to arguments need to be reflected in OpenSubMenu
	def Open(self, items=None, callback=None, callbackDetails=None,
	         highlightedItems=None, disabledItems=None, dividersAfterItems=None,
	         checkedItems=None, subMenuItems=None, autoClose=None,
	         shortcuts=None,
	         rolloverCallback=None, allowStickySubMenus=None):
		"""
		Open the menu.

		items: a list of item strings for the menu. Default is to use the
			items set up in the comp. These options will replace the ones in the
			component's Items parameter.
			If this is None, use parameters for defaults.
		callback: a method that will be called when a selection is made. If not
			provided, Callback DAT will be searched.
		callbackDetails: will be passed to callbacks in addition to item chosen.
		highlightedItems: list of strings for items to highlight
		disabledItems: list of strings for greyed out, unselectable items.
		dividersAfterItems: list of strings for items with dividers below them.
		checkedItems: list of strings for items with check marks next to them.
			Will show the 'check' graphic in configComp.
			Also accepts a dict of strings with 'item': bool. Will show the
				'checkOn' or 'checkOff' graphic depending on bool.
			Also accepts a string which will be used as an EXPRESSION to
				continually evaluate.
		subMenuItems: list of strings for items with indicator and will select
			on rollOver instead of click. Always use OpenSubMenu in handler
			function. Set SubMenu parameter to another popMenu comp. Default is
			[]... no parameter available for submenus.
		autoClose: will close after selection or click away.
		rolloverCallback: will be called when a cell is rolledOver. A callback
			with cell -1 will be called when mouse leaves menu or menu closes.
			Uses same callbackDetails as selection callback. If not provided,
			Callback DAT will be searched
		allowStickySubMenus: if True, clicking on subMenu items will lock their
			submenus open
		"""
		if items is not None:
			if not isinstance(items, list):
				raise TypeError(
					"PopMenu items must be list of strings",
					self.ownerComp)
			self.ownerComp.par.Items.val = str(items)
			# change parameter defaults
			if disabledItems is None:
				disabledItems = []
			if dividersAfterItems is None:
				dividersAfterItems = []
			if checkedItems is None:
				checkedItems = []
			if shortcuts is None:
				shortcuts = {}
			if subMenuItems is None:
				subMenuItems = []
			if highlightedItems is None:
				highlightedItems = []
			if autoClose is None:
				autoClose = True
			if allowStickySubMenus is None:
				allowStickySubMenus = True
		if disabledItems is not None:
			if not isinstance(disabledItems, list):
				raise TypeError(
					"PopMenu disabled items must be list of strings",
					self.ownerComp)
			self.ownerComp.par.Disableditems.val = str(disabledItems)
		if highlightedItems is not None:
			if not isinstance(highlightedItems, list):
				raise TypeError(
					"PopMenu highlighted items must be list of strings",
					self.ownerComp)
			self.ownerComp.par.Highlighteditems.val = str(highlightedItems)
		if dividersAfterItems is not None:
			if not isinstance(dividersAfterItems, list):
				raise TypeError(
					"PopMenu dividersAfterItems must be list of strings",
					self.ownerComp)
			self.ownerComp.par.Dividersafteritems.val = str(dividersAfterItems)
		if checkedItems is not None:
			if not isinstance(checkedItems, (list, dict, str)):
				raise TypeError(
					"PopMenu checkedItems must be list of strings, dict"
					" of 'item':bool or a str expression that evaluates to "
					"one of those.", self.ownerComp)
			if isinstance(checkedItems, str):
				self.ownerComp.par.Checkeditems.expr = checkedItems
			else:
				self.ownerComp.par.Checkeditems.val = str(checkedItems)
		if shortcuts is not None:
			if not isinstance(shortcuts, dict):
				raise TypeError(
					"PopMenu shortcuts must be a dict of item: shortcut.",
					self.ownerComp)
			self.ownerComp.par.Shortcuts.val = str(shortcuts)
		if subMenuItems is not None:
			self.SubMenuItems = subMenuItems.copy()
		else:
			self.SubMenuItems = []
		if callback:
			self.SetCallback(callback, "onSelect")
		else:
			self.SetCallback(None, "onSelect")
		if rolloverCallback:
			self.SetCallback(rolloverCallback, "onRollover")
		else:
			self.SetCallback(None, "onRollover")
		self.SubMenuCell = None
		if autoClose is not None:
			self.ownerComp.par.Autoclose = autoClose
		if allowStickySubMenus is not None:
			self.ownerComp.par.Allowstickysubmenus = allowStickySubMenus
		self.CallbackDetails = callbackDetails
		self.updateCheckedItems(self.ownerComp.par.Checkeditems.eval())
		self.Lister.par.Refresh.pulse()
		self.Selected = -1
		self.winOpen()

	# self._openDelay = run(
	# 		'op("' + self.ownerComp.path + '").ext.PopMenuExt.winOpen()',
	# 		delayFrames=1, delayRef=op.TDResources)

	def SetCallback(self, callback, callbackName="onSelect"):
		self.ownerComp.ext.CallbacksExt.SetAssignedCallback(callbackName,
		                                                    callback)

	def winOpen(self):
		self.Close()
		self.setDimensions()
		self.RecalculateOffsets()
		ext.CallbacksExt.DoCallback('onOpen', self.infoDict())
		self.Lister.Refresh()
		self.Window.par.winopen.pulse()
		if not self.ParentMenu:
			self.ownerComp.setFocus()

	def OpenSubMenu(self, items=None, callback=None, callbackDetails=None,
	                highlightedItems=None, disabledItems=None, dividersAfterItems=None,
	                checkedItems=None,
	                subMenuItems=None, autoClose=True, shortcuts=None,
	                rolloverCallback=None, allowStickySubMenus=None):
		"""
		Open this menu's sub-menu (uses op in subMenu parameter by default).
		Takes all the same arguments as Open()
		"""
		self._subMenuArgs = (items, callback, callbackDetails, highlightedItems,
		                     disabledItems, dividersAfterItems, checkedItems,
		                     subMenuItems, autoClose, shortcuts,
		                     rolloverCallback, allowStickySubMenus)
		self.SubMenu.Close()
		self.ownerComp.setFocus()
		self.doOpenSubMenu()

	def doOpenSubMenu(self):
		"""
		Do the actual opening called for in OpenSubMenu, which can be delayed to
		prevent frame-rate drop when dragging mouse over submenuitems quickly.
		"""
		self.SubMenu.ParentMenu = self.ownerComp
		self.SubMenu.Open(*self._subMenuArgs)
		self.SubMenuCell = self.LastCell
		# HACK focus is lost so we have to restore rollover
		self.Lister.ext.ListerExt.onRollover(
			self.LastCell, 0, (0, 0), -1, -1, (0, 0))

	def SetPlacement(self, hAlign='Left', vAlign='Top', alignOffset=(0, 0),
	                 buttonComp=None, hAttach='Left', vAttach='Bottom',
	                 matchWidth=False):
		"""
		Set up placement parameters for the popMenu.
		hAlign: set Horizontal Align
		vAlign: set Vertical Align
		alignOffset: set Align Offset
		buttonComp: set Button COMP
		hAttach: set Horizontal Attach
		vAttach: set Vertical Attach
		matchWidth: match width of menu to width of button Comp
		"""
		self.ownerComp.par.Horizontalalign = hAlign
		self.ownerComp.par.Verticalalign = vAlign
		self.ownerComp.par.Alignoffset1 = alignOffset[0]
		self.ownerComp.par.Alignoffset2 = alignOffset[1]
		self.ownerComp.par.Buttoncomp = buttonComp
		self.ownerComp.par.Horizontalattach = hAttach
		self.ownerComp.par.Verticalattach = vAttach
		if matchWidth:
			self.ownerComp.par.w = buttonComp.par.w
		else:
			self.ownerComp.par.w.expr = 'me.OptimalWidth'

	@property
	def SubMenu(self):
		"""
		Delayed because window location is not ready until next frame
		"""
		return self.ownerComp.par.Submenu.eval()

	def CloseAll(self):
		"""
		Utility for submenus... close all open menus
		"""
		topMenu = self.ownerComp
		while topMenu.ParentMenu:
			topMenu = topMenu.ParentMenu
		topMenu.Close()

	def Close(self):
		"""
		Close the menu
		"""
		try:
			self._openDelay.kill()
		except:
			pass
		self._openDelay = None

		if self.IsOpen:
			ext.CallbacksExt.DoCallback('onRollover', self.infoDict(-1))
			ext.CallbacksExt.DoCallback('onClose', self.infoDict())
			self.ownerComp.par.Checkeditems.mode = ParMode.CONSTANT
			self.Window.par.winclose.pulse()
			if self.ParentMenu:
				if not self.ParentMenu.panel.focusselect:
					self.ParentMenu.setFocus()
				self.ParentMenu = None
		self.callback = None

	def OnRollover(self, cell):
		"""
		Called by panel exec when mouse is over a new cell.
		-1: mouse is not over a cell
		"""
		if not self.ownerComp.panel.focusselect:
			self.ownerComp.setFocus()
		self.LastCell = cell
		# sanity check
		if self.ParentMenu and not self.ParentMenu.IsOpen:
			self.Close()
		try:
			ext.CallbacksExt.DoCallback('onRollover', self.infoDict(cell))
		except:
			self.Close()
			raise
		# deal with submenu closing and opening
		if self.SubMenu:
			if self.infoDict(cell)['item'] in self.SubMenuItems and \
					self.infoDict(cell)['item'] not in self.DisabledItems:
				if cell == self.SubMenuCell:
					# going back to current submenu cell. Close sub sub menu
					if self.SubMenu.SubMenu and self.SubMenu.SubMenu.IsOpen:
						self.SubMenu.SubMenu.Close()
						self.SubMenu.SubMenuCell = None
				elif not self.SubMenu.IsOpen or self.SubMenu.par.Autoclose \
						or not self.ownerComp.par.Allowstickysubmenus.eval():
					# new submenu cell
					self.OnSelect(cell, doautoClose=False)
			elif self.SubMenu and cell != -1:
				if self.SubMenu.IsOpen and (self.SubMenu.par.Autoclose
				                            or not self.ownerComp.par.Allowstickysubmenus.eval()):
					self.SubMenu.Close()
					self.SubMenuCell = None
					self.ownerComp.setFocus()

	def OnSelect(self, cell, doautoClose=True):
		"""
		Item selected according to Select Style parameter.
		"""
		infoDict = self.infoDict(cell)
		# disabled items
		if cell is not None and infoDict['item'] in self.DisabledItems:
			return
		# submenus
		if self.SubMenu and self.SubMenu.IsOpen:
			if self.SubMenuCell == cell:
				if self.ownerComp.par.Allowstickysubmenus.eval():
					self.SubMenu.par.Autoclose = \
						not self.SubMenu.par.Autoclose.eval()
				return
			else:
				if infoDict['item'] in self.SubMenuItems and \
						not self.SubMenu.par.Autoclose.eval() and \
						self.ownerComp.par.Allowstickysubmenus.eval():
					# 	run("op('" + self.SubMenu.path + "').par.Autoclose=False",
					# 		delayFrames=1, delayRef=op.TDResources)
					# else:
					self.SubMenu.par.Autoclose = False
				self.SubMenu.Close()
				self.Lister.Refresh()
		# ordinary selects...
		try:
			ext.CallbacksExt.DoCallback('onSelect', infoDict)
		except:
			self.Close()
			import traceback;
			print(traceback.format_exc())
		self.Selected = cell
		if self.ownerComp.par.Autoclose.eval() and doautoClose and \
				cell != self.SubMenuCell:
			parentMenu = self.ParentMenu
			self.autoClose()
			if parentMenu:
				# close all parents until one doesn't have autoClose
				while parentMenu:
					if parentMenu.par.Autoclose.eval():
						parentMenu.SubMenuCell = None
						pm = parentMenu.ParentMenu  # close destroys value
						parentMenu.Close()
						parentMenu = pm
					else:
						parentMenu = None

	def OnMouseUp(self, cell):
		"""
		Called by panel exec when mouse is released. No cell is provided.
		"""
		ext.CallbacksExt.DoCallback('onMouseUp', self.infoDict(cell))

	def OnClick(self, cell):
		# button style click
		ext.CallbacksExt.DoCallback('onClick', self.infoDict(cell))
		# if self.ownerComp.par.Selectionstyle.eval() == 'Click':
		self.OnSelect(cell)

	def OnMouseDown(self, cell):
		"""
		Called by panel exec when mouse is pressed.
		"""
		if cell == -1:
			if self.ownerComp.par.Autoclose:
				self.autoClose()
			else:
				return
		ext.CallbacksExt.DoCallback('onMouseDown', self.infoDict(cell))

	# if self.ownerComp.par.Selectionstyle.eval() == 'Press':
	# 	self.OnSelect(cell)

	def infoDict(self, cell=None):
		"""
		Return info dict for a given cell. Used for callbacks.
		"""
		if cell is not None:
			return {'index': cell,
			        'item': self.GetLabel(cell),
			        'row': self.GetItemRow(cell),
			        'details': self.CallbackDetails,
			        'menu': self.ownerComp}
		else:
			return {'details': self.CallbackDetails,
			        'menu': self.ownerComp}

	def GetLabel(self, cell):
		"""
		Returns the label of a given cell id
		"""
		try:
			return self.itemsTable[cell, 0].val
		except:
			# no corresponding data. Means empty cell or -1
			return None

	def GetItemRow(self, cell):
		"""
		Returns the table row of a given cell id
		"""
		try:
			return self.ownerComp.op('rowTable').row(cell)
		except:
			# no corresponding data. Means empty cell or -1
			None

	@property
	def IsOpen(self):
		return self.Window.isOpen

	@property
	def Items(self):
		try:
			return [row[0].val for row in self.itemsTable.rows()]
		except:
			return []

	@property
	def DisabledItems(self):
		parVal = self.ownerComp.par.Disableditems.eval()
		if parVal.strip():
			return eval(parVal.strip())
		else:
			return []

	@property
	def HighlightedItems(self):
		parVal = self.ownerComp.par.Highlighteditems.eval()
		if parVal.strip():
			return eval(parVal.strip())
		else:
			return []

	@property
	def DividersAfterItems(self):
		if self.NumCols > 1:
			return []
		parVal = self.ownerComp.par.Dividersafteritems.eval()
		if parVal.strip():
			return eval(parVal.strip())
		else:
			return []

	@property
	def CheckedItems(self):
		return self._CheckedItems.val

	def updateCheckedItems(self, val=None):
		if val is None:
			val = self.ownerComp.par.Checkeditems.eval()
		if self.NumCols > 1:
			self._CheckedItems.val = []
		if val.strip():
			try:
				self._CheckedItems.val = eval(val.strip())
			except:
				self._CheckedItems.val = []
		else:
			self._CheckedItems.val = []

	@property
	def Shortcuts(self):
		if self.NumCols > 1:
			return {}
		parVal = self.ownerComp.par.Shortcuts.eval()
		if parVal.strip():
			return eval(parVal.strip())
		else:
			return {}

	@property
	def NumCols(self):
		return self.ownerComp.par.Columns.eval()

	@property
	def ConfigComp(self):
		return self.configComp

	def setDimensions(self):
		self.CalculateOptimalDimensions()
		self.Lister.par.w = self.Window.par.winw = self.ownerComp.par.w.eval()
		self.Lister.par.h = self.Window.par.winh = self.ownerComp.par.h.eval()
		if not self.Window.isOpen:
			self.RecalculateOffsets()

	def CalculateOptimalDimensions(self):
		# if self.Window.isOpen:
		# 	self.Window.par.winclose.pulse()
		# items
		iwidth = 10
		for i in self.Items:
			self.buttonFormat.par.text = i
			if self.buttonFormat.textWidth > iwidth:
				iwidth = self.buttonFormat.textWidth
		self._ColumnWidth.val = iwidth + \
		                        self.buttonFormat.par.position1.eval() * 3
		width = self.NumCols * self.ColumnWidth

		# shortcuts
		swidth = 10
		for i in self.Shortcuts.values():
			self.buttonFormat.par.text = i
			if self.buttonFormat.textWidth > swidth:
				swidth = self.buttonFormat.textWidth
		self._ShortcutWidth.val = swidth + \
		                          self.buttonFormat.par.position1.eval() * 10
		if self.NumCols == 1 and self.Shortcuts:
			width += self.ShortcutWidth

		# symbols
		if self.NumCols == 1 and (self.CheckedItems or self.SubMenuItems or \
		                          self.ownerComp.par.Checkeditems.mode == ParMode.EXPRESSION):
			width += int(self.configComp.op('colDefine')['width', 'Symbol'])

		self._OptimalWidth.val = max(16, width)
		rowHeight = self.configComp.op('master').par.resolutionh
		self._OptimalHeight.val = rowHeight * self.layoutTable.numRows + \
		                          len([i for i in self.DividersAfterItems if i in self.Items])

		if self.ownerComp.par.Maxheight.eval() and \
				self._OptimalHeight.val > self.ownerComp.par.Maxheight.eval():
			self._OptimalWidth.val += 13  # lister scrollbar size
			self._OptimalHeight.val = self.ownerComp.par.Maxheight.eval()
			self._ShowScrollbar.val = True
		else:
			self._ShowScrollbar.val = False

	def CellLocationY(self, cell):
		if cell < 0 or cell > len(self.Items):
			return 0  # just fake it
		baseLocation = cell * self.configComp.op('master').par.resolutionh
		numDividers = len([c for c in self.Items[:cell]
		                   if c in self.DividersAfterItems])
		return baseLocation + numDividers

	def LostFocus(self):
		if self.ownerComp.par.Autoclose:
			if self.SubMenu and self.SubMenu.IsOpen:
				# recurse to bottom subMenu
				subMenu = self.SubMenu
				while subMenu.SubMenu and subMenu.SubMenu.IsOpen:
					# if subMenu.panel.inside:
					# 	doClose = False
					subMenu = subMenu.SubMenu
				if not subMenu.panel.inside:
					self.Close()
			else:
				ext.CallbacksExt.DoCallback('onLostFocus')
				self.autoClose()

	def autoClose(self):
		if self.SubMenu and self.SubMenu.IsOpen:
			return
		self.Close()

	def RecalculateOffsets(self):
		"""
		Recalculate the window offsets. This is called when parent window moves
		or alignment changes. This is a bit slow, but shouldn't matter when
		moving windows is involved.
		"""
		halfWidth = self.Window.par.winw * 0.5
		halfHeight = self.Window.par.winh * 0.5
		if not self.Window.isOpen:
			mouseX = self.mouseXChan.eval()
			mouseY = self.mouseYChan.eval()
		else:
			mouseX = self.Window.x - self.Window.par.winoffsetx.eval()
			mouseY = self.Window.y - self.Window.par.winoffsety.eval()

		monitor = monitors[int(self.mouseMonitorChan.eval())]
		self.ScreenAdjustX = self.OffsetX = 0
		self.ScreenAdjustY = self.OffsetX = 0
		buttonComp = self.ownerComp.par.Buttoncomp.eval() if \
			self.ownerComp.par.Buttoncomp.eval() and \
			self.ownerComp.par.Buttoncomp.eval().panel.inside else None
		if self.ParentMenu:
			# submenu placement
			self.OffsetX = \
				self.ParentMenu.Window.x \
				+ self.ParentMenu.Window.par.winw
			self.OffsetY = \
				self.ParentMenu.Window.y \
				+ self.ParentMenu.Window.par.winh \
				- self.ParentMenu.CellLocationY(self.ParentMenu.LastCell) \
				- 2 * halfHeight

		else:
			# mouse relative
			if self.ownerComp.par.Horizontalalign == 'Center':
				self.OffsetX = 0
			elif self.ownerComp.par.Horizontalalign == 'Left':
				self.OffsetX = halfWidth
			elif self.ownerComp.par.Horizontalalign == 'Right':
				self.OffsetX = -halfWidth
			if self.ownerComp.par.Verticalalign == 'Center':
				self.OffsetY = 0
			elif self.ownerComp.par.Verticalalign == 'Top':
				self.OffsetY = -halfHeight
			elif self.ownerComp.par.Verticalalign == 'Bottom':
				self.OffsetY = halfHeight
			if buttonComp:
				# button relative adjustments
				# store values in case we need to screen-correct
				toButton = (-int(buttonComp.panel.insideu * buttonComp.width),
				            -int(buttonComp.panel.insidev * buttonComp.height))
				# first set offsets to button's 0,0
				self.OffsetX += toButton[0]
				self.OffsetY += toButton[1]
				if self.ownerComp.par.Horizontalattach == 'Center':
					self.OffsetX += buttonComp.width * 0.5
				elif self.ownerComp.par.Horizontalattach == 'Right':
					self.OffsetX += buttonComp.width
				if self.ownerComp.par.Verticalattach == 'Center':
					self.OffsetY += buttonComp.height * 0.5
				elif self.ownerComp.par.Verticalattach == 'Top':
					self.OffsetY += buttonComp.height

		# force menu onto screen
		if self.ParentMenu:
			winLeft = self.Window.par.winoffsetx.eval()
			winRight = winLeft + 2 * halfWidth
			winBottom = self.Window.par.winoffsety.eval()
			winTop = winBottom + 2 * halfHeight
		else:
			winLeft = mouseX + self.Window.par.winoffsetx.eval() - halfWidth
			winRight = winLeft + 2 * halfWidth
			winBottom = mouseY + self.Window.par.winoffsety.eval() - halfHeight
			winTop = winBottom + 2 * halfHeight

	# if winLeft < monitor.scaledLeft:
	# 	if buttonComp:
	# 		self.OffsetX = toButton[0] + halfWidth + buttonComp.width
	# 	# else:
	# 	# 	self.ScreenAdjustX = monitor.left - winLeft
	# if winRight > monitor.scaledRight:
	# 	if self.ParentMenu:
	# 		# move to other side of menu
	# 		self.OffsetX -= 2 * halfWidth + self.ParentMenu.width - 1
	# 	elif buttonComp:
	# 		self.OffsetX = toButton[0] - halfWidth
	# 	# else:
	# 	# 	self.ScreenAdjustX = monitor.right - winRight + 1
	# if winTop > monitor.scaledTop:
	# 	if buttonComp:
	# 		self.OffsetY = toButton[1] - halfHeight
	# 	# else:
	# 	# 	self.ScreenAdjustY = monitor.top - winTop
	# if winBottom < monitor.scaledBottom:
	# 	if buttonComp:
	# 		self.OffsetY = toButton[1] + halfHeight + buttonComp.par.h
	# 	# else:
	# 	# 	self.ScreenAdjustY = monitor.bottom - winBottom

	def setAttachPars(self):
		enable = self.ownerComp.par.Buttoncomp.eval()
		self.ownerComp.par.Horizontalattach.enable = \
			self.ownerComp.par.Verticalattach.enable = enable

	def refresh(self):
		"""
		Update menu display
		"""
		self.updateCheckedItems()
		self.setDimensions()
		self.Lister.Refresh()

	# hack to make sure par execs cook properly
	# run('op(' + str(self.ownerComp.id) + ').cook(force=True)',
	# 	delayFrames=1, delayRef=op.TDResources)

	def onParValueChange(self, par, val, prev):
		if par.name in ['Horizontalalign', 'Verticalalign']:
			self.RecalculateOffsets()
		elif par.name == 'Columns':
			self.ownerComp.par.Checkeditems.enable = par.eval() == 1
			self.ownerComp.par.Dividersafteritems.enable = par.eval() == 1
			self.Lister.ext.ListerExt.setupAutoColDefine(True)
			self.Lister.Refresh()
		elif par.name in ['Items', 'Dividersafteritems', 'Checkeditems',
		                  'Disableditems', 'Highlighteditems', 'w', 'h',
		                  'Shortcuts']:
			self.Lister.ext.ListerExt.setupAutoColDefine(True)
			if self.IsOpen or self.ownerComp.viewer:
				self.refresh()
		elif par.name == 'Buttoncomp':
			self.setAttachPars()

	def onParPulse(self, par):
		if par.name == 'Open':
			self.Open()
		elif par.name == 'Close':
			self.Close()
		elif par.name == 'Editcallbacks':
			dat = self.ownerComp.par.Callbackdat.eval()
			dat.par.edit.pulse()
		elif par.name == 'Helppage':
			ui.viewFile('https://docs.derivative.ca/index.php?'
			            'title=Palette:popMenu')
		elif par.name == 'Refreshlookconfig':
			self.Lister.par.Refresh.pulse()




