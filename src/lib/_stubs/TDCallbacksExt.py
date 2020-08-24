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

# callbacks extension

import traceback
import reprlib

#short form repr for print callbacks
shortRepr = reprlib.Repr()
shortRepr.maxlevel = 1
shortRepr.maxlist = 10
shortRepr.maxdict = 10
shortRepr.maxtuple = 10
shortRepr.maxset = 10
shortRepr.maxfrozenset = 10
shortRepr.maxdeque = 3
shortRepr.maxlong = 20
shortRepr.maxstring = 200
shortRepr.maxother = 200

class CallbacksExt:
	"""
	Component extension providing a python callback system. Just call
	DoCallback( callbackname, callbackInfo dictionary). See DoCallback method
	for details.

	Assigned callbacks can be created for easier, more specific use. See
	SetAssignedCallback for details.

	This extension looks for two parameters on its component: A toggle named
	Printcallbacks, and a DAT named Callbackdat. If these aren't present, the
	(non-promoted!) members callbackDat and printCallbacks can be set.

	If you want to set up a chain of callback targets, use PassCallbacksTo to
	set the next target. This target can be a dat or a function. 
	Unfound callbacks will then be sent to the appropriate callback in the dat
	or to the function. Also, from within a callback, you can call
		info['ownerComp'].PassOnCallback(info)
	to pass it on to the target. If you need to return a value, use:
		info['returnValue'] = <my return value>
		return info['ownerComp'].PassOnCallback(info)
	NOTE: Returning values in chained callbacks is tricky and requires special
		attention both to what is being ultimately returned and how the
		receiver is looking at it.
	"""

	def __init__(self, ownerComp):
		#The component to which this extension is attached
		self.ownerComp = ownerComp
		self.AssignedCallbacks = {}
		self.PassTarget = None
		self._printCallbacks = False
		if hasattr(ownerComp.par, 'Callbackdat'):
			self.callbackDat = ownerComp.par.Callbackdat.eval()
			if self.callbackDat:
				try:
					if self.callbackDat.text.strip():
						self.callbackDat.module
				except:
					print(traceback.format_exc())
					self.ownerComp.addScriptError("Error in Callback DAT. "
											"See textport for details.")
					raise

		else:
			self.callbackDat = None

		# repr function for short prints
		self.shortRepr = shortRepr

	def SetAssignedCallback(self, callbackName, callback):
		"""
		An assigned callback is a callback system made to call specified python
		methods rather than searching a callback DAT.

		callbackName is the name to be passed to the DoAssignedCallback method
		callback is a python function that takes a single callbackInfo argument,
			just like standard callbacks. If callback is None, callbackName is
			removed from the assigned callback system.
		details is extra info to be passed in the ['details'] key of infoDict
			when callback is called. callbackName will also be added to infoDict
		"""
		if callback is not None:
			if callable(callback):
				self.AssignedCallbacks[callbackName] = callback
			else:
				raise TypeError("SetAssignedCallback" + callbackName +
								"attempted to assign non-callable object: "
								+ callback)
		else:
			try:
				del self.AssignedCallbacks[callbackName]
			except:
				pass

	# def DoAssignedCallback(self, callbackName, callbackInfo=None):
	# 	"""
	# 	Perform the assigned callback with callbackName. See DoCallback for
	# 	full details.
	# 	"""
	# 	try:
	# 		callback, details = self.AssignedCallbacks[callbackName]
	# 	except:
	# 		if self.PrintCallbacks:
	# 			debug(callbackInfo)
	# 			self.DoCallback(callbackName + " (assigned callback)",
	# 							callbackInfo, None)
	# 		return
	# 	if callbackInfo is None:
	# 		callbackInfo = {'callbackName': callbackName}
	# 	if details is not None:
	# 		callbackInfo['details'] = details
	# 	self.DoCallback(callbackName, callbackInfo, callback)
	#
	def DoCallback(self, callbackName, callbackInfo=None, callbackOrDat=None):
		"""
		If it exists, call the named callback in ownerComp.par.Callbackdat.
		Pass any data inside callbackInfo. callbackInfo['ownerComp'] is set to
		self.ownerComp. If callback needs special instructions, such as looking
		for return data, put them in an callbackInfo['about']

		callbackOrDat is used for redirection to a DAT or specific function

		If callback is provided, the mod search is skipped and it will be
		called instead.

		If a user callback was found, returns callbackInfo with the callback
		return value in callbackInfo['returnValue']. If no callback found,
		returns None.

		If ownerComp has a parameter called Printcallbacks, and that parameter
		is True, callbacks will be printed when called.
		"""
		if callable(callbackOrDat):
			callback = callbackOrDat
		else:
			callback = self.AssignedCallbacks.get(callbackName)
		if not callback:
			if callbackOrDat:
				moduleDat = callbackOrDat
			else:
				try:
					self.callbackDat = moduleDat = \
										self.ownerComp.par.Callbackdat.eval()
				except:
					self.callbackDat = moduleDat = None
			try:
				try:
					callbackMod = self.callbackDat.module
					callback = getattr(callbackMod, callbackName, None)
				except:
					pass
			except:
				if moduleDat:
					print(self.ownerComp, "Invalid callback DAT:",
						  										moduleDat.path)
					raise
				else:
					if not self.PrintCallbacks:
						# callback dat is blank and no print, just forget it.
						return
					callback = None
		if callbackInfo is None:
			callbackInfo = {}
		callbackInfo.setdefault('ownerComp', self.ownerComp)
		callbackInfo['callbackName'] = callbackName
		# do callback if found
		if callback:
			# the next line is the actual function call
			# put returnValue into the callbackInfo dict
			callbackInfo['returnValue'] = callback(callbackInfo)
			retvalue = callbackInfo
			printCallback = self.PrintCallbacks
		# pass callback on if pass target
		elif self.PassTarget and self.PassTarget != callbackOrDat:
			callbackInfo['returnValue'] = self.PassOnCallback(callbackInfo)
			retvalue = callbackInfo
			printCallback = False
		# no callback
		else:
			retvalue = None
			printCallback = self.PrintCallbacks
		# print callback
		if printCallback:
			if retvalue is None or callback and self.PassTarget:
				notfound = 'NOT FOUND -'
			else:
				notfound = '-'
			print(callbackName, notfound,'callbackInfo: ',
				  self.shortRepr.repr(callbackInfo), '\n')
		return retvalue

	def PassCallbacksTo(self, passTarget):
		"""
		Set a target DAT or function for passing on unfound callbacks to.
		"""
		if callable(passTarget):
			self.PassTarget = passTarget
		elif isinstance(passTarget, DAT):
			try:
				passTarget.module
			except:
				self.ownerComp.error = traceback.format_exc() + \
					"\nError in Callback DAT. See textport for details."
				raise
			self.PassTarget = passTarget
		else:
			raise TypeError('PassCallbacksTo target must be callable or DAT. '
							'Got ' + str(passTarget) + '.')

	def PassOnCallback(self, info):
		"""
		Pass this callback to ContextExt's PassTarget. Use PassCallbacksTo to
		set target
		"""
		callbackName = info['callbackName']
		firstReturnValue = info.get('returnValue',None)
		returnDict = self.DoCallback(callbackName, info, self.PassTarget)
		if returnDict:
			if returnDict['returnValue'] is None:
				return firstReturnValue
			else:
				return returnDict['returnValue']
		else:
			return firstReturnValue

	@property
	def CallbackDat(self):
		return self.callbackDat
	@CallbackDat.setter
	def CallbackDat(self, val):
		self.callbackDat = val
		if hasattr(ownerComp.par, 'Callbackdat'):
			ownerComp.par.Callbackdat.val = self.callbackDat

	@property
	def PrintCallbacks(self):
		if hasattr(self.ownerComp.par, 'Printcallbacks'):
			return self.ownerComp.par.Printcallbacks.eval()
		else:
			return self._printCallbacks
	@PrintCallbacks.setter
	def PrintCallbacks(self, val):
		if hasattr(self.ownerComp.par, 'Printcallbacks'):
			self.ownerComp.par.Printcallbacks = val
		else:
			self._printCallbacks = val
