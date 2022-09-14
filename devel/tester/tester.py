from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, List, Optional
from raytkTest import TestCaseResult, TestFindingStatus, processTest
from raytkUtil import RaytkContext, recloneComp, Version

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from devel.components.testInspectorCore.testInspectorCore import TestInspectorCore

	class _Pars(ParCollection):
		Testcasefolder: 'StrParamT'
		Buildfolder: 'StrParamT'

	class _COMP(COMP):
		par: _Pars

	class _UiStatePars:
		Resultlevelfilter: 'StrParamT'
		Includealpha: 'BoolParamT'
		Includebeta: 'BoolParamT'
		Includedeprecated: 'BoolParamT'
		Running: 'BoolParamT'
		Filtertext: 'StrParamT'
	ipar.uiState = _UiStatePars()

	# noinspection PyTypeChecker
	iop.testInspectorCore = TestInspectorCore(COMP())

class TestManager:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.logTable = ownerComp.op('log')  # type: DAT
		self.currentTestName = tdu.Dependency()
		self.successCount = tdu.Dependency(0)
		self.warningCount = tdu.Dependency(0)
		self.errorCount = tdu.Dependency(0)
		self._caseResults = {}  # type: Dict[str, TestCaseResult]

	def onInit(self):
		self.resetAll()

	@property
	def _testHost(self) -> 'COMP':
		return self.ownerComp.op('test_host')

	@property
	def _testComp(self) -> 'Optional[COMP]':
		for o in self._testHost.children:
			return o

	@property
	def _testTable(self) -> 'DAT':
		return self.ownerComp.op('testTable')

	@property
	def _testQueue(self) -> 'DAT':
		return self.ownerComp.op('testQueue')

	@property
	def _resultTable(self) -> 'DAT':
		return self.ownerComp.op('resultTable')

	def reloadTestTable(self):
		self.ownerComp.op('test_folder').par.refreshpulse.pulse()

	def buildTestTable(self, dat: 'DAT', fileTable: 'DAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow([
			'name',
			'tox',
		])
		alpha = ipar.uiState.Includealpha
		beta = ipar.uiState.Includebeta
		deprecated = ipar.uiState.Includedeprecated
		filterText = ipar.uiState.Filtertext.eval().strip().lower()
		casesFolder = Path(self.ownerComp.par.Testcasefolder.eval())
		for row in range(1, fileTable.numRows):
			baseName = str(fileTable[row, 'basename'])
			relPath = str(fileTable[row, 'relpath'])
			if filterText:
				if '/' in filterText:
					if filterText not in relPath.lower():
						continue
				else:
					if filterText not in baseName.lower():
						continue
			if 'operators/' in relPath:
				opName = baseName.split('_', 1)[0]
				if not opTable[opName, 'name']:
					continue
				status = opTable[opName, 'status']
				if status == 'alpha' and not alpha:
					continue
				elif status == 'beta' and not beta:
					continue
				elif status == 'deprecated' and not deprecated:
					continue
			relFile = Path(relPath)
			toxFile = casesFolder / relFile
			dat.appendRow([
				relFile.with_suffix('').as_posix(),
				toxFile.as_posix(),
			])

	def buildToolkitVersionTable(self, dat: 'DAT', fileTable: 'DAT'):
		dat.clear()
		dat.appendRow(['name', 'label', 'version', 'tox'])
		dat.appendRow(['src', 'Current Source', '(current)', 'src/raytk.tox'])
		buildFolder = Path(self.ownerComp.par.Buildfolder.eval())
		for row in range(1, fileTable.numRows):
			relFile = Path(str(fileTable[row, 'relpath']))
			toxFile = buildFolder / relFile
			versionStr = toxFile.stem
			isExp = versionStr.endswith('-exp')
			if isExp:
				versionStr = versionStr.replace('-exp', '')
			if '-' in versionStr:
				versionStr = versionStr.split('-', 1)[1]
			try:
				version = Version(versionStr)
			except ValueError:
				version = None
			expSuffix = ' (exp)' if isExp else ''
			dat.appendRow([
				toxFile.stem,
				f'Build {version}{expSuffix}' if version else f'{toxFile.stem}{expSuffix}',
				f'{version or ""}{expSuffix}',
				toxFile.as_posix(),
			])

	def loadToolkitTox(self, toxPath: str):
		self.log(f'Loading toolkit tox {toxPath}')
		self._queueCall(self._loadToolkitTox, toxPath)

	def _loadToolkitTox(self, toxPath: str):
		toolkit = RaytkContext().toolkit()
		if toolkit:
			toolkit.par.externaltox = toxPath
			toolkit.par.reinitnet.pulse()
		else:
			toolkit = root.loadTox(toxPath)
			toolkit.name = 'raytk'
		# Do this early since it switches off things like automatically writing to the opList.txt file.
		# See https://github.com/t3kt/raytk/issues/95
		toolkit.par.Devel = False
		self.log('Finished loading toolkit')

	def queueFailedTests(self):
		resultTable = self.ownerComp.op('failedResultTable')
		if resultTable.numRows < 2 or not resultTable.col('case'):
			names = []
		else:
			names = [n.val for n in resultTable.col('case')[1:]]
		self.reloadTestTable()
		self._copyTestsToQueue(filterNames=names)

	def reloadTestQueue(self):
		self.reloadTestTable()
		self._copyTestsToQueue()

	def _copyTestsToQueue(self, filterNames: 'Optional[List[str]]' = None):
		queue = self._testQueue
		queue.clear()
		if filterNames is None:
			queue.appendCol(self._testTable.col('name')[1:])
		else:
			queue.appendCol([
				c
				for c in self._testTable.col('name')[1:]
				if c.val in filterNames
			])

	def clearResults(self):
		table = self._resultTable
		table.clear()
		table.appendRow(['case', 'path', 'status', 'source', 'message', 'detail'])
		self._caseResults = {}
		self.successCount.val = 0
		self.warningCount.val = 0
		self.errorCount.val = 0

	@property
	def hasResultCounts(self):
		return self.successCount.val > 0 or self.warningCount.val > 0 or self.errorCount.val > 0

	def _addResult(self, result: 'TestCaseResult'):
		self._caseResults[result.name] = result
		table = self._resultTable
		if not result.findings:
			table.appendRow([
				result.name,
				'',
				TestFindingStatus.success.name,
				'',
				f'No findings for case {result.name}',
			])
			self.successCount.val += 1
			return
		basePath = self._testComp.path + '/'
		if result.hasError:
			self.errorCount.val += 1
		elif result.hasWarning:
			self.warningCount.val += 1
		else:
			self.successCount.val += 1
		for finding in result.findings:
			table.appendRow([
				result.name
			] + finding.toTableRowVals(basePath, includeDetail=True))

	def cancelTestRun(self):
		if not ipar.uiState.Running:
			self.log('Already stopped, no canceling necessary')
			return
		self.log('Canceling test run...')
		ipar.uiState.Running = False

	def runQueuedTests(self):
		queue = self._testQueue
		if queue.numRows < 1:
			raise Exception('No tests queued!')
		self.clearResults()
		self.log(f'Running {queue.numRows} queued tests...')
		ipar.uiState.Running = True
		self._runNextTest(continueAfter=True)

	def runAllTests(self):
		self.reloadTestQueue()
		self.runQueuedTests()

	def _runNextTest(self, continueAfter=True):
		queue = self._testQueue
		if queue.numRows < 1:
			self._onQueueFinished()
			return
		name = str(queue[0, 0])
		queue.deleteRow(0)
		self.log(f'Running test {name}...')
		self.currentTestName.val = name
		self._queueCall(self._runNextTest_stage, 0, name, continueAfter)

	def _runNextTest_stage(self, stage: int, name: str, continueAfter: bool):
		if not ipar.uiState.Running:
			self.log('Canceled test run')
			return
		if stage == 0:
			tox = self._testTable[name, 'tox']
			if not tox:
				raise Exception(f'Unable to find tox for test {name!r}')
			self.loadTestTox(str(tox))
			self._queueCall(self._runNextTest_stage, stage + 1, name, continueAfter)
		elif stage == 1:
			self._processTest(lambda: self._runNextTest_stage(stage + 1, name, continueAfter))
		elif stage == 2:
			result = self._buildTestCaseResult()
			if result.hasError:
				self.log(f'Test {name} resulted in ERROR')
			elif result.hasWarning:
				self.log(f'Test {name} resulted in WARNING')
			else:
				self.log(f'Test {name} resulted in SUCCESS')
			self._addResult(result)
			self._queueCall(self._runNextTest_stage, stage + 1, name, continueAfter)
		elif stage == 3:
			self._unloadTestCase()
			self.log(f'Finished running test {name}')
			if continueAfter:
				self._queueCall(self._runNextTest, True)

	def _onQueueFinished(self):
		self.log('Finished running queued tests')
		ipar.uiState.Running = False
		ui.messageBox('Tests completed', 'Finished running tests!')

	def _unloadTestCase(self):
		self.currentTestName.val = None
		host = self._testHost
		for o in list(host.children):
			if not o.valid:
				continue
			# noinspection PyBroadException
			try:
				o.destroy()
			except:
				pass

	def loadTestTox(self, toxPath: str):
		self.log(f'Loading test {toxPath}')
		host = self._testHost
		host.loadTox(toxPath)
		self.log(f'Finished loading {toxPath}')

	def _processTest(self, thenRun: 'Callable'):
		comp = self._testComp
		processTest(comp, thenRun, log=self.log)

	def _buildTestCaseResult(self) -> 'Optional[TestCaseResult]':
		comp = self._testComp
		if not comp:
			raise Exception('No test loaded!')
		return TestCaseResult(
			name=self.currentTestName.val,
			findings=iop.testInspectorCore.GetFindings(),
		)

	def clearLog(self):
		self.logTable.clear()

	def log(self, message: str):
		print(message)
		stamp = datetime.now().strftime('%H:%M:%S')
		self.logTable.appendRow([stamp, message])

	@property
	def resultLevelFilterValues(self):
		level = ipar.uiState.Resultlevelfilter.eval()
		if level == 'error':
			return [TestFindingStatus.error.name, TestFindingStatus.unknown.name]
		if level == 'warning':
			return [TestFindingStatus.error.name, TestFindingStatus.warning.name, TestFindingStatus.unknown.name]
		return ['*']

	def openLog(self):
		self.ownerComp.op('full_log_text').openViewer(unique=True)

	def resetAll(self):
		self.clearLog()
		self.clearResults()
		self.reloadTestQueue()
		ipar.uiState.Running = False
		ipar.uiState.Filtertext = ''

	@staticmethod
	def onCountLabelClick(label: 'COMP'):
		name = label.name.split('_')[0]
		if name == 'success':
			ipar.uiState.Resultlevelfilter = 'all'
		else:
			ipar.uiState.Resultlevelfilter = name

	@staticmethod
	def _queueCall(method: Callable, *args, delayFrames=5):
		run('args[0](*(args[1:]))', method, *args, delayFrames=delayFrames, delayRef=root)
