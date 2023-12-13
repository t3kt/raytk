from pathlib import Path
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
	def _scopeRoot(self) -> COMP | None:
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
			scope.path,
			scope.warnings(recurse=False),
			TestFindingSource.opWarning,
			TestFindingStatus.warning,
			includeDetail=includeDetail,
		)
		for child in scope.children:
			findings += self._parseErrorLines(
				scope,
				child.path,
				child.scriptErrors(recurse=True),
				TestFindingSource.scriptError,
				TestFindingStatus.error,
				includeDetail=includeDetail,
			)
		findings += self._parseErrorLines(
			scope,
			scope.path,
			scope.errors(recurse=False),
			TestFindingSource.opError,
			TestFindingStatus.error,
			includeDetail=includeDetail,
		)
		for child in scope.children:
			findings += self._parseErrorLines(
				scope,
				child.path,
				child.errors(recurse=True),
				TestFindingSource.opError,
				TestFindingStatus.error,
				includeDetail=includeDetail,
			)
		findings += self._parseErrorLines(
			scope,
			scope.path,
			scope.warnings(recurse=False),
			TestFindingSource.opWarning,
			TestFindingStatus.warning,
			includeDetail=includeDetail,
		)
		for child in scope.children:
			findings += self._parseErrorLines(
				scope,
				child.path,
				child.warnings(recurse=True),
				TestFindingSource.opWarning,
				TestFindingStatus.warning,
				includeDetail=includeDetail,
			)
		findings = self._dedupFindings(findings)
		return findings

	def _parseErrorLines(
			self,
			scope: COMP,
			defaultPath: str,
			text: str,
			source: 'TestFindingSource',
			status: 'TestFindingStatus',
			includeDetail: bool = False,
	) -> 'List[TestFinding]':
		if not text:
			return []
		findings = []
		# for line in text.splitlines():
		for line in [text]:
			line = line.strip()
			if not line:
				continue
			finding = TestFinding.parseErrorLine(
				defaultPath,
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
			scope: COMP,
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

	def buildFindingTable(self, dat: DAT):
		dat.clear()
		dat.appendRow([
			'path',
			'relPath',
			'status',
			'source',
			'message',
		])
		includeDetail = self.ownerComp.par.Includedetail.eval()
		if includeDetail:
			dat.appendCol(['detail'])
		scope = self._scopeRoot
		if not scope:
			return
		basePath = scope.path + '/'
		findings = self.GetFindings()
		for finding in findings:
			dat.appendRow(
				[
					finding.path,
				] + finding.toTableRowVals(
					basePath,
					includeDetail=includeDetail,
				))

	def WriteSnapshots(
			self,
			caseRootFolder: str,
			imagesRootFolder: str,
			sourceFolder: str,
	):
		scope = self._scopeRoot
		if not scope:
			print(self.ownerComp, f'No scope currently loaded')
			return
		if not caseRootFolder.endswith('/'):
			caseRootFolder += '/'
		if not imagesRootFolder.endswith('/'):
			imagesRootFolder += '/'
		if not sourceFolder.endswith('/'):
			sourceFolder += '/'
		tox = str(scope.par.externaltox)
		if not tox.startswith(caseRootFolder) or not tox.endswith('_test.tox'):
			print(self.ownerComp, f'Tox does not support snapshots: {tox!r}')
			return
		for o in scope.children:
			if not o.par['Enablesnapshot']:
				continue
			top = o.op('snapshot')  # type: TOP
			if not top:
				continue
			if o.par['Isthumb']:
				suffix = '_thumb.png'
			elif o.par['Snapshotname']:
				suffix = '_' + o.par.Snapshotname.eval() + '.png'
			else:
				continue
			imagePath = imagesRootFolder + '/' + tox.replace(caseRootFolder, '').replace('_test.tox', suffix)
			top.save(imagePath, createFolders=True)

