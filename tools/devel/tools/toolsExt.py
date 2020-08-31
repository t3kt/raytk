from develCommon import *

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class Tools:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@staticmethod
	def IncrementMajor():
		version = getToolkitVersion()
		setToolkitVersion(Version(version.major + 1, 0))

	@staticmethod
	def IncrementMinor():
		version = getToolkitVersion()
		setToolkitVersion(Version(version.major, version.minor + 1))

	@staticmethod
	def ShowLibraryParams():
		getToolkit().openParameters()

	def UpdateROPMetadata(self, comp: 'COMP' = None):
		if comp is None:
			comp = self.GetCurrentROP()
		if not comp:
			return
		updateROPMetadata(comp)

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

	def SaveROP(self, incrementVersion=False, rop: 'COMP' = None):
		if not rop:
			rop = self.GetCurrentROP()
		if not rop:
			# TODO: warning?
			return
		self.UpdateROPMetadata(rop)
		if incrementVersion:
			rop.par.Raytkopversion = int(rop.par.Raytkopversion or 0) + 1
		tox = rop.par.externaltox.eval()
		rop.save(tox)
		ui.status = f'Saved TOX {tox} (version: {rop.par.Raytkopversion})'

	def ShowCreateNewRopTypeDialog(self):
		# noinspection PyUnresolvedReferences
		self.ownerComp.op('newRopTypeDialog').ShowDialog()

	def OnCreateNewRopTypeAccept(self, info: dict):
		name = info['opName']
		category = info['opCategory']
		dest = getToolkit().op('operators/' + category)
		if not dest:
			raise Exception(f'Invalid ROP category: {category!r}')
		template = dest.op('_template')
		if not template:
			raise Exception(f'No template available for category {category!r}')
		newOp = dest.copy(template, name=name)
		newOp.par.clone = newOp.path
		newOp.par.externaltox = f'src/operators/{category}/{name}.tox'
		self.UpdateROPMetadata(newOp)
		newOp.par.Raytkopversion = 0
		self.SaveROP(rop=newOp)
		newOp.selected = True
		newOp.nodeX = 0
		newOp.nodeY = -300
		opDef = newOp.op('opDefinition')
		codeDat = opDef.par.Functemplate.eval()
		if codeDat and codeDat.par['file'] is not None:
			codeDat.par.file = f'src/operators/{category}/{name}.glsl'
		self.NavigateTo(dest)

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

def setToolkitVersion(version: Version):
	toolkit = getToolkit()
	if toolkit.par['Raytkversion'] is None:
		page = toolkit.appendCustomPage('RayTK')
		page.appendStr('Raytkversion', label='RayTK Version')
	par = toolkit.par.Raytkversion
	par.val = str(version)
	par.readOnly = True
