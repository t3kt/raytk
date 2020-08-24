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

import shlex
import inspect
import collections
import TDStoreTools
import warnings
import datetime


def clamp(value, inMin, inMax):
	"""returns the value clamped between inMin and inMax"""
	return min(inMax, max(inMin, value))

def parentLevel(parentOp, childOp):
	"""
	determines if op1 is a parent of op2 at any depth. Returns None or the
	depth of parenthood. i.e. op2.parent(returnValue) will yield op1.
	This method returns None so that op2.parent(returnValue) will error in
	that case.
	"""
	if parentOp == childOp:
		return 0
	parentLev = 1
	while True:
		parent = childOp.parent(parentLev)
		if parent is None:
			return None
		elif parent is parentOp:
			return parentLev
		parentLev += 1

def sharedParent(op1, op2):
	"""
	Returns the nearest shared parent of op1 and op2. Returns None if root is
	result.
	"""
	if op1 == root or op2 == root:
		return None
	checkPath = op1.path.rpartition('/')[0]
	while checkPath != '':
		if op2.path.startswith(checkPath):
			return op(checkPath)
		checkPath = checkPath.rpartition('/')[0]

def getShortcutPath(fromOp, toOp, toParName=None):
	"""
	Return a shortcut path expression from fromOp to toOp or a parameter on
	toOp. This expression is suitable for use in any OP parameter on fromOp.
		OP portion of shortcut will be the first of:
			me
			op('/')
			op('./<path>')  -  Direct child
			op('<toOp.name>')  -  Direct sibling
			parent.<parentshortcut>
			parent.<parentshortcut>.op('<path>')
			op.<opshortcut>
			op.<opshortcut>.op('<path>')
			parent(#)
			parent(#).op('<path>')
			op('<toOp.path>')


	toParName: (string) if provided, the shortcut will be to that parameter on
				toOp. If possible, the 'ipar' shortcut will be used.

	"""
	def rootChild(rootOp, rootExpr=''):
		if rootOp == op('/'):
			fromRoot = toOp.path
		else:
			fromRoot = toOp.path[len(rootOp.path) + 1:]
		return rootExpr + "op('" + fromRoot + "')"

	def parCheck(shortcutPath):
		if toParName:
			return shortcutPath +'.par.' + toParName
		else:
			return shortcutPath

	if fromOp is None:
		raise ValueError("getShortcutPath: invalid fromOp")
	if toOp is None:
		raise ValueError("getShortcutPath: invalid toOp")

	# me
	if fromOp == toOp:
		return parCheck('me')

	# op('/')
	if toOp == op('/'):
		return parCheck("op('/')")

	# op('./<path>')  -  Direct child
	if parentLevel(fromOp, toOp) and fromOp != op('/'):
		return parCheck("op('." + toOp.path[len(fromOp.path):] + "')")

	# op('<toOp.name>')  -  Direct sibling
	if fromOp.parent() == toOp.parent():
		return parCheck("op('" + toOp.name + "')")

	# parent.<parentshortcut>
	if parentLevel(toOp, fromOp) and getattr(toOp.par, 'parentshortcut') \
			and toOp.par.parentshortcut.eval().strip():
		return parCheck('parent.' + toOp.par.parentshortcut)

	# op.<opshortcut>
	if getattr(toOp.par, 'opshortcut', None) \
			and toOp.par.opshortcut.eval().strip():
		return parCheck('op.' + toOp.par.opshortcut.eval())

	# parent(#)
	if True: # toOp.parent() != op('/'):
		if parentLevel(toOp, fromOp) and toOp != root:
			level = parentLevel(toOp, fromOp)
			return parCheck('parent(' + (str(level) if level > 1 else '') + ')')
		# parent(#).op('<path>')
		# search for common parents
		sanity = 100
		searchOp = toOp
		while searchOp != op('/'):
			sanity -= 1  # reduce sanity
			if sanity == 0:
				raise Exception("parentLevel search exceeded max depth",
								fromOp, toOp)
			searchOp = searchOp.parent()
			level = parentLevel(searchOp, fromOp)
			if level:
				if level > 1 and searchOp != root:
					rootExpr = 'parent(' + \
							   		(str(level) if level > 1 else '') + ').'
				else:
					rootExpr = ''
				return parCheck(rootChild(searchOp, rootExpr))

	# op.<globalshortcut>.op('<path>')
	# search for common shortcut parents
	sanity = 100
	searchOp = toOp
	while searchOp != op('/'):
		sanity -= 1  # reduce sanity
		if sanity == 0:
			raise Exception("parentLevel search exceeded max depth",
							fromOp, toOp)
		searchOp = searchOp.parent()
		opShortcut = searchOp.par.opshortcut.eval().strip()
		if opShortcut:
			rootExpr = 'op.' + opShortcut + '.'
			return parCheck(rootChild(searchOp, rootExpr))

	# op('<toOp.path>')
	# debug('!', toOp.path)
	# debug(parCheck("op('" + toOp.path + "')"))
	return parCheck("op('" + toOp.path + "')")

