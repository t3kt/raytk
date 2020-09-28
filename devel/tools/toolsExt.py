from develCommon import *
from typing import Callable, Tuple
import popMenu

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

	def UpdateCurrentROPsMetadata(self, incrementVersion=False):
		rops = self.getCurrentROPs(primaryOnly=False)
		for rop in rops:
			updateROPMetadata(rop, incrementVersion=incrementVersion)

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
		rops = self.getCurrentROPs(primaryOnly=True)
		return rops[0] if rops else None

	def getCurrentROPs(self, primaryOnly=False):
		pane = self.GetActiveEditor()
		if not pane:
			return []
		comp = pane.owner
		if comp is self.ownerComp or comp.path.startswith(self.ownerComp.path + '/'):
			return None
		rop = _getROP(comp) or _getROP(comp.currentChild)
		if rop and primaryOnly:
			return [rop]
		rops = [rop]
		for child in comp.selectedChildren:
			rop = _getROP(child, checkParents=False)
			if rop:
				rops.append(rop)
		return rops

	def SaveCurrentROPs(self, incrementVersion=False):
		rops = self.getCurrentROPs(primaryOnly=False)
		if not rops:
			return
		for rop in rops:
			self.SaveROP(incrementVersion=incrementVersion, rop=rop)
		if len(rops) > 1:
			ui.status = f'Saved {len(rops)} ROP TOXs'

	def SaveROP(self, incrementVersion=False, rop: 'COMP' = None):
		if not rop:
			rop = self.GetCurrentROP()
		if not rop:
			# TODO: warning?
			return
		self.updateROPParams(rop)
		updateROPMetadata(rop, incrementVersion=incrementVersion)
		tox = rop.par.externaltox.eval()
		rop.save(tox)
		ui.status = f'Saved TOX {tox} (version: {rop.op("opDefinition").par.Raytkopversion})'
		for dat in getToolkit().ops('opfind_rops', 'opCategoryTable'):
			dat.cook(force=True)

	@staticmethod
	def updateROPParams(rop: 'COMP'):
		if rop.customPages:
			page = rop.customPages[0]
		else:
			page = rop.appendCustomPage('Settings')
		opDef = rop.op('opDefinition')
		if rop.ops('definition_1', 'definition_2', 'definition_3', 'definition_4') and 'raytkOutput' not in rop.tags:
			enablePar = rop.par['Enable']
			if enablePar is None:
				enablePar = page.appendToggle('Enable')[0]
				enablePar.val = True
			enablePar.order = -1
			enablePar.default = True
			if not opDef.par.Enable.expr:
				opDef.par.Enable.expr = "op('..').par.Enable"

		inspectPar = rop.par['Inspect']
		if inspectPar is None:
			inspectPar = page.appendPulse('Inspect')[0]
		inspectPar.startSection = True
		inspectPar.order = 99999

	def editCurrentROPMaster(self):
		rop = self.GetCurrentROP()
		if not rop:
			return
		rop = rop.par.clone.eval() or rop
		self.NavigateTo(rop.par.clone.eval())

	def setCurrentROPBeta(self, beta: bool):
		rops = self.getCurrentROPs()
		color = self.getColorPar('Betacolor' if beta else 'Defaultcolor')
		for rop in rops:
			opDef = rop.op('opDefinition')
			if opDef:
				_toggleTag(opDef, 'raytkBeta', beta)
				opDef.color = color
			rop.color = color

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
		updateROPMetadata(newOp)
		self.SaveROP(rop=newOp)
		newOp.selected = True
		newOp.nodeX = 0
		newOp.nodeY = -300
		opDef = newOp.op('opDefinition')
		codeDat = opDef.par.Functemplate.eval()
		if codeDat and codeDat.par['file'] is not None:
			codeDat.par.file = f'src/operators/{category}/{name}.glsl'
		self.NavigateTo(dest)

	def OnOperatorsShortcutRightClick(self, button: 'COMP'):
		def goToItem(name, path):
			return popMenu.Item(
				name,
				callback=lambda: self.NavigateTo(op(path)),
			)

		categoryTable = self.ownerComp.op('rop_categories')
		popMenu.fromButton(button, h='Right', v='Top').Show(
			[
				goToItem(categoryTable[i, 'name'].val, categoryTable[i, 'path'])
				for i in range(1, categoryTable.numRows)
			]
		)

	def setBuildExcludeStateOnSelected(self, state: bool):
		self.setTagAndColorOnSelected(
			'buildExclude', state,
			self.getColorPar('Buildexcludecolor' if state else 'Defaultcolor'))

	def setFileSyncOnSelected(self, state: bool):
		self.setTagAndColorOnSelected(
			'fileSync', state,
			self.getColorPar('Filesynccolor' if state else 'Defaultcolor'),
			update=lambda o: _updateFileSyncPars(o, state))

	def setTagAndColorOnSelected(
			self, tag: str, state: bool, color: Tuple[float, float, float],
			update: Callable = None):
		def _action(o: 'OP'):
			_toggleTag(o, tag, state)
			o.color = color
			if update:
				update(o)
		self.forEachSelected(_action)

	def getColorPar(self, name: str):
		return (
			float(self.ownerComp.par[name + 'r']),
			float(self.ownerComp.par[name + 'g']),
			float(self.ownerComp.par[name + 'b']),
		)

	def DestroySelectedCustomPars(self):
		def _action(o: 'OP'):
			print('OMG destroy pars', o)
			if hasattr(o, 'destroyCustomPars'):
				o.destroyCustomPars()
		self.forEachSelected(_action)

	def forEachSelected(self, action):
		editor = self.GetActiveEditor()
		if not editor:
			return
		for o in editor.owner.selectedChildren:
			action(o)

def _updateFileSyncPars(o: 'OP', state: bool):
	if o.isDAT:
		par = o.par['syncfile']
		if par is not None:
			par.expr = ''
			par.val = state
			if not state:
				for par in o.pars('loadonstart', 'loadonstartpulse', 'write', 'writepulse'):
					par.expr = ''
					par.val = False
		else:
			for par in o.pars('loadonstart', 'loadonstartpulse', 'write', 'writepulse'):
				par.expr = ''
				par.val = state
	else:
		# TODO: support for other types of OPs
		raise Exception(f'updateFileSyncPars does not yet support op: {o}')

def _toggleTag(o: 'OP', tag: str, state: bool):
	if not o:
		return
	if state:
		o.tags.add(tag)
	elif tag in o.tags:
		o.tags.remove(tag)

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
