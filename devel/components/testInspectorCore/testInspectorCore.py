from typing import List, Optional
from raytkTest import TestFinding, TestFindingSource, TestFindingStatus

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Par:
		Scope: 'OPParamT'

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
		findings = []  # type: List[TestFinding]
		findings += TestFinding.fromValidationTable(validationErrors)
		findings += TestFinding.parseErrorLines(
			scope.scriptErrors(recurse=True), TestFindingSource.scriptError, TestFindingStatus.error)
		findings += TestFinding.parseErrorLines(
			scope.warnings(recurse=True), TestFindingSource.opWarning, TestFindingStatus.warning)
		findings += TestFinding.parseErrorLines(
			scope.errors(recurse=True), TestFindingSource.opError, TestFindingStatus.error)
		return findings

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
		for finding in findings:
			dat.appendRow(
				[
					finding.path,
				] + finding.toTableRowVals(basePath))

