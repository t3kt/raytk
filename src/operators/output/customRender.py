# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCreateParPulse(action: str):
	if action == 'Createmaincode':
		ui.undo.startBlock('Create shader main code')
		createMainCode()
		ui.undo.endBlock()
	elif action == 'Createcustomrenderconfig':
		ui.undo.startBlock('Create custom render config')
		createCustomRenderConfig()
		ui.undo.endBlock()

def createMainCode():
	o = parent()
	par = o.par.Maincode
	if par.eval():
		return
	template = op('defaultMainCode')
	dat = o.parent().create(textDAT, parent().name + '_main')
	dat.text = template.text
	dat.par.language = 'glsl'
	dat.nodeX = o.nodeX
	dat.nodeY = o.nodeY - o.nodeHeight - 50
	dat.viewer = True
	dat.dock = o
	par.val = dat
	o.showDocked = True

def createCustomRenderConfig():
	o = parent()
	par = o.par.Customrenderconfig
	if par.eval():
		return
	comp = o.parent().copy(op('defaultCustomRenderConfig'), name=parent().name + '_customRenderConfig')
	comp.nodeX = o.nodeX + 150
	comp.nodeY = o.nodeY - o.nodeHeight - 50
	par.val = comp
	comp.dock = o
	o.showDocked = True

def onCreate(master=None, **kwargs):
	createMainCode()
	createCustomRenderConfig()

def _getConfigParSeq(name):
	config = parent().par.Customrenderconfig.eval() or op('defaultCustomRenderConfig')
	parSeq = config.seq['Input']
	return parSeq if parSeq is not None else []

def buildOutputTable(dat: scriptDAT):
	dat.clear()
	dat.appendRow(['name', 'label', 'macro', 'special', 'enable', 'path', 'enablePar', 'available'])
	parSeq = _getConfigParSeq('Output')
	path = op('shaderExecutor/render_glsl').path
	for i, block in enumerate(parSeq):
		name: str = block.par.Name.eval()
		dat.appendRow([
			name + 'Out',
			name.capitalize(),
			'OUTPUT_' + name.upper(),
			'', '1', path, '', '1',
		])

def buildInputTable(dat: scriptDAT):
	dat.clear()
	dat.appendRow(['name', 'exists', 'coordType', 'contextType', 'returnType'])
	parSeq = _getConfigParSeq('Input')
	n = len(parSeq)
	for i in range(8):
		if i < n:
			block = parSeq[i]
			dat.appendRow([
				block.par['Name'] or '',
				'1',
				block.par['Coordtype'] or '',
				block.par['Contexttype'] or '',
				block.par['Returntype'] or '',
			])
		else:
			dat.appendRow(['', '', '', '', ''])
