"""
Utilities used for automated toolkit testing.

This should only be used within development tools.
"""

import dataclasses
from dataclasses import dataclass
from enum import Enum
import re
from typing import Callable, List, Optional, Union
from raytkUtil import RaytkContext, recloneComp

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
	detail: List[str] = dataclasses.field(default_factory=list)

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
	def parseErrorLine(
			cls,
			defaultPath: str,
			line: str,
			source: 'TestFindingSource',
			status: 'TestFindingStatus',
			includeDetail: bool = False,
	):
		line = line.strip()
		match = _opErrorPattern.fullmatch(line)
		if not match:
			return cls(
				path=defaultPath,
				status=status,
				source=source,
				message=line,
			)
		message = match.group(1)
		path = match.group(2)
		detail = None
		if message.startswith(path + ':'):
			message = message.replace(path + ':', '', 1)
		message = message.strip()
		if source in (TestFindingSource.opError, TestFindingSource.scriptError) and message.startswith('Error:'):
			message = message.replace('Error:', '', 1).strip()
		elif source == TestFindingSource.opWarning and message.startswith('Warning:'):
			message = message.replace('Warning:', '', 1).strip()
		o = op(path)
		if o and isinstance(o, (glslTOP, glslmultiTOP)):
			detail = _parseCompileResultDetail(o)
			if not detail:
				detail = o.compileResult.splitlines()
				status = TestFindingStatus.error
			elif all('warning' in line.lower() and 'error' not in line.lower() for line in detail):
				status = TestFindingStatus.warning
			else:
				status = TestFindingStatus.error
			if detail:
				detail = [d for d in detail if d.strip()]
		return cls(
			path=path or defaultPath,
			status=status,
			source=source,
			message=message,
			detail=(detail if includeDetail else None) or [],
		)

	def toTableRowVals(
			self,
			basePath: 'Optional[str]',
			includeDetail: bool = False,
	) -> 'List[str]':
		vals = [
			self.path.replace(basePath, '') if self.path and basePath else (self.path or ''),
			self.status.name,
			self.source.name,
			self.message,
		]
		if includeDetail and self.detail:
			vals.append(repr(self.detail))
		return vals

_opErrorPattern = re.compile(r'(.*) \((/.*)\)')

def _parseCompileResultDetail(o: 'Union[glslTOP, glslmultiTOP]') -> 'List[str]':
	text = o.compileResult
	# print('DEBUG ATTEMPTING to extract COMPILE DETAIL')
	text = text.strip()
	if not text:
		print('DEBUG failed to extract compile detail')
		return []
	detail = []
	for line in text.splitlines():
		line = line.strip()
		if not line or _matchesIgnoredPattern(line):
			continue
		line = _cleanShaderErrorLine(line)
		if line not in detail:
			detail.append(line)
	# print(f'DEBUG extracted compile detail:\n{detail}')
	return detail

_ignoredCompilerPatterns = [
	re.compile(r'.* Results:$'),
	re.compile(r'\s*'),
	re.compile(r'Compiled Successfully'),
	re.compile(r'Linked Successfully'),
	re.compile(r'Fragment info'),
	re.compile(r'=+'),
	re.compile(r'-+'),
]

def _matchesIgnoredPattern(line: str) -> bool:
	return any(
		bool(p.fullmatch(line))
		for p in _ignoredCompilerPatterns
	)

_shaderErrorLinePattern = re.compile(r'0\(\d+\)\s*:\s*error\s*[0-9A-F]+:\s*(.+)')

def _cleanShaderErrorLine(line: str) -> str:
	match = _shaderErrorLinePattern.fullmatch(line)
	message = match.group(1) if match else None
	return message or line

def processTest(comp, log: 'Callable[[str], None]' = None):
	if not comp:
		return
	if not comp.valid:
		log and log(f'For some reason {comp!r} is invalid!')
		return
	rops = RaytkContext().ropChildrenOf(comp, maxDepth=2)
	log and log(f'Found {len(rops)} ROPs in test')
	# This is breaking connections made by outputOpController on initialization
	for rop in rops:
		if not rop.valid:
			log and log(f'For some reason {rop!r} is invalid!')
			continue
		rop.par.reinitnet.pulse()
		recloneComp(rop)
		if rop.par['Updateop'] is not None:
			rop.par.Updateop.pulse()
	for rop in RaytkContext().ropOutputChildrenOf(comp, maxDepth=4):
		if not rop.valid:
			continue
		for o in rop.outputs:
			if o.valid:
				o.cook(force=True)
