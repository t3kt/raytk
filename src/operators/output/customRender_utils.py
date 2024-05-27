# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCreateParPulse(action: str):
	o = parent()
	if action == 'Createbodytemplate':
		par = o.par.Bodytemplate
		template = op('default_body_template')
		suffix = '_body'
		offsetX = 0
		desc = 'shader body'
		opType = textDAT
	elif action == 'Createoutputbuffertable':
		par = o.par.Outputbuffertable
		template = op('default_output_table')
		suffix = '_output_buffers'
		offsetX = 150
		desc = 'output buffer table'
		opType = tableDAT
	else:
		return
	if par.eval():
		return
	ui.undo.startBlock('Create ' + desc)
	dat = o.parent().create(opType, parent().name + suffix)
	dat.text = template.text
	dat.nodeX = o.nodeX + offsetX
	dat.nodeY = o.nodeY - o.nodeHeight - 50
	dat.viewer = True
	dat.dock = o
	par.val = dat
	o.showDocked = True
	ui.undo.endBlock()
