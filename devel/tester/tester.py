from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Callable, List, Union, Optional
import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Pars(ParCollection):
		Testcasefolder: 'StrParamT'

	class _COMP(COMP):
		par: _Pars

class TestManager:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.logTable = ownerComp.op('log')  # type: DAT
		self._currentTestName = None  # type: Optional[str]
		self._currentTestTox = None  # type: Optional[str]

	@property
	def _testHost(self) -> 'COMP':
		return self.ownerComp.op('test_host')

	@property
	def _testComp(self) -> 'Optional[COMP]':
		for o in self._testHost.children:
			return o

	def reloadTestTable(self):
		self.ownerComp.op('tests_folder').par.refreshpulse.pulse()

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

	def unloadTestCase(self):
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

	def _buildTestCaseResult(self) -> 'Optional[_TestCaseResult]':
		comp = self._testComp
		if not comp:
			return
		result = _TestCaseResult(
			name=self._currentTestName,
			tox=self._currentTestTox,
		)
		validationErrors = self.ownerComp.op('validationErrors')
		result.findings += _Finding.fromValidationTable(validationErrors)
		result.findings += _Finding.parseErrorLines(
			comp.scriptErrors(recurse=True), _FindingSource.scriptError, _FindingStatus.error)
		result.findings += _Finding.parseErrorLines(
			comp.warnings(recurse=True), _FindingSource.opWarning, _FindingStatus.warning)
		result.findings += _Finding.parseErrorLines(
			comp.errors(recurse=True), _FindingSource.opError, _FindingStatus.error)
		return result

	def buildTestCaseResultTable(self, dat: 'DAT'):
		dat.clear()
		dat.appendRow(['path', 'status', 'source', 'message'])
		result = self._buildTestCaseResult()
		if not result:
			return
		for finding in result.findings:
			dat.appendRow([
				finding.path,
				finding.status.name,
				finding.source.name,
				finding.message,
			])

	def ClearLog(self):
		self.logTable.clear()

	def log(self, message: str):
		print(message)
		self.logTable.appendRow([message])

	@staticmethod
	def _queueCall(method: Callable, *args):
		run('args[0](*(args[1:]))', method, *args, delayFrames=5, delayRef=root)

@dataclass
class _TestCaseResult:
	name: Optional[str] = None
	tox: Optional[str] = None
	findings: List['_Finding'] = field(default_factory=list)

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
	status: _FindingStatus
	source: _FindingSource
	path: Optional[str] = None
	message: Optional[str] = None

	@classmethod
	def fromValidationTable(cls, dat: 'DAT'):
		return [
			cls.fromValidationRow(dat, row)
			for row in range(1, dat.numRows)
		]

	@classmethod
	def fromValidationRow(cls, dat: 'DAT', row: int):
		return _Finding(
			path=str(dat[row, 'path']),
			message=str(dat[row, 'message']),
			status=_FindingStatus.parse(dat[row, 'level']),
			source=_FindingSource.validation,
		)

	@classmethod
	def parseErrorLines(cls, text: str, source: '_FindingSource', status: '_FindingStatus') -> 'List[_Finding]':
		if not text:
			return []
		results = []
		for line in text.splitlines():
			line = line.strip()
			if line:
				results.append(cls.parseErrorLine(line, source, status))
		return results

	@classmethod
	def parseErrorLine(cls, line: str, source: '_FindingSource', status: '_FindingStatus'):
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
				path=path,
				status=status,
				source=source,
				message=message,
			)
		return cls(
			status=status,
			source=source,
			message=line,
		)

_opErrorPattern = re.compile(r'(.*) \((/.*)\)')