menuObject = collections.namedtuple('menuObject', ['menuNames', 'menuLabels'])

def parMenu(menuNames, menuLabels=None):
	"""
	Returns an object suitable for menuSource property of parameters.
	menuNames must be a collection of strings.
	menuLabels defaults to menuNames.
	"""
	if menuLabels is None:
		menuLabels = menuNames
	return menuObject(menuNames, menuLabels)

def incrementStringDigits(string, min=1):
	"""
	method for iterating a string with digits on the end, or adding
	digits if none are there. This simulates the automatic naming of duplicate
	operators.
	"""
	returnString = string
	digits = tdu.digits(string)
	if digits is None:
		returnString += str(min)
	else:
		digitString = str(digits)
		prefix = string[0:string.rfind(digitString)]
		suffix = string[string.rfind(digitString)+len(digitString):]
		returnString = prefix + str(digits+1) + suffix
	return returnString

def findNetworkEdges(comp, ignoreNodes=None):
	"""
	returns a dictionary of 'nodes' and 'positions' at extremes of network.
		returns None if no nodes found. Dictionary keys are 'top', 'left',
		'right', 'bottom'
	ignoreNodes is a list of nodes in network to ignore...
	"""
	if ignoreNodes is None:
		ignoreNodes = []
	if not isinstance(comp, COMP):
		raise ValueError ('findNetworkEdges requires COMP to search', comp)

	childOps = comp.findChildren(depth=1, key=lambda x: x not in ignoreNodes)
	if not childOps:
		return None
	edgeNodes = {'top': None, 'left': None, 'right': None, 'bottom': None}
	positions = {'top': None, 'left': None, 'right': None, 'bottom': None}

	for tOp in childOps:
		nX = tOp.nodeX
		nY = tOp.nodeY
		nW = tOp.nodeWidth
		nH = tOp.nodeHeight

		if positions['right'] is None or nX + nW >= positions['right']:
			edgeNodes['right'] = tOp
			positions['right'] = nX + nW

		if positions['top'] is None or nY + nH >= positions['top']:
			edgeNodes['top'] = tOp
			positions['top'] = nY + nH

		if positions['left'] is None or nX < positions['left']:
			edgeNodes['left'] = tOp
			positions['left'] = nX

		if positions['bottom'] is None or nY < positions['bottom']:
			edgeNodes['bottom'] = tOp
			positions['bottom'] = nY

	return {'nodes': edgeNodes, 'positions': positions}

def arrangeNode(node, position='bottom', spacing=20):
	"""
	Arrange a node according to the other nodes in the network
	position: can be 'bottom', 'top', 'left' or 'right'
		left, right will be placed parallel with top nodes.
		top, bottom will be placed parallel with left nodes.
	"""
	edges = findNetworkEdges(node.parent(), [node])
	if edges is None:
		node.nodeX = node.nodeY = 0
		return
	extremes = edges['positions']
	if position == 'bottom':
		node.nodeX = extremes['left']
		node.nodeY = extremes['bottom'] - node.nodeHeight - spacing
	elif position == 'top':
		node.nodeX = extremes['left']
		node.nodeY = extremes['top'] + spacing
	elif position == 'right':
		node.nodeX = extremes['right'] + spacing
		node.nodeY = extremes['top'] - node.nodeHeight
	elif position == 'left':
		node.nodeX = extremes['left'] - node.nodeWidth - spacing
		node.nodeY = extremes['top'] - node.nodeHeight
	else:
		raise ValueError ('Invalid arrangeNode position', position)

def createProperty(classInstance, name, value=None, attributeName=None,
						 readOnly=False, dependable=True):
	"""
	Use this method to add a property (called name) that accesses
	an attribute (called attributeName). attributeName defaults to '_' + name.
	The attribute will be set to value argument.
	If dependable is True, the attribute will store value in a dependency obj.
		If dependable is 'deep', lists, sets, or dicts will be created as
		dependable collections from TDStoreTools
	If readonly is True, the property will be read only
	WARNING: the property is added to the CLASS of instance, so all objects of
	instance's class will now have this property.
	"""
	if dependable == 'Deep':
		dependable = 'deep'
	if attributeName is None:
		attributeName = '_' + name
	if dependable:
		if dependable == 'deep':
			depValue = makeDeepDependable(value)
		else:
			depValue = tdu.Dependency(value)
		setattr(classInstance, attributeName, depValue)
		def getter(self):
			if dependable == 'deep' and readOnly:
				try:
					return getattr(self, attributeName).val.getRaw()
				except:
					return getattr(self, attributeName).val
			else:
				return getattr(self, attributeName).val
		def setter(self, val):
			getattr(self, attributeName).val = val
		def deleter(self):
			getattr(self, attributeName).modified()
			delattr(self, attributeName)
	else:
		setattr(classInstance, attributeName, value)
		def getter(self):
			return getattr(self, attributeName)
		def setter(self, val):
			setattr(self, attributeName, val)
		def deleter(self):
			getattr(self, attributeName).modified()
			delattr(self, attributeName)
	setattr(classInstance.__class__, name, property(getter,
											   None if readOnly else setter,
											   deleter))

def makeDeepDependable(value):
	"""
	returns a deeply dependable object out of the provided python object.
	Deeply dependable collections will cause cooks when their contents change.
	"""
	if isinstance(value, dict):
		depValue = TDStoreTools.DependDict(value)
	elif isinstance(value, list):
		depValue = TDStoreTools.DependList(value)
	elif isinstance(value, set):
		depValue = TDStoreTools.DependSet(value)
	else:
		depValue = tdu.Dependency(value)
	return depValue

def forceCookNonDatOps(comp):
	"""
	Recursively force cook op and all children of op, unless they are DATs
	"""
	if not isinstance(comp, COMP):
		return
	for child in comp.children:
		forceCookNonDatOps(child)
	comp.cook(force=True)

def showInPane(operator, pane='Floating', inside=False):
	"""
	Open an operator for viewing in a chosen editor pane.  The pane will be
	focused on the chosen operator unless inside is True, in which case it will
	show the inside if possible.

	operator: the operator to view
	pane: a ui.pane or 'Floating' for a new floating pane.
	inside: if inside is True, try to show view inside comps
	"""
	if isinstance(operator, COMP) and inside:
		homeViewOp = None
	else:
		homeViewOp = operator
		operator = operator.parent()
		for o in operator.children:
			o.selected = False
		homeViewOp.current = True
	if pane is None:
		return
	# check for closed pane...
	if pane is not 'Floating' and pane.id not in [p.id for p in ui.panes]:
		print ('showInPane: Target pane not found, creating floating pane.')
		pane = 'Floating'

	if pane == 'Floating':
		targetPane = ui.panes.createFloating(type=PaneType.NETWORKEDITOR)
		targetPane.owner = operator
		try:
			targetPane.name = operator.name
		except:
			pass
	else:
		try:
			pane.owner = operator
		except:
			print('Unable to open ' + str(operator) + ' in ' + str(pane))
			raise
		targetPane = pane  # for name set
	if homeViewOp:
		run("ui.panes['" + targetPane.name + "'].homeSelected(zoom=True)",
				delayFrames=1)
	else:
		run("ui.panes['" + targetPane.name + "'].home(zoom=True)",
				delayFrames=1)
	return targetPane

def tScript(cmd):
	"""
	Run a tscript command. Use at your own risk, this is basically a hack.
	Also, it's slow because it creates and destroys an operator. If you need
	this to be faster, build an optimized network with its own tscript dat.
	"""
	dat = op('/').create(textDAT, 'tScripter')
	dat.python = False
	dat.text = cmd
	dat.run()
	dat.destroy()

def parStringToIntList(parString):
	"""
	Convert a space delimited string to a list of ints
	"""
	return [int(x) for x in parString.split()]

def listToParString(l):
	"""
	Convert a list to a space delimited string
	"""
	return ' '.join([str(x) for x in l])

def replaceOp(dest, source=None):
	"""
	Replace dest with an exact copy of source. If source is None and dest is a
	comp, try to use dest's clone parameter.
	"""
	# check dest and source
	if not isinstance(dest, OP):
		raise ValueError('replaceOp: invalid dest', dest)
	if source is None and hasattr(dest.par,'clone'):
		source = op(dest.par.clone.eval())
		clonePar = dest.par.clone
	else:
		clonePar = None
	if not isinstance(source, OP):
		raise AttributeError('replaceOp: invalid source ' + str(source) + ' '
														  'for ' + str(dest))
	# save dest info
	destName = dest.name
	# attributes
	destAttrs = ['nodeX', 'nodeY', 'nodeWidth', 'nodeHeight', 'color', 'dock']
	destAttrDict = {}
	for attr in destAttrs:
		destAttrDict[attr] = getattr(dest, attr)
	# connections
	if hasattr(dest, 'inputCOMPs'):
		destInputCOMPs = [c.path for c in dest.inputCOMPs]
	else:
		destInputCOMPs = None
	if hasattr(dest, 'outputCOMPs'):
		destOutputCOMPs = [c.path for c in dest.outputCOMPs]
	else:
		destOutputCOMPs = None
	destInputs = [o.path for o in dest.inputs]
	destOutputs = [o.path for o in dest.outputs]

	# do copy
	parent = dest.parent()
	newDest = parent.copy(source)
	try:
		# attrs
		for attr, value in destAttrDict.items():
			setattr(newDest, attr, value)
		# clone
		if clonePar:
			newDest.par.clone.val = clonePar.val
			newDest.par.clone.expr = clonePar.expr
			newDest.par.clone.mode = clonePar.mode
		# connections
		if destInputCOMPs:
			newInput = newDest.inputCOMPConnectors[0]
			for path in destInputCOMPs:
				newInput.connect(op(path))
		if destOutputCOMPs:
			newOutput = newDest.outputCOMPConnectors[0]
			for path in destOutputCOMPs:
				newOutput.connect(op(path))
		for i, path in enumerate(destInputs):
			newDest.inputConnectors[i].connect(op(path))
		for i, path in enumerate(destOutputs):
			newDest.outputConnectors[i].connect(op(path))
	except:
		newDest.destroy()
		raise
	dest.destroy()
	newDest.name = destName
	return newDest

def getParInfo(sourceOp, pattern='*', names=None,
			   				includeCustom=True, includeNonCustom=True):
	"""
	Returns parInfo dict for sourceOp. Filtered in the following order:
	pattern is a pattern match string
	names can be a list of names to include, default None includes all
	includeCustom to include custom parameters
	includeNonCustom to include non-custom parameters

	parInfo is {<parName>:(par.val, par.expr, par.mode string, par.bindExpr,
							par.default)...}
	"""
	parInfo = {}
	for p in sourceOp.pars(pattern):
		if (names is None or p.name in names) and \
				((p.isCustom and includeCustom) or \
										(not p.isCustom and includeNonCustom)):
			parInfo[p.name] = [p.val, p.expr if p.expr else '', p.mode.name,
							   p.bindExpr, p.default]
	return parInfo

def applyParDefaults(targetOp, parInfo):
	"""
	Attempt to apply par defaults from parInfo dict to targetOp. If application
		fails, no exception will be raised!

	parInfo is {<parName>:(par.val, par.expr, par.mode string, par.bindExpr,
							par.default)...}
	"""
	for p in targetOp.pars():
		if p.name in parInfo:
			info = parInfo[p.name]
			default = info[4] if len(info) > 4 else None
			if default is not None:
				try:
					p.default = default
				except:
					pass

def applyParInfo(targetOp, parInfo, setDefaults=False):
	"""
	Attempt to apply par values, expressions, and modes from parInfo dict to
	targetOp. If application fails, no exception will be raised!

	parInfo is {<parName>:(par.val, par.expr, par.mode string, par.bindExpr,
							par.default)...}
	setDefaults: if True, set the par.default as well
	"""
	if setDefaults:
		applyParDefaults(targetOp, parInfo)
	for p in targetOp.pars():
		if p.name in parInfo:
			# this dance is to maintain mode and priority of value.
			# otherwise bad things happen when an expression value
			# is a constant.
			info = parInfo[p.name]
			val = info[0]
			expr = info[1] if info[1] is not None else ''
			mode = info[2]
			bindExpr = info[3] if len(info) > 3 else ''
			if type(mode) == str:
				mode = getattr(ParMode, info[2])
			if mode == ParMode.CONSTANT:
				try:
					p.expr = expr
				except:
					pass
				try:
					p.bindExpr = bindExpr
				except:
					pass
				try:
					p.val = val
				except:
					pass
				p.mode = mode
			elif mode == ParMode.EXPRESSION:
				try:
					p.val = val
				except:
					pass
				try:
					p.bindExpr = bindExpr
				except:
					pass
				try:
					p.expr = expr
				except:
					pass
				p.mode = mode
			elif mode == ParMode.BIND:
				if p.bindMaster is not None:
					bindVal = p.bindMaster.eval()
				try:
					p.val = val
				except:
					pass
				try:
					p.expr = expr
				except:
					pass
				try:
					p.bindExpr = bindExpr
				except:
					pass
				p.mode = mode
				try:
					p.val = bindVal
				except:
					pass
			else:
				try:
					p.val = val
				except:
					pass
				try:
					p.bindExpr = bindExpr
				except:
					pass
				try:
					p.expr = expr
				except:
					pass
				p.mode = mode

def panelParentShortcut(panel, parentShortcut):
	"""
	return the first panelParent of panel that has the provided parentShortcut.
	Returns None if no panelParent with shortcut is found.
	"""
	while hasattr(panel, 'panelParent'):
		panel = panel.panelParent()
		if panel is None or panel.par.parentshortcut == parentShortcut:
			return panel

def getMenuLabel(menuPar):
	"""
	Return menuPar's currently selected menu item's label
	"""
	try:
		return menuPar.menuLabels[menuPar.menuIndex]
	except IndexError:
		raise
	except:
		raise TypeError("getMenuLabel: invalid menu par " + repr(menuPar))

def setMenuLabel(menuPar, label):
	"""
	Sets menuPar's selected menu item to the item with menuLabel == label
	"""
	try:
		menuPar.menuIndex = menuPar.menuLabels.index(label)
	except ValueError:
		raise ValueError("setMenuLabel: invalid label " + label + " - " +
						 repr(menuPar))
	except:
		raise TypeError("setMenuLabel: invalid menu par " + repr(menuPar))

def validChannelName(name):
	"""
	Returns a valid channel name based on name.
	"""
	name = name.replace(' ', '_')
	op('constant1').par.name0 = name
	validName = op('constant1')[0].name
	op('constant1').par.name0 = ''
	return validName

