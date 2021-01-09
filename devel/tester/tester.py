from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Callable, Dict, List, Union, Optional
import re
from raytkUtil import RaytkContext, recloneComp, Version

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Pars(ParCollection):
		Testcasefolder: 'StrParamT'
		Buildfolder: 'StrParamT'

	class _COMP(COMP):
		par: _Pars

	class _UiStatePars:
		Resultlevelfilter: 'StrParamT'
	ipar.uiState = _UiStatePars()

class TestManager:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.logTable = ownerComp.op('log')  # type: DAT
		self.currentTestName = tdu.Dependency()
		self.successCount = tdu.Dependency(0)
		self.warningCount = tdu.Dependency(0)
		self.errorCount = tdu.Dependency(0)
		self._caseResults = {}  # type: Dict[str, _TestCaseResult]

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

	def buildTestTable(self, dat: 'DAT', fileTable: 'DAT'):
		dat.clear()
		dat.appendRow([
			'name',
			'tox',
		])
		casesFolder = Path(self.ownerComp.par.Testcasefolder.eval())
		for row in range(1, fileTable.numRows):
			relFile = Path(str(fileTable[row, 'relpath']))
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
			if '-' in versionStr:
				versionStr = versionStr.split('-', 1)[1]
			try:
				version = Version(versionStr)
			except ValueError:
				version = None
			dat.appendRow([
				toxFile.stem,
				f'Build {version}' if version else toxFile.stem,
				version or '',
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

	def reloadTestQueue(self):
		self.reloadTestTable()
		queue = self._testQueue
		queue.clear()
		queue.appendCol(self._testTable.col('name')[1:])

	def clearResults(self):
		table = self._resultTable
		table.clear()
		table.appendRow(['case', 'path', 'status', 'source', 'message'])
		self._caseResults = {}
		self.successCount.val = 0
		self.warningCount.val = 0
		self.errorCount.val = 0

	@property
	def hasResultCounts(self):
		return self.successCount.val > 0 or self.warningCount.val > 0 or self.errorCount.val > 0

	def _addResult(self, result: '_TestCaseResult'):
		self._caseResults[result.name] = result
		table = self._resultTable
		if not result.findings:
			table.appendRow([
				result.name,
				'',
				_FindingStatus.success.name,
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
				result.name,
				finding.path.replace(basePath, '') if finding.path and basePath else (finding.path or ''),
				finding.status.name,
				finding.source.name,
				finding.message,
			])

	def runQueuedTests(self):
		queue = self._testQueue
		if queue.numRows < 1:
			raise Exception('No tests queued!')
		self.clearLog()
		self.clearResults()
		self.log(f'Running {queue.numRows} queued tests...')
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
		if stage == 0:
			tox = self._testTable[name, 'tox']
			if not tox:
				raise Exception(f'Unable to find tox for test {name!r}')
			self.loadTestTox(str(tox))
			self._queueCall(self._runNextTest_stage, stage + 1, name, continueAfter)
		elif stage == 1:
			self._processTest()
			self._queueCall(self._runNextTest_stage, stage + 1, name, continueAfter)
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
		# TODO: ??
		pass

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

	def _processTest(self):
		comp = self._testComp
		if not comp:
			return
		for rop in RaytkContext().ropChildrenOf(comp):
			recloneComp(rop)
		for rop in RaytkContext().ropOutputChildrenOf(comp):
			rop.outputs[0].cook(force=True)

	def _buildTestCaseResult(self) -> 'Optional[_TestCaseResult]':
		comp = self._testComp
		if not comp:
			raise Exception('No test loaded!')
		name = self.currentTestName.val
		result = _TestCaseResult(name=name)
		validationErrors = self.ownerComp.op('validationErrors')
		result.findings += _Finding.fromValidationTable(name, validationErrors)
		result.findings += _Finding.parseErrorLines(
			name, comp.scriptErrors(recurse=True), _FindingSource.scriptError, _FindingStatus.error)
		result.findings += _Finding.parseErrorLines(
			name, comp.warnings(recurse=True), _FindingSource.opWarning, _FindingStatus.warning)
		result.findings += _Finding.parseErrorLines(
			name, comp.errors(recurse=True), _FindingSource.opError, _FindingStatus.error)
		return result

	def clearLog(self):
		self.logTable.clear()

	def log(self, message: str):
		print(message)
		self.logTable.appendRow([message])

	@property
	def resultLevelFilterValues(self):
		level = ipar.uiState.Resultlevelfilter.eval()
		if level == 'error':
			return [_FindingStatus.error.name]
		if level == 'warning':
			return [_FindingStatus.error.name, _FindingStatus.warning.name]
		return ['*']

	def openLog(self):
		self.ownerComp.op('full_log_text').openViewer(unique=True)

	def resetAll(self):
		self.clearLog()
		self.clearResults()
		self.reloadTestQueue()

	@staticmethod
	def _queueCall(method: Callable, *args):
		run('args[0](*(args[1:]))', method, *args, delayFrames=5, delayRef=root)

@dataclass
class _TestCaseResult:
	name: Optional[str] = None
	findings: List['_Finding'] = field(default_factory=list)

	@property
	def hasError(self):
		return any([finding.isError for finding in self.findings])

	@property
	def hasWarning(self):
		return any([finding.isWarning for finding in self.findings])

class _FindingStatus(Enum):
	success = 'success'
	warning = 'warning'
	error = 'error'
	unknown = 'unknown'

	@classmethod
	def parse(cls, s: 'Union[str, Cell]'):
		s = str(s or '')
		if not s:
			return _FindingStatus.unknown
		if s == 'error':
			return _FindingStatus.error
		if s == 'warning':
			return _FindingStatus.warning
		if s == 'success':
			return _FindingStatus.success
		return _FindingStatus.unknown

class _FindingSource(Enum):
	validation = 'validation'
	scriptError = 'scriptError'
	opError = 'opError'
	opWarning = 'opWarning'

@dataclass
class _Finding:
	case: str
	status: _FindingStatus
	source: _FindingSource
	path: Optional[str] = None
	message: Optional[str] = None

	@property
	def isError(self):
		return self.status == _FindingStatus.error

	@property
	def isWarning(self):
		return self.status in (_FindingStatus.warning, _FindingStatus.unknown)

	@classmethod
	def fromValidationTable(cls, case: str, dat: 'DAT'):
		return [
			cls.fromValidationRow(case, dat, row)
			for row in range(1, dat.numRows)
		]

	@classmethod
	def fromValidationRow(cls, case: str, dat: 'DAT', row: int):
		return _Finding(
			case=case,
			path=str(dat[row, 'path']),
			message=str(dat[row, 'message']),
			status=_FindingStatus.parse(dat[row, 'level']),
			source=_FindingSource.validation,
		)

	@classmethod
	def parseErrorLines(cls, case: str, text: str, source: '_FindingSource', status: '_FindingStatus') -> 'List[_Finding]':
		if not text:
			return []
		results = []
		for line in text.splitlines():
			line = line.strip()
			if line:
				results.append(cls.parseErrorLine(case, line, source, status))
		return results

	@classmethod
	def parseErrorLine(cls, case: str, line: str, source: '_FindingSource', status: '_FindingStatus'):
		line = line.strip()
		match = _opErrorPattern.fullmatch(line)
		if match:
			message = match.group(1)
			path = match.group(2)
			if message.startswith(path + ':'):
				message = message.replace(path + ':', '', 1)
			message = message.strip()
			if source in (_FindingSource.opError, _FindingSource.scriptError) and message.startswith('Error:'):
				message = message.replace('Error:', '', 1).strip()
			elif source == _FindingSource.opWarning and message.startswith('Warning:'):
				message = message.replace('Warning:', '', 1).strip()
			o = op(path)
			if o and isinstance(o, (glslTOP, glslmultiTOP)):
				status = _FindingStatus.error
			return cls(
				case=case,
				path=path,
				status=status,
				source=source,
				message=message,
			)
		return cls(
			case=case,
			status=status,
			source=source,
			message=line,
		)

_opErrorPattern = re.compile(r'(.*) \((/.*)\)')
