from raytkUtil import RaytkContext, ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: scriptDAT):
	dat.clear()
	dat.appendRow(['name', 'label'])
	context = RaytkContext()
	for rop in context.allMasterOperators():
		info = ROPInfo(rop)
		if not info.isOutput:
			continue
		bufs = rop.op('outputBuffers')  # type: DAT
		if not bufs:
			continue
		for row in range(1, bufs.numRows):
			name = bufs[row, 'name'].val
			label = bufs[row, 'label'].val
			if dat[name, 0] is not None:
				continue
			dat.appendRow([name, label])