def messageDialog(text, title):
	"""
	Open a popup dialog (after one frame delay), with just an OK button

	text: text of dialog
	title: title of dialog
	"""
	run("""op.TDResources.op('popDialog').Open(
		text=""" + repr(text) + ", title=" + repr(title) +
		""",
		buttons=['OK'],
		callback=None,
		details=None,
		textEntry=False,
		escButton=1,
		escOnClickAway=True,
		enterButton=1)
		""", delayFrames=1, delayRef=op.TDResources
		)

errorDialog = messageDialog # for backwards compatibility

def extensionOPFromPar(comp, userIndex):
	"""
	Return extension module, internal parameter comp, or best guess given
	extension par text

	:param comp: the component holding extension
	:param userIndex: the 1 based index of extension parameter
	"""
	ext = getattr(comp.par, 'extension' + str(userIndex)).eval()
	extension = comp.extensions[userIndex - 1]
	if extension:
		eop = extensionOP(extension)
	else:
		eop = None
		# try best guess
		if '.module.' in ext:
			try:
				extParts = ext.split('.module.')
				eop = comp.evalExpression(extParts[0])
			except:
				eop = None
	return eop


def extensionOP(extension):
	"""
	Get an extension's associated operator

	:param extension: the extension
	:return: the DAT source of extension or the internal parameters' comp or
				None if undetermined
	"""
	eop = None
	if isinstance(extension, ParCollection):
		# assume internal parameters
		eop = extension.stdswitcher1.owner
	elif extension:
		try:
			eop = op(extension.__class__.__module__)
		except:
			eop = None
	return eop

def editExtensionOP(extOP):
	"""
	Attempt to open the appropriate editor for the given extension operator.
	Viewer for uneditable DATs, editor for other DATs. CompEditor for Internal
	Parameters.

	:param extension: the extension
	:return:
	"""
	if isinstance(extOP, textDAT):
		extOP.par.edit.pulse()
	elif isinstance(extOP, DAT):
		extOP.openViewer()
	elif isinstance(extOP, COMP):
		op.TDDialogs.op('CompEditor').Connect(extOP)
		op.TDDialogs.op('CompEditor').openViewer()

def bindChain(par, parsOnly=False):
	"""
	Return a list of parameters, starting with par, followed by its bind master,
	if available, followed by it's master's master if available etc.
	:param par: the parameter to start the chain search
	:param parsOnly: if True, only return parameters in the chain
	:return: list of [par, par's bind master, ...]
	"""
	chain = [par]
	try:
		master = par.mode == ParMode.BIND and par.bindMaster
	except:
		master = None
	while master:
		chain.append(master)
		try:
			master = master.mode == ParMode.BIND and master.bindMaster
		except:
			master = None
	if parsOnly and not isinstance(chain[-1], Par):
		chain.pop(-1)
	return chain

def unbindReferences(par, modeOnly=False):
	"""
	Erase bind strings or change modes for all bindReferences of a parameter

	:param par: the bindMaster parameter
	:param modeOnly: if True, just change the references modes to prevMode
	:return: the references that were changed
	"""
	refs = par.bindReferences
	for p in refs:
		p.mode = p.prevMode
		if not modeOnly:
			p.bindExpr = ''
	return refs

def timestampFromISO(iso, zeroOnError=True):
	"""
	Get a float representation from an ISO formatted time string. See
	https://docs.python.org/3/library/datetime.html#datetime-objects

	:param iso: time string
	:param zeroOnError: return zero if there is an exception, otherwise raise it
	:return: timestamp float of the iso
	"""
	try:
		return datetime.datetime.fromisoformat(iso).timestamp()
	except:
		if zeroOnError:
			return 0
		else:
			raise

def getCustomPage(comp, name):
	"""
	Get a custom page by name
	Args:
		comp: comp with custom page
		name: page name

	Returns:
		Page object or None if name not found
	"""
	for p in comp.customPages:
		if p.name == name:
			return p