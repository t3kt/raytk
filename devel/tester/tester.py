from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Callable, Dict, List, Union, Optional
import re
from raytkUtil import RaytkContext, recloneComp

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Pars(ParCollection):
		Testcasefolder: 'StrParamT'

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
			return
		basePath = self._testComp.path + '/'
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
		self.log(f'Running {queue.numRows} queued tests...')
		self.clearResults()
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
		tox = self._testTable[name, 'tox']
		if not tox:
			raise Exception(f'Unable to find tox for test {name!r}')
		self.loadTestTox(str(tox))
		self._processTest()
		result = self._buildTestCaseResult()
		if result.hasError:
			self.log(f'Test {name} resulted in ERROR')
		elif result.hasWarning:
			self.log(f'Test {name} resulted in WARNING')
		else:
			self.log(f'Test {name} resulted in SUCCESS')
		self._addResult(result)
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

	@staticmethod
	def resultLevelFilterValues():
		level = ipar.uiState.Resultlevelfilter.eval()
		if level == 'error':
			return [_FindingStatus.error.name]
		if level == 'warning':
			return [_FindingStatus.error.name, _FindingStatus.warning.name]
		return ['*']

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
