# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class Tools:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def UpdateOpType(self, comp: 'COMP' = None):
		if comp is None:
			comp = self.GetCurrentROP()
		if not comp:
			return
		toolkit = comp.parent.raytk
		path = toolkit.relativePath(comp)
		if path.startswith('./'):
			path = path[2:]
		opDef = getOpDef(comp)
		opDef.par.Optype = 'raytk.' + path.replace('/', '.')

	def FillMonitorHeight(self, usePrimary=True):
		height = _getMonitorHeight(usePrimary)
		height -= 270
		self.ownerComp.par.h = height

	def NavigateTo(self, comp: 'COMP'):
		if not comp:
			return
		pane = self.GetActiveEditor()
		if not pane:
			return
		pane.owner = comp

	@staticmethod
	def GetActiveEditor():
		pane = ui.panes.current
		if pane.type == PaneType.NETWORKEDITOR:
			return pane
		for pane in ui.panes:
			if pane.type == PaneType.NETWORKEDITOR:
				return pane

	def GetCurrentROP(self):
		pane = self.GetActiveEditor()
		if not pane:
			return None
		comp = pane.owner
		if comp is self.ownerComp or comp.path.startswith(self.ownerComp.path + '/'):
			return None
		rop = _getROP(comp) or _getROP(comp.currentChild)
		if rop:
			return rop
		for child in comp.selectedChildren:
			rop = _getROP(child, checkParents=False)
			if rop:
				return rop

	def SaveROP(self, incrementVersion=False):
		rop = self.GetCurrentROP()
		if not rop:
			# TODO: warning?
			return
		opDef = getOpDef(rop)
		if incrementVersion:
			opDef.par.Opversion += 1
		tox = rop.par.externaltox.eval()
		rop.save(tox)
		ui.status = f'Saved TOX {tox} (version: {opDef.par.Opversion})'

def _getROP(comp: 'COMP', checkParents=True):
	if not comp or comp is root:
		return None
	if 'raytkOP' in comp.tags:
		return comp
	if comp.name == 'opDefinition':
		host = comp.par.Hostop.eval()
		if host and 'raytkOP' in host.tags:
			return host
	if checkParents:
		return _getROP(comp.parent())

def _getMonitorHeight(usePrimary=True):
	if usePrimary:
		return monitors.primary.height
	for m in monitors:
		if not m.isPrimary:
			return m.height
	for m in monitors:
		return m.height

def getOpDef(comp: 'COMP'):
	return comp and comp.op('opDefinition')


