from raytkUtil import RaytkContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	dat.appendRow(['opPath', 'thumbFile'])
	thumbFiles = dat.inputs[0]
	context = RaytkContext()
	opsRootPath = context.operatorsRoot().path + '/'
	for row in range(1, thumbFiles.numRows):
		thumbRelPath = thumbFiles[row, 'relpath'].val
		opPath = opsRootPath + thumbRelPath.replace('_thumb.png', '')
		dat.appendRow([opPath, thumbFiles[row, 'path']])

