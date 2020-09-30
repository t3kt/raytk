from raytkUtil import ROPInfo, RaytkTags

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List, Optional
	parent.raytk = COMP()

class LibraryInfoBuilder:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def Forcebuild(self, _=None):
		for o in self.ownerComp.ops('build_opTable', 'build_categoryTable', 'build_opHelpTable', 'eval_build_info'):
			o.cook(force=True)
		self.ownerComp.op('opTable_writeFile').par.write.pulse()

	@staticmethod
	def buildROPTable(dat: 'tableDAT'):
		dat.clear()
		opsRoot = parent.raytk.op('operators')
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
			if not ropInfo.isMaster:
				continue
			category = rop.parent()
			dat.appendRow([
				rop.name,
				rop.path,
				category.path,
				' '.join(rop.tags),
				category.name,
				f'{category.name}/{rop.name}',
				ropInfo.opType,
				ropInfo.opVersion,
				'beta' if ropInfo.isBeta else '',
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
				self.extractHelpSummary(ropInfo),
				helpDAT.path if helpDAT else '',
			])

	@staticmethod
	def extractHelpSummary(ropInfo: ROPInfo):
		dat = ropInfo.helpDAT
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
