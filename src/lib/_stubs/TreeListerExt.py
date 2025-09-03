"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

For more info, see: http://www.derivative.ca/wiki099/index.php?title=Extensions
"""

from collections import namedtuple
from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions
TDJSON = op.TDModules.mod.TDJSON
ListerExtMod = op('lister/ListerExt').module
ListerExt = ListerExtMod.ListerExt
COLLOOKOVERLAYER = ListerExtMod.COLLOOKOVERLAYER
ROLLOVERLAYER = ListerExtMod.ROLLOVERLAYER

class TreeListerExt(ListerExt):
	"""
	TreeListerExt extends ListerExt for use as a tree.

	Each item in the tree must have a unique ID. This is commonly a path, but
	can be any string, int, float, or tuple.
	It stores it's tree as dicts of dicts, keyed by ID.
	"""

	# region Main

	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.TreeLister = self.treeListerComp = parent() # treeLister container
		self.Lister = ownerComp
		self.treeInputDAT = self.treeListerComp.op('input')
		self.jsonAutoColDefine = self.treeListerComp.op('jsonAutoColDefine')
		self.tableAutoColDefine = self.treeListerComp.op('tableAutoColDefine')
		
		self.NoPassToListerPars = ['Selectedoutput']
		self.setupListerPars()
		# stored items (persistent across saves and re-initialization):
		storedItems = [
			# Expanded is a dictionary of {<rootID>: set(<expandedPaths>)}
			{'name': 'Expanded', 'default': {}, 'property': True,
			 							'readOnly': True, 'dependable': True}
		]
		self.stored = StorageManager(self, ownerComp, storedItems)

		#TDF.createProperty(self, 'Expanded', {}, dependable='deep')
		self.setupExpanded()

		# extra data needed for tree
		self.DefaultRoots = [] # if root parameter is empty
		self.wiredOverlayCols = [] # for wired overlay color info
		self.wirePathColName = 'wirePath' # for flexibility/backwards compat.
		self.parentPathColName = 'parentPath' # ditto

		# tree info for visible rows
		self.treeDataDict = {}
		class TreeData(object):
			__slots__ = ('parent', 'root', 'indent', 'wiredChild')
			def __init__(self, *args):
				self.parent, self.root, self.indent, self.wiredChild = args
		self._TreeData = TreeData
		self.indent = 0 # defined later by customDefine table

		# tree info for persistent trees created with JSON
		self.json = None
		self.jsonIDObjDict = None
		self.jsonObjIDDict = None
		class JSONObj(object):
			__slots__ = ('key', 'id', 'value', 'type', 'children')
			def __init__(self, *args):
				self.key, self.id, self.value, self.type, self.children = args
		self._JSONObj = JSONObj

		self.SetError()
		ListerExt.__init__(self, ownerComp)

		#debug( self.ownerComp.par.Saveselectedrows.eval, self.ownerComp.par.Selectedrows.eval(), ListerExt._SelectedRows)
		# HACK: someday maybe we can remove this
		# it's here because deleting config breaks old tree listers due to the
		# wrong kind of immunity
		if self.configComp and self.configComp == self.TreeLister.op('config'):
			self.configComp.cloneImmune = False
			self.configComp.componentCloneImmune = True
		# move script errors to treeLister
		if self.ownerComp.scriptErrors():
			self.SetError(self.ownerComp.scriptErrors())
		# update sorts/filters
		for p in ['Sortcols', 'Sortreverse', 'Filtercols', 'Selectedrows']:
			self.TreeLister.par[p] = self.ownerComp.par[p].eval()

	def PostInit(self):
		scriptErrors = self.ownerComp.scriptErrors()
		try:
			self.ReloadInput()
		except:
			self.SetError('Error on initial input load. See textport.')
			import traceback; traceback.print_exc()
		ListerExt.PostInit(self)
		if scriptErrors:
			self.SetError(scriptErrors)

	@property
	def IDObjDict(self):
		return self.jsonIDObjDict

	@property
	def ObjIDDict(self):
		return self.jsonObjIDDict

	def setupExpanded(self):
		for root, expanded in self.Expanded.items():
			remove = set()
			for c in expanded:
				if not op(c):
					remove.add(c)
			expanded -= remove

	def setupListerPars(self):
		lister = self.ownerComp

		# match pars
		pars = self.treeListerComp.customPars
		for p in self.NoPassToListerPars:
			pars.remove(self.treeListerComp.par[p])
		for filter in self.treeListerComp.op(
				'parExec_passToListerBuiltIns').par.pars.eval().split():
			pars += self.ownerComp.pars(filter)
		for p in pars:
			try:
				getattr(lister.par, p.name).val = p.eval()
			except:
				pass

	def exportJSONNode(self, jsonObject):
		children = self.GetObjectChildren(jsonObject)
		if children is not None:
			node = jsonObject.type()
			if isinstance(node, dict):
				for child in children:
					node[child.key] = self.exportJSONNode(child)
			elif isinstance(node, list):
				for child in children:
					node.append(self.exportJSONNode(child))
			return node
		else:
			try:
				return jsonObject.value
			except:
				return jsonObject


	def processJSONNode(self, key, node, prefix=None, pathSeparator=None):
		"""
		recursive function for building JSON info dicts and IDs
		"""
		if prefix is None:
			prefix = tuple()
		if not pathSeparator:
			ID = prefix + (key,)
		else:
			ID = prefix + key
		if isinstance(node, dict):
			value = None
			children = []
			for k, v in node.items():
				children.append( self.processJSONNode(k, v, ID, pathSeparator))
		elif isinstance(node, list):
			value = None
			children = []
			for i, v in enumerate(node):
				children.append( self.processJSONNode(i, v, ID, pathSeparator))
		else:
			value = node
			children = None
		# make tree object and insert info into dicts
		treeObject = self._JSONObj(key, ID, value, type(node), children)
		self.jsonIDObjDict[ID] = treeObject
		self.jsonObjIDDict[id(treeObject)] = ID
		return treeObject

	def buildTreeData(self, objects, parent=None, depth=0, root=None,
					  												hide=False):
		"""
		Recursively add items to treeData, rawData, and convertData.
		objects: a list of objects
		parent: the parent's ID. Roots will have None. (used by recursion)
		depth: how many branches deep (used by recursion)
		root: the tree root this entry is below  (used by recursion)
		hide: don't include this node, but include children
		"""
		objRowData = [self.rowObjectToWorkingData(obj) for obj in objects]
		separator = self.treeListerComp.par.Pathseparator.eval()
		#print(project.pythonStack())
		# debug(objRowData)
		# keyList = None if self.SortCols else [lambda x:x[-1]['__row__']]
		if list(self.SortCols) or self.TreeLister.par.Alphabetizetree:
			self.SortDataRows(objRowData)
		else:
			# sort by input table
			try:
				objRowData.sort(key=lambda x:x[-1]['__row__'])
			except:
				pass
		for row in objRowData:
			try:
				obj = row[-1]
			except:
				continue
			#debug('  '*depth,obj['path'], obj['__children__'])
			id = self.GetIDFromObject(obj)
			if parent is None:
				root = id
			if not hide:
				try:
					wiredChild = bool(obj[self.wirePathColName].count(
																	separator))
				except:
					wiredChild = False
				self.treeDataDict[
						len(self.workingData) + (1 if self.header else 0)] = \
							self._TreeData(parent, root, depth * self.indent,
										   wiredChild)
				self.workingData.append(row)
				childDepth = depth + 1
			else:
				self.ToggleExpand(id, True, root)
				childDepth = depth
			self.visibleIDs[root].add(id)

			# recurse through children
			children = self.GetObjectChildren(obj)
			#print(len(children))
			if children:
				if id in self.Expanded[root]:
					row[1] = '1'
					self.buildTreeData(children, obj, childDepth, root)
				else:
					row[1] = '0'
			else:
				row[1] =  ''
		if self.doAdvancedCallbacks:
			self.DoCallback('onBuildTreeData', {
				'listerExt': self,
				'workingData': self.workingData, 'treeData': self.treeDataDict,
				'about': "Adjust workingData, and treeData in place."})

	# endregion

	# region Promoted Methods

	def Refresh(self, pulseReset=True):
		if self.initialized:
			self.SetError()
		self.wiredOverlayCols = [int(col) for col in
			 	self.customDefine['wiredOverlayCols', 1].val.strip().split()]
		self.wiredOverlayColor = [float(i) for i in
			self.customDefine['wiredOverlayColor', 1].val.strip().split()]
		ListerExt.Refresh(self, pulseReset)

	def RecreateAutoColumns(self):
		self.setupAutoColDefine(True)
		self.ReloadInput()
		#run('args[0].Refresh()', self, delayFrames=1, delayRef=op.TDResources)

	def ReloadInput(self):
		"""
		Reload input JSON or table and refresh tree.
		"""
		self.SetLoadError()
		if self.ownerComp.par.Autodefinecols:
			self.setupAutoColDefine()
		self.json = dict()
		self.jsonIDObjDict = dict()
		self.jsonObjIDDict = dict()
		if self.treeInputDAT.text:
			try:
				if self.treeListerComp.par.Inputmode == 'JSON':
					self.LoadJSON(self.treeInputDAT.text)
				elif self.treeListerComp.par.Inputmode.eval() == \
													'Table_with_"path"_col':
					self.LoadInputWithPathCol(self.treeInputDAT)
				elif self.treeListerComp.par.Inputmode.eval() == \
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols':
					self.LoadInputWithPathCol(self.treeInputDAT, True)
			except:
				import traceback
				print(traceback.format_exc())
				self.SetLoadError("Error loading input. See Textport.")
		if not self.json:
			self.DefaultRoots = []
		try:
			self.DoCallback('onReloadInput', { 'listerExt': self,
					'json': self.json, 'jsonIDObjDict': self.jsonIDObjDict,
					'jsonObjIDDict': self.jsonObjIDDict,
					'defaultRoots': self.DefaultRoots, 'about':
					'Set up json, jsonIDObjDict, jsonObjIDDict in place.'})
		except:
			self.SetLoadError("Error in onReloadInput callback. See Textport.")
		self.FrameRefresh()

	def LoadInputWithPathCol(self, table, useWirePath=False):
		separator = self.treeListerComp.par.Pathseparator.eval()
		if not separator:
			self.SetLoadError(
					'Path Separator parameter required to load input.')
		pathCell = table[0, 'path']
		if pathCell is None:
			self.treeListerComp.SetLoadError('Input has no "path" column.')
		if useWirePath:
			wirePathCell = table[0, 'wirePath']
			self.wirePathColName = 'wirePath'
			if wirePathCell is None:
				wirePathCell = table[0, 'wirepath']
				self.wirePathColName = 'wirepath'
			if wirePathCell is None:
				self.treeListerComp.SetLoadError(
						'Input has no "wirePath" column.')
			parentPathCell = table[0, 'parentPath']
			self.parentPathColName = 'parentPath'
			if parentPathCell is None:
				self.parentPathColName = 'parentpath'
				parentPathCell = table[0, 'parentpath']
			if parentPathCell is None:
				self.treeListerComp.SetLoadError(
						'Input has no "parentPath" column.')
		if not separator or pathCell is None or (useWirePath 
				and (parentPathCell is None or wirePathCell is None)):						
			return
		self.LoadTableWithPathCol(table, separator, useWirePath)

	def LoadTableWithPathCol(self, table, separator, useWirePath=False):
		keys = [c.val for c in table.row(0)]
		numCols = len(keys)
		rows = []
		for index, entry in enumerate(table.rows()):
			if index == 0:
				continue # header
			rowData = {keys[i]:entry[i].val for i in range(numCols)}
			rowData['__row__'] = index
			rowData['__children__'] = dict()
			rows.append(rowData)
		self.LoadDictsWithPathKey(rows, separator, useWirePath)

	def LoadDictsWithPathKey(self, dicts, separator, useWirePath=False):
		def wirePath(d):
			"""
			sort key generator
			"""
			path = d['path']
			wirePath = d[self.wirePathColName]
			nameSeparator = path.rfind(separator)
			return path[:nameSeparator], \
				   '' if wirePath == 'root' else \
					   				(wirePath or path[nameSeparator + 1:]), \
				   path.count(separator)

		if self.treeListerComp.par.Inputmode.eval() == \
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols':
			dicts.sort(key=lambda x: wirePath(x))
		elif self.treeListerComp.par.Numericpath.eval() \
				and self.treeListerComp.par.Inputmode.eval() == \
														'Table_with_"path"_col':
			dicts.sort(key=lambda x:
								[float(f) for f in x['path'].split(separator)])
		else:
			dicts.sort(key=lambda x:
								[f for f in x['path'].split(separator)])

		# debug('checksort')
		# for d in dicts:
		# 	print(d['path'], '-', wirePath(d))

		self.json = dict()
		json = self.json
		rootPath = None
		for d in dicts:
			path = d['path']
			splitPath = path.split(separator)
			name = splitPath[-1]
			if name == '':
				name = separator
			if self.treeListerComp.par.Inputmode.eval() == \
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols':
				parentPath = d[self.parentPathColName] \
							or path[:d['path'].rfind(separator)]
				if parentPath in self.jsonIDObjDict:
					self.jsonIDObjDict[parentPath]['__children__'][path] = d
				else:
					json[path] = d
			else:
				if rootPath is None \
					 			or not path.startswith(rootPath + separator):
					rootPath = path
					json[path] = d
				else:
					segments = path[len(rootPath):].split(separator)[1:-1]
					currDict = json[rootPath]
					for segment in segments:
						if segment in currDict['__children__']:
							currDict = currDict['__children__'][segment]
					currDict['__children__'][name] = d
			self.jsonIDObjDict[path] = d
			self.jsonObjIDDict[id(d)] = path
		self.DefaultRoots = list(self.json.keys())

	def LoadJSON(self, JSON):
		if isinstance(JSON, DAT):
			self.json = TDJSON.datToJSON(JSON)
		elif isinstance(JSON, str):
			self.json = TDJSON.textToJSON(JSON)
		else:
			self.json = JSON
		self.jsonIDObjDict = dict()
		self.jsonObjIDDict = dict()
		self.DefaultRoots = []
		if self.json:
			for k, v in self.json.items():
				treeObject = self.processJSONNode(k, v)
				self.DefaultRoots.append(treeObject.id)

	def CreateJSONObject(self, roots=None):
		if self.treeListerComp.par.Inputmode != 'JSON':
			raise Exception(
					'CreateJSONObject only works when using Input Mode "JSON"')

		if roots is None:
			roots = self.Roots

		jsonObject = type(self.json)()
		for id in roots:
			root = self.jsonIDObjDict[id]
			if isinstance(jsonObject, dict):
				jsonObject[root.key] = self.exportJSONNode(root)
			else:
				jsonObject.append(self.exportJSONNode(root))
		return jsonObject

	def CreateJSONText(self, roots=None):
		return TDJSON.jsonToText(self.CreateJSONObject(roots))

	def ToggleExpand(self, ID, value=None, root=None):
		"""
		Switch the expanded setting of id. Requires a "Refresh()" call to show
		changes.

		Args:
			ID: object ID
			value: if provided, switch to that value
			root: for trees with overlapping roots displayed, you can specify 
				root with this. Otherwise, it will toggle in ALL roots.
		
		Return:
			Value the toggle is set to
		"""
		if root is not None:
			roots = [root]
		else:
			roots = self.Expanded.keys()
		for root in roots:
			rootSet = self.Expanded[root]
			if value is None:
				value = ID not in rootSet
			if value:
				rootSet.add(ID)
			else:
				rootSet.remove(ID)
		return value

	def CollapseAll(self, refresh=False):
		"""
		Collapse all tree branches

		Args:
			refresh: if True, refresh after expanding. Otherwise, a manual call
				to Refresh is required to see changes. Default: False
		"""
		for rootSet in self.Expanded.values():
			rootSet.clear()
		if refresh:
			self.Refresh()

	def ExpandAll(self, refresh=False):
		"""
		Expand all tree branches

		Args:
			refresh: if True, refresh after expanding. Otherwise, a manual call
				to Refresh is required to see changes. Default: False
		"""
		def setChildrenExpanded(id, obj):
			if len(obj['__children__']) > 0:
				self.ToggleExpand(obj['path'])
				for child, childObj in obj['__children__'].items():
					setChildrenExpanded(child, childObj)

		for id, obj in self.json.items():
			setChildrenExpanded(id, obj)
		if refresh:
			self.Refresh()

	def GetObjectChildren(self, obj):
		"""
		Get a tree object's children

		:param obj: the tree object
		:return: object's children
		"""
		if self.json:
			if hasattr(obj, 'children'):
				jsonChildren = obj.children
			else:
				try:
					jsonChildren = obj['__children__'].values()
				except:
					jsonChildren = None
		else:
			jsonChildren = None
		returnDict = self.DoCallback('getObjectChildren', {
						'jsonChildren': jsonChildren,
						'object': obj, 'listerExt': self, 'about':
						'Return a list of child objects.'})
		if returnDict and returnDict.get('returnValue', None) is not None:
			return returnDict['returnValue']
		elif jsonChildren is not None:
			return jsonChildren

	def GetObjectFromID(self, ID):
		"""
		Get object from tree ID.

		:param ID: Unique object identifier used by tree
		:return: row object or None if not found
		"""
		try:
			jsonObject = self.jsonIDObjDict[ID]
		except:
			jsonObject = None
		returnDict = self.DoCallback('getObjectFromID', {
						'jsonObject': jsonObject,
						'id': ID, 'listerExt': self, 'about':
						'Return the tree object identified by the given id.'})
		if returnDict and returnDict.get('returnValue', None):
			return returnDict['returnValue']
		elif jsonObject is not None:
			return jsonObject
		else:
			raise IndexError('getObjectFromID callback must return object.\n'
							'	Sent ID: ' + str(ID))

	def GetIDFromObject(self, obj):
		"""
		Get unique tree ID from object

		:param obj: row object
		:return: unique tree ID for object or None if not found
		"""
		try:
			jsonID = self.jsonObjIDDict[id(obj)]
		except:
			jsonID = None
		returnDict = self.DoCallback('getIDFromObject', {
						'jsonID': jsonID,
						'object': obj, 'listerExt': self, 'about':
						'Return the id associated with given tree object.'
						'Return None if it has no unique ID.'})
		if returnDict and returnDict.get('returnValue', None):
			return returnDict['returnValue']
		elif jsonID:
			return jsonID
		else:
			raise IndexError('getIDFromObject callback must return ID.\n'
							'	Sent object: ' + str(obj))

	def SetError(self, error=''):
		"""
		Add script error to tree lister

		:param error: error to set or '' to clear script errors
		"""
		if error == '':
			self.treeListerComp.clearScriptErrors(error='TreeLister:*')
		else:
			self.treeListerComp.addScriptError("TreeLister: " + error)
			print(self.ownerComp.path + ":", error)

	def SetLoadError(self, error=''):
		"""
		Add load script error to tree lister

		:param error: error to set or '' to clear load script errors
		"""
		if error == '':
			self.treeListerComp.clearScriptErrors(error='TreeLister Load:*')
		else:
			self.treeListerComp.addScriptError("TreeLister Load: " + error)
			print(self.ownerComp.path + " Load Error:", error)			

	def OpenToPath(self, path, doRefresh=True):
		"""
		Open tree to the provided path. Only works in "path" col modes.

		:param path: The path to open to.
		:param doRefresh: If True, call Refresh() after expanding items.
		:return: True if successful, root opened in if already open, otherwise
				None.
		"""
		if self.treeListerComp.par.Inputmode.eval() in ['Table_with_"path"_col',
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols']:
			# check to see if already open
			separator = self.treeListerComp.par.Pathseparator.eval()
			testPath, sep, tail = path.rpartition(separator)
			for root, expanded in self.Expanded.items():
				if testPath in expanded or path == root:
					return root
			# open to path
			for root in self.Roots:
				if path.startswith(root):
					self.ToggleExpand(root, True)
					while path != root:
						path, sep, tail = path.rpartition(separator)
						self.ToggleExpand(path, True, root)
					if doRefresh:
						self.Refresh()
					return True
		else:
			raise Exception("OpenToPath only allowed in "
							"\"path\" col' modes.")


	def FromPathGetRowNum(self, path, startRow=0):
		"""
		Get the row number with the given path. Only works in "path"
		col modes. Return None if row object is not currently visible.

		:param path: The object's path
		:param startRow: Start the search at this row. Default: 0.
		:return: The first visible row number for that path
		"""
		if self.treeListerComp.par.Inputmode.eval() in ['Table_with_"path"_col',
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols']:
			for i, row in enumerate(self.Data[startRow:]):
				if row['rowObject'] and (row['rowObject']['path'] == path):
					return i
			return None
		else:
			raise Exception("FromPathGetRowNum only allowed in "
							"\"path\" col modes.")

	def FromPathsSelectRows(self, paths, addSelection=False, expand=True):
		"""
		Select the rows with the provided paths. Tree can be expanded to
		selected paths. Only works in "path" col modes. Any paths
		not found will be ignored and returned.

		:param paths: a list of path strings matching paths in the input table
		:param addSelection: if True, add to current selection. Default: False
		:param expand: if True, expand tree to display selected paths. 
			Otherwise, only visible paths will be selected.

		:return: list of paths that were not found
		"""
		if self.treeListerComp.par.Inputmode.eval() in ['Table_with_"path"_col',
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols']:
			needsRefresh = False
			if expand:
				for p in paths:
					if self.OpenToPath(p, False) == True:
						needsRefresh = True
			if needsRefresh:
				self.Refresh()
			notFound = []
			rowObjects = []
			for path in paths:
				row = self.FromPathGetRowNum(path)
				if row is not None:
					rowObjects.append(self.Data[row]['rowObject'])
				else:
					notFound.append(path)
			if needsRefresh:
				run('op("' + self.ownerComp.path + '").FromPathsSelectRows(' +
						str(paths) + ', ' + str(addSelection) + 
						', expand=False)',
						delayFrames=2, delayRef=op.TDResources)
			else:
				self.SelectObjects(rowObjects, addSelection)
			return notFound
		else:
			raise Exception("FromPathsSelectRows only allowed in "
							"\"path\" col modes.")

	@property
	def SelectedPaths(self):
		"""
		All selected paths. Only works in "path" col modes.

		:return: list of selected paths
		"""
		if self.treeListerComp.par.Inputmode.eval() in ['Table_with_"path"_col',
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols']:
			return [rowObject['path'] for rowObject in self.SelectedRowObjects]
		else:
			raise Exception("SelectedPaths only works in "
							"\"path\" col modes.")

	def setupRefreshIcon(self):
		attribs = self.ownerComp.cellAttribs[0,1]
		attribs.help = 'Click To Refresh'
		attribs.fontFace = 'Material Design Icons'
		attribs.textOffsetX = 1
		attribs.textOffsetY = 0
		attribs.fontBold = True
		attribs.fontSizeX = self.ownerComp.Looks['header']['fontSizeX'] * 1.5
		attribs.text = eval(self.customDefine['refreshChar', 'Data'].val)

	# endregion

	# region Properties

	@property
	def Roots(self):
		if self.treeListerComp.par.Usedefaultroots.eval():
			roots = self.DefaultRoots
		else:
			roots = tdu.split(self.treeListerComp.par.Roots.eval())
		return roots

	@property
	def SelectedInputTableRows(self):
		if self.treeListerComp.par.Inputmode.eval() in ['Table_with_"path"_col',
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols']:
			try:
				return [self.Data[r]['rowObject']['__row__']
											for r in sorted(self.SelectedRows)]
				
				# selectedIDs = [self.GetIDFromObject(self.Data[r]['rowObject'])
				# 									for r in self.SelectedRows]
				# pathCol = self.treeInputDAT[0, 'path'].col
				# return [r for r in range(self.treeInputDAT.numRows)
				# 				if self.treeInputDAT[r, pathCol] in selectedIDs]
			except:
				return []
		else:
			return []

	# endregion

	# region Overrides

	def restorePreviousSelection(self, oldData, oldSelectedRows):
		for oldRow in oldSelectedRows:
			rowData = None
			try:
				rowData = oldData[oldRow]
				oldPath = rowData['rowObject']['path']
				if self.Data[oldRow]['rowObject']['path'] == oldPath:
					newRowNum = oldRow
				else:
					newRowNum = self.FromPathGetRowNum(oldPath)
				if newRowNum is not None:
					self._SelectedRows.val.append(newRowNum)
					self._SelectedRows.modified()
				else:
					raise Exception
			except:
				if rowData:
					self.DoCallback('onRemovedSelectedRow',
									{'row': oldRow, 'rowData': rowData})

	def GetRawData(self):
		ListerExt.GetRawData(self)
		self.AutoSort = False
		self.indent = int(self.customDefine['indentWidth',1])
		roots = self.Roots
		if not self.rawData:
			self.rawData = []
			self.workingData = []
			self.treeDataDict = dict()
			self.visibleIDs = {root:set() for root in roots}
			# reset Expanded dicts
			for r in roots:
				if r not in self.Expanded:
					self.Expanded[r] = set()
				try:
					self.GetObjectFromID(r)
				except:
					self.SetError('Invalid root ID: ' + r)
					import traceback; print(traceback.format_exc())
					return
			# do processing
			self.buildTreeData(
							[self.GetObjectFromID(r) for r in roots],
							hide=not self.treeListerComp.par.Showroots.eval())
			# delete invalid Expanded keys
			if self.initialized:
				for r in list(self.Expanded.keys()):
					if r not in roots and r in self.Expanded:
						try:
							del self.Expanded[r]
						except:
							# timing problem with expanded + filter change
							pass
				# close hidden items
				for root, rootSet in self.Expanded.items():
					for ID in list(rootSet):
						if root in self.visibleIDs:
							if ID not in self.visibleIDs[root]:
								self.ToggleExpand(ID, False, root)
						else:
							try:
								del self.Expanded[root]
							except:
								pass

	def rowObjectToWorkingData(self, rowObject):
		convertedRow = ListerExt.rowObjectToWorkingData(self, rowObject)
		for i, dataCell in enumerate(self.colDefine.row('sourceDataMode')[1:]):
			if dataCell.val == 'id':
				convertedRow[i] = self.GetIDFromObject(rowObject)
		return convertedRow

	def setupAutoColDefine(self, clear=False):
		self.autoHeader = True
		if clear:
			ListerExt.setupAutoColDefine(self, True)
			return
		if self.treeListerComp.par.Inputmode.eval() in ['Table_with_"path"_col',
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols']:
			self.autoColDefine.text = self.tableAutoColDefine.text
			# defer to name but use path if we must
			labelCol = 'name'
			if not self.treeInputDAT.col('name'):
				labelCol = 'path'
			self.autoColDefine['sourceData', 'Name'] = labelCol
			self.autoColDefine['column', 'Name'] = labelCol.capitalize()
			# add all other cols
			insertAt = 4
			sourceCol = self.autoColDefineDefaults.col(1)
			rowDict = {c.val: c.row for c in self.tableAutoColDefine.col(0)}
			for col in self.treeInputDAT.cols():
				if col[0].val == labelCol:
					continue
				self.autoColDefine.insertCol([c.val for c in sourceCol],
											 insertAt)
				defCol = self.autoColDefine.col(insertAt)
				defCol[rowDict['column']].val = col[0].val.capitalize()
				defCol[rowDict['sourceData']].val = col[0].val
				defCol[rowDict['cellLook']].val = ''
				insertAt += 1
		else:
			self.autoColDefine.text = self.jsonAutoColDefine.text
		columns = [c.val for c in
				   self.autoColDefine.row('column')[1:]]
		self.columnDict = dict((columns[i], i) for i in range(len(columns)))
		self.colNumDict = {v: k for k, v in self.columnDict.items()}
		self.colDefine = self._colDefine.val = self.autoColDefine

	# def SelectColumn(self, col):
	# 	ListerExt.SelectColumn(self, col)
	# 	self.Refresh()

	def InitCell(self, row, col):
		ListerExt.InitCell(self, row, col)
		rowObject = self.Data[row]['rowObject']
		if type(rowObject) == self._JSONObj \
					and self.colDefine['sourceData', col+1].val == 'value' \
					and rowObject.children is not None:
			self.ownerComp.cellAttribs[row,col].editable = 0
		if row == 0 and col == 1 and self.ownerComp.par.Header:
			self.ownerComp.cellAttribs[row,col].rightBorderOutColor = [0,0,0,0]
			if self.treeListerComp.par.Clickcornertorefresh:
				self.setupRefreshIcon()

	def InitRow(self, row, stripingOnly=False):	
		ListerExt.InitRow(self, row, stripingOnly)
		if self.header and row == 0:
			return
		if row in self.treeDataDict: # filter change timing check
			treeInfo = self.treeDataDict[row]
			self.ownerComp.rowAttribs[row].rowIndent = treeInfo.indent
			if self.treeListerComp.par.Inputmode.eval() == \
						'Table_with_"path",_"wirePath",_and_"parentPath"_cols' \
					and treeInfo.wiredChild:
				for col in self.wiredOverlayCols:
				   self.SetCellOverlay(row, col, self.wiredOverlayColor)
			else:
				for col in self.wiredOverlayCols:
					self.RemoveOverlay(row, col, 50)

		if self.doAdvancedCallbacks:
			self.DoCallback('onTreeInitRow', {'row': row})

	def RollCell(self, row, col, on=True):
		# unroll the cell if we're rolling over an empty expando
		if col == 1 and not self.expando(row) \
										and (not self.header or row > 0):
			on = False
		ListerExt.RollCell(self, row, col, on)
		if row == 0 and col == 1 and self.ownerComp.par.Header and \
								self.treeListerComp.par.Clickcornertorefresh:
			look = 'headerRoll'
			doCallbacks = self.doAdvancedCallbacks
			if on:
				self.SetCellLook(row, col, look, True,
						ROLLOVERLAYER, doCallback=doCallbacks)
				self.setupRefreshIcon()
			else:
				self.RemoveOverlay(row, col, ROLLOVERLAYER)
				self.SetCellLook(row, col, None, look,
						ROLLOVERLAYER, doCallback=doCallbacks)
				self.setupRefreshIcon()

	def PressCell(self, row, col):
		if row == 0 and col == 1 and self.ownerComp.par.Header and \
								self.treeListerComp.par.Clickcornertorefresh:
			self.SetCellLook(row, col, 'headerPress', True,
						ROLLOVERLAYER, self.doAdvancedCallbacks)
			self.setupRefreshIcon()
		# don't press if we're pressing an empty expando
		elif col == 1 and not self.expando(row) \
									and (not self.header or row > 0):
			return
		else:
			ListerExt.PressCell(self, row, col)

	def Click(self, row, col):
		# don't press if we're pressing an empty expando
		if col == 1 and self.Data[row]['Expando'] is not None and \
								(not self.header or row > 0):
			root = self.treeDataDict[row].root
			id = self.GetIDFromObject(self.Data[row]['rowObject'])
			self.ToggleExpand(id, root=root)
			self.FrameRefresh()
		ListerExt.Click(self, row, col)
		if row == 0 and col == 1 and self.ownerComp.par.Header and \
								self.treeListerComp.par.Clickcornertorefresh:
			self.Refresh()

	def SetCellText(self, row, col, text, outTableSync=True):
		rowObject = self.Data[row]['rowObject']
		if type(rowObject) == self._JSONObj \
					and self.colDefine['sourceData', col+1].val == 'value' \
					and rowObject.children is not None:
			text = ''
		ListerExt.SetCellText(self, row, col, text, outTableSync)

	def onEdit(self, row, col, val, addUndo=True):
		ListerExt.onEdit(self, row, col, val, addUndo)
		rowObject = self.Data[row]['rowObject']
		if type(rowObject) == self._JSONObj \
					and self.colDefine['sourceData', col+1].val == 'value':
			attribs = self.ownerComp.cellAttribs[row, col]
			text = attribs.text
			try:
				val = rowObject.type(text)
			except:
				try:
					val = eval(text)
				except:
					val = text
			rowObject.value = val

	def onSelect(self, startrow, startcol, startcoords, endrow, endcol,
													endcoords, start, end):
		if startcol == 1 and not self.expando(startrow) \
										and (not self.header or startrow > 0):
			startcol = 0
		if endcol == 1 and not self.expando(startrow) \
										and (not self.header or endrow > 0):
			endcol = 0
		ListerExt.onSelect(self, startrow, startcol, startcoords, endrow,
						   					endcol, endcoords, start, end)

	def fixConfig(self):
		"""
		Use the Data in configDefault comp to update Data in the clone-
			protected config comp
		"""
		self.treeDefaultConfig = self.treeListerComp.op('configDefault')
		for expandoLook in ('expandoPress', 'expandoRoll', 'expando'):
			if self.configComp.op(expandoLook) is None:
				n = self.configComp.copy(self.defaultConfig.op(expandoLook))
				TDF.arrangeNode(n, 'left')
		ListerExt.fixConfig(self)
		# fix define table
		defineTable = self.configComp.op('define')
		if defineTable:
			for i,row in enumerate(self.treeDefaultConfig.op('define').rows()):
				rowName = row[0].val
				try:
					defineTable[rowName, 0].val
				except:
					defineTable.insertRow(row, i)	
		# fix extra autocoldefines
		defaultOp = self.defaultConfig.op('colDefine')
		for colDefine in [self.jsonAutoColDefine,
							self.tableAutoColDefine]:
			if colDefine:
				for i, row in enumerate(defaultOp.rows()):
					rowName = row[0].val
					try:
						colDefine[rowName, 0].val
					except: 
						colDefine.insertRow([rowName] +
								[defaultOp[rowName, 1]]
										* (colDefine.numCols - 1), i)
			

	def expando(self, row):
		"""
		Return value of Expando for the given row
		"""
		return self.Data[row]['Expando']
	# endregion

	# region Callbacks

	def OnParValueChange(self, par, val, prev):
		if par.name in ['Usedefaultroots', 'Roots', 'Showroots',
						'Clickcornertorefresh', 'Sortcols', 'Sortreverse',
						'Alphabetizetree']:
			self.Refresh()
		elif par.name in ['Pathseparator', 'Inputmode', 'Numericpath',
							'Autodefinecols', 'Usesortindicatorchars']:
			self.ReloadInput()
		elif par.name in ['Header', 'Clickableheader'] \
									and self.ownerComp.par.Autodefinecols:
			self.SelectedRows = []
			if par.name == 'Clickableheader' and prev != 'Off':
				self.SelectColumn(None)
				self.ownerComp.par.Sortcols = ''
				self.ownerComp.par.Filtercols = ''
			ListerExt.setupAutoColDefine(self, True)
			self.setupAutoColDefine()
			self.Refresh()
		else:
			ListerExt.OnParValueChange(self, par, val, prev)

	def OnParPulse(self, par):
		if par.name == 'Collapseall':
			self.CollapseAll(True)
		if par.name == 'Expandall':
			self.ExpandAll(True)
		elif par.name == 'Reloadinput':
			self.ReloadInput()
		elif par.name == 'Helppage':
			ui.viewFile('https://docs.derivative.ca/index.php?'
						'title=Palette:treeLister')
		else:
			ListerExt.OnParPulse(self, par)

	# endregion

	pass