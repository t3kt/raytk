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
import copy
import collections.abc
import traceback
import ast
from itertools import groupby
from CallbacksExt import CallbacksExt
from distutils.version import LooseVersion

TDF = op.TDModules.mod.TDFunctions
popDialog = op.TDResources.op('popDialog')

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
LOOKATTRS = {'bgColor', 'textColor', 'rowHeight', 'textOffsetX',
					'textOffsetY', 'fontSizeX', 'fontFace', 'fontFile',
					'fontBold',	'fontItalic', 'leftBorderInColor', 
					'rightBorderInColor', 'topBorderInColor', 
					'bottomBorderInColor', 'leftBorderOutColor', 
					'rightBorderOutColor', 'topBorderOutColor', 
					'bottomBorderOutColor', 'sizeInPoints',
					'wordWrap'}
LOOKPARS = { #convert textTOP pars to textCOMP for look conversion
	'fontsizex': 'fontsize',
	'fontsizexunit': 'fontsizeunits',
	'positionx': 'textoffsetx',
	'positiony': 'textoffsety',
	'positionunit': 'textoffsetunits',
	'resolutionw': 'w',
	'resolutionh': 'h',
}

MOUSECHOP : mouseinCHOP = op.TDResources.MouseCHOP

class ListerExt(CallbacksExt):

	# region main

	def __init__(self, ownerComp):
		# config stuff
		self.ownerComp : listCOMP = ownerComp
		self.configComp = ownerComp.par.Configcomp.eval()
		if self.configComp is None:
			raise Exception("Invalid Config Comp (see Advanced parameter page)")
		self.colDefine = None # non-dependable for speed
		self._colDefine = tdu.Dependency(None) # dependable for promotion
		self.customDefine = self.configComp.op('define')
		self.defaultConfig = ownerComp.op('configDefault')
		self.inputTable = self.ownerComp.op('inputTableFinal')
		self.autoColDefine = self.ownerComp.op('autoColDefine')
		self.autoColDefineDefaults = ownerComp.op('autoColDefineDefaults')	
		self.outLinked = self.ownerComp.op('outLinked')
		self.outLinkedCon = self.ownerComp.outputConnectors[0]
		self.outLinkRun = None # run object for once-per-frame update
		self.linkedTable = None # chosen in parameter. Set in Refresh
		self.settings = self.configComp.op('settings')
		self.callbackDat = self.ownerComp.par.Callbackdat.eval()
		try:
			self.fixConfig()
		except:
			# do our best to fix stuff for users, but sometimes they have
			# made changes beyond simple updates...
			pass
		self.ownerComp.par.Header.enable = True
		self.header = self.ownerComp.par.Header.eval() \
					  					and self.ownerComp.par.Header.enable
		self.AutoFilter = True  # do automated filtering behavior of Data
		self.AutoSort = True  # built in sorting behavior
		self.setupSelectedCol()
		
		# Data
		self.inputHasHeader = None # True if input table has header row
		self.rawData = []  # all Data available
		self.workingData = []  # post filter, post sort Data
		self.Data = []  # final Data, laid out in an dict
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
		self.refreshRun = None # delayed command for refresh
		self.resetRun = None # delayed command for reset
		self.sizeColInfo = {'active': False, 'leftCol': None, 'rightCol': None,
				'startPos': None, 'stretchy': None, 'leftStretch': None,
				'rightStretch': None, 'leftMin': None, 'rightMin': None,
		      	'startLeftWidth': None, 'startRightWidth': None, 'run': None, 
				'lastMouseX': None, 'ownerWidth':None} # info for sizing cols 
		self._SelectedRows = tdu.Dependency()
		self.sizedColWidths = {}
		if not self.ownerComp.par.Saveselectedrows:
			self._SelectedRows.val = oldSelected = []
		else:
			self._SelectedRows.val = oldSelected = [int(r) \
						for r in self.ownerComp.par.Selectedrows.eval().split()]
		self.dropHighlightInfo = None # current dropHighlight info
		self.dragToRow = None # the row we are dragging to
		self.dragRowColors = None # stores previous color info
		self.doAdvancedCallbacks = self.ownerComp.par.Advancedcallbacks.eval()
		if not self.ownerComp.par.Savesort:
			self.ownerComp.par.Sortcols = ''
			self.ownerComp.par.Sortreverse = False
		if not self.ownerComp.par.Savefilter:
			self.ownerComp.par.Filtercols = ''
		
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
		if not self.ownerComp.par.Saveselectedrows:
			self.SelectedRows = []
		else:
			self.SelectedRows = oldSelected
		run("op(" + str(ownerComp.id) + ").PostInit() "
				"if op(" + str(ownerComp.id) + ") and "
				"hasattr(op(" + str(ownerComp.id) + "), 'PostInit') else None",
				endFrame=True, delayRef=op.TDResources) # scrollbar reset
		# version hack
		self.ownerComp.par.Editcoldefine.enable = True
		# DEBUG print('Lister init done')
		# import traceback; traceback.print_stack()

	def PostInit(self):
		# cheap version update
		if self.ownerComp.par.enablecloning.eval() and \
					self.ownerComp.par.clone.eval() and \
					not self.ownerComp.par.clone.eval() == self.ownerComp and\
					self.ownerComp.par.clone.eval().par.enablecloning.eval():
			self.ownerComp.par.Version = \
							self.ownerComp.par.clone.eval().par.Version.eval()
			self.ownerComp.par.Toxsavebuild = \
					self.ownerComp.par.clone.eval().par.Toxsavebuild.eval()
		self.initialized = True
		self.setupAutoColDefine()
		self.checkLegacyDragDrop()
		#self.ownerComp.scroll(0,0)
		self.DoCallback('onPostInit', {'listerExt': self})
		self.doReset()

	def FrameRefresh(self):
		"""
		Re-init table at end of frame, refreshing all Data and formatting all 
		cells. Using this function will only cause one refresh per frame. To
		immediately refresh, use Refresh()
		"""
		#debug('======================FrameRefresh', absTime.frame)
		if self.refreshRun is None:
			self.refreshRun = run('args[0]()', self.Refresh, endFrame=True,
											delayRef=op.TDResources)

	def Refresh(self, pulseReset=True):
		"""
		Re-init table, refreshing all Data and formatting all cells
		"""
		#debug('**************************Refresh', absTime.frame)
		try:
			self.refreshRun.kill()
		except:
			pass
		self.refreshRun = None

		# parameters
		self.header = self.ownerComp.par.Header.eval() \
					  					and self.ownerComp.par.Header.enable
		self.linkedTable = self.ownerComp.par.Linkedtable.eval()
		if self.initialized:
			self.cookOutLinked()
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
			self.colDefine = self._colDefine.val = self.autoColDefine
			self.setupAutoColDefine()
			columns = [c.val for c in self.colDefine.row('column')[1:]]
			self.columnDict = dict((columns[i], i) for i in range(len(columns)))
			self.colNumDict = {v: k for k, v in self.columnDict.items()}

		# check for valid column names
		if len(columns) != len(set(columns)):
			dupes = set()
			for colName in columns:
				if columns.count(colName) > 1:
					dupes.add(colName)
			raise Exception(
					f'Duplicate column name{"" if len(dupes) == 1 else "s"}: '\
							f'{", ".join(dupes)}')

		# process workingData
		self.ConvertData()
		for i, workingDataRow in enumerate(self.workingData):
			workingDataRow.insert(-1, i + self.inputHasHeader)

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
			defaultHeaders += ['Auto-Header', None] # sourceIndex, rowObject
			self.workingData.insert(0, defaultHeaders)

		# create Data as list of Dicts
		self.Data = []
		for i, d in enumerate(self.workingData):
			formattedData = self.WorkingDataToDataRow(d, d[-2])
			self.Data.append(formattedData)

		self.Filter()
		
		self.nCols = self.colDefine.numCols - 1
		if self.nCols < 1:
			self.nRows = 0
		else:
			self.nRows = len(self.Data)
		self.Sort(False)
		self._SelectedRows.val = []
		self.restorePreviousSelection(oldData, oldSelectedRows)
		self.testAllowEmptySelection()
		self.ownerComp.par.Selectedrows.val = listToParString(
														self._SelectedRows.val)

		self.DataChanged(pulseReset=pulseReset)
		# callback
		self.DoCallback('onRefresh', {'listerExt': self})
		# debug('refresh', self.ownerComp)

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
				if newRowNum is None and \
									self.ownerComp.par.Saveseloninputchange:
					newRowNum = oldRow
				if newRowNum == 0 and self.header:
					# if header was just turned on this can happen
					newRowNum = None
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

	def MoveRows(self, rowList, destination, outTableSync=True):
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
			# deal with sync'd table info
			if outTableSync and self.SyncTable:
				syncTable = self.SyncTable
				sourceRowNum = rownum + offset + int(not self.header)
				destRowNum = dest + int(not self.header)
				rowData = [c.val for c in syncTable.row(sourceRowNum)]
				syncTable.deleteRow(sourceRowNum)
				syncTable.insertRow(rowData, destRowNum)
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

	def DeleteRow(self, row):
		"""
		Delete a row
		"""
		self.DeleteRows([row])

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
			if self.rolledCell and self.rolledCell[0] == row:
				self.rolledCell = None
			if self.rolledRow == row:
				self.rolledRow = None
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
			formattedData = dict()
			for c in range(self.nCols):
				colName = self.colNumDict[c]
				formattedData[colName] = rowData[colName]
		elif rowObject != '__no__object__':
			formattedData = self.RowObjectToDataRow(rowObject)
			callbackInfo['rowObject'] = rowObject
		else:
			if rowDict is None:
				rowDict = {}
			formattedData = dict()
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

	def DataChanged(self, selectionObjects=None, pulseReset=True):
		"""
		Call this when you change the Lister's Data. Refreshes text and size.
		Does not get raw Data, convert Data, sort or filter.
		selectionObjects will be selected if present in rowObjects
		"""
		# DEBUG print ('DataChanged', len(self.Data), self.Data)
		self.nCols = self.colDefine.numCols - 1
		if self.nCols < 1:
			self.nRows = 0
		else:
			self.nRows = len(self.Data)
		self.doClick = False
		#self.rolledCell = None
		if selectionObjects is not None:
			self.SelectObjects(selectionObjects)
		self.DoCallback('onDataChanged')
		self.resetOwner(pulseReset)

	def resetOwner(self, pulseReset=True):
		# debug ("resetOwner")
		self._clickedOnce = False
		nRows = self.nRows - self.AutoHeaderRows
		if self.ownerComp.par.Inputtablehasheaders:
			nRows += 1
		for table in self.OutTables:
			table.setSize(nRows, self.nCols)
		syncTable = self.SyncTable
		if syncTable:
			syncTable.setSize(nRows, syncTable.numCols)
		if self.initialized and pulseReset:
			self.doReset()

	def doReset(self):
		"""
		Run the listCOMP reset once per frame only
		"""
		if self.resetRun is None:
			self.resetRun = run('args[0]()', self.ownerComp.reset, 
								endFrame=True, delayRef=op.TDResources)

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

	def RowObjectToDataRow(self, rowObject, sourceIndex=None):
		"""
		Convert a rowObject into a dict in the proper format for the 
		lister's Data dictionary.

		Args:
			rowObject: any valid row object (list, dict, or Python object), 
			sourceIndex: used to reference back to original data order. 
				Probably unnecessary if rows are being added manually.
		"""
		workingDataRow = self.rowObjectToWorkingData( rowObject)
		return self.WorkingDataToDataRow(workingDataRow, sourceIndex)

	def WorkingDataToDataRow(self, workingData, sourceIndex=None):
		"""
		Convert a list of data to a dict keyed by column names from
		colDefine. The final item will be the rowObject.

		If you don't need to alter the data in the columns, use 
		RowObjectToDataRow instead.

		Args:
			workingData: a list of data corresponding to each column of the 
				lister, followed by the original row object.
			sourceIndex: used to reference back to original data order. 
				Default is to add to the end.				
		"""
		stringData = workingData[:-1]
		if sourceIndex is None:
			sourceIndex = len(self.Data) + self.AutoHeaderRows
		try:
			return dict(
						[(self.colNumDict[i], stringData[i]) \
										for i in range(len(self.colNumDict))]
					+ [('sourceIndex', sourceIndex)]
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
		self.inputHasHeader = False
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
				if len(self.rawData) > 1:
					self.rawData = self.stringListToDictList(self.rawData)
				self.inputHasHeader = True
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
					if len(self.rawData) > 1:
						self.rawData = self.stringListToDictList(self.rawData)
					self.inputHasHeader = True
		if self.inputHasHeader and self.rawData \
				and not isinstance(self.rawData[0], dict) \
				and (not self.ownerComp.par.Autodefinecols \
		  				or not self.ownerComp.par.Header):
			self.rawData = self.rawData[1:]
		self.workingData = None
		returnDict = self.DoCallback('onGetRawData', { 'listerExt': self,
											 'data': self.rawData, 'about':
									'Return the raw Data for Lister. ' +
					'Usually a list of objects, dicts, or string lists'})
		if returnDict is not None and \
						returnDict.get('returnValue', None) is not None:
			self.rawData = returnDict['returnValue']

	def datPathToStringList(self, path, testOnly=False):
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
		Convert a list of lists of strings into a list of dictionaries.
		Used to convert tableDATs with headers into dicts. Does not output 
		header row!

		Args:
			stringList: a list of lists of strings, first item is expected to be
			used as dict keys. Must have 2 items to return anything.

		Returns: a list of dicts

		"""
		dictList = []
		if len(stringList) < 2:
			return dictList
		keys = stringList[0]
		for data in stringList[1:]:
			entry = dict()
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
		dataKeys = list(rowObject.keys()) \
								if isinstance(rowObject, dict) else None
		for dataCell in self.colDefine.row('sourceDataMode')[1:]:
			if dataCell.val == 'constant':
				convertedCell = self.colDefine['sourceData',
												   dataCell.col].val
			elif dataCell.val == 'eval':
				sourceData = self.colDefine['sourceData', dataCell.col].val
				if sourceData.strip():
					convertedCell = eval(sourceData, {'object':rowObject,
													'rowObject':rowObject})
				else:
					convertedCell = ''
			elif dataCell.val == 'rowNum':
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
						key = self.colDefine['sourceData', dataCell.col].val
						if not key:
							key = self.colDefine['column', dataCell.col].val
						convertedCell = rowObject[key]
					except:
						convertedCell = None
					#debug(key, column, dataIndex, convertedCell)
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
		Filter Data
		"""
		badFilters = [col for col in self.FilterCols
					  			if col < 0 or col >= self.colDefine.numCols - 1]
		if badFilters:
			filterCols = list(self.FilterCols)
			for c in badFilters:
				filterCols.remove(c)
			self.FilterCols = filterCols
			#raise ValueError("Invalid filter column:", badFilters)
		if not self.Data:
			return
		if self.AutoFilter and self.FilterCols:
			if self.FilterString:
				filteredList = []
				if self.header:
					filteredList.append(self.Data[0])
				for rowNum, dataRow in enumerate(self.Data):
					if self.header and rowNum == 0:
						continue
					filterout = True
					for col in self.FilterCols:
						outputText = self.textFromData(rowNum, col)
						if self.FilterString.lower() in outputText.lower():
							filterout = False
							break
					if not filterout:
						filteredList.append(dataRow)
				self.Data = filteredList
		# user callback
		returnDict = self.DoCallback('onFilter', {'listerExt': self,
					'data': self.Data, 'about':'Return filtered Data'})
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
		if indexType == str:
			dataRows.sort(key=lambda x:x['sourceIndex'], 
							reverse=self.SortReverse)
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
								  self.autoColDefine, 
								  self.configComp.op('autoColDefineDefaults')]:
					if colDefine:
						for i, row in enumerate(defaultOp.rows()):
							rowName = row[0].val
							try:
								colDefine[rowName, 0].val
							except: 
								colDefine.insertRow([rowName] +
										[defaultOp[rowName, 1]]
												* (colDefine.numCols - 1), i)
								# debug('Updated', colDefine.path,'to include '
								# 		'"' + rowName +'" row. No further'
								# 		' action required. ')
			# copy any missing rows in define table
			elif defaultOp.name == 'define':
				defineTable = self.configComp.op('define')
				if defineTable:
					for i,row in enumerate(defaultOp.rows()):
						rowName = row[0].val
						try:
							defineTable[rowName, 0].val
						except:
							defineTable.insertRow(row, i)
							# debug('Added row', rowName, 'to', defineTable.path)

	def checkLegacyDragDrop(self):
		if self.CallbackDat:
			for callback in dir(self.CallbackDat.module):
				if callback.startswith('onDrop') \
						or callback.startswith('onDropHover'):
					self.ownerComp.store('legacyDragDrop', True)
					return
		self.ownerComp.unstore('legacyDragDrop')

	def RecreateAutoColumns(self):
		self.setupAutoColDefine(True)
		self.Refresh()

	def setupAutoColDefine(self, clear=False):
		# width utilities
		masterLookOp = self.configComp.op('master')
		headerSelectOp = (self.ownerComp.par.Clickableheader != 'Off' and
							self.configComp.op('headerSelect')) or \
							self.configComp.op('header') or \
							masterLookOp
		textOffsetX = masterLookOp.par.position1 \
				if isinstance(masterLookOp, textTOP) else \
					masterLookOp.par.textoffsetx
		if self.header and self.ownerComp.par.Usesortindicatorchars \
					and self.ownerComp.par.Clickableheader != 'Off':
			sortWidth = headerSelectOp.evalTextSize(
							' ' + self.ownerComp.par.Sortchar.eval())[0]
			sortReverseWidth = headerSelectOp.evalTextSize(
						' ' + self.ownerComp.par.Sortreversechar.eval())[0]
			sortCharWidth = max(sortWidth, sortReverseWidth)
		else:
			sortCharWidth = 0
		def colWidth(tList):
			maxWidth = 10
			for i,t in enumerate(tList):
				if i == 0 and self.header:
					textWidth = headerSelectOp.evalTextSize(t)[0] + \
							sortCharWidth
				else:
					textWidth = masterLookOp.evalTextSize(t)[0]
				if textWidth > maxWidth:
					maxWidth = textWidth
			maxWidth += max(textOffsetX * 2, 10) + 1
			return math.ceil(maxWidth)
		# setup columns
		self.autoHeader = True
		colDefine = self.autoColDefine
		if clear:
			colDefine.clear(keepFirstCol=True)
		else:
			if not self.rawData:
				return
			Data = copy.copy(self.rawData)
			if isinstance(Data, DAT):
				Data = self.datPathToStringList(Data.path)
			# column info
			rowNames = [c.val for c in colDefine.col(0)]
			rowDefaults = {}
			for row in self.autoColDefineDefaults.rows():
				rowDefaults[row[0].val] = row[1].val
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
					textList = [r if isinstance(r,str)
											else str(r[col]) for r in Data]
					if column:
						colInfo[rowNames.index('column')] = column
					else:
						colInfo[rowNames.index('column')] = 'col' + str(col)
					width = colWidth(textList) if rowDefaults['width'] \
							== 'auto' else int(rowDefaults['width'])
					colInfo[rowNames.index('width')] = width if col != 0 else ''
					colInfo[rowNames.index('stretch')] = 1 if col == 0 else 0
					colDefine.appendCol(colInfo)
					# debug(colInfo)

			elif isinstance(row, dict):
				currentCols = [c.val for c in colDefine.row('column')[1:]]
				for colNum, column in enumerate(row.keys()):
					if column in currentCols:
						continue
					textList = [column] + [str(r[column]) for r in Data] 
					width = colWidth(textList) if rowDefaults['width'] \
							== 'auto' else int(rowDefaults['width'])
					# width = str(max([len(str(r[column])) for r in Data]+[2]) *
					# 							self.DefaultWidthMultiplier)
					colInfo[rowNames.index('sourceData')] = column
					colInfo[rowNames.index('column')] = column
					colInfo[rowNames.index('width')] = \
												width if colNum != 0 else ''
					colInfo[rowNames.index('stretch')] = 1 if colNum == 0 else 0
					colDefine.appendCol(colInfo)
			else: # objects don't do defaults
				if colDefine.numCols == 1:
					column = 'objects'
					textList = [str(r) for r in Data]
					width = colWidth(textList) if rowDefaults['width'] \
							== 'auto' else int(rowDefaults['width'])
					# width = str(max([len(str(r)) for r in Data]+[2]) *
					# 							self.DefaultWidthMultiplier)
					colInfo[rowNames.index('column')] = column
					colInfo[rowNames.index('width')] = ''
					colInfo[rowNames.index('stretch')] = 1

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

	def InitRow(self, row, stripingOnly=False):
		#debug('InitRow', row)
		if self.ownerComp.rowAttribs[row] is None:
			return
		if not stripingOnly:
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
		elif self.ownerComp.par.Rowstriping == 'Dividing_Line' and not stripingOnly:
			dividingLineColor = \
					[float(c) for c in self.configComp.op('define')
										['dividingLineColor',1].val.split()]
			try:
				self.ownerComp.rowAttribs[row].bottomBorderOutColor = \
					dividingLineColor
			except:
				debug('Init Row Error:', row, self.nRows, 
						self.ownerComp.par.rows.eval())

		if self.doAdvancedCallbacks and not stripingOnly:
			self.DoCallback('onInitRow', {'row': row})

	def InitCol(self, col, cellLookName=None):
		"""
		set columns attributes

		cellLookName: override the look in colDefine
		"""
		# DEBUG print('InitCol', col)
		colDefine = self.colDefine

		infoTypes = {'stretch': int, 'width': int, 'justify': str,
			   		'topFill': str,
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

			look = self.looks.get(info['cellLook']) if cellLookName is None \
								else self.looks.get(cellLookName)
			if look:
				attribs.textOffsetX = look['textOffsetX']
			else:
				attribs.textOffsetX = self.looks['master']['textOffsetX']
			#stretch and width
			if info['stretch']:
				attribs.colStretch = True
				attribs.colWidth = info['width']
			else:
				attribs.colStretch = False
				attribs.colWidth = self.sizedColWidths.get(col, info['width'])

			#fontBold

			if 'fontBold' in info and colDefine['fontBold', col + 1] and \
										colDefine['fontBold', col + 1].val:
				if info['fontBold']:
					attribs.fontBold = True
				else:
					attribs.fontBold = False
			#fontItalic
			if 'fontItalic' in info and colDefine['fontItalic', col + 1] and\
										colDefine['fontItalic', col + 1].val:
				if info['fontItalic']:
					attribs.fontItalic = True
				else:
					attribs.fontItalic = False
			# justify
			try:
				attribs.textJustify = getattr(JustifyType, info['justify'])
			except:
				if look:
					attribs.textJustify = look['textJustify']
				else:
					attribs.textJustify = self.looks['master']['textJustify']
			# topFill
			try:
				attribs.topFill = getattr(FillMode, info['topFill'])
			except:
				if look:
					attribs.topFill = look['topFill']
				else:
					attribs.topFill = self.looks['master']['topFill']					
			#draggable
			attribs.draggable = info['draggable']

	def onInitTable(self, attribs):
		"""
		Initialize table attribs in this order: table, cols, header row,
		 header cells, rows, cells
		"""
		if not self.initialized:
			# this avoids some strange timing bugs...
			run("args[0].par.reset.pulse() if args[0] else None",
				self.ownerComp, endFrame=True)
			return
		if self.refreshRun is not None:
			try:
				self.refreshRun
			except:
				pass
			else:
				self.FrameRefresh()
				return
		self.resetRun = None				
		if self.autoColDefine \
					and self.ownerComp.par.cols != self.colDefine.numCols - 1:
			self.RecreateAutoColumns()
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
		self.setLook(self.looks['master'], attribs, None)
		# cols
		for c in range(self.nCols):
			self.InitCol(c)
		# rows (header, if it exists, is row 0)
		for r in range(self.nRows):
			self.InitRow(r)	
			for c in range(self.nCols):
				self.InitCell(r, c)
		# if self.rolledRow:
		# 	try:
		# 		self.setRollOverlay(self.rolledRow, True)
		# 	except:
		# 		pass
		# if rolledCell:
		# 	try:
		# 		self.RollCell(rolledCell[0], rolledCell[1])
		# 	except:
		# 		pass
		# restore looks
		for r in self._SelectedRows.peekVal:
			self.SetRowLook(r, 'rowSelect', True, SELECTOVERLAYER)

		self.DoCallback("onInitTable", {'listerExt':self})

	# endregion

	###########################################################################
	# region text and sourceDataMode text interpreters

	def SetCellText(self, row, col, data, outTableSync=True):
		"""
		Use this to set a cell's text field.
		Sends change to Linked DAT and Synced Input DAT if outTableSync is true.
		This will use sourceDataMode effects, e.g. color will be updated.
		Returns old text.
		"""
		# DEBUG print ("SetCellText", row, col, data)
		attribs = self.ownerComp.cellAttribs[row, col]

		try:
			oldText = attribs.text
		except:
			return # HACK this only happens in weird cloning init cases
			#tdu.printStack()
			for i in range(0,row):
				print(self.ownerComp.cellAttribs[row,0].text)
			raise Exception("Badattribs", row, col, data,
							self.ownercomp.par.rows, self.ownercomp.par.cols)
			return
		# sourceDataMode processing
		
		try:
			sourceDataMode = self.colDefine["sourceDataMode", col+1].val
		except:
			debug('SetCellText error:', row, col, data)
			raise
		rowData = self.Data[row]
		rowObject = rowData['rowObject']
		sourceCol = self.colNumDict[col]
		if sourceDataMode == 'color':
			color, ctext = self.ProcessColorModeText(data)
			if color:
				color.append(COLORDATALAYER)
				self.SetCellOverlay(row, col, color)
		newText = self.textFromData(row, col, data)				
		# help
		help = self.colDefine['help', col + 1].val.strip()
		rowObject = self.Data[row]['rowObject']
		if help.startswith('*'):
			if not self.header or row > 0:
				if help == '*':
					attribs.help = newText
				else:
				# "object" left in for backwards compatibility, use "rowObject"
					attribs.help = eval(help[1:],{'object': rowObject,
													'rowObject': rowObject,
													'text': newText,
													'rowData': rowData})
			else:
				attribs.help = ''					
		# actual displayed text
		attribs.text = newText
		# Data
		# 	to actually change Data, set "text" above
		self.Data[row][sourceCol] = data
		# output tables...
		self.cookOutLinked()
		if outTableSync:
			tableRow = row - self.AutoHeaderRows
			if self.ownerComp.par.Inputtablehasheaders:
				tableRow += 1
			syncTable = self.SyncTable
			if syncTable and tableRow > 0:
				mode = self.colDefine['sourceDataMode', col+1]
				if mode in SYNCABLEDATAMODES:
					if syncTable.col(sourceCol):
						if mode == 'blank':
							cellText = data
						else:
							cellText = newText
						syncTable[tableRow, sourceCol] = \
										cellText if cellText is not None else ''
			for table in self.OutTables:
				if 0 <= tableRow < table.numRows and col < table.numCols:
					if data is None:
						table[tableRow, col].val = ''
					else:
						table[tableRow, col].val = data
		if self.doAdvancedCallbacks:
			self.DoCellCallback('onSetCellText', row, col, {'text': data,
														'displayText': newText,
														'oldText': oldText})
		return oldText

	def textFromData(self, row, col, data=None):
		"""
		Returns the actual displayed text after formatting etc.

		Args:
			row (int): destination row (for header calculations)
			col (int): destination col 
			data (str): text before formatting. If None, use current lister data

		Returns:
			newText (str): the actual text that would display in the cell
		"""
		# sourceDataMode processing
		if data is None:
			data = self.Data[row][self.colNumDict[col]]
		try:
			sourceDataMode = self.colDefine["sourceDataMode", col+1].val
		except:
			debug('SetCellText error:', row, col, data)
			raise
		rowData = self.Data[row]
		rowObject = rowData['rowObject']
		sourceCol = self.colNumDict[col]
		headerCell = self.header and row==0
		if sourceDataMode == 'color':
			color, newText = self.ProcessColorModeText(data)
		elif sourceDataMode == 'rowNum' and not headerCell:
			newText = data = str(row)
			self.Data[row][sourceCol] = str(row)
		elif sourceDataMode == 'sourceIndex' and not headerCell:
			newText = data = str(rowData['sourceIndex'])
		elif sourceDataMode == 'blank' and not (self.header and row==0):
			newText = ''
		else:
			newText = data
		if headerCell and col in self.SortCols \
					and self.ownerComp.par.Usesortindicatorchars:
			sortChar = self.ownerComp.par.Sortreversechar.eval() \
					if self.ownerComp.par.Sortreverse \
						else self.ownerComp.par.Sortchar.eval()
			if sortChar:
				newText += ' ' + sortChar
		# format
		if not headerCell:
			try:
				format = self.colDefine['textFormat', col+1].val.strip()
			except:
				format = ''
			if format:
				if skipError := format.startswith('*'):
					format = format[1:]
				if sourceDataMode == 'float':
					val = makefloat(newText)
				elif sourceDataMode == 'int':
					val = makeint(newText)
				else:
					val = data
				try:
					newText = TDF.formatString(format, 
											{'rowObject': rowObject,
					 						'text': newText,
											'val': val,
											'rowData': self.Data[row]})
				except Exception as e:
					if skipError:
						pass
					else:
						e.args = (e.args[0] +
							f'\nLister context: cell ({row}, {col})\n\t'
							f'Documentation: See "format" in'
							    f' https://docs.derivative.ca/'
								f'Experimental:Palette:lister#colDefine_table',)
						raise		
		return newText

	def cookOutLinked(self):
		def doCookOutLinked():
			# debug(self.Data[1])
			self.outLinkRun = None
			self.outLinked.cook(force=True)
		if self.outLinkedCon.connections:
			if self.outLinkRun is None:
				self.outLinkRun = run('args[0]()', doCookOutLinked, 
						endFrame=True, delayRef=op.TDResources)

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
		newSelected = []
		if row is None and not addRow:
			pass
		elif addRow is False:
			newSelected = [row]
		elif row not in self.SelectedRows:
			newSelected = self.SelectedRows + [row]
		if self.SelectedRows != newSelected:
			self.SelectedRows = newSelected

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

	def setupSelectedCol(self):
		"""
		Just takes best guess at selectedCol based on data
		"""
		clickable = self.ownerComp.par.Clickableheader.eval()
		sortCols = set(self.SortCols)
		filterCols = set(self.FilterCols)
		if 'Filter' in clickable and 'Sort' in clickable:
			cols = sortCols.intersection(filterCols)
		elif 'Filter' in clickable:
			cols = filterCols
		elif 'Sort' in clickable:
			cols = sortCols		
		else:
			cols = None	
		if cols:
			self.selectedCol = cols.pop()
		else:
			self.selectedCol = None


	# a column was selected.
	def SelectColumn(self, col, asClick=False):
		"""
		Select a column for filters and sorts
		"""
		# debug('Select Column', col)
		oldSelected = self.selectedCol
		if asClick:
			setFilter = 'Filter' in self.ownerComp.par.Clickableheader.eval()	
			setSort = 'Sort' in self.ownerComp.par.Clickableheader.eval()
			if setSort:
				if col == oldSelected:
					if col is not None:
						if self.SortReverse:
							self.SortReverse = False
							col = None
						else:
							self.SortReverse = True
				else:
					self.SortReverse = False
			else:
				if col == oldSelected:
					col = None
			if col is None:
				if setFilter:
					self.FilterCols = []
				if setSort:
					self.SortCols = []
			else:
				if setFilter:
					self.FilterCols = [col]
				if setSort:
					self.SortCols = [col]
		self.selectedCol = col
		if oldSelected != col and oldSelected is not None:
			self.SetCellLook(0, oldSelected, None)					
		if col is not None:
			# set look except textOffsetX
			attribs = self.ownerComp.cellAttribs[0, col]
			offsetX = attribs.textOffsetX	
			self.SetCellLook(0, col, 'headerSelect', True, COLOVERLAYER)
			attribs.textOffsetX = offsetX
		self.Refresh()
		self.DoCallback('onSelectColumn', {'col': col,
							'colName': list(self.columnDict.keys())[col]
											if col is not None else None})

	# endregion

	###########################################################################
	# region user interaction

	def onRollover(self, row, col, coords, prevrow, prevcol, prevcoords):
		if row == 0 and col not in NONCELL and self.header \
				and self.ownerComp.par.Sizablecols.eval() \
				and self.startSizeCol(col, coords, testOnly=True):
			self.ownerComp.par.cursor = 'arrowLeftRight'
		else:
			self.ownerComp.par.cursor = 'pointer'
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
			if self.ownerComp.par.Clickableheader.menuIndex:
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
						# set look, except textOffsetX
						if on:
							attribs = self.ownerComp.cellAttribs[row, col]
							offsetX = attribs.textOffsetX
							self.SetCellLook(row, col, look, True,
									ROLLOVERLAYER, doCallback=doCallbacks)
							attribs.textOffsetX = offsetX
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
					if isinstance(top, TOP) and attribs:
						attribs.top = top
			else:
				if topPath:
					top = self.configComp.op(topPath)
					attribs = self.ownerComp.cellAttribs[row, col]
					if isinstance(top, TOP) and attribs:
						attribs.top = top

	def ClickHeader(self, col):
		"""
		Perform a click on the given header cell.
		"""
		if self.ownerComp.par.Clickableheader.menuIndex:
			selectCol = col
			# select None if ctrl down
			if list(self.Data[0].values())[col]:
				if self.ownerComp.panel.ctrl.val:
					selectCol = None
			# select none if click on selected and already reversed			
			self.SelectColumn(selectCol, asClick=True)
			self.RollCell(0, col)
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
			if startrow == -1:
				self.SelectRow(None)
			elif self.header and startrow == 0:
				if self.ownerComp.par.Sizablecols.eval():
					self.startSizeCol(startcol, startcoords)
			else:
				if self.ownerComp.par.Selectablerows.eval() and \
								int('0' + self.colDefine['selectRow',
														 startcol+1].val):
					if self.ownerComp.par.Multiplerowselect.eval():
						# ctrl - add row
						if self.ownerComp.panel.ctrl.val:
							if startrow in self.SelectedRows:
								if self.ownerComp.par.Allowemptyselection\
										or len(self.SelectedRows) > 1:
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
						if self.ownerComp.panel.ctrl.val \
								and startrow in self.SelectedRows\
								and self.ownerComp.par.Allowemptyselection:
							self.DeselectRow(startrow)
						else:
							self.SelectRow(startrow)
				# drag rows must be initiated here
				if self.ownerComp.par.Dragtoreorderrows.eval() and \
									not (self.ownerComp.panel.ctrl.val
										or self.ownerComp.panel.shift.val) \
									and not self.ownerComp.par.Sortcols:
					self.testStartDragRows(startrow)
				# this makes select and rollover play nice
				self.setRollOverlay(startrow, False)
				self.setRollOverlay(startrow, True)
			self.PressCell(endrow, endcol)
		elif end:
			self.stopSizeCol()
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
					self.setRollOverlay(self.selectedCell[0], False)
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

	def startSizeCol(self, col, coords, testOnly=False):
		# SET this up later!
		# if not self.colDefine['sizable', col]:
		# 	return
		# if not self.ownerComp.par.Sizablecols:
		# 	return
		info = self.sizeColInfo
		if info['active']:
			self.stopSizeCol()
		width = self.ownerComp.displayColWidth(col)
		leftCol = None
		rightCol = None
		stretchy = any([self.ownerComp.displayAttribs[0, c].colStretch 
				  								for c in range(self.nCols)])
		# figure out the two columns the border is between and if they are 
		# valid for width changing
		if coords.x > width - 5 and (col + 1 < self.nCols 
				or (self.ownerComp.par.hscrollbar and not stretchy)):
			leftCol = col
			if col + 1 < self.nCols:
				rightCol = col + 1
		elif coords.x < 5 and col > 0:
			if stretchy:
				rightCol = col 
				leftCol = col - 1
		# make sure cols are sizable
		if stretchy:
			if (leftCol is not None and \
					not makebool(self.colDefine['sizable', leftCol + 1].val)) \
				or (rightCol is not None and \
					not makebool(self.colDefine['sizable', rightCol + 1].val)):
				leftCol = rightCol = None
		else:
			rightCol = None
			if leftCol is not None and \
					not makebool(self.colDefine['sizable', leftCol + 1].val):
				leftCol = None
		doSize = not(leftCol is None and rightCol is None)
		if testOnly:
			return doSize
		if not doSize:
			return

		info['active'] = True
		info['stretchy'] = stretchy
		info['leftCol'] = leftCol
		info['rightCol'] = rightCol
		if leftCol is not None:
			info['startLeftWidth'] = self.ownerComp.displayColWidth(leftCol)
			info['leftStretch'] = \
					self.ownerComp.displayAttribs[0, leftCol].colStretch
			if info['leftStretch']:
				try:
					info['leftMin'] = \
							int(self.colDefine['width', leftCol + 1].val)
				except:
					info['leftMin'] = 20				
			else:
				info['leftMin'] = 20
		else:
			info['startLeftWidth'] = None
			info['leftStretch'] = None
			info['leftMin'] = None
		if rightCol is not None:
			info['startRightWidth'] = self.ownerComp.displayColWidth(rightCol)
			info['rightStretch'] = \
					self.ownerComp.displayAttribs[0, rightCol].colStretch
			if info['rightStretch']:
				try:
					info['rightMin'] = \
							int(self.colDefine['width', rightCol + 1].val)
				except:
					info['rightMin'] = 20				
			else:
				info['rightMin'] = 20
		else:
			info['startRightWidth'] = None
			info['rightStretch'] = None
			info['rightMin'] = None
		info['startPos'] = MOUSECHOP['abs_mouse_x'].eval()
		info['ownerWidth'] = self.ownerComp.width \
			 					 - 14 if self.ownerComp.par.hscrollbar else 0
		info['run'] = run(self.whileSizeCol, 
										delayFrames=1, delayRef=op.TDResources)
		
	def stopSizeCol(self):
		info = self.sizeColInfo
		try:
			info['run'].kill()
		except:
			pass
		info['active'] = False
		info['lastMouseX'] = None
		# save new widths to column definitions
		leftCol = info['leftCol']
		rightCol = info['rightCol']
		if self.ownerComp.par.Savecolresizes:
			if leftCol is not None and not info['leftStretch']:
				self.colDefine['width', leftCol + 1] = \
						self.sizedColWidths[leftCol]
			if rightCol is not None and not info['rightStretch']:
				self.colDefine['width', rightCol + 1] = \
						self.sizedColWidths[rightCol]

	def whileSizeCol(self):
		# debug(self.sizeColInfo)
		info = self.sizeColInfo
		if info['lastMouseX'] != MOUSECHOP['abs_mouse_x'].eval():
			info['lastMouseX'] = MOUSECHOP['abs_mouse_x'].eval()
			offset = int(MOUSECHOP['abs_mouse_x'] - info['startPos'])
			leftCol = info['leftCol']
			rightCol = info['rightCol']
			newLeftWidth = info['startLeftWidth']
			newRightWidth = info['startRightWidth']
			leftMin = info['leftMin']
			rightMin = info['rightMin']
			if leftCol is not None:
				newLeftWidth = info['startLeftWidth'] + offset
			if info['stretchy'] or not self.ownerComp.par.hscrollbar:
				if rightCol is not None:
					newRightWidth = info['startRightWidth'] - offset
				if newRightWidth is not None \
						and newRightWidth < rightMin:
					if newLeftWidth is not None:
						newLeftWidth = newLeftWidth - (rightMin - newRightWidth)
					newRightWidth = rightMin
				elif newLeftWidth is not None \
						and newLeftWidth < leftMin:
					if newRightWidth is not None:
						newRightWidth = newRightWidth - (leftMin - newLeftWidth)
					newLeftWidth = leftMin
			else:
				if leftCol is not None and newLeftWidth < 20:
					newLeftWidth = 20
				rightCol = None
			# set new widths
			if leftCol is not None:
				self.ownerComp.colAttribs[leftCol].colWidth = \
						self.sizedColWidths[leftCol] = newLeftWidth
			if rightCol is not None:
				self.ownerComp.colAttribs[rightCol].colWidth = \
						self.sizedColWidths[rightCol] = newRightWidth
		info['run'] = run(self.whileSizeCol,
										delayFrames=1, delayRef=op.TDResources)

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
			if self.ownerComp.par.Clickableheader.menuIndex and \
									list(self.Data[0].values())[col]:
				# set look except textOffsetX
				attribs = self.ownerComp.cellAttribs[0, col]
				offsetX = attribs.textOffsetX					
				self.SetCellLook(0, col, 'headerPress', True, ROLLOVERLAYER)
				attribs.textOffsetX = offsetX
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
		#debug('a', row, col, overColor)
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
			self.setLook(look, attribs, ['textOffsetX'])
			if isinstance(self.configComp.op('header'), textCOMP):
				attribs.textJustify = look['textJustify']  
			attribs.fontFace = look['fontFace']
			attribs.fontFile = look['fontFile']
			attribs.fontItalic = look['fontItalic']
			attribs.bgColor = look['bgColor']
			attribs.textColor = look['textColor']
			attribs.fontBold = look['fontBold']
			attribs.wordWrap = look['wordWrap']
		attribs.draggable = False

		for col in range(self.nCols):
			if self.colDefine['justify', col + 1]:
				attribs = self.ownerComp.cellAttribs[0, col]
				attribs.textJustify = getattr(JustifyType, 
									self.colDefine['justify', col + 1].val)

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
			lookName: name of look (see textTOPs in config comp)
				Use None to unset individual cell look (goes back to col look)
				Use '' to remove column look and unset individual cell look
		"""
		if lookName == '':
			lookName = '__No look__'
		elif lookName is None:
			self.cellLookNames[(row, col)] = ''
			lookName = self.getCellLookName(row, col)
		self.cellLookNames[(row, col)] = lookName
		self.SetCellLook(row, col, None, True)
		self.SetCellLook(row, col, lookName)
		self.InitRow(row, stripingOnly=True)

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
		setAttribs = LOOKATTRS - {'bgColor', 'rowHeight'}
		if look:
			if overlay:
				self.SetCellOverlay(row, col, look['bgColor'] +	(overlayOrder,))
			else:
				attribs.bgColor = look['bgColor']
				try:
					self.overlays[(row,col)]['original'] = attribs.bgColor
				except:
					pass
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
		if not self.ownerComp.par.Highlightrollover.eval() or row in NONCELL:
			return
		# DEBUG print("setRollOverlay", row, on)
		# take away overlay just in case we got weird rolls
		self.SetRangeOverlay(row, 0, 1, self.nCols,
					self.looks['rowRoll']['bgColor'] + (ROLLOVERLAYER,), False)
		if on:
			self.SetRangeOverlay(row, 0, 1, self.nCols,
					self.looks['rowRoll']['bgColor'] + (ROLLOVERLAYER,), on)

	@staticmethod
	def setLook(look, attrs, skipAttrs='rowHeight'):
		if not attrs:
			return
		if skipAttrs is None:
			skipAttrs = set()
		else:
			skipAttrs = set(skipAttrs)
		attrNames = LOOKATTRS
		for attrName in attrNames.difference(skipAttrs):
			if attrName in look:
				setattr(attrs, attrName, look[attrName])

	def loadLooks(self, top=None):
		# table looks found in configComp textTOPs
		self.looks = {}
		if top is None:
			tops = self.configComp.findChildren(
					type=(textTOP, textCOMP), depth=1)
		else:
			tops = [top]
		for top in tops:
			if not top.lock:
				self.looks[top.name] = self.LoadLook(top)

	@staticmethod
	def LoadLook(lookOp):
		# lookOP is the operator in config defining the look
		isTOP = isinstance(lookOp, textTOP)
		lookDict = dict()
		lookDict['name'] = lookOp.name
		lookDict['rowHeight'] = lookOp.par.resolution2.eval() \
				if isTOP else lookOp.par.h.eval()
		lookDict['fontBold'] = lookOp.par.bold.eval()
		lookDict['fontItalic'] = lookOp.par.italic.eval()
		lookDict['fontSizeX'] = lookOp.par.fontsizex.eval() \
				if isTOP else lookOp.par.fontsize.eval()
		lookDict['sizeInPoints'] = (lookOp.par.fontsizexunit.eval() \
				if isTOP else lookOp.par.fontsizeunits.eval()) == 'points'
		if lookOp.par.font.eval() in lookOp.par.font.menuNames:
			lookDict['fontFace'] = lookOp.par.font.menuLabels[
					lookOp.par.font.menuNames.index(lookOp.par.font.eval())]
		else:
			lookDict['fontFace'] = ''
		if (ff:=lookOp.par.fontfile.eval()):
			lookDict['fontFile'] = ff
		else:
			lookDict['fontFile'] = ''
		lookDict['wordWrap'] = lookOp.par.wordwrap.eval()
		textColor = ('fontcolorr', 'fontcolorg', 'fontcolorb', 'fontalpha')
		lookDict['textColor'] = \
					tuple(getattr(lookOp.par, i).eval() for i in textColor)
		# textjustify
		justifyString = lookOp.par.aligny.eval().upper() \
						+ lookOp.par.alignx.eval().upper()
		if justifyString == 'CENTERCENTER':
			justifyString = 'CENTER'
		lookDict['textJustify'] = getattr(JustifyType, justifyString)
		#topFill
		try:
			topFillString = lookOp.par.topfill.eval().upper()
			if topFillString == 'OFF':
				topFillString = 'STRETCH'
		except:
			topFillString = 'STRETCH'
		lookDict['topFill'] = getattr(FillMode, topFillString)
		# textOffset x/y
		if lookDict['name'].startswith('header'):
			lookDict['textOffsetX'] = None
		else:
			lookDict['textOffsetX'] = (lookOp.par.positionx.eval() \
					if isTOP else lookOp.par.textoffsetx.eval())
		lookDict['textOffsetY'] = (lookOp.par.positiony.eval() \
				if isTOP else lookOp.par.textoffsety.eval()) 				
		# bgcolor
		bgColor = ('bgcolorr', 'bgcolorg', 'bgcolorb', 'bgalpha')
		lookDict['bgColor'] = \
					tuple(getattr(lookOp.par, i).eval() for i in bgColor)
		# borders
		borderAPars = ['borderar', 'borderag', 'borderab', 'borderaalpha']
		borderBPars = ['borderbr', 'borderbg', 'borderbb', 'borderbalpha']
		borderAColor = \
					tuple(getattr(lookOp.par, i).eval() for i in borderAPars)
		borderBColor = \
					tuple(getattr(lookOp.par, i).eval() for i in borderBPars)
		borderStatePars = []
		for side in ('left', 'right', 'top', 'bottom'):
			for location in (('In','i'), ('Out','')):
				lookKey = side + 'Border' + location[0] + 'Color'
				stateParName = side + 'border' + location[1]
				borderStatePars.append(stateParName)
				borderType = getattr(lookOp.par, stateParName).eval()
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
		"""
		Deals with drop highights and legacy ondrop and hover callbacks. 
		If new drag/drop callbacks are being used, this will only do relevant 
		highlighting.
		"""
		legacyMode = parent.Lister.fetch('legacyDragDrop', 0)

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
		dropHighlightPos = None
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
			if dropHighlightMenu in ['Cell']:
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
		if legacyMode:
			if not dragItems:
				return
			info = {'prevRow':prevRow, 'prevCol': prevCol, 
					'dragItems': dragItems,'about': about, 'dropPos': dropPos}
			dragItem = dragItems[0]
			# special info from other listers
			if isinstance(dragItem, listCOMP) and \
											hasattr(dragItem.ext, "ListerExt"):
				info['fromListerInfo'] = dragItem.DropInfo
			else:
				info['fromListerInfo'] = None
			retVal = self.DoCellCallback(callback, row, col, info)
		else:
			retVal = {'returnValue': True}
		if retVal or (not legacyMode and self.ownerComp.panel.dropready):
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
		if par.name in ['Header', 'Inputtablehasheaders', 
						'Usesortindicatorchars', 'Sortchar', 'Sortreversechar',
						'Clickableheader']:
			# self.SelectColumn(None)
			if par.name == 'Header' and par.eval():
				self.ownerComp.par.Inputtablehasheaders = True
			def delayChange():
				if self.ownerComp.par.Autodefinecols:
					self.SelectedRows = []
					self.setupAutoColDefine(clear=True)
				self.FrameRefresh()
			run('args[0]()', delayChange, delayFrames=1)
		elif par.name in ['Rowstriping', 'Autodefinecols', 
						'Linkedtable', 'Filtercols', 'Filterstring', 'Rawdata',
						'Advancedcallbacks', 'Sourceindexinoutput']:
			if par.name == 'Filtercols':
				self.setupSelectedCol()
			self.FrameRefresh()
			if par.name == 'Advancedcallbacks':
				self.doAdvancedCallbacks = par.eval()
		elif par.name in ['Sortcols', 'Sortreverse']:
			self.setupSelectedCol()
			self.Sort()
			# else:
			# 	self.FrameRefresh() 
		elif par.name in ['Selectedrows']:
			self.onParSelectrowsChange(val, prev)
		elif par.name == 'Clickableheader':
			self.setupSelectedCol()
			self.FrameRefresh()
		elif par.name == 'Selectablerows':
			if not par.eval():
				self.SelectedRows = []
		elif par.name == 'Drophighlight':
			self.dropHighlightInfo = None
		elif par.name in ['Callbackdat', 'Configcomp']:
			self.__init__(self.ownerComp)
		elif par.name == 'Allowemptyselection':
			self.testAllowEmptySelection()

	def testAllowEmptySelection(self):
		if not self.ownerComp.par.Allowemptyselection and not self.SelectedRows\
							and self.nRows > self.header:
				self.SelectedRows = [int(self.header)]

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
			self.Refresh()
		elif par.name == 'Recreateautocolumns':
			self.RecreateAutoColumns()
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
		# elif par.name == 'Helppage':
		# 	ui.viewFile('https://docs.derivative.ca/index.php?'
		# 				'title=Palette:lister')
		elif par.name == 'Copyautocolstoconfig':
			colDefine = self.ownerComp.par.Configcomp.eval().op('colDefine')
			colDefine.text = self.autoColDefine.text
			print("Copied autoColDefine to " + colDefine.path)
		elif par.name == 'Editcoldefine':
			if self.ownerComp.par.Autodefinecols.eval():
				def editcoldefine(info):
					if info['button'] == 'Cancel':
						return
					if info['button'] == 'Copy':
						self.OnParPulse(self.ownerComp.par.Copyautocolstoconfig)
					self.ownerComp.par.Autodefinecols = False
					self.OnParPulse(par)
				popDialog.OpenDefault(
					'You are currently using automatically defined columns.\n\n'
					'Manual: Switch to manual cols.\n'\
					'Copy: Copy current Auto-cols and switch to manual.',
					'Edit Column Definitions',
					buttons=['Manual', 'Copy', 'Cancel'],
					escButton=3, enterButton=1, callback=editcoldefine
					)
			else:
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
			if not self.ownerComp.par.Allowemptyselection and not newRows:
				newRows = [1 if self.header else 0]
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
		self.SelectColumn(value)

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

def makebool(s):
	return s not in ['', '0', 'False']

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