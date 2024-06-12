from raytkUtil import RaytkTags, ROPInfo, ModuleInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class ModuleInfoBuilder:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def Forcebuild(self, _=None):
		for o in self.ownerComp.ops(
				'build_opTable'):
			o.cook(force=True)

	def _moduleDef(self) -> COMP | None:
		return self.ownerComp.par.Moduledef.eval()

	def _moduleInfo(self):
		modDef = self._moduleDef()
		if not modDef:
			return None
		return ModuleInfo(modDef.parent())

	def buildROPTable(self, dat: scriptDAT, thumbTable: DAT | None, chipTable: DAT | None):
		dat.clear()
		dat.appendRow([
			'name', 'path', 'tags', 'category', 'displayCategory', 'opType', 'opVersion',
			'status', 'keywords', 'shortcuts', 'chip', 'thumb', 'flags', 'module',
		])
		moduleInfo = self._moduleInfo()
		if not moduleInfo:
			return
		opsRoot = moduleInfo.operatorsRoot()
		if not opsRoot:
			return
		rops = opsRoot.findChildren(type=COMP, tags=['raytk*'], depth=2, maxDepth=2)
		if not rops:
			return
		modName = moduleInfo.moduleName
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
				(chipTable and chipTable[rop.name, 'chip']) or '',
				(thumbTable and thumbTable[rop.path, 'thumb']) or '',
				ropInfo.opDefPar['Flags'] or '',
				modName,
			])
