# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onSetupParameters(dat):
	pg = dat.appendCustomPage('Thumbs')  # type: Page
	pg.appendTOP('Layout')
	pg.appendInt('Thumbsize')

def onCook(dat: 'scriptDAT'):
	dat.clear()
	opThumbFiles = dat.inputs[0]  # type: DAT
	layoutTop = dat.par.Layout.eval()  # type: TOP
	thumbSize = dat.par.Thumbsize.eval()
	fullWidth = layoutTop.width
	fullHeight = layoutTop.height
	cols = fullWidth / thumbSize
	dat.appendRow(['opPath', 'row', 'col', 'l', 'b'])
	for i in range(1, opThumbFiles.numRows):
		r = int((i - 1) / cols)
		c = int((i - 1) % cols)
		dat.appendRow([
			opThumbFiles[i, 'opPath'],
			r,
			c,
			c * thumbSize,
			fullHeight - (r+1) * thumbSize,
		])
