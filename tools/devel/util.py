# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def getOpDef(comp: 'COMP'):
	return comp and comp.op('opDefinition')

def updateOpType(comp: 'COMP' = None):
	if comp is None:
		comp = getCurrentROp()
	toolkit = comp.parent.raytk
	path = toolkit.relativePath(comp)
	if path.startswith('./'):
		path = path[2:]
	opDef = getOpDef(comp)
	opDef.par.Optype = 'raytk.' + path.replace('/', '.')

# op.raytkDevel.mod.util.updateOpType()

def getCurrentROp():
	pane = _getActiveEditor()
	if not pane:
		return None
	comp = pane.owner
	if not comp:
		return None
	if 'raytkOP' in comp.tags:
		return comp
	if comp.name == 'opDefinition':
		host = comp.par.Hostop.eval()
		if host and 'raytkOP' in host.tags:
			return host

def _getActiveEditor():
	pane = ui.panes.current
	if pane.type == PaneType.NETWORKEDITOR:
		return pane
	for pane in ui.panes:
		if pane.type == PaneType.NETWORKEDITOR:
			return pane
