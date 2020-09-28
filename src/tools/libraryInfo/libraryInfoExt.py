# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List
	parent.raytk = COMP()

class LibraryInfoBuilder:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def buildROPTable(dat: 'tableDAT'):
		dat.clear()
		opsRoot = parent.raytk.op('operators')
		rops = opsRoot and opsRoot.findChildren(type=COMP, tags=['raytk*'], depth=2, maxDepth=2)  # type: List[COMP]
		dat.appendRow(['name', 'path', 'parentPath', 'tags', 'category', 'fullName', 'opVersion', 'status'])
		if not rops:
			return
		rops.sort(key=lambda o: o.path.lower())
		for rop in rops:
			if 'buildExclude' in rop.tags or rop.name.startswith('_'):
				continue
			category = rop.parent()
			opDef = rop.op('opDefinition')
			version = opDef and opDef.par['Raytkopversion']
			beta = bool(opDef and 'raytkBeta' in opDef.tags)
			dat.appendRow([
				rop.name,
				rop.path,
				category.path,
				' '.join(rop.tags),
				category.name,
				f'{category.name}/{rop.name}',
				version if version is not None else '',
				'beta' if beta else '',
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
