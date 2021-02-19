import dataclasses
from dataclasses import dataclass
from enum import Enum
import re
from typing import List, Optional, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *


@dataclass
class TestCaseResult:
	name: Optional[str] = None
	findings: List['TestFinding'] = dataclasses.field(default_factory=list)

	@property
	def hasError(self):
		return any([finding.isError for finding in self.findings])

	@property
	def hasWarning(self):
		return any([finding.isWarning for finding in self.findings])

class TestFindingStatus(Enum):
	success = 'success'
	warning = 'warning'
	error = 'error'
	unknown = 'unknown'

	@classmethod
	def parse(cls, s: 'Union[str, Cell]'):
		s = str(s or '')
		if not s:
			return TestFindingStatus.unknown
		if s == 'error':
			return TestFindingStatus.error
		if s == 'warning':
			return TestFindingStatus.warning
		if s == 'success':
			return TestFindingStatus.success
		return TestFindingStatus.unknown

class TestFindingSource(Enum):
	validation = 'validation'
	scriptError = 'scriptError'
	opError = 'opError'
	opWarning = 'opWarning'

@dataclass
class TestFinding:
	status: TestFindingStatus
	source: TestFindingSource
	path: Optional[str] = None
	message: Optional[str] = None

	@property
	def isError(self):
		return self.status == TestFindingStatus.error

	@property
	def isWarning(self):
		return self.status in (TestFindingStatus.warning, TestFindingStatus.unknown)

	@classmethod
	def fromValidationTable(cls, dat: 'DAT'):
		return [
			cls.fromValidationRow(dat, row)
			for row in range(1, dat.numRows)
		]

	@classmethod
	def fromValidationRow(cls, dat: 'DAT', row: int):
		return TestFinding(
			path=str(dat[row, 'path']),
			message=str(dat[row, 'message']),
			status=TestFindingStatus.parse(dat[row, 'level']),
			source=TestFindingSource.validation,
		)

	@classmethod
	def parseErrorLines(cls, text: str, source: 'TestFindingSource', status: 'TestFindingStatus') -> 'List[TestFinding]':
		if not text:
			return []
		results = []
		for line in text.splitlines():
			line = line.strip()
			if line:
				results.append(cls.parseErrorLine(line, source, status))
		return results

	@classmethod
	def parseErrorLine(cls, line: str, source: 'TestFindingSource', status: 'TestFindingStatus'):
		line = line.strip()
		match = _opErrorPattern.fullmatch(line)
		if match:
			message = match.group(1)
			path = match.group(2)
			if message.startswith(path + ':'):
				message = message.replace(path + ':', '', 1)
			message = message.strip()
			if source in (TestFindingSource.opError, TestFindingSource.scriptError) and message.startswith('Error:'):
				message = message.replace('Error:', '', 1).strip()
			elif source == TestFindingSource.opWarning and message.startswith('Warning:'):
				message = message.replace('Warning:', '', 1).strip()
			o = op(path)
			if o and isinstance(o, (glslTOP, glslmultiTOP)):
				status = TestFindingStatus.error
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

	def toTableRowVals(self, basePath: 'Optional[str]') -> 'List[str]':
		return [
			self.path.replace(basePath, '') if self.path and basePath else (self.path or ''),
			self.status.name,
			self.source.name,
			self.message,
		]

_opErrorPattern = re.compile(r'(.*) \((/.*)\)')
