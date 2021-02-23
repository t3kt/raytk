from typing import List, Optional
from raytkTest import TestFinding, TestFindingSource, TestFindingStatus

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Par:
		Scope: 'OPParamT'
		Includedetail: 'BoolParamT'

	class _Comp(COMP):
		par: _Par

class TestInspectorCore:
	def __init__(self, ownerComp: '_Comp'):
		self.ownerComp = ownerComp

	@property
	def _scopeRoot(self) -> 'Optional[COMP]':
		return self.ownerComp.par.Scope.eval()

	def GetFindings(self,) -> List[TestFinding]:
		scope = self._scopeRoot
		if not scope:
			return []
		validationErrors = self.ownerComp.op('validationErrors')
		includeDetail = self.ownerComp.par.Includedetail.eval()
		findings = []  # type: List[TestFinding]
		findings += TestFinding.fromValidationTable(validationErrors)
		findings += self._parseErrorLines(
			scope,
			scope.scriptErrors(recurse=True),
			TestFindingSource.scriptError,
			TestFindingStatus.error,
			includeDetail=includeDetail,
		)
		findings += self._parseErrorLines(
			scope,
			scope.warnings(recurse=True),
			TestFindingSource.opWarning,
			TestFindingStatus.warning,
			includeDetail=includeDetail,
		)
		findings += self._parseErrorLines(
			scope,
			scope.errors(recurse=True),
			TestFindingSource.opError,
			TestFindingStatus.error,
			includeDetail=includeDetail,
		)
		findings = self._dedupFindings(findings)
		return findings

	def _parseErrorLines(
			self,
			scope: 'COMP',
			text: str,
			source: 'TestFindingSource',
			status: 'TestFindingStatus',
			includeDetail: bool = False,
	) -> 'List[TestFinding]':
		if not text:
			return []
		findings = []
		for line in text.splitlines():
			line = line.strip()
			if not line:
				continue
			finding = TestFinding.parseErrorLine(
				line,
				source, status,
				includeDetail
			)
			if finding in findings:
				continue
			if finding.status != TestFindingStatus.success and includeDetail:
				self._investigateFinding(scope, finding)
			findings.append(finding)
		return findings

	def _investigateFinding(
			self,
			scope: 'COMP',
			finding: 'TestFinding'):
		o = scope.op(finding.path)
		if not o:
			return
		self._investigateShaderInputError(o, finding)

	@staticmethod
	def _investigateShaderInputError(o: 'OP', finding: 'TestFinding'):
		if not isinstance(o, (glslTOP, glslmultiTOP)):
			return
		matched = False
		for detail in finding.detail:
			if 'undefined variable "sTD2DInputs"' in detail:
				matched = True
				break
		if not matched:
			return
		rop = o.parent()
		texSources = rop.op('texture_sources')
		finding.detail.append(f'# tex sources: {texSources.numRows}')
		for conn in o.inputConnectors:
			finding.detail.append(f'in{conn.index} #: {len(conn.connections)}')

	@staticmethod
	def _dedupFindings(findings: 'List[TestFinding]') -> 'List[TestFinding]':
		results = []
		for finding in findings:
			if finding not in results:
				results.append(finding)
		return results

	def buildFindingTable(self, dat: 'DAT'):
		dat.clear()
		dat.appendRow([
			'path',
			'relPath',
			'status',
			'source',
			'message',
		])
		scope = self._scopeRoot
		if not scope:
			return
		basePath = scope.path + '/'
		findings = self.GetFindings()
		includeDetail = self.ownerComp.par.Includedetail.eval()
		for finding in findings:
			dat.appendRow(
				[
					finding.path,
				] + finding.toTableRowVals(
					basePath,
					includeDetail=includeDetail,
				))

