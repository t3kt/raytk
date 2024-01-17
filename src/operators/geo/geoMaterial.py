# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def mergeDefinitions(
		dat: scriptDAT,
		vertexDefinitions: DAT,
		pixelDefinitions: DAT,
):
	dat.clear()
	if vertexDefinitions.numRows == 0:
		dat.copy(pixelDefinitions)
		return
	dat.copy(vertexDefinitions)
	dat.appendCol(['stage'] + ['vertex'] * (vertexDefinitions.numRows - 1))
	if pixelDefinitions.numRows == 0:
		return
	for pixelRow in range(1, pixelDefinitions.numRows):
		name = pixelDefinitions[pixelRow, 'name'].val
		stageCell = dat[name, 'stage']
		if stageCell is not None:
			stageCell.val = 'both'
		else:
			dat.appendRow([
				name,
				*pixelDefinitions.row(pixelRow)[1:],
				'pixel',
			])
