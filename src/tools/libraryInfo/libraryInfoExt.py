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
		context = RaytkContext()
		if context.develMode():
			buildType = 'devel'
		elif context.experimentalMode():
			buildType = 'experimental'
		else:
			buildType = 'production'
		dat.insertRow(['toolkitBuildType', buildType], 'toolkitBuildDate')
		dat.appendRow(['buildOsName', app.osName])
		dat.appendRow(['buildOsVersion', app.osVersion])

	@staticmethod
	def buildROPTable(dat: 'scriptDAT', thumbTable: 'DAT'):
		dat.clear()
		opsRoot = RaytkContext().operatorsRoot()
		rops = []  # type: List[COMP]
		if opsRoot:
			rops = opsRoot.findChildren(type=COMP, tags=['raytk*'], depth=2, maxDepth=2)
		dat.appendRow(['name', 'path', 'tags', 'category', 'displayCategory', 'opType', 'opVersion', 'status', 'keywords', 'shortcuts', 'thumb'])
		if not rops:
			return
		rops.sort(key=lambda o: o.path.lower())
		for rop in rops:
			if RaytkTags.buildExclude.isOn(rop) or rop.name.startswith('_'):
				continue
			ropInfo = ROPInfo(rop)
			if not ropInfo or not ropInfo.isMaster:
				continue
			dat.appendRow([
				rop.name,
				rop.path,
				' '.join(sorted(rop.tags)),
				rop.parent().name,
				ropInfo.displayCategoryName or '',
				ropInfo.opType,
				ropInfo.opVersion,
				ropInfo.statusLabel,
				' '.join(sorted(ropInfo.keywords)),
				' '.join(sorted(ropInfo.shortcuts)),
				thumbTable[rop.path, 'thumb'] or '',
			])

	@staticmethod
	def buildCategoryTable(dat: 'tableDAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow(['category', 'path'])
		categoryNames = set(c.val for c in opTable.col('category')[1:] if c)
		for catComp in sorted(RaytkContext().allCategories(), key=lambda o: o.name):
			if catComp.name in categoryNames:
				dat.appendRow([catComp.name, catComp.path])

	def buildROPHelpTable(self, dat: 'tableDAT', opTable: 'DAT'):
		dat.clear()
		dat.appendRow(['path', 'summary'])
		for row in range(1, opTable.numRows):
			path = opTable[row, 'path']
			ropInfo = ROPInfo(path)
			helpDAT = ropInfo.helpDAT
			dat.appendRow([
				path,
				self.extractHelpSummary(helpDAT),
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
