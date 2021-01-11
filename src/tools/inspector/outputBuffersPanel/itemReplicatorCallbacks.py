# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .outputBuffersPanel import OutputBuffersPanel
	ext.outputBuffersPanel = OutputBuffersPanel(COMP())

def onRemoveReplicant(comp, replicant):
	replicant.destroy()

def onReplicate(comp, allOps, newOps, template, master):
	ext.outputBuffersPanel.onItemReplicate(comp, allOps, template, master)
