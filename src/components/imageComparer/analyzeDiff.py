import numpy as np

def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')
	p = page.appendTOP('Image')
	p = page.appendFloat('Threshold')[0]
	p.normMax = 0.1

def onCook(scriptOp):
	scriptOp.clear()
	thresh = scriptOp.par.Threshold.eval()
	top = scriptOp.par.Image.eval()
	data = top.numpyArray() [:,:,[0]]
	scriptOp.appendChan('diffMax')
	scriptOp.appendChan('diffCount')
	scriptOp.appendChan('diffRatio')
	scriptOp['diffMax'][0]=np.nanmax(data)
	diffCount = (data > thresh).sum()
	scriptOp['diffCount'][0] = diffCount
	scriptOp['diffRatio'][0] = diffCount / (top.width * top.height)
