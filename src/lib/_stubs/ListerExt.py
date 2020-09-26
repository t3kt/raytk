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


#from operator import dataRowgetter
import functools
import copy
import re
import collections
import collections.abc
import sys
import traceback
import ast
from itertools import groupby
from CallbacksExt import CallbacksExt
from distutils.version import LooseVersion

TDF = op.TDModules.mod.TDFunctions

ROWSTRIPELAYER = 30
CELLOVERLAYER = 50
ROLLOVERLAYER = 60
SELECTOVERLAYER = 70
COLLOOKOVERLAYER = 65
ROWOVERLAYER = 45
COLOVERLAYER = 40
RANGEOVERLAYER = 100
COLORDATALAYER = 10

NONCELL = (-1, None) # values that indicate a non-cell value from callback

SYNCABLEDATAMODES = ['int', 'float', 'string', 'version', 'blank', 'color']

class ListerExt (CallbacksExt):

	# region main

	def __init__(self, ownerComp):
		# config stuff
		self.ownerComp = ownerComp
		self.configComp = ownerComp.par.Configcomp.eval()
		if self.configComp is None:
			raise Exception("Invalid Config Comp (see Advanced parameter page)")
		self.colDefine = None # non-dependable for speed
		self._colDefine = tdu.Dependency(None) # dependable for promotion
		self.customDefine = self.configComp.op('define')
		self.defaultConfig = ownerComp.op('configDefault')
		self.inputTable = self.ownerComp.op('inputTableFinal')
		self.autoColDefine = self.ownerComp.op('autoColDefine')
		self.outLinked = self.ownerComp.op('outLinked')
		self.linkedTable = None # chosen in parameter. Set in Refresh
		self.settings = self.configComp.op('settings')
		self.callbackDat = self.ownerComp.par.Callbackdat.eval()
		try:
			self.fixConfig()
		except:
			# do our best to fix stuff for users, but sometimes they have
			# made changes beyond simple updates...
			pass
		self.header = self.ownerComp.par.Header.eval() \
					  					and self.ownerComp.par.Header.enable
		self.AutoFilter = True  # do automated filtering behavior of Data
		self.AutoSort = True  # built in sorting behavior
		self.selectedCol = None

		# Data
		self.rawData = []  # all Data available
		self.workingData = []  # post filter, post sort Data
		self.Data = ()  # final Data, laid out in an OrderedDictionary
		self.columnDict = {}  # column: colnum... helper for callbacks
		self.colNumDict = {} # colnum: column... another helper
		self.loadLooks()
		self.overlays = {}  # Overlays are stored in the form:
			# {(row, col): {'overlays': [overlaycolor,...], 'original': bgcolor}
		self.cellLookNames = {} # Individually set cell look names in the form:
			# {(row, col): look Name}
		self.cellTopPaths = {} # Individually set cell TOP paths in the form:
			# {(row, col): TOP path}

		# state
		self.rolledRow = None
		self.rolledCell = None
		self.initialized = False
		self.doClick = True # for aborting click actions
		self._clickedOnce = False # for setting up doubleclick
		self.ButtonDown = None # which button is currently down, if any
		self.DropInfo = None # info to be viewed by whatever one of my cells
								# is dropped into
		self.autoHeader = False # header created from colDefine
		self.holdRun = None  # delayed command for mouse hold
		self._SelectedRows = tdu.Dependency()
		self._SelectedRows.val = []
		self.dropHighlightInfo = None # current dropHighlight info
		self.dragToRow = None # the row we are dragging to
		self.dragRowColors = None # stores previous color info
		self.doAdvancedCallbacks = self.ownerComp.par.Advancedcallbacks.eval()
		# mouse-down trackers
		self.lastCellSelect = None # last cell rolled over with mouse done
		self.holdCell = None # cell to test for mouse hold
		self.selectedCell = None # cell selected for clicking
		self.skipSetCellCallback = False

		TDF.createProperty(self, 'nRows', 0, dependable=True)
		TDF.createProperty(self, 'nCols', 0,  dependable=True)
		self.ownerComp.par.rows = 0
		self.ownerComp.par.cols = 0
		self.ownerComp.par.rows.expr = \
							'ext.ListerExt.nRows if me.extensionsReady else 0'
		self.ownerComp.par.cols.expr = \
							'ext.ListerExt.nCols if me.extensionsReady else 0'

		# anything that could fail needs to be in try/except so that the
		# extension is guaranteed to init
		# set up callbacks
		try:
			CallbacksExt.__init__(self, ownerComp)
		except:
			self.ownerComp.addScriptError(traceback.format_exc() + \
					"Error in CallbacksExt __init__. See textport.")
			print()
			print("Error initializing callbacks - " + self.ownerComp.path)
			print(traceback.format_exc())
		try:
			self.DoCallback('onInit', {'listerExt':self})
		except:
			self.ownerComp.addScriptError(traceback.format_exc() + \
					"Error in custom onInit callback. See textport.")
			print(traceback.format_exc())
		try:
			self.setupAutoColDefine(clear=True)
		except:
			self.ownerComp.addScriptError(traceback.format_exc() + \
					"Error setting up auto column define. See textport.")
			print(traceback.format_exc())
		try:
			self.Refresh()
		except:
			pass
			self.ownerComp.addScriptError(traceback.format_exc() +
								   "Error in initial Refresh. See textport.")
			print(traceback.format_exc())
		self.SelectedRows = []
		run("op(" + str(ownerComp.id) + ").PostInit() "
				"if op(" + str(ownerComp.id) + ") and "
				"hasattr(op(" + str(ownerComp.id) + "), 'PostInit') else None",
				delayFrames=1, delayRef=op.TDResources) # scrollbar reset

		# DEBUG print('Lister init done')
		# import traceback; traceback.print_stack()

	def PostInit(self):
		# cheap version update
		if self.ownerComp.par.enablecloning.eval() and \
							self.ownerComp.par.clone.eval():
			self.ownerComp.par.Version = \
							self.ownerComp.par.clone.eval().par.Version.eval()
		self.initialized = True
		self.ownerComp.par.reset.pulse()
		#self.ownerComp.scroll(0,0)
		self.DoCallback('onPostInit', {'listerExt': self})

	def Refresh(self):
		"""
		Re-init table, refreshing all Data and formatting all cells
		"""
		# debug('Refresh', me)

		# parameters
		self.header = self.ownerComp.par.Header.eval() \
					  					and self.ownerComp.par.Header.enable
		self.linkedTable = self.ownerComp.par.Linkedtable.eval()
		if self.initialized:
			self.ownerComp.op('table_autoHeader').cook(force=True)
		if self.linkedTable:
			self.ownerComp.op('linkedWatcher').cook(force=True)
			self.ownerComp.op('linkedSyncer').cook(force=True)

		# store info about selections and Data before we change all the Data
		oldData = self.Data # self.Data recreated in self.GetRawData
		oldSelectedRows = self.SelectedRows

		# pre-set reference dicts if possible
		if not self.ownerComp.par.Autodefinecols.eval():
			# set up column info for later use
			self.colDefine = self._colDefine.val = \
												self.configComp.op('colDefine')
			if self.colDefine is None:
				raise Exception('No colDefine table found in config comp!')
			columns = [c.val for c in self.colDefine.row('column')[1:]]
			self.columnDict = dict((columns[i], i) for i in range(len(columns)))
			self.colNumDict = {v: k for k, v in self.columnDict.items()}
			self.setupAutoColDefine(clear=True)

		# get rawdata
		self.GetRawData()
		# set up coldefine
		if self.ownerComp.par.Autodefinecols.eval():
			self.colDefine = self._colDefine.val = \
											self.autoColDefine
			self.setupAutoColDefine()
			columns = [c.val for c in self.colDefine.row('column')[1:]]
			self.columnDict = dict((columns[i], i) for i in range(len(columns)))
			self.colNumDict = {v: k for k, v in self.columnDict.items()}

		# process workingData
		self.ConvertData()
		self.Filter()

		if self.header and self.autoHeader:
			defaultHeaders = []
			for i, columnLabel in enumerate(self.colDefine.row('columnLabel')):
				# skip first col
				if i == 0:
					continue
				if columnLabel != '*':
					headerText = columnLabel  # anything but asterisk
				else:
					# other types use 'column'
					headerText = self.colDefine['column', i].val
				defaultHeaders.append(headerText)
			defaultHeaders.append(None)
			self.workingData.insert(0, defaultHeaders)

		# create Data as list of OrderedDicts
		self.Data = []
		for i, d in enumerate(self.workingData):
			formattedData = self.WorkingDataToDataRow(d)
			self.Data.append(formattedData)

		self.nRows = len(self.Data)
		self.nCols = self.colDefine.numCols - 1
		self.Sort(False)
		self._SelectedRows.val = []
		self.restorePreviousSelection(oldData, oldSelectedRows)
		self.ownerComp.par.Selectedrows.val = listToParString(
														self._SelectedRows.val)

		self.DataChanged()
		# callback
		self.DoCallback('onRefresh', {'listerExt': self})

	def restorePreviousSelection(self, oldData, oldSelectedRows):
		for oldRow in oldSelectedRows:
			rowData = None
			try:
				rowData = oldData[oldRow]
				oldRowObject = rowData['rowObject']
				if self.Data[oldRow]['rowObject'] == oldRowObject:
					newRowNum = oldRow
				else:
					newRowNum = self.GetObjectRowNum(oldRowObject)
				if newRowNum is not None:
					self._SelectedRows.val.append(newRowNum)
					self._SelectedRows.modified()
				else:
					raise Exception
			except:
				if rowData:
					self.DoCallback('onRemovedSelectedRow',
									{'row': oldRow, 'rowData': rowData})

	# DEBUG print('refresh end')

	# endregion

	###########################################################################
	# region table manipulation

	def MoveRows(self, rowList, destination):
		"""
		Move Data rows in rowList to the destination index, preserving order.
		Rows must be contiguous and dest cannot be in rows.
		"""
		# check for contiguous
		if set(rowList) != set(range(min(rowList),
									 min(rowList) + len(rowList))):
			print("MoveRows rowList must be contiguous")
			return
		rowList = list(rowList)
		rowList.sort(reverse=True)
		offset = 0
		dest = destination
		for rownum in rowList:
			self.Data.insert(dest, self.Data.pop(rownum + offset))
			if destination > rownum:
				dest -= 1
			else:
				offset += 1
		# select moved rows
		destAdjust = 1 - len(rowList) if destination > rowList[0] else 0
		self.SelectedRows = list(range(destination + destAdjust,
									   destination + len(rowList) + destAdjust))
		# DEBUG print('MoveRows', rowList, destination)
		self.DoCallback('onMoveRows', {'rowList': rowList,
									'destination': destination})
		self.DataChanged()

	def undoMoveRows(self, isUndo, info):
		"""
		info: rowList, destination
		"""
		if isUndo:
			if info[1] > info[0][0]:
				moveRows = range(info[1] - len(info[0]) + 1, info[1] + 1)
				destination = min(info[0])
			else:
				moveRows = range(info[1], info[1] + len(info[0]))
				destination = max(info[0])
			self.MoveRows(moveRows, destination)
		else:
			self.MoveRows(info[0], info[1])

	def DeleteRows(self, rows, addUndo=True):
		"""
		Delete a list of rows.
		"""
		if addUndo and self.ownerComp.par.Allowundo:
			ui.undo.startBlock(
							'Delete Rows - ' + self.ownerComp.path)
			ui.undo.addCallback(self.undoDeleteRows,
					[(r, self.Data[r]) for r in rows])
			ui.undo.endBlock()		
		if len(set(rows)) != len(rows):
			raise Exception(self.ownerComp.path + ' - DeleteRows: rows argument'
												  ' cannot contain duplicates')
		rowData = []
		for row in reversed(sorted(rows)):
			if row >= self.nRows:
				continue
			rowData.append(self.Data.pop(row))

		selectedRows = self.SelectedRows
		# fix selections:
		for i, selectRow in enumerate(selectedRows):
			# remove from selected if we deleted the row
			if selectRow in rows:
				# roundabout assignment to keep property up to date
				selectedRows.remove(selectRow)
				continue
			# adjust value if we deleted rows above it
			newval = selectRow - len([r for r in rows if r < selectRow])
			selectedRows[i] = newval
		self.SelectedRows = selectedRows
		self.DoCallback('onDeleteRows', {'rows': rows, 'rowData': rowData})
		self.DataChanged()

	def undoDeleteRows(self, isUndo, info):
		"""
		info: [(rowNum, rowData)]
		"""
		if isUndo:
			info.sort(key=lambda x: x[0])
			for i in info:
				self.AddRow(i[0], i[1])
			self.SelectedRows = [i[0] for i in info]
		else:
			self.DeleteRows([i[0] for i in info], addUndo=False)

	def AddRow(self, rowNumber=None, rowData=None, rowObject='__no__object__',
			   rowDict=None, addUndo=True):
		"""
		Add a row to lister data

		Args:
			rowNumber: where to insert the row. None (default) appends it.
			rowData: a full row data dictionary including all cols and
				'rowObject' key
			rowObject: a rowObject to be processed by RowObjectToDataRow.
				Ignored if rowData is provided.
			rowDict: a dictionary of colName:data to fill row. Missing columns
				will be blank. None	(default) will create a blank row. Ignored
				if rowObject or rowData is provided.
			addUndo: if True, add an undo step for this

		Returns:
			rowData
		"""
		if rowNumber is None:
			rowNumber = self.nRows
		if rowNumber == 0 and self.header:
			raise Exception('Unable to AddRow before header - '
														+ self.ownerComp.path)
		callbackInfo = {'rowObject': None, 'rowDict': None}
		if rowData is not None:
			formattedData = collections.OrderedDict()
			for c in range(self.nCols):
				colName = self.colNumDict[c]
				formattedData[colName] = rowData[colName]
		elif rowObject != '__no__object__':
			formattedData = self.RowObjectToDataRow(rowObject)
			callbackInfo['rowObject'] = rowObject
		else:
			if rowDict is None:
				rowDict = {}
			formattedData = collections.OrderedDict()
			for c in range(self.nCols):
				colName = self.colNumDict[c]
				formattedData[colName] = rowDict.get(colName, '')
			formattedData['rowObject'] = rowDict
			callbackInfo['rowDict'] = rowDict
		callbackInfo.update({'row': rowNumber, 'rowData': formattedData})
		self.Data.insert(rowNumber, formattedData)
		self.DoCallback('onAddRow', {'row': rowNumber,
									 'rowData': formattedData})
		self.DataChanged()
		if addUndo and self.ownerComp.par.Allowundo:
			ui.undo.startBlock('Add Row (' + str(rowNumber) + ') - '
							   					+ self.ownerComp.path)
			ui.undo.addCallback(self.undoAddRow, (rowNumber, rowData, rowObject,
			   										rowDict))
			ui.undo.endBlock()
		return formattedData

	def undoAddRow(self, isUndo, info):
		if isUndo:
			self.DeleteRows([info[0]], addUndo=False)
		else:
			self.AddRow(*info, False)

	def DataChanged(self, selectionObjects=None):
		"""
		Call this when you change the Lister's Data. Refreshes text and size.
		Does not get raw Data, convert Data, sort or filter.
		selectionObjects will be selected if present in rowObjects
		"""
		# DEBUG print ('DataChanged', len(self.Data), self.Data)
		self.nRows = len(self.Data)
		self.nCols = self.colDefine.numCols - 1
		self.doClick = False
		self.rolledCell = None
		if selectionObjects is not None:
			self.SelectObjects(selectionObjects)
		self.DoCallback('onDataChanged')
		self.resetOwner()

	def resetOwner(self):
		# debug ("resetOwner")
		if self.initialized:
			self.ownerComp.par.reset.pulse()
		self._clickedOnce = False
		nRows = self.nRows - self.AutoHeaderRows
		if self.ownerComp.par.Inputtablehasheaders:
			nRows += 1
		for table in self.OutTables:
			table.setSize(nRows, self.nCols)
		syncTable = self.SyncTable
		if syncTable:
			syncTable.setSize(nRows, syncTable.numCols)


	def onEdit(self, row, col, val, addUndo=True):
		# DEBUG print ("onEdit", row, col, val, me.time.frame)
		attribs = self.ownerComp.cellAttribs[row, col]
		prevText = attribs.text
		# text
		mode = self.colDefine["sourceDataMode", col+1].val
		if mode == 'repr':
			try:
				newval = ast.literal_eval(val)
			except:
				pass
			newval = repr(newval)
		elif mode == 'int':
			try:
				newval = ast.literal_eval(val)
				newval = int(newval)
			except:
				return
		elif mode == 'float':
			try:
				float(val)
				newval = val
			except:
				return
		else:
			newval = val
		self.SetCellText( row, col, newval)
		# callback
		self.DoCellCallback("onEditEnd", row, col, {'prevText': prevText,
													'text': val,
													'rowData': self.Data[row]})
		if addUndo and self.ownerComp.par.Allowundo:
			ui.undo.startBlock('Edit Cell Text (' + str(row) + ',' +
							   str(col) +') - ' + self.ownerComp.path)
			ui.undo.addCallback(self.undoCellEdit, (row, col, prevText, val))
			ui.undo.endBlock()

	def undoCellEdit(self, isUndo, info):
		"""
		info: row, col, prevText, newText
		"""
		self.onEdit(info[0], info[1], info[2] if isUndo else info[3], False)

	def onLinkedCellChange(self, dat, cells, prev):
		for c in cells:
			cellRow = c.row + self.AutoHeaderRows
			if self.ownerComp.par.Inputtablehasheaders:
				if c.row == 0:
					continue
				cellRow -= 1
			if cellRow < self.nRows and c.col < self.nCols:
				if c.val != self.ownerComp.cellAttribs[cellRow, c.col]:
					self.SetCellText(cellRow, c.col, c.val, False)

	def onLinkedSizeChange(self, dat):
		# this is really for rows only... column changes should not be real time
		if self.nRows - self.AutoHeaderRows != dat.numRows:
			self.Refresh()

	# endregion

	###########################################################################
	# region Data processing

	def RowObjectToDataRow(self, rowObject):
		workingDataRow = self.rowObjectToWorkingData( rowObject)
		return self.WorkingDataToDataRow(workingDataRow)

	def WorkingDataToDataRow(self, workingData):
		"""
		Convert a list of data to an OrderedDict keyed by column names from
		colDefine. Original rowObject will be appended
		"""
		stringData = workingData[:-1]
		try:
			return collections.OrderedDict(
						[(self.colNumDict[i], stringData[i]) \
										for i in range(len(self.colNumDict))]
					+ [('rowObject', workingData[-1])]) # add rowObject
		except Exception as e:
			raise ValueError("Data doesn't match column definitions in row.\n"\
					"Cols: " + str([c.val for c in
									self.colDefine.row('column')[1:]]) + '\n'\
					"Data: " + str(workingData[:-1])) from e

	def GetRawData(self):
		"""
		Set up raw Data for Lister. Currently, valid types are: list of
		strings, list of objects, list of dictionaries, list of list of strings,
		path to dat table, or dat table operator
		"""
		self.rawData = []
		# op input
		if self.inputTable.text:
			self.rawData = self.datPathToStringList(self.inputTable.path)
			if self.ownerComp.par.Inputtablehasheaders.eval():
				#validate input table headers
				headers = []
				for i, header in enumerate(self.rawData[0]):
					if header == '':
						raise Exception('Blank header in col ' + str(i))
					elif header in headers:
						raise Exception('Duplicate header in col ' + str(i))
					headers.append(header)
				self.rawData = self.stringListToDictList(self.rawData)
		else:
			parData = self.ownerComp.par.Rawdata.eval()
			if isinstance(parData, Par):
				parData = parData.eval()
			if not self.ownerComp.inputs and parData:
				self.rawData = parData
			# Linked table
			elif self.ownerComp.par.Linkedtable.eval():
				self.rawData = self.datPathToStringList(
									self.ownerComp.par.Linkedtable.eval().path)
				if self.ownerComp.par.Inputtablehasheaders.eval():
					self.rawData = self.stringListToDictList(self.rawData)
		self.workingData = None
		returnDict = self.DoCallback('onGetRawData', { 'listerExt': self,
											 'data': self.rawData, 'about':
									'Return the raw Data for Lister. ' +
					'Usually a list of objects, dicts, or string lists'})
		if returnDict is not None and \
						returnDict.get('returnValue', None) is not None:
			self.rawData = returnDict['returnValue']

	def datPathToStringList(self, path, testOnly=False):
		if type(path) == DAT:
			path = path.path
		if type(path) == str:
			if path == tdu.legalName(path):
				dat = self.ownerComp.evalExpression("op('" + path + "')")
			else:
				dat = None
			# if dat is None:
			# 	dat = self.ownerComp.op(path)
			if isinstance(dat, DAT):
				if testOnly:
					return True
				text = dat.text
				text = text.replace('\r', '')
				return [row.split('\t') for row in text.split('\n')][:-1]
			else:
				if testOnly:
					return False
				else:
					raise ValueError("Invalid table dat:", path)
		else:
			if testOnly:
				return False
			else:
				raise TypeError("Invalid path to table dat:", path)

	def stringListToDictList(self, stringList):
		"""
		Convert a list of lists of strings into a list of ordered dictionaries.
		Used to convert tableDATs with headers into ordered dicts.

		Args:
			stringList: a list of lists of strings, first item is expected to be
			used as dict keys. Must have 2 items to return anything.

		Returns: a list of ordered Dicts

		"""
		dictList = []
		if len(stringList) < 2:
			return dictList
		keys = stringList[0]
		for data in stringList[1:]:
			entry = collections.OrderedDict()
			for i, d in enumerate(data):
				entry[keys[i]] = d
			dictList.append(entry)
		return dictList

	def ConvertData(self):
		"""
		Convert rawData into a usable form.
		rawData can be:
		 	list of objects: fields corresponding to colDefine['sourceData'].
		 	list of dictionaries: keys corresponding to colDefine['sourceData'].
		 	list of lists of objects: fill columns directly or index by
		 												colDefine['sourceData']
		 	list of strings: fill first column
		 	path to table dat: like list of lists of strings
		 	table dat: just like path to table dat
		The rawData item itself will be appended as last element of list.
		"""
		if self.workingData is None:
			workingData = copy.copy(self.rawData)
			convertedData = []
			if isinstance(workingData, DAT):
				workingData = workingData.path
			if type(workingData) == str:
				workingData = self.datPathToStringList( workingData)
			if type(workingData) == tuple:
				workingData = list(workingData)
			if type(workingData) == list:
				for rowObject in workingData:
					convertedRow = self.rowObjectToWorkingData(rowObject)
					if convertedRow:
						convertedData.append(convertedRow)
			elif type(workingData) == dict:
				pass
				# TODO: convert dictionary (append key)

			self.workingData = convertedData
		# user callback
		returnDict = self.DoCallback('onConvertData',
										 {'data': self.workingData,
										  'listerExt': self,
										  'about':
				"Return working Data for Lister: a list of lists containing "
				"string Data for each column, with the row's object from raw "
				"Data at the end."})
		if returnDict is not None and \
						returnDict.get('returnValue', None) is not None:
			self.workingData = returnDict['returnValue']

	def rowObjectToWorkingData(self, rowObject):
		"""
		Convert one of the accepted rowObject types to working Data format,
		which is a list of strings for the lister columns with the original
		rowObject attached to the end.
		"""
		convertedRow = []
		dataIndex = 0 # for lists
		for dataCell in self.colDefine.row('sourceDataMode')[1:]:
			if dataCell.val == 'constant':
				convertedCell = self.colDefine['sourceData',
												   dataCell.col].val
			elif dataCell.val == 'eval':
				sourceData = self.colDefine['sourceData', dataCell.col].val
				if sourceData.strip():
					convertedCell = eval(sourceData, {'object':rowObject})
				else:
					convertedCell = ''
			elif not(dataCell.val.strip()):
				convertedCell = None
			else:
				if isinstance(rowObject, str):
					convertedCell = rowObject
				elif isinstance(rowObject, list) \
											or isinstance(rowObject, tuple):
					try:
						index = int(self.colDefine['sourceData',
												   dataCell.col].val)
					except:
						index = dataIndex
						dataIndex += 1
					if index < len(rowObject):
						convertedCell = rowObject[index]
				elif isinstance(rowObject, dict):
					try:
						convertedCell = rowObject[
								self.colDefine['sourceData',
												   dataCell.col].val]
					except:
						convertedCell = None
				else:
					try:
						convertedCell = getattr(rowObject,
											self.colDefine['sourceData',
													 dataCell.col].val)
					except:
						if self.ownerComp.par.Autodefinecols.eval() or \
									not self.colDefine['sourceData',
											   dataCell.col].val.strip():
							convertedCell = rowObject
						else:
							convertedCell = None
			if dataCell.val == 'repr':
				convertedCell = repr(convertedCell)
			convertedRow.append(convertedCell)

		if convertedRow:
			# TODO: add advanced callback
			convertedRow.append(rowObject)
		if self.doAdvancedCallbacks:
			returnDict = self.DoCallback('onRowObjectToWorkingData',
										 {'convertedRow': convertedRow,
										  'listerExt': self,
										  'about':
					"Return a list of strings for row, with rowObject at end. "
					"info['convertedRow'] is default."})
			if returnDict is not None and \
							returnDict.get('returnValue', None) is not None:
				convertedRow = returnDict['returnValue']
		return convertedRow

	def Filter(self):
		"""
		Filter workingData
		"""
		badFilters = [col for col in self.FilterCols
					  						if col < 0 or col >= self.nCols]
		if badFilters:
			filterCols = list(self.FilterCols)
			for c in badFilters:
				filterCols.remove(c)
			self.FilterCols = filterCols
			#raise ValueError("Invalid filter column:", badFilters)
		if not self.workingData:
			return
		if self.AutoFilter and self.FilterCols:
			if self.FilterString:
				if self.header and not self.autoHeader:
					headerRow = self.workingData.pop(0)
				else:
					headerRow = None
				filteredList = []
				for dataRow in self.workingData:
					filterout = True
					for col in self.FilterCols:
						if self.FilterString.lower() in dataRow[col].lower():
							filterout = False
							break
					if not filterout:
						filteredList.append(dataRow)
				if headerRow:
					filteredList.insert(0, headerRow)
				self.workingData = filteredList
		# user callback
		returnDict = self.DoCallback('onFilter', {'listerExt': self,
					'data': self.workingData, 'about':'Return filtered Data'})
		if returnDict is not None and \
						returnDict.get('returnValue', None) is not None:
			self.workingData = returnDict['returnValue']



	def Sort(self, updateLister=True, keyList=None):
		"""
		Sort Data according to sortCols and sortReverse.
		if updateLister is false, Data will be changed but Lister view and
			output will be unchanged...
		keyList is a list of lambda keys corresponding to Lister columns. None
			uses default
		"""
		# DEBUG print ('Sort', list(self.SortCols), self.AutoSort, self)
		self.fixBadSorts()
		if not self.Data:
			return
		selectedObjects = self.GetSelectedRowObjects()
		if self.AutoSort and self.SortCols:
			if self.header:
				headerRow = self.Data.pop(0)
			else:
				headerRow = None
			self.SortDataRows(self.Data, keyList)
			if headerRow:
				self.Data.insert(0, headerRow)
		# user callback
		returnDict = self.DoCallback('onSort', {'data': self.Data,
												'listerExt': self,
												'updateLister': updateLister,
												'about':'Return sorted Data.'})
		if returnDict is not None and \
						returnDict.get('returnValue', None) is not None:
			self.Data = returnDict['returnValue']
		if updateLister:
			self.DataChanged(selectedObjects)

	def fixBadSorts(self):
		badSorts = [col for col in self.SortCols
					if col < 0 or col >= self.nCols]
		if badSorts:
			sortCols = list(self.SortCols)
			for c in badSorts:
				sortCols.remove(c)
			self.SortCols = sortCols
		# raise ValueError("Invalid sort columns", badSorts)

	def SortDataRows(self, dataRows, keyList=None):
		"""
		Sort a list of row data in place. This will sort using the columns set
		by the lister's Sort Columns parameter.

		dataRows: a list of data rows.
		keyList: A list of sort keys to apply to their corresponding columns.
			These will override standard sort methods. A value of None in the
			list means to use standard sort.
		"""
		if not dataRows:
			return
		def makeColorText(s):
			try:
				t = self.ProcessColorModeText(s)[1]
				if t is None:
					t = ''
			except:
				raise
				t = ''
			return t
		self.fixBadSorts()
		indexType = int if type(dataRows[0]) == list else str
		for col in self.SortCols:
			if indexType == str:
				index = self.colNumDict[col]
			else:
				index = col
			if keyList is not None and keyList[col] is not None:
				key = keyList[col]
			else:
				mode = self.colDefine["sourceDataMode", col + 1].val
				if mode == "int":
					key = lambda x: makeint(x[index])
				elif mode == "float":
					key = lambda x: makefloat(x[index])
				elif mode == "color":
					key = lambda x: makeColorText(x[index])
				elif mode == "version":
					key = lambda x: makeversion(x[index])
				else:
					key = lambda x: str(x[index]).lower()
			dataRows.sort(key=key, reverse=self.SortReverse)
		if self.doAdvancedCallbacks:
			self.DoCallback('onSortDataRows',
									 			{'dataRows': dataRows,
												 'keyList': keyList,
												'listerExt': self,
												'about':'Sort rows in place.'})
	# endregion

	###########################################################################
	# region initialization

	def fixConfig(self):
		"""
		Use the Data in configDefault comp to update Data in the clone-
			protected config comp
		"""
		defaultConfig = self.defaultConfig
		for defaultOp in defaultConfig.children:
			# if defaultOp.name == 'callbacks':
			# 	continue
			# # copy any missing ops into configComp
			# if self.configComp.op(defaultOp.name) is None:
			# 	self.configComp.copy(defaultOp)
			# 	print('Copied', defaultOp.name, 'into', self.configComp.path)
			# copy any missing rows in colDefine tables
			if defaultOp.name == 'colDefine':
				for colDefine in [self.configComp.op('colDefine'),
								  self.autoColDefine]:
					if colDefine:
						for row in defaultOp.rows():
							rowName = row[0].val
							try:
								colDefine[rowName, 0].val
							except:
								colDefine.appendRow([rowName] +
										[defaultOp[rowName, 1]]
													* (colDefine.numCols - 1))
								print('Added row', rowName, 'to',
									  colDefine.path)
			# copy any missing rows in define table
			elif defaultOp.name == 'define':
				defineTable = self.configComp.op('define')
				if defineTable:
					for row in defaultOp.rows():
						rowName = row[0].val
						try:
							defineTable[rowName, 0].val
						except:
							defineTable.appendRow(row)
							print('Added row', rowName, 'to', defineTable.path)

	def setupAutoColDefine(self, clear=False):
		def colWidth(tList):
			textDAT = self.configComp.op('master')
			startText = textDAT.par.text
			maxWidth = 10
			for t in tList:
				textDAT.par.text = t
				textWidth = textDAT.textWidth
				if textWidth > maxWidth:
					maxWidth = textWidth
			textDAT.par.text = startText
			maxWidth += textDAT.par.position1 * 2
			return maxWidth
		self.autoHeader = True
		colDefine = self.autoColDefine
		if clear:
			for c in range(1, colDefine.numCols):
				colDefine.deleteCol(1)
			return
		else:
			if not self.rawData:
				return
			Data = copy.copy(self.rawData)
			if type(Data) == str:
				Data = self.datPathToStringList(Data)
			# column info
			rowNames = [c.val for c in colDefine.col(0)]
			rowDefaults = {}
			for row in self.ownerComp.op('configDefault/colDefine').rows():
				rowDefaults[row[0].val] = row[1].val
			rowDefaults.update({'sourceDataMode':'string'})
			# set up default column info
			colInfo = [rowDefaults.get(rowNames[i], '')
					   							for i in range(len(rowNames))]
			if not Data:
				return
			row = Data[0]
			if type(row) == str:
				row = [row]
			if type(row) == list or type(row) == tuple:
				self.autoHeader = False
				colNames = []
				for col, item in enumerate(row):
					if col < colDefine.numCols-1:
						continue
					column = item if self.header and item else str(col)
					while column in colNames:
						column = TDF.incrementStringDigits(column, 2)
					colNames.append(column)
					textList = [str(r) if isinstance(r,str)
											else str(r[col]) for r in Data]
					width = colWidth(textList)
					# width = str(max([len(str(r[col])) for r in Data]+[2]) *
					# 							self.DefaultWidthMultiplier)
					if column:
						colInfo[rowNames.index('column')] = column
					else:
						colInfo[rowNames.index('column')] = 'col' + str(col)
					colInfo[rowNames.index('width')] = width
					colDefine.appendCol(colInfo)

			elif isinstance(row, dict):
				currentCols = [c.val for c in colDefine.row('column')[1:]]
				for column in row.keys():
					if column in currentCols:
						continue
					textList = [str(r[column]) for r in Data] + [column]
					width = colWidth(textList)
					# width = str(max([len(str(r[column])) for r in Data]+[2]) *
					# 							self.DefaultWidthMultiplier)
					colInfo[rowNames.index('sourceData')] = column
					colInfo[rowNames.index('column')] = column
					colInfo[rowNames.index('width')] = width
					colDefine.appendCol(colInfo)
			else: # objects don't do defaults
				if colDefine.numCols == 1:
					column = 'objects'
					textList = [str(r) for r in Data]
					width = colWidth(textList)
					# width = str(max([len(str(r)) for r in Data]+[2]) *
					# 							self.DefaultWidthMultiplier)
					colInfo[rowNames.index('column')] = column
					colInfo[rowNames.index('width')] = width
					colInfo[rowNames.index('stretch')] = 1
					colDefine.appendCol(colInfo)

		try:
			self.DoCallback('onSetupAutoColDefine', {'autoColDefine':
												 self.autoColDefine})
		except:
			traceback.print_exc()
			print("Error in onSetupAutoColDefine callback")

	def InitCell(self, row, col):
		# DEBUG print('InitCell',row,col, self)
		attribs = self.ownerComp.cellAttribs[row, col]
		if attribs is None:
			# this is a fringe case for badly timed updates
			return
		data = list(self.Data[row].values())[col]
		self.SetCellText(row, col, data)
		if self.header and row == 0:
			if col == self.selectedCol:
				self.SetCellLook(0, col, 'headerSelect', True, COLOVERLAYER)
			else:
				self.SetCellLook(0, col, None, 'headerSelect', COLOVERLAYER)
		else:
			lookName = self.getCellLookName(row, col)
			if lookName:
				self.SetCellLook(row, col, lookName)
			else:
				self.SetCellLook(row, col, None)
			self.RollCell(row, col, False)
			# specific column settings from colDefine
			if self.colDefine['draggable', col + 1] and \
								eval(self.colDefine['draggable', col + 1].val):
				attribs.draggable = True
			else:
				attribs.draggable = False
			if self.colDefine['editable', col+1].val:
				attribs.editable = ast.literal_eval(
										self.colDefine['editable', col+1].val)
			else:
				attribs.editable = 0
		# user callback
		if self.doAdvancedCallbacks:
			self.DoCellCallback('onInitCell', row, col,
					{'attribs': attribs, 'rowData': self.Data[row],
					'about':'Set attribs (.text is text, .help is tooltip)'})
		attribs.bgColor = self.CalculateOverlays(row, col)

	def InitHeader(self):
		if not self.header:
			return
		self.SetHeaderLook(None)
		if self.doAdvancedCallbacks:
			self.DoCallback('onInitHeader')

	def InitRow(self, row, doSelect=True):
		#debug('InitRow', row)
		if self.header and row == 0:
			self.InitHeader()
			return
		self.SetRowLook(row, None)
		# striping
		if self.ownerComp.par.Rowstriping == 'Striping' and row % 2 == 0:
			rowStripeColor = \
					[float(c) for c in self.configComp.op('define')
										['rowStripeOverlayColor',1].val.split()]
			self.SetRangeOverlay(row, 0, 1, self.nCols,
					rowStripeColor+[ROWSTRIPELAYER,])
		elif self.ownerComp.par.Rowstriping == 'Dividing_Line':
			dividingLineColor = \
					[float(c) for c in self.configComp.op('define')
										['dividingLineColor',1].val.split()]
			self.ownerComp.rowAttribs[row].bottomBorderOutColor = \
					dividingLineColor

		if self.doAdvancedCallbacks:
			self.DoCallback('onInitRow', {'row': row})

	def InitCol(self, col):
		"""
		set columns attributes
		"""
		# DEBUG print('InitCol', col)
		colDefine = self.colDefine

		infoTypes = {'stretch': int, 'width': int, 'justify': str,
				   'cellLook': str, 'help': str, 'draggable': int,
					 'fontBold': int, 'fontItalic': int}
		info = {}

		for key, converter in infoTypes.items():
			try:
				info[key] = converter(colDefine[key, col + 1])
			except:
				if converter == str:
					info[key] = ''
				elif converter == int:
					info[key] = 0

		# get attribs from listCOMP
		attribs = self.ownerComp.colAttribs[col]
		if attribs:
			# tooltip
			if info['help'] and not info['help'].startswith('*'):
				attribs.help = info['help']
			# find cellLook
			#if isinstance(self.configComp.op(info['cellLook']), textTOP):
			look = self.looks.get(info['cellLook'])
			if look is not None:
				self.setLook(look, attribs)
				#textOffset
				attribs.textOffsetX = look['textOffsetX']
				attribs.textOffsetY = look['textOffsetY']
			#stretch
			if info['stretch']:
				attribs.colStretch = True
			else:
				attribs.colStretch = False
			#fontBold
			if colDefine['fontBold', col + 1] and \
										colDefine['fontBold', col + 1].val:
				if info['fontBold']:
					attribs.fontBold = True
				else:
					attribs.fontBold = False
			#fontItalic
			if colDefine['fontItalic', col + 1] and \
										colDefine['fontItalic', col + 1].val:
				if info['fontItalic']:
					attribs.fontItalic = True
				else:
					attribs.fontItalic = False
			# width
			attribs.colWidth = info['width']
			# justify
			try:
				attribs.textJustify = getattr(JustifyType, info['justify'])
			except:
				attribs.textJustify = JustifyType.CENTERLEFT
			#draggable
			attribs.draggable = info['draggable']

	def loadLooks(self, top=None):
		# table looks found in configComp textTOPs
		self.looks = {}
		if top is None:
			tops = self.configComp.findChildren(type=textTOP, depth=1)
		else:
			tops = [top]
		for top in tops:
			if not top.lock:
				self.looks[top.name] = self.LoadLook(top)

	def onInitTable(self, attribs):
		"""
		Initialize table attribs in this order: table, cols, header row,
		 header cells, rows, cells
		"""
		# debug('onInitTable')
		if not self.initialized:
			# this avoids some strange timing bugs...
			run("args[0].par.reset.pulse() if args[0] else None",
				self.ownerComp, delayFrames=1)
			return
		# self.nRows = self.ownerComp.par.rows.eval()
		# self.nCols = self.ownerComp.par.cols
		self.dragToRow = None  # the row we are dragging to
								# -1 means dragging to invalid row
		self.dragRowColors = None  # list of cell border colors to restore
		self.holdCell = None  # used to track mouse holds
		self.lastCellSelect = None # used to track mousedown rollover
		self.overlays = {}  # Overlays are stored in the form:
			# {(row, col): {'overlays': [overlaycolor,...], 'original': bgcolor}
		self.cellLookNames = {}
		self.cellTopPaths = {}
		rolledCell = self.rolledCell

		# table
		self.setLook(self.looks['master'], attribs)
		# cols
		for c in range(self.nCols):
			self.InitCol(c)
		# rows (header, if it exists, is row 0)
		for r in range(self.nRows):
			self.InitRow(r)
			for c in range(self.nCols):
				self.InitCell(r, c)
		if self.rolledRow:
			try:
				self.setRollOverlay(self.rolledRow, True)
			except:
				pass
		if rolledCell:
			try:
				self.RollCell(rolledCell[0], rolledCell[1])
			except:
				pass
		# restore looks
		for r in self._SelectedRows.peekVal:
			self.SetRowLook(r, 'rowSelect', True, SELECTOVERLAYER)

		self.DoCallback("onInitTable", {'listerExt':self})

	# endregion

	###########################################################################
	# region text and sourceDataMode text interpreters

	def SetCellText(self, row, col, text, outTableSync=True):
		"""
		Use this to set a cell's text field.
		Only sends callback if text is different (onChangeCellText).
		Sends change to Linked DAT and Synced Input DAT if outTableSync is true.
		This will use sourceDataMode effects, e.g. color will be updated.
		Returns old text.
		"""
		# DEBUG print ("SetCellText", row, col, text)
		attribs = self.ownerComp.cellAttribs[row, col]

		try:
			oldText = attribs.text
		except:
			return # HACK this only happens in weird cloning init cases
			#tdu.printStack()
			for i in range(0,row):
				print(self.ownerComp.cellAttribs[row,0].text)
			raise Exception("Badattribs", row, col, text,
							self.ownercomp.par.rows, self.ownercomp.par.cols)
			return
		# sourceDataMode processing
		sourceDataMode = self.colDefine["sourceDataMode", col+1].val
		if sourceDataMode == 'color':
			color, newText = self.ProcessColorModeText(text)
			if color:
				color.append(COLORDATALAYER)
				self.SetCellOverlay(row, col, color)
		elif sourceDataMode == 'rowNum' and not (self.header and row==0):
			newText = str(row)
		elif sourceDataMode == 'blank' and not (self.header and row==0):
			newText = ''
		else:
			newText = text
		# actual displayed text
		attribs.text = newText
		# help
		help = self.colDefine['help', col + 1].val.strip()
		if help.startswith('*'):
			if not self.header or row > 0:
				if help == '*':
					attribs.help = attribs.text
				else:
					attribs.help = eval(help[1:],
										{'object': self.Data[row]['rowObject'],
										 'text': attribs.text})
			else:
				attribs.help = ''

		# Data
		self.Data[row][self.colNumDict[col]] = text
		# output tables...
		self.outLinked.cook(force=True)
		if outTableSync:
			tableRow = row - self.AutoHeaderRows
			if self.ownerComp.par.Inputtablehasheaders:
				tableRow += 1
			syncTable = self.SyncTable
			if syncTable and tableRow > 0:
				mode = self.colDefine['sourceDataMode', col+1]
				if mode in SYNCABLEDATAMODES:
					sourceCol = self.colDefine['sourceData', col+1]
					if syncTable.col(sourceCol):
						if mode == 'blank':
							cellText = text
						else:
							cellText = newText
						syncTable[tableRow, sourceCol] = \
										cellText if cellText is not None else ''
			for table in self.OutTables:
				if 0 <= tableRow < table.numRows and col < table.numCols:
					if text is None:
						table[tableRow, col].val = ''
					else:
						table[tableRow, col].val = text
		if self.doAdvancedCallbacks:
			self.DoCellCallback('onSetCellText', row, col, {'text': text,
															'oldText': oldText})
		return oldText

	def ProcessColorModeText(self, text):
		"""
		Process a color sourceDataMode text string. Returns (color, text)
		Text can be list [r, g, b, a] or [r, g, b, a, "text"]
		Anything else will be treated as text with color = None
		"""
		try:
			l = eval(text)
		except:
			l = text
		if type(l) in (list, tuple):
			l = list(l)
			if len(l) == 5:
				return [l[:4], l[4]]
			elif len(l) == 4:
				return l[:4], ''
			else:
				return None, text
		else:
			return None, text

	def GetCellText(self, row, col):
		"""
		Get the text at the given location
		"""
		return list(self.Data[row].values())[col]

	# endregion

	###########################################################################
	# region selection system

	def GetSelectedRowObjects(self):
		"""
		Obsolete. Use .SelectedRowObjects property.

		:return: self.SelectedRowObjects
		"""
		return self.SelectedRowObjects

	@property
	def SelectedRowObjects(self):
		"""
		Returns a list of all rowObjects in selected rows. Useful for sending
		to SelectObjects after changing Data
		"""
		if self.Data:
			# list comprehension for speed
			selectedRowObjects = [self.Data[r]['rowObject']
							for r in self.SelectedRows
							# only if valid row and rowObject is not empty
							if r < len(self.Data) and self.Data[r]['rowObject']]
		else:
			selectedRowObjects = []
		return selectedRowObjects

	def SelectObjects(self, objects, addSelection=False):
		"""
		Select a list of objects if present in rowObjects.
		"""
		obRows = []

		startRow = 1 if self.header else 0
		for i, r in enumerate(self.Data[startRow:]):
			try:
				if r['rowObject'] in objects:
					obRows.append(i + startRow)
					objects.remove(r['rowObject'])
			except:
				pass
		if addSelection:
			selectRows = self.SelectedRows
		else:
			selectRows = []
		selectRows += obRows
		self.SelectedRows = selectRows

	def GetObjectRowNum(self, object):
		"""Returns the row number of the provided object"""
		selectRow = None
		startRow = 1 if self.header else 0
		for i, r in enumerate(self.Data[startRow:]):
			try:
				if object == r['rowObject']:
					selectRow = i + startRow
					break
			except:
				pass
		return selectRow

	def SelectRow(self, row, addRow=False):
		"""
		Set selected row.
		Set row to None and addRow to False to remove all selections
		Use addRow for multiple selections.
		"""
		# DEBUG print('SelectRow', row, addRow, self.SelectedRows)

		if row is not None and ((self.header and row == 0)
										or row >= len(self.Data) or row < 0):
			return
		if row is None and not addRow:
			self.SelectedRows = []
			return
		if addRow is False:
			self.SelectedRows = [row]
		elif row not in self.SelectedRows:
			self.SelectedRows += [row]

	def doSelectRowCallback(self, row):
		# needed for multiple places where we have to call this
		self.DoCallback('onSelectRow', {'row': row,
										'rowData': self.Data[row]})

	def doDeselectRowCallback(self, row):
		# needed for multiple places where we have to call this
		self.DoCallback('onDeselectRow', {'row': row,
											'rowData': self.Data[row]})

	def DeselectRow(self, row):
		"""
		Deselect a single row
		Set lookOnly to true to set look but skip callbacks.
		"""
		# DEBUG	print('DeselectRow', row, lookOnly, self.SelectedRows)
		selectedRows = self.SelectedRows
		if row not in selectedRows or row >= len(self.Data) or row < 0:
			return
		selectedRows.remove(row)
		self.SelectedRows = selectedRows

	def SelectRowRange(self, first, last, addRows=False):
		"""
		Select a range of rows in the given order.
		First can be greater than last.
		If addRows is False, deselect all other rows
		"""
		if first == -1 or last == -1:
			return
		if first > last:
			last -= 1
			step = -1
		else:
			last += 1
			step = 1
		newSelection = range(first, last, step)
		# DEBUG print('SelectRowRange', addRows, list(newSelection))
		if addRows:
			selectRows = self.SelectedRows
			# add new rows
			for r in newSelection:
				if r not in selectRows:
					selectRows.append(r)
		else:
			selectRows = list(newSelection)
		self.SelectedRows = selectRows

	def SelectCell(self, row, col):
		"""
		Mousedown on cell. No mouse up yet... that call is 'Click'
		"""
		# DEBUG print('SelectCell',row, col)

		if row is None or col is None:
			row = col = None
		self.selectedCell = self.DropInfo = (row, col)

	# a column was selected.
	def SelectColumn(self, col):
		"""
		Unlike other selects, this is called on mouse click, not mouse down
		"""
		# debug('Select Column', col)
		oldSelected = self.selectedCol
		self.selectedCol = col
		if oldSelected != col and oldSelected is not None:
			self.SetCellLook(0, oldSelected, None)
		if col is None:
			self.FilterCols = []
			self.SortCols = []
		else:
			if col == oldSelected:
				self.SortReverse ^= True
			else:
				self.SortReverse = False
			self.SetCellLook(0, col, 'headerSelect', True, COLOVERLAYER)
			self.FilterCols = [col]
			self.SortCols = [col]
		self.DoCallback('onSelectColumn', {'col': col,
							'colName': list(self.columnDict.keys())[col]
											if col is not None else None})
		self.Sort()

	# endregion

	###########################################################################
	# region user interaction

	def onRollover(self, row, col, coords, prevrow, prevcol, prevcoords):
		if row is None and prevrow in NONCELL:
			return
		if row is None:
			row = -1
			col = -1
		doCallbacks = self.doAdvancedCallbacks
		if self.ownerComp.par.Highlightrollover.eval():
			# row changes
			if row != prevrow:
				# HACK when listcomp resets it should know to set prevrow to -1
				if prevrow and prevrow >= self.nRows:
					prevrow = -1
				# restore prevrow look
				if prevrow not in NONCELL and (prevrow != 0 or not self.header):
					if prevrow in self.SelectedRows:
						self.setRollOverlay(prevrow, False)
					else:
						self.SetRowLook(prevrow, None, 'rowRoll', ROLLOVERLAYER,
										doCallback=doCallbacks)
				# set row look
				if row not in NONCELL and (row != 0 or not self.header):
					self.rolledRow = row
					if row in self.SelectedRows:
						self.setRollOverlay(row, True)
					else:
						self.SetRowLook(row, 'rowRoll', True, ROLLOVERLAYER,
										doCallback=doCallbacks)
				else:
					self.rolledRow = None
		# cell changes

		if col != prevcol or row != prevrow:
			# if there was a previous cell
			if prevrow not in NONCELL and prevcol not in NONCELL:
				self.RollCell(prevrow, prevcol, False)
			if row not in NONCELL and col not in NONCELL:
				self.RollCell(row, col)
			if doCallbacks:
				self.DoCallback( "onRollover", {"row": row,
							"col": col, "prevrow": prevrow, "prevcol": prevcol})

	def EditCell(self, row, col, selectAll=False):
		oldEditable = self.ownerComp.cellAttribs[row,col].editable
		self.ownerComp.cellAttribs[row,col].editable = 1
		self.ownerComp.setKeyboardFocus( row, col, selectAll=selectAll)
		self.ownerComp.cellAttribs[row,col].editable = oldEditable

	def RollCell(self, row, col, on=True):
		if row in NONCELL:
			return
		self.rolledCell = (row, col) if on else None
		doCallbacks = self.doAdvancedCallbacks
		# header
		if row == 0 and self.header:
			if self.ownerComp.par.Clickableheader.eval():
				if list(self.Data[0].values())[col]:
					look = 'headerRoll'
					if col == self.selectedCol:
						# just set bgColor
						if on:
							self.SetCellOverlay(row, col,
									self.looks['headerRoll']['bgColor'] +
												(ROLLOVERLAYER,), True)
						else:
							self.RemoveOverlay(row, col, ROLLOVERLAYER)
					else:
						# set look
						if on:
							self.SetCellLook(row, col, look, True,
									ROLLOVERLAYER, doCallback=doCallbacks)
						else:
							self.RemoveOverlay(row, col, ROLLOVERLAYER)
							self.SetCellLook(row, col, None, look,
									ROLLOVERLAYER, doCallback=doCallbacks)
		else: # table
			# look
			lookName = self.getCellLookName(row, col)
			if lookName:
				look = lookName + 'Roll'
				if on:
					self.SetCellLook(row, col, look, True,
									 COLLOOKOVERLAYER, doCallback=doCallbacks)
				else:
					self.RemoveOverlay(row, col, COLLOOKOVERLAYER)
					self.SetCellLook(row, col, None, look,
									 COLLOOKOVERLAYER, doCallback=doCallbacks)
					self.SetCellLook(row, col, lookName)
			# image
			topPath = self.getTopPath(row, col)
			if on:
				if topPath:
					top = self.configComp.op(topPath + 'Roll')
					attribs = self.ownerComp.cellAttribs[row, col]
					if top and attribs:
						attribs.top = top
			else:
				if topPath:
					top = self.configComp.op(topPath)
					attribs = self.ownerComp.cellAttribs[row, col]
					if top and attribs:
						attribs.top = top

	def ClickHeader(self, col):
		"""
		Perform a click on the given header cell.
		"""
		if self.ownerComp.par.Clickableheader.eval():
			if list(self.Data[0].values())[col]:
				self.SelectColumn(col)
		self.DoCellCallback('onClickHeader', 0, col)

	def DoubleClickHeader(self, col):
		"""
		Perform a doubleclick on the given header cell.
		"""
		self.DoCellCallback('onDoubleClickHeader', 0, col)

	def MouseHold(self, row, col):
		"""
		Mouse is being held down on cell.
		"""
		returnDict = self.DoCellCallback('onMouseHold', row, col,
							{'rowData': None if row in NONCELL else
																self.Data[row],
							 'about': 'return True to still do click on up'})
		if returnDict is not None and \
						returnDict.get('returnValue', None) is not None:
			self.doClick = returnDict['returnValue']

	def Click(self, row, col):
		"""
		Click on the given cell.
		"""
		# DEBUG print ('Click', row, col)
		if row == 0 and self.header:
			self.ClickHeader(col)
			return
		else:
			self.DoCellCallback('onClick', row, col,
								{'rowData': None if row in NONCELL else
																self.Data[row]})

	def DoubleClick(self, row, col):
		"""
		Double click on the given cell.
		"""
		# debug ('DoubleClick', row, col)
		if row == 0 and self.header:
			self.DoubleClickHeader(col)
			return
		else:
			self.DoCellCallback('onDoubleClick', row, col,
								{'rowData': None if row in NONCELL else
																self.Data[row]})

	def onFocus(self, row, col, prevRow, prevCol):
		if prevRow >= 0 and prevCol >= 0:
			self.ownerComp.panel.click.val = 1

	def onSelect(self, startrow, startcol, startcoords, endrow, endcol,
													endcoords, start, end):
		"""
		The mouse is down and over the listCOMP. This is called multiple times
		as mouse is dragged across comp. Called by internalCallbacks.
		"""
		# start is true, end is false when mouse is first pressed on a cell
		# start is false, end is true when mouse is released on a cell
		# start and end are both false while mouse is held and dragged

		# debug('onSelect', startrow, startcol, endrow, endcol, start,end)

		if endrow not in NONCELL and endrow >= self.nRows:
			# table must have changed under us. This can happen when filter is
			# typed but click on table causes focus change
			return

		# don't do anything unless cell changed
		if not (start or end) and self.lastCellSelect == (endrow, endcol):
			return
		self.lastCellSelect = (endrow, endcol)
		self.holdCell = None

		if start:
			self.SelectCell(startrow, startcol)
			self.doClick = True
			# hold testing
			self.holdCell = (startrow, startcol)
			try:
				self.holdRun.kill()
			except:
				pass
			if startrow not in NONCELL:
				self.holdRun = run('op("' + self.ownerComp.path +
						'").CheckHold(' + str(startrow) + ', ' + str(startcol)
								   				+ ')', delayMilliSeconds=1000)
		elif end and endrow is None:
			self.setDragToRow(startrow, None)
			self.doClick = False

		# middle and right button
		if start and \
				(self.ownerComp.panel.rselect or self.ownerComp.panel.mselect):
			button = 'Right' if self.ownerComp.panel.rselect else 'Middle'
			self.ButtonDown = button
			# if button == 'Right' and startrow not in self.SelectedRows:
			# 	if self.ownerComp.par.Selectablerows.eval() and \
			# 					int('0' + self.colDefine['selectRow',
			# 											 startcol+1].val):
			#		self.SelectRow(startrow)
			self.DoCellCallback('onMouse' + button + 'Down',
								startrow, startcol)
			return
		if self.ButtonDown in ['Right', 'Middle']:
			if end:
				self.DoCellCallback('onMouse' + self.ButtonDown + 'Up',
									endrow, endcol)
				if self.doClick and self.selectedCell == (endrow, endcol):
					if endrow == 0 and self.header:
						self.DoCellCallback( 'onClickHeader' +
												 self.ButtonDown, 0, startcol)
					else:
						self.DoCellCallback('onClick' + self.ButtonDown,
										startrow, startcol)
				self.ButtonDown = None
			else:
				infoDict = {'startRow': startrow, 'startCol': startcol,
							'endRow': endrow, 'endCol': endcol}
				self.DoCallback('onMouse' + self.ButtonDown + 'Drag',
										  							infoDict)
			return
		# left button
		if start:
			self.DoCellCallback('onMouseDown', startrow, startcol)
			#self.PressCell(startrow, startcol)
			self.ButtonDown = "Left"
			# row select
			if not ((self.header and startrow == 0) or startrow == -1):
				if self.ownerComp.par.Selectablerows.eval() and \
								int('0' + self.colDefine['selectRow',
														 startcol+1].val):
					if self.ownerComp.par.Multiplerowselect.eval():
						# ctrl - add row
						if self.ownerComp.panel.ctrl.val:
							if startrow in self.SelectedRows:
								self.DeselectRow(startrow)
							else:
								self.SelectRow(startrow, True)
							self.doClick = False
						# shift - select range to last selected row
						elif self.ownerComp.panel.shift.val:
							if not self.SelectedRows:
								self.SelectRow(startrow)
							else:
								self.SelectRowRange(startrow,
													self.SelectedRows[-1])
							self.doClick = False
						# normal, select this if it's not selected already...
						elif startrow not in self.SelectedRows:
							self.SelectRow(startrow)
					else:
						self.SelectRow(startrow)
				# drag rows must be initiated here
				if self.ownerComp.par.Dragtoreorderrows.eval() and \
									not (self.ownerComp.panel.ctrl.val
											or self.ownerComp.panel.shift.val):
					self.testStartDragRows(startrow)
				# this makes select and rollover play nice
				self.setRollOverlay(startrow, False)
				self.setRollOverlay(startrow, True)
				self.PressCell(endrow, endcol)
		elif end:
			self.ButtonDown = None
			# end hold testing
			try:
				self.holdRun.kill()
			except:
				pass
			infoDict = {'startRow': startrow, 'startCol': startcol}
			if endrow not in NONCELL:
				self.DoCellCallback('onMouseUp', endrow, endcol, infoDict)

			# mouse up on same cell as mouse down
			if self.selectedCell == (endrow, endcol):
				if self.doClick and self.ownerComp.panel.inside:
					# HACK panel.inside test because no leaving lister callback
					if endrow not in NONCELL \
							and self.ownerComp.par.Selectablerows\
							and self.ownerComp.par.Multiplerowselect.eval() \
							and int('0' + self.colDefine['selectRow',
										 					startcol+1].val):
						self.SelectRow(endrow)
					if self.ownerComp.panel.click == 2 and self._clickedOnce:
						self.DoubleClick(endrow, endcol)
						self._clickedOnce = False
						self.ownerComp.panel.click = 0
					else:
						self.Click(endrow, endcol)
						self._clickedOnce = True
					self.RollCell(endrow, endcol)
			# mouse down on one cell, mouse up on another
			elif startrow != endrow and self.ownerComp.panel.inside:
				# check drag rows
				if self.dragToRow is not None and self.dragToRow >= 0:
					# move selected rows
					self.setRollOverlay(self.rolledRow, False)
					moveRows = self.SelectedRows
					self.MoveRows(moveRows, endrow)
					if self.ownerComp.par.Allowundo:
						ui.undo.startBlock('MoveRows - ' + self.ownerComp.path)
						ui.undo.addCallback(self.undoMoveRows,
											(moveRows, endrow))
						ui.undo.endBlock()

			# reset drag rows
			self.setDragToRow(startrow, None)
			# mouse-down trackers
			self.lastCellSelect = self.holdCell = self.selectedCell = None
		# moving around with mouse down
		else:
			if endcol not in NONCELL and \
					int('0' + self.colDefine['clickOnDrag', endcol + 1].val) \
														and endcol == startcol:
				# press cell when we roll over with mouse down
				if self.selectedCell and self.selectedCell != (endrow, endcol):
					self.RollCell(self.selectedCell[0], self.selectedCell[1],
									 False)
				if endrow not in NONCELL and not (self.header and endrow == 0):
					self.RollCell(endrow, endcol, False)
					self.selectedCell = (endrow, endcol)
					if self.ownerComp.par.Selectablerows.eval() and \
							int('0' + self.colDefine['selectRow',
													 endcol + 1].val):
						self.SelectRow(endrow)
					if self.doClick:
						self.PressCell(endrow, endcol)
						self.Click(endrow, endcol)
				else:
					self.selectedCell = None
			elif self.selectedCell == (endrow, endcol):
				if self.doClick:
					self.PressCell(endrow, endcol)
			elif endrow not in NONCELL:
				self.RollCell(startrow, startcol, False)
			if self.dragToRow is not None and endrow != self.dragToRow:
				self.setDragToRow(startrow,
								  endrow if endrow is not None else -1)
			infoDict = {'startRow': startrow, 'startCol': startcol,
						'endRow': endrow, 'endCol': endcol}
			if not start:
				self.DoCallback('onMouseDrag', infoDict)

	def testStartDragRows(self, startrow):
		# DEBUG print('testStartDragRows', startrow)
		if startrow not in self.SelectedRows:
			return False
		# test for contiguous selected rows using arcane python magic
		if len(list(groupby(enumerate(sorted(self.SelectedRows)),
											lambda ix: ix[0] - ix[1]))) > 1:
			return False
		self.dragToRow = startrow
		return startrow

	def setDragToRow(self, originrow, newrow=None):
		# restore row borders
		dragRowColors = self.dragRowColors
		dragToRow = self.dragToRow
		if dragRowColors is not None and dragToRow not in NONCELL:
			for col in range(self.nCols):
				attribs = self.ownerComp.cellAttribs[dragToRow, col]
				if dragToRow < originrow:
					attribs.topBorderOutColor = dragRowColors[col]
				else:
					attribs.bottomBorderOutColor = dragRowColors[col]
		if (newrow == 0 and self.header) or newrow in self.SelectedRows:
			newrow = -1  # dragging to invalid row
		dragToRow = newrow
		self.dragToRow = dragToRow
		if newrow is None:
			return
		if newrow == originrow or newrow == -1:
			# invalid row
			dragRowColors = None
		else:
			# set row borders and store old ones
			dragRowColors = []
			borderColor = [float(x) for x in self.configComp.op('define')
										['rowDragColor', 1].val.split(' ')]
			for col in range(self.nCols):
				attribs = self.ownerComp.cellAttribs[dragToRow, col]
				if dragToRow < originrow:
					dragRowColors.append(attribs.topBorderOutColor)
					attribs.topBorderOutColor = borderColor
				else:
					dragRowColors.append(attribs.bottomBorderOutColor)
					attribs.bottomBorderOutColor = borderColor
			# remove roll
			self.setRollOverlay(newrow, False)
		self.dragRowColors = dragRowColors

	def PressCell(self, row, col):
		"""
		The cell is being pressed like a button, but has not been released.
		This can happen multiple times if the user presses the button and drags
		onto and off the cell.
		"""
		# debug ("PressCell", row, col, self.colDefine['cellType',col])
		if row in NONCELL:
			return
		if row == 0 and self.header:
			if self.ownerComp.par.Clickableheader.eval() and \
									list(self.Data[0].values())[col]:
				self.SetCellLook(0, col, 'headerPress', True, ROLLOVERLAYER)
		else:
			lookName = self.getCellLookName(row, col)
			if lookName:
				self.SetCellLook(row, col, lookName + 'Press', True,
								 COLLOOKOVERLAYER)
			# image
			topPath = self.getTopPath(row, col)
			if topPath:
				top = self.configComp.op(topPath + 'Press')
				attribs = self.ownerComp.cellAttribs[row, col]
				if top and attribs:
					attribs.top = top
		if self.doAdvancedCallbacks:
			self.DoCallback('onPressCell', {'row': row, 'col': col})

	def AbortClick(self):
		"""
		Call this to make a click NOT happen when there has been a mousedown
		but no mouse up yet
		"""
		self.doClick = False
		# DEBUG print("ABORT")
		# DEBUG import traceback; traceback.print_stack()

	def CheckHold(self, row, col):
		"""
		Delayed call to check when mouse is held down on a cell
		"""
		if self.holdCell == (row, col):
			self.MouseHold(row, col)

	def keyPressed(self, key, state, shift, ctrl, alt, cmd):
		# DEBUG print('keyPressed', key, state, shift, ctrl, alt, cmd)
		# DELETE
		if state:
			if key == 'delete' and self.ownerComp.par.Deletekey.eval():
				self.DeleteRows( self.SelectedRows)
			if key in ['up', 'down'] and self.ownerComp.par.Arrowkeys.eval() \
								and self.ownerComp.par.Selectablerows.eval() \
								and self.SelectedRows:
				lastrow = self.SelectedRows[-1]
				newrow = lastrow + (1 if key == 'down' else -1)
				if key == 'up' and lastrow > self.header\
						or key == 'down' and lastrow < self.nRows - 1:
					if shift:
						self.SelectRowRange(self.SelectedRows[0], newrow)
					else:
						self.SelectRow(newrow)

		# if self.ownerComp.par.Allowundo:
		# 	if key == ord('z') and ctrl:
		# 		ui.undo.undo()
		# 	if key == ord('y') and ctrl:
		# 		ui.undo.redo()
			self.DoCallback('onKeyPressed', {'key': key, 'ctrl': ctrl,
										 'shift': shift, 'alt': alt,
										 'cmd': cmd, 'state': state})
		else:
			self.DoCallback('onKeyReleased', {'key': key, 'ctrl': ctrl,
											 'shift': shift, 'alt': alt,
											 'cmd': cmd, 'state': state})
	# endregion

	###########################################################################
	# region callback system

	def DoCellCallback(self, callbackName, row, col, eventInfo=None):
		if eventInfo is None:
			eventInfo = {}
		retVal = None
		eventInfo.update({'row': row, 'col': col, 'colName':None})
		if row not in NONCELL:
			colName = self.colDefine[0, col + 1].val
			eventInfo.update({'rowData': self.Data[row], 'colName':colName,
						'cellText': self.ownerComp.cellAttribs[row, col].text})
			# # try CallbackRowColname
			# retVal = self.DoCallback(callbackName +
			# 									str(row) + colName, eventInfo)
			# Didn't seem that useful, and slowed things down. Removed

			# try CallbackColname
			retVal = self.DoCallback(callbackName + colName.partition(' ')[0],
											   eventInfo)
		# try Callback
		eventInfo["callbackName"] = callbackName
		newRetVal = self.DoCallback(callbackName, eventInfo)
		return newRetVal if newRetVal else retVal

	# endregion

	###########################################################################
	# region overlay system

	def SetCellOverlay(self, row, col, overColor, apply=True):
		"""
		Apply (or remove) overlay overColors to a cell.
		overColor is color to overlay. Alpha of overColor will be used.
			overColor has an optional 5th element which is a number used for
			ordering overlays. Will default to 50. Higher # = higer layer
		If overColor is None, remove all overlays.
		If apply is false, the overColor overlay will be removed IF FOUND.
		Returns removeArgs tuple - SetCellOverlay(*removeArgs)
		"""
		if overColor:
			overColor = list(overColor)
			if len(overColor) == 4:
				overColor.append(CELLOVERLAYER)
		self.SetRangeOverlay(row, col, 1, 1, overColor, apply)
		return row, col, overColor, False

	def SetRowOverlay(self, row, overColor, apply=True):
		"""
		Apply (or remove) overlay overColors to a cell.
		overColor is color to overlay. Alpha of overColor will be used.
			overColor has an optional 5th element which is a number used for
			ordering overlays. Will default to 45. Higher # = higer layer
		If overColor is None, remove all overlays.
		If apply is false, the overColor overlay will be removed IF FOUND.
		Returns removeArgs tuple - SetCellOverlay(*removeArgs)
		"""
		if overColor:
			if len(overColor) == 4:
				overColor.append(ROWOVERLAYER)
		self.SetRangeOverlay(row, 0, 1, self.nCols, overColor, apply)
		return row, overColor, False

	def SetColOverlay(self, col, overColor, apply=True):
		"""
		Apply (or remove) overlay overColors to a cell.
		overColor is color to overlay. Alpha of overColor will be used.
			overColor has an optional 5th element which is a number used for
			ordering overlays. Will default to 40. Higher # = higer layer
		If overColor is None, remove all overlays.
		If apply is false, the overColor overlay will be removed IF FOUND.
		Returns removeArgs tuple - SetCellOverlay(*removeArgs)
		"""
		if overColor:
			if len(overColor) == 4:
				overColor.append(COLOVERLAYER)
		self.SetRangeOverlay(0, col, self.nRows, 1, overColor, apply)
		return col, overColor, False

	def SetRangeOverlay(self, row, col, height, width, overColor, apply=True):
		"""
		Apply (or remove) overlay overColors to a rectangle of cells.
		row and col define top left corner.
		width and height define size of rectangle.
		overColor is color to overlay. Alpha of overColor will be used.
			overColor has an optional 5th element which is a number used for
			ordering overlays. Will default to 100. Higher # = higer layer
		If overColor is None, remove all overlays.
		If apply is false, the overColor overlay will be removed IF FOUND.
		Returns removeArgs tuple - SetCellOverlay(*removeArgs)
		"""
		# DEBUG print('SetRangeOverlay',row,col,width, height, overColor, apply)
		if overColor:
			alpha = overColor[3]
			if alpha == 0:
				return
			if len(overColor) == 4:
				overColor += (RANGEOVERLAYER,)
		# lastColor = lastMix = None # to speed up repetitive calculations
		for r in range(row, row + height):
			for c in range(col, col + width):
				attribs = self.ownerComp.cellAttribs[r, c]
				overlayInfo = self.overlays.setdefault((r,c),
												{'overlays':[], 'original':()})
				if overColor:
					if apply:
						# remove colors with same order number
						overlayInfo['overlays'] = \
								[color for color in overlayInfo['overlays']
								 		if color[4] != overColor[4]]
						overlayInfo['overlays'].append(overColor)
						if overlayInfo['original'] == ():
							overlayInfo['original'] = attribs.bgColor
						attribs.bgColor = self.CalculateOverlays(r, c,
																 overlayInfo)
						# DEBUG print("ov", r, c, overColor, attribs.bgColor)
					else:  # removing overlay
						overlays = overlayInfo['overlays']
						if overColor in overlays:
							overlays.remove(overColor)
							attribs.bgColor = overlayInfo['original']
							if overlays:
								attribs.bgColor = self.CalculateOverlays(
														r, c, overlayInfo)
							else:
								del self.overlays[(r, c)]
				else:
					attribs.bgColor = overlayInfo['original']
					del self.overlays[(r, c)]
		return row, col, height, width, overColor, False

	def RemoveOverlay(self, row, col, layer):
		"""
		Remove overlay at the given layer of selected cell.
		"""
		overlayInfo = self.overlays.get((row,col))
		if overlayInfo:
			removeColor = None
			for color in overlayInfo['overlays']:
				if color[4] == layer:
					removeColor = color
					break
			if removeColor:
				overlayInfo['overlays'].remove(removeColor)
				attribs = self.ownerComp.cellAttribs[row,col]
				if attribs:
					attribs.bgColor = self.CalculateOverlays(
														row, col, overlayInfo)


	def CalculateOverlays(self, row, col, overlayInfo=None):
		"""
		Return cell color including overlays of selected cell.
		"""
		if overlayInfo is None:
			overlayInfo = self.overlays.setdefault((row, col),
												{'overlays':[], 'original':()})
		cellColor = overlayInfo["original"]
		if not cellColor:
			cellColor = self.GetCellColor( row, col, False)
		overlayInfo['overlays'].sort(key=lambda x: x[4])
		for color in overlayInfo['overlays']:
			cellColor = mixColor(cellColor, color)
		return cellColor

	def GetCellColor(self, row, col, checkCellAttribs=True):
		"""
		Search the attrib hierarchy for cell's current color.
		If checkCellAttribs is False, only look at row, col, and table.
		"""
		if checkCellAttribs:
			color = self.ownerComp.cellAttribs[row, col].bgColor
			if color:
				return color
		color = self.ownerComp.rowAttribs[row].bgColor
		if color:
			return color
		try:
			color = self.ownerComp.colAttribs[col].bgColor
			if color:
				return color
		except:
			pass
		color = self.ownerComp.attribs.bgColor
		if color:
			return color
		# this happens if table is in the middle of initializing.
		return 0,0,0,0

	# endregion

	###########################################################################
	# region look system

	def getTopPath(self, row, col):
		topPath = self.cellTopPaths.get((row, col), None)
		if topPath is not None:
			return topPath
		root = self.colDefine['topPath', col + 1].val
		if root:
			if root.endswith('*'):
				root = root[:-1] + str(list(self.Data[row].values())[col])
			return root

	def SetHeaderLook(self, lookName=None):
		"""
		Pass a look from look dictionary to set header look, or None to clear
		"""
		# DEBUG print('SetHeaderLook', row, col, look)
		look = self.looks.get(lookName, None)
		attribs = self.ownerComp.rowAttribs[0]
		attribs.editable = 0
		if look is None:
			look = self.looks['header']
		if look:
			# don't use justify
			self.setLook(look, attribs, ['textOffsetX', 'textOffsetY'])
			# attribs.textJustify = look['textJustify']
			attribs.fontItalic = look['fontItalic']
			attribs.bgColor = look['bgColor']
			attribs.textColor = look['textColor']
			attribs.fontBold = look['fontBold']
		attribs.draggable = False

		if self.selectedCol is not None and self.selectedCol >= 0:
			self.SetCellLook(0, self.selectedCol, 'headerSelect', True,
							 COLOVERLAYER)
		if self.doAdvancedCallbacks:
			self.DoCallback('onSetHeaderLook', {'look': look,
												'attribs': attribs})

	def SetCellLookName(self, row, col, lookName):
		"""
		Set the individual cell look name. Generally, this should be set in the
		onInitCell (individual cell) or onInitTable (whole table) callbacks

		Args:
			row: cell row #
			col: cell col #
			lookName: name of look (see textTOPs in config comp) or None to
						unset individual cell look (goes back to col look)
		"""
		if lookName is None:
			try:
				del self.cellLookNames[(row, col)]
			except:
				pass
		else:
			self.cellLookNames[(row, col)] = lookName
		self.SetCellLook(row, col, lookName)

	def SetCellTopPath(self, row, col, topPath):
		"""
		Set the individual cell TOP path. Generally, this should be set in the
		onInitCell (individual cell) or onInitTable (whole table) callbacks

		Args:
			row: cell row #
			col: cell col #
			topPath: TOP path or None to unset individual TOP path (goes back
						to col look)
		"""
		if topPath is None:
			try:
				del self.cellTopPaths[(row, col)]
			except:
				pass
		else:
			self.cellTopPaths[(row, col)] = topPath
		self.ownerComp.cellAttribs[(row, col)].top = op(topPath)

	def getCellLookName(self, row, col):
		look = self.cellLookNames.get((row,col), '')
		if look == '':
			try:
				look = self.colDefine['cellLook', col + 1].val
			except:
				pass
		return look

	def SetCellLook(self, row, col, lookName=None, overlay=False,
					overlayOrder=CELLOVERLAYER, doCallback=True):
		"""
		Pass a look from look dictionary to set cell look, or None to clear
		If overlay is True and look is not None, apply look's bgcolor as overlay
		If overlay is True and look is None, remove all overlays
		If overlay is a look name and look is None, remove that look's overlay
		overlayOrder is for layered overlays. Higher # = higher overlay.
			default = 50
		If doCallback is True, send user callbacks
		"""
		if row in NONCELL or row >= self.nRows:
			return
		# debug('SetCellLook', row, col, lookName,overlay,overlayOrder)

		look = self.looks.get(lookName, None)
		if look is None and lookName:
			# look not found
			return
		attribs = self.ownerComp.cellAttribs[row, col]
		if attribs is None:
			return
		if look:
			if overlay:
				self.SetCellOverlay(row, col, look['bgColor'] +	(overlayOrder,))
			else:
				attribs.bgColor = look['bgColor']
				try:
					self.overlays[(row,col)]['original'] = attribs.bgColor
				except:
					pass
				setAttribs = ['textColor', 'fontBold', 'fontItalic',
								 'leftBorderInColor', 'rightBorderInColor',
								 'topBorderInColor', 'bottomBorderInColor',
								 'leftBorderOutColor', 'rightBorderOutColor',
								 'topBorderOutColor', 'bottomBorderOutColor',
								 'sizeInPoints']
				for a in setAttribs:
					setattr(attribs, a, look[a])
		elif overlay == True:
			# remove all overlays
			self.SetCellOverlay(row, col, None)
		elif overlay:
			# remove the specified overlay
			removeLook = self.looks.get(overlay, None)
			if removeLook:
				self.SetCellOverlay(row, col, removeLook['bgColor']
									+ (overlayOrder,), False)
		else:
			attribs.bgColor = None
			try:
				self.overlays[(row,col)]['original'] = None
			except:
				pass
			setAttribs = ['textColor', 'fontBold', 'fontItalic',
							 'leftBorderInColor', 'rightBorderInColor',
							 'topBorderInColor', 'bottomBorderInColor',
							 'leftBorderOutColor', 'rightBorderOutColor',
							 'topBorderOutColor', 'bottomBorderOutColor',
							 'sizeInPoints']
			for a in setAttribs:
				setattr(attribs, a, None)

		# top images
		# if not (row == 0 and self.header):
		# 	attribs.top = None
		# 	image = self.colDefine['topPath', col + 1].val
		# 	if image:
		# 		attribs.top = self.configComp.op(image)
		attribs.bgColor = self.CalculateOverlays(row, col)
		if not self.skipSetCellCallback:
			self.skipSetCellCallback = True
			if self.doAdvancedCallbacks and doCallback:
				self.DoCellCallback('onSetCellLook', row, col, {'look': look,
									'attribs': attribs})
			self.skipSetCellCallback = False

	def SetRowLook(self, row, lookName=None, overlay=False,
				   overlayOrder=ROWOVERLAYER, doCallback=True):
		"""
		Set row look to lookName, or None to clear
		If overlay is True and look is not None, apply look's bgcolor as overlay
		If overlay is True and look is None, remove all overlays
		If overlay is a look name and look is None, remove that look's overlay
		overlayOrder is for layered overlays. Higher # = higher overlay.
			default = 100
		if doCallback is True, send user callback
		"""
		if row in NONCELL or row >= self.nRows:
			return
		look = self.looks.get(lookName, None)
		if row == 0 and self.header:
			self.SetHeaderLook(lookName)
			return
		# DEBUG	print('SetRowLook', row, overlay, look)
		attribs = self.ownerComp.rowAttribs[row]
		if attribs is None:
			return
		if look:
			if overlay:
				self.SetRangeOverlay(row, 0, 1, self.nCols, look['bgColor'] +
								  						(overlayOrder,))
			else:
				attribs.bgColor = look['bgColor']
			attribs.textColor = look['textColor']
			attribs.fontBold = look['fontBold']
			attribs.fontItalic = look['fontItalic']
		else:
			attribs.bgColor = None
			attribs.textColor = None
			attribs.fontBold = None
			attribs.fontItalic = None
			if overlay is True:
				# remove all overlays
				self.SetRangeOverlay(row, 0, 1, self.nCols, None)
			elif overlay:
				# remove the specified overlay
				removeLook = self.looks.get(overlay, None)
				if removeLook:
					self.SetRangeOverlay(row, 0, 1, self.nCols,
								removeLook['bgColor'] + (overlayOrder,), False)
		if self.doAdvancedCallbacks and doCallback:
			self.DoCallback('onSetRowLook', {'row': row, 'look': look,
										'overlay': overlay, 'attribs': attribs})

	def setRollOverlay(self, row, on=True):
		"""
		Sets overlay but not look.
		"""
		if not self.ownerComp.par.Highlightrollover.eval():
			return
		# DEBUG print("setRollOverlay", row, on)
		# take away overlay just in case we got weird rolls
		self.SetRangeOverlay(row, 0, 1, self.nCols,
					self.looks['rowRoll']['bgColor'] + (ROLLOVERLAYER,), False)
		if on:
			self.SetRangeOverlay(row, 0, 1, self.nCols,
					self.looks['rowRoll']['bgColor'] + (ROLLOVERLAYER,), on)

	@staticmethod
	def setLook(look, attrs, skipAttrs=None):
		if not attrs:
			return
		if skipAttrs is None:
			skipAttrs = set()
		else:
			skipAttrs = set(skipAttrs)
		attrNames = {'bgColor', 'textColor', 'rowHeight', 'textOffsetX',
					 'textOffsetY', 'fontSizeX', 'fontFace', 'fontBold',
					 'fontItalic','leftBorderInColor', 'rightBorderInColor',
					 'topBorderInColor', 'bottomBorderInColor',
					 'leftBorderOutColor', 'rightBorderOutColor',
					 'topBorderOutColor', 'bottomBorderOutColor',
					 'sizeInPoints'}
		for attrName in attrNames.difference(skipAttrs):
			if attrName in look:
				setattr(attrs, attrName, look[attrName])

	@staticmethod
	def LoadLook(textTop):
		lookDict = dict()
		lookDict['name'] = textTop.name
		lookDict['textOffsetX'] = textTop.par.position1.eval()
		lookDict['textOffsetY'] = textTop.par.position2.eval()
		lookDict['rowHeight'] = textTop.par.resolution2.eval()
		lookDict['fontBold'] = textTop.par.bold.eval()
		lookDict['fontItalic'] = textTop.par.italic.eval()
		lookDict['fontSizeX'] = textTop.par.fontsizex.eval()
		lookDict['sizeInPoints'] = textTop.par.fontsizexunit.eval() == 'points'
		if textTop.par.font.eval() in textTop.par.font.menuNames:
			lookDict['fontFace'] = textTop.par.font.menuLabels[
					textTop.par.font.menuNames.index(textTop.par.font.eval())]
		lookDict['wordWrap'] = textTop.par.wordwrap.eval()
		textColor = ('fontcolorr', 'fontcolorg', 'fontcolorb', 'fontalpha')
		lookDict['textColor'] = \
					tuple(getattr(textTop.par, i).eval() for i in textColor)
		# textjustify
		justifyString = textTop.par.aligny.eval().upper() \
						+ textTop.par.alignx.eval().upper()
		if justifyString == 'CENTERCENTER':
			justifyString = 'CENTER'
		lookDict['textJustify'] = getattr(JustifyType, justifyString)
		# bgcolor
		bgColor = ('bgcolorr', 'bgcolorg', 'bgcolorb', 'bgalpha')
		lookDict['bgColor'] = \
					tuple(getattr(textTop.par, i).eval() for i in bgColor)
		# borders
		borderAPars = ['borderar', 'borderag', 'borderab', 'borderaalpha']
		borderBPars = ['borderbr', 'borderbg', 'borderbb', 'borderbalpha']
		borderAColor = \
					tuple(getattr(textTop.par, i).eval() for i in borderAPars)
		borderBColor = \
					tuple(getattr(textTop.par, i).eval() for i in borderBPars)
		borderStatePars = []
		for side in ('left', 'right', 'top', 'bottom'):
			for location in (('In','i'), ('Out','')):
				lookKey = side + 'Border' + location[0] + 'Color'
				stateParName = side + 'border' + location[1]
				borderStatePars.append(stateParName)
				borderType = getattr(textTop.par, stateParName).eval()
				if borderType == 'off':
					lookDict[lookKey] = None
				elif borderType == 'bordera':
					lookDict[lookKey] = borderAColor
				else:
					lookDict[lookKey] = borderBColor

		### If we decide to automate readonly pars in look TOPs:
		# usedPars = ['position1', 'resolution2', 'bold', 'italic', 'fontsizex',
		# 			'font', 'wordwrap', 'fontcolorr', 'aligny', 'alignx',
		# 			'bgcolorr', 'bgalpha', 'fontalpha', 'text'] \
		# 				+ borderAPars + borderBPars + borderStatePars
		# for p in textTop.pars():
		# 	p.readOnly = True
		# for pName in usedPars:
		# 	textTop.par[pName].readOnly = False

		#currently not implemented
		#padding = ['borderspace1','borderspace1','borderspace2','borderspace2']
		return lookDict

	# endregion

	###########################################################################
	# region drag and drop

	def onDropOrHover(self, isHover, comp, row, col, coords, prevRow, prevCol,
					  prevCoords, dragItems):
		if isHover:
			about = "Return True if interested in the drop"
			callback = "onDropHover"
		else:
			about = "Return True if the drop was used"
			callback = "onDrop"

		# drop highlight info
		dropHighlightMenu = self.ownerComp.par.Drophighlight.eval()
		cellAttribs = self.ownerComp.cellAttribs
		dropPos = None
		if row is not None:
			define = self.configComp.op('define')
			if dropHighlightMenu == 'Off':
				dropPos = row - self.AutoHeaderRows
				dropHighlightPos = None
			elif dropHighlightMenu == 'Above_Row':
				dropAttribName = 'topBorderOutColor'
				if row == 0 and self.header:
					dropPos = 0
					dropHighlightPos = 1
				elif row == -1:
					dropPos = self.nRows
					dropHighlightPos = self.nRows - 1
					dropAttribName = 'bottomBorderOutColor'
				else:
					dropPos = row - self.AutoHeaderRows
					dropHighlightPos = row
			elif dropHighlightMenu == 'Below_Row':
				dropAttribName = 'bottomBorderOutColor'
				if row == 0 and self.header:
					dropPos = 0
					dropHighlightPos = 0
				elif row == -1:
					dropPos = self.nRows
					dropHighlightPos = self.nRows - 1
					dropAttribName = 'bottomBorderOutColor'
				else:
					dropPos = row - self.AutoHeaderRows + 1
					dropHighlightPos = row
			elif dropHighlightMenu == 'Row':
				dropAttribName = 'bgColor'
				if row == 0 and self.header:
					dropPos = 'header'
					dropHighlightPos = 0
				elif row == -1:
					dropPos = -1
					dropHighlightPos = None
				else:
					dropPos = row - self.AutoHeaderRows
					dropHighlightPos = row
			elif dropHighlightMenu == 'Cell':
				dropAttribName = 'bgColor'
				if row == 0 and self.header:
					dropPos = ('header', col)
					dropHighlightPos = (row, col)
				elif row == -1:
					dropPos = (-1, -1)
					dropHighlightPos = None
				else:
					dropPos = (row - self.AutoHeaderRows, col)
					dropHighlightPos = (row, col)

		# remove old highlight
		if self.dropHighlightInfo:
			if dropHighlightMenu == 'Cell':
				setattr(cellAttribs[self.dropHighlightInfo['pos'][0],
									self.dropHighlightInfo['pos'][1]],
						self.dropHighlightInfo['attr'],
						self.dropHighlightInfo['vals'][0])
			else:
				for c in range(self.nCols):
					setattr(cellAttribs[self.dropHighlightInfo['pos'], c],
										self.dropHighlightInfo['attr'],
										self.dropHighlightInfo['vals'][c])
			self.dropHighlightInfo = None

		# callback
		if not dragItems:
			return
		info = {'prevRow':prevRow, 'prevCol': prevCol, 'dragItems': dragItems,
				'about': about, 'dropPos': dropPos}
		dragItem = dragItems[0]
		# special info from other listers
		if isinstance(dragItem, listCOMP) and \
											hasattr(dragItem.ext, "ListerExt"):
			info['fromListerInfo'] = dragItem.DropInfo
		else:
			info['fromListerInfo'] = None
		retVal = self.DoCellCallback(callback, row, col, info)
		if retVal:
			# add highlight if hover
			if isHover and retVal['returnValue'] and dropHighlightMenu != 'Off'\
						and dropHighlightPos is not None and row is not None:
				lineColor, overlayColor = ([float(x) for x in
											define[entry, 1].val.split()]
										   for entry in
										   ['dragDropLineColor',
											'dragDropOverlayColor'])
				self.dropHighlightInfo = {'pos': dropHighlightPos,
										  'attr': dropAttribName,
										  'vals': []}
				if dropHighlightMenu in ['Cell', 'Row']:
					row, cols = (dropHighlightPos, range(self.nCols))\
									if dropHighlightMenu == 'Row' \
										else (dropHighlightPos[0],
											  [dropHighlightPos[1]])

					for c in cols:
						attribs = cellAttribs[row, c]
						oldColor = getattr(attribs, dropAttribName)
						# strore value for restore
						self.dropHighlightInfo['vals'].append(oldColor)
						setattr(attribs, dropAttribName, mixColor(oldColor,
																  overlayColor))
				else:
					for c in range(self.nCols):
						attribs = cellAttribs[dropHighlightPos, c]
						# strore value for restore
						self.dropHighlightInfo['vals'].append(
									 		getattr(attribs, dropAttribName))
						setattr(attribs, dropAttribName, lineColor)

			# return value to internal callback
			return retVal['returnValue']
		else:
			return False

	# endregion

	###########################################################################
	# region parameters

	def OnParValueChange(self, par, val, prev):
		if par.name in ['Rowstriping', 'Autodefinecols', 'Header',
						'Linkedtable', 'Filtercols', 'Filterstring', 'Rawdata',
						'Advancedcallbacks', 'Inputtablehasheaders']:
			self.Refresh()
			if par.name in ['Header', 'Inputtablehasheaders']:
				self.SelectColumn(None)
				if self.ownerComp.par.Autodefinecols:
					self.SelectedRows = []
					self.setupAutoColDefine(clear=True)
					self.Refresh()
		elif par.name in ['Sortcols', 'Sortreverse']:
			self.Sort()
		elif par.name in ['Selectedrows']:
			self.onParSelectrowsChange(val, prev)
		elif par.name == 'Clickableheader':
			self.SelectColumn(None)
		elif par.name == 'Selectablerows':
			if not par.eval():
				self.SelectedRows = []
		elif par.name == 'Advancedcallbacks':
			self.doAdvancedCallbacks = par.eval()

	# par callback
	def onParSelectrowsChange(self, val, prev):
		try:
			newRows = parStringToIntList(val)
		except:
			self.SelectedRows = []
			print('Invalid Selected Rows', val)
			raise
		if newRows != self.SelectedRows:
			self.SelectedRows = newRows

	def OnParPulse(self, par):
		if par.name == 'Refresh':
			self.loadLooks()
			self.Refresh()
		elif par.name == 'Recreateautocolumns':
			self.setupAutoColDefine(clear=True)
		elif par.name == 'Editcallbacks':
			dat = self.ownerComp.par.Callbackdat.eval()
			if dat:
				if dat.pars('edit'):
					dat.par.edit.pulse()
			else:
				print("No callback dat for", self.ownerComp.path)
		elif par.name == 'Editconfigcomp':
			TDF.showInPane(self.ownerComp.par.Configcomp.eval(), 'Floating',
						   True)
		elif par.name == 'Helppage':
			ui.viewFile('https://docs.derivative.ca/index.php?'
						'title=Palette:lister')
		elif par.name == 'Copyautocolstoconfig':
			colDefine = self.ownerComp.par.Configcomp.eval().op('colDefine')
			colDefine.text = self.autoColDefine.text
			print("Copied autoColDefine to " + colDefine.path)
		elif par.name == 'Editcoldefine':
			self.ownerComp.par.Configcomp.eval().\
											op('colDefine').openViewer()

	# endregion

	###########################################################################
	# region properties

	@property
	def ColumnDict(self):
		"""
		column: column number
		"""
		return self.columnDict

	@property
	def ColNumDict(self):
		"""
		column number: column
		"""
		return self.colNumDict

	@property
	def AutoHeaderRows(self):
		"""
		This is one if a header row was generated. Otherwise 0.
		If we are using the top row of Data, this is 0.
		"""
		return 1 if self.header and self.autoHeader else 0

	@property
	def RolledRow(self):
		return self.rolledRow

	@property
	def Looks(self):
		return self.looks

	@property
	def OwnerComp(self):
		return self.OwnerComp

	@property
	def ColDefine(self):
		return self._colDefine.val

	@property
	def ConfigComp(self):
		return self.configComp

	@property
	def CustomDefine(self):
		return self.customDefine

	@property
	def SortCols(self):
		try:
			cols = parStringToIntList(self.ownerComp.par.Sortcols.eval())
		except:
			cols = []
		return reversed(cols)
	@SortCols.setter
	def SortCols(self, value):
		self.ownerComp.par.Sortcols.val = listToParString(value)

	@property
	def SortReverse(self):
		return self.ownerComp.par.Sortreverse.eval()
	@SortReverse.setter
	def SortReverse(self, value):
		self.ownerComp.par.Sortreverse.val = value

	@property
	def FilterCols(self):
		try:
			cols = parStringToIntList(self.ownerComp.par.Filtercols.eval())
		except:
			cols = []
		return cols
	@FilterCols.setter
	def FilterCols(self, value):
		self.ownerComp.par.Filtercols.val = listToParString(value)

	@property
	def SelectedRows(self):
		return self._SelectedRows.val.copy()
	@SelectedRows.setter
	def SelectedRows(self, value):
		if isinstance(value, collections.abc.Iterable):
			newRows = []
			for i in value:
				if isinstance(i, int):
					if i not in newRows:
						newRows.append(i)
				else:
					raise TypeError('SelectedRows entry must be int', i)
			oldRows = self._SelectedRows.val
			self._SelectedRows.val = newRows
			# DEBUG print("SelectedRows setter:",oldRows, newRows)
			for r in oldRows:
				self.SetRowLook(r, None, 'rowSelect', SELECTOVERLAYER)
				if r not in newRows and 0 <= r < len(self.Data):
					self.doDeselectRowCallback(r)
			for r in newRows:
				self.SetRowLook(r, 'rowSelect', True, SELECTOVERLAYER)
				if r not in oldRows and 0 <= r < len(self.Data):
					self.doSelectRowCallback(r)
			self.ownerComp.par.Selectedrows.val = listToParString(value)
		else:
			raise TypeError('Invalid value for Lister.SelectedRows', value)


	@property
	def FilterString(self):
		return self.ownerComp.par.Filterstring.eval()
	@FilterString.setter
	def FilterString(self, value):
		self.ownerComp.par.Filterstring.val = value

	@property
	def SelectedCell(self):
		return self.selectedCell

	@property
	def SelectedCol(self):
		"""
		This is the column selected by clicking in the header.
		"""
		return self.selectedCol
	@SelectedCol.setter
	def SelectedCol(self, value):
		self.selectedCol = value
		self.FilterCols = [value]
		self.SortCols = [value]

	@property
	def OutTables(self):
		"""
		Tables lister outputs to. Lister only receives Data from Linked Table.
		"""
		return [self.linkedTable] if self.linkedTable else []

	@property
	def SyncTable(self):
		inTable = self.ownerComp.par.Inputtabledat.eval()
		if inTable and self.ownerComp.par.Autosyncinputtable.eval() and \
					self.ownerComp.par.Inputtablehasheaders.eval():
			return inTable
		else:
			return None

	@property
	def InputTable(self):
		return self.inputTable

	# endregion

	pass

###########################################################################
# region utility functions

def parStringToIntList(parString):
	return [int(x) for x in parString.split()]

def listToParString(l):
	return ' '.join([str(x) for x in l])

def mixColor( originalColor, overColor):
	"""
	Use overColor's alpha to overlay it on top of original Color
	Color parameters in form [r, g, b, a]
	Returns [r, g, b, 1]
	"""
	alpha = overColor[3]
	if alpha == 1:
		return overColor[:4]
	else:
		out = [0, 0, 0, 1]
		for i in range(3):
			out[i] = originalColor[i] * (1 - alpha) + overColor[i] * alpha
		return out

def makeint(s):
	try:
		return int(s)
	except:
		return 0


def makefloat(s):
	try:
		return float(s)
	except:
		return 0

def makeversion(s):
	try:
		return LooseVersion(s)
	except:
		return LooseVersion(0)


# endregion

pass