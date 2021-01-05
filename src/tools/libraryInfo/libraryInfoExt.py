from datetime import datetime
from raytkUtil import ROPInfo, RaytkTags, RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List
	parent.raytk = COMP()

class LibraryInfoBuilder:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def Forcebuild(self, _=None):
		for o in self.ownerComp.ops(
				'build_opTable',
				'build_categoryTable',
				'build_opHelpTable',
				'build_versionInfo',
				'build_buildInfo',
				'eval_info_text_exprs'):
			o.cook(force=True)

	@staticmethod
	def buildVersionTable(dat: 'tableDAT'):
		dat.clear()
		dat.appendRow(['toolkitVersion', RaytkContext().toolkitVersion()])
		dat.appendRow(['touchDesignerVersion', app.version])
		dat.appendRow(['touchDesignerBuild', app.build])

	def buildBuildInfoTable(self, dat: 'tableDAT'):
		self.buildVersionTable(dat)
		dat.insertRow(['toolkitBuildDate', datetime.now().isoformat(sep=' ')], 'touchDesignerVersion')
		dat.appendRow(['buildOsName', app.osName])
		dat.appendRow(['buildOsVersion', app.osVersion])

	@staticmethod
	def buildROPTable(dat: 'tableDAT'):
		dat.clear()
		opsRoot = RaytkContext().operatorsRoot()
		rops = []  # type: List[COMP]
		if opsRoot:
			rops = opsRoot.findChildren(type=COMP, tags=['raytk*'], depth=2, maxDepth=2)
		dat.appendRow(['name', 'path', 'parentPath', 'tags', 'category', 'fullName', 'opType', 'opVersion', 'status'])
		if not rops:
			return
		rops.sort(key=lambda o: o.path.lower())
		for rop in rops:
			if RaytkTags.buildExclude.isOn(rop) or rop.name.startswith('_'):
				continue
			ropInfo = ROPInfo(rop)
			if not ropInfo or not ropInfo.isMaster:
				continue
			category = rop.parent()
			dat.appendRow([
				rop.name,
				rop.path,
				category.path,
				' '.join(sorted(rop.tags)),
				category.name,
				f'{category.name}/{rop.name}',
				ropInfo.opType,
				ropInfo.opVersion,
				ropInfo.statusLabel,
			])

	@staticmethod
	def buildCategoryTable(dat: 'tableDAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow(['category', 'path'])
		categoryPaths = set(c.val.lower() for c in opTable.col('parentPath')[1:])
		for path in sorted(categoryPaths):
			dat.appendRow([
				path.rsplit('/', maxsplit=1)[-1],
				path,
			])

	def buildROPHelpTable(self, dat: 'tableDAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow(['path', 'opType', 'category', 'summary', 'helpPath'])
		for row in range(1, opTable.numRows):
			path = opTable[row, 'path']
			ropInfo = ROPInfo(path)
			helpDAT = ropInfo.helpDAT
			dat.appendRow([
				path,
				ropInfo.opType,
				opTable[row, 'category'],
				self.extractHelpSummary(helpDAT),
				helpDAT.path if helpDAT else '',
			])

	def buildCategoryHelpTable(self, dat: 'tableDAT', categoryTable: 'DAT'):
		dat.clear()
		dat.appendRow(['category', 'path', 'summary', 'helpPath'])
		for row in range(1, categoryTable.numRows):
			path = categoryTable[row, 'path']
			category = op(path)
			helpDAT = category.op('help')
			dat.appendRow([
				categoryTable[row, 'category'],
				path,
				self.extractHelpSummary(helpDAT),
				helpDAT.path if helpDAT else '',
			])

	@staticmethod
	def extractHelpSummary(dat: 'DAT'):
		if not dat or not dat.text:
			return ''
		for line in dat.text.splitlines():
			line = line.strip()
			if not line:
				continue
			if line.startswith('# '):
				continue
			return line
		return ''
