# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from typing import List

def onRemoveReplicant(comp, replicant):

	replicant.destroy()
	return

def onReplicate(comp, allOps: 'List[TOP]', newOps, template: 'DAT', master):

	for i, c in enumerate(allOps):
		c.par.file = template[i+1, 'thumbFile']
