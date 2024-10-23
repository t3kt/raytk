from datetime import datetime
from raytkUtil import RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	parent.raytk = COMP()

def forceBuild():
	op('moduleInfoBuilder').Forcebuild()
	for o in ops(
			'build_categoryTable',
			'build_versionInfo',
			'build_buildInfo',
			'eval_info_text_exprs'):
		o.cook(force=True)

def buildVersionTable(dat: tableDAT):
	dat.clear()
	dat.appendRow(['toolkitVersion', RaytkContext().toolkitVersion()])
	dat.appendRow(['touchDesignerVersion', app.version])
	dat.appendRow(['touchDesignerBuild', app.build])

def buildBuildInfoTable(dat: tableDAT):
	buildVersionTable(dat)
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

def buildCategoryTable(dat: tableDAT, opTable: DAT):
	dat.clear()
	dat.appendRow(['category', 'path'])
	categoryNames = set(c.val for c in opTable.col('category')[1:] if c)
	for catComp in sorted(RaytkContext().allCategories(), key=lambda o: o.name):
		if catComp.name in categoryNames:
			dat.appendRow([catComp.name, catComp.path])