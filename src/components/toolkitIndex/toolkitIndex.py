# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

def buildModuleTable(dat: scriptDAT):
	dat.clear()
	dat.appendRow(['name', 'root', 'moduleDefinition'])
	dat.appendRow(['raytk', op.raytk, op.raytk.op('moduleDefinition')])
	modules = root.findChildren(type=baseCOMP, tags=['raytkModule'])
	for module in modules:
		modDef = module.op('moduleDefinition')
		name = modDef.par['Modulename'] or ''
		if name:
			dat.appendRow([name, module, modDef])

def prepareOpTable(dat: scriptDAT, mergedOpTable: DAT, moduleTable: DAT):
	dat.copy(mergedOpTable)
	for i in range(1, dat.numRows):
		moduleName = dat[i, 'module'].val
		path = dat[i, 'path'].val
		prefix = '/raytkAddons/' + moduleName + '/'
		moduleRoot = moduleTable[moduleName, 'root']
		if moduleRoot and path.startswith(prefix):
			path = moduleRoot.val + '/' + path[len(prefix):]
			dat[i, 'path'] = path