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

from TDStoreTools import StorageManager

class PopDialogExt:

	def __init__(self, ownerComp):
		"""
		Popup dialog extension. Just call the DoPopup method to create a popup.
		Provide info in that method. This component can be used over and over,
		no need for a different component for each dialog, unless you want to
		change the insides.
		"""
		self.ownerComp = ownerComp
		self.windowComp = ownerComp.op('popDialogWindow')
		self.details = None
		storedItems = [
			{'name':'EnteredText', 'default':''}
		]
		self.stored = StorageManager(self, ownerComp, storedItems)
		self.UpdateTextHeight()

	def OpenDefault(self, text='', title='', buttons=('OK',), callback=None,
					details=None, textEntry=False, escButton=1,
					escOnClickAway=True, enterButton=1):
		self.Open(text, title, buttons, callback, details, textEntry, escButton,
				  escOnClickAway, enterButton)

	def Open(self, text=None, title=None, buttons=None, callback=None,
			 			details=None, textEntry=None, escButton=None,
			 			escOnClickAway=None, enterButton=None):
		"""
		Open a popup dialog.
		text goes in the center of the dialog. Default None, use pars.
		title goes on top of the dialog. Blank means no title bar. Default None,
			use pars
		buttons is a list of strings. The number of buttons is equal to the
			number of buttons, up to 4. Default is ['OK']
		callback: a method that will be called when a selection is made, see the
		 	SetCallback method. This is in addition to all internal callbacks.
		 	If not provided, Callback DAT will be searched.
		details: will be passed to callback in addition to item chosen.
			Default is None.
		If textEntry is a string, display textEntry field and use the string
			as a default. If textEntry is False, no entry field. Default is
			None, use pars
		escButton is a number from 1-4 indicating which button is simulated when
			esc is pressed or False for no button simulation. Default is None,
			use pars. First button is 1 not 0!!!
		enterButton is a number from 1-4 indicating which button is simulated
			when enter is pressed or False for no button simulation. Default is
			None, use pars. First button is 1 not 0!!!
		escOnClickAway is a boolean indicating whether esc is simulated when user
			clicks somewhere besides the dialog. Default is None, use pars
		"""
		self.Close()
		# text and title
		if text is not None:
			self.ownerComp.par.Text = text
		if title is not None:
			self.ownerComp.par.Title = title
		# buttons
		if buttons is not None:
			if not isinstance(buttons, list):
				buttons = ['OK']
			self.ownerComp.par.Buttons = len(buttons)
			for i, label in enumerate(buttons[:4]):
				getattr(self.ownerComp.par,
										'Buttonlabel' + str(i + 1)).val = label
		# callbacks
		if callback:
			ext.CallbacksExt.SetAssignedCallback('onSelect', callback)
		else:
			ext.CallbacksExt.SetAssignedCallback('onSelect', None)
		# textEntry
		if textEntry is not None:
			if isinstance(textEntry, str):
				self.ownerComp.par.Textentryarea = True
				self.ownerComp.par.Textentrydefault = str(textEntry)
			elif textEntry:
				self.ownerComp.par.Textentryarea = True
				self.ownerComp.par.Textentrydefault = ''
			else:
				self.ownerComp.par.Textentryarea = False
		self.EnteredText = self.ownerComp.par.Textentrydefault.eval()
		self.details = details
		self.ownerComp.op('entry/inputText').par.text = \
				self.ownerComp.op('entry').panel.field = self.EnteredText
		self.ownerComp.op('entry').cook(force=True)
		if escButton is not None:
			if escButton is False or not (1 <= escButton <= 4):
				self.ownerComp.par.Escbutton = 'None'
			else:
				self.ownerComp.par.Escbutton = str(escButton)
		if escOnClickAway is not None:
			self.ownerComp.par.Esconclickaway = escOnClickAway
		if enterButton is not None:
			if enterButton is False or not (1 <= enterButton <= 4):
				self.ownerComp.par.Enterbutton = 'None'
			else:
				self.ownerComp.par.Enterbutton = str(enterButton)
		self.UpdateTextHeight()
		run("op('" + self.ownerComp.path + "').ext.PopDialogExt.actualOpen()",
										delayFrames=1, delayRef=op.TDResources)

	def actualOpen(self):
		# needs to be deferred so that sizes can update properly
		self.windowComp.par.winopen.pulse()
		ext.CallbacksExt.DoCallback('onOpen')
		if self.ownerComp.op('entry').par.display.eval():
			self.ownerComp.setFocus()
			# hack should be automatically set by kbfocus
			# self.ownerComp.op('entry').setFocus()
			# hack shouldn't have to wait a frame
			run('op("' + self.ownerComp.path + '").op("entry").'
							'setKeyboardFocus(selectAll=True)',
							delayFrames=1, delayRef=op.TDResources)
		else:
			self.ownerComp.setFocus()
			self.ownerComp.op('entry').setKeyboardFocus(selectAll=True)
		# HACK shouldn't be necessary - problem with clones/replicating
		self.ownerComp.op('replicator1').par.recreateall.pulse()

	def Close(self):
		"""
		Close the dialog
		"""
		ext.CallbacksExt.SetAssignedCallback('onSelect', None)
		ext.CallbacksExt.DoCallback('onClose')
		self.windowComp.par.winclose.pulse()
		self.ownerComp.op('entry/inputText').par.text = \
				self.ownerComp.op('entry').panel.field = self.EnteredText

	def OnButtonClicked(self, buttonNum):
		"""
		Callback from buttons
		"""
		infoDict = {'buttonNum': buttonNum,
					'button': getattr(self.ownerComp.par,
										'Buttonlabel' + str(buttonNum)).eval(),
					'details': self.details}
		if self.ownerComp.par.Textentryarea.eval():
			infoDict['enteredText'] = self.EnteredText
		try:
			ext.CallbacksExt.DoCallback('onSelect', infoDict)
		finally:
			self.Close()
		
	def OnKeyPressed(self, key):
		"""
		Callback for esc or enterpressed.
		"""
		if key == 'esc' and self.ownerComp.par.Escbutton.eval() != 'None':
			button = int(self.ownerComp.par.Escbutton.eval())
			if button <= self.ownerComp.par.Buttons:
				self.OnButtonClicked(button)
		if key == 'enter' and self.ownerComp.par.Enterbutton.eval() != 'None':
			button = int(self.ownerComp.par.Enterbutton.eval())
			if button <= self.ownerComp.par.Buttons:
				self.OnButtonClicked(button)

	def OnClickAway(self):
		"""
		Callback for esc pressed. Only happens when Escbutton is not None
		"""
		if self.ownerComp.par.Esconclickaway.eval():
			self.OnKeyPressed('esc')

	def OnParValueChange(self, par, val, prev):
		"""
		Callback for when parameters change
		"""
		if par.name == "Textentryarea":
			self.ownerComp.par.Textentrydefault.enable = par.eval()
		if par.name == "Escbutton":
			self.ownerComp.par.Esconclickaway.enable = par.eval() != "None"

	def OnParPulse(self, par):
		if par.name == "Open":
			self.Open()
		elif par.name == "Close":
			self.Close()
		elif par.name == 'Editcallbacks':
			dat = self.ownerComp.par.Callbackdat.eval()
			if dat:
				dat.par.edit.pulse()
			else:
				print("No callback dat for", self.ownerComp.path)
		elif par.name == 'Helppage':
			ui.viewFile('https://docs.derivative.ca/'
						'index.php?title=Palette:popDialog')

	def UpdateTextHeight(self):
		self.ownerComp.op('text').par.h = \
								self.ownerComp.op('text/text').textHeight