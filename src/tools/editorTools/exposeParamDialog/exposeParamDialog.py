from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class _StructureTypes:
	same = 0
	separate = 1

class ExposeParamDialog:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.header = ownerComp.op('header')
		self.window = ownerComp.op('window')
		self.sceneField = ownerComp.op('sceneField')
		self.prefixField = ownerComp.op('prefixField')
		self.pageDropDownField = ownerComp.op('pageDropDownField')
		self.structureDropDownMenu = ownerComp.op('structureDropDownMenu')
		self.targetPar = None  # type: Optional[Par]
		self.targetTuplet = None  # type: Optional[ParTupletT]

	def ShowForParam(self, par: 'Par', scene: 'Optional[COMP]'):
		self.header.par.Headerlabel = f'Expose Parameter: {par.label} ({par.name})'
		self.targetPar = par
		self.targetTuplet = None
		self._initializeAndShow(scene)

	def ShowForTuplet(self, parTuplet: 'ParTupletT', scene: 'Optional[COMP]'):
		if len(parTuplet) == 1:
			self.ShowForParam(parTuplet[0], scene)
			return
		tupletName = parTuplet[0].tupletName
		suffixes = ''.join([p.name.replace(tupletName, '') for p in parTuplet])
		self.header.par.Headerlabel = f'Expose Parameter: {parTuplet[0].label} ({tupletName}[{suffixes}])'
		self.targetPar = None
		self.targetTuplet = parTuplet
		self._initializeAndShow(scene)

	def _initializeAndShow(self, scene: 'Optional[COMP]'):
		if self.targetPar is not None:
			if not scene:
				scene = self.targetPar.owner.parent()
			self.structureDropDownMenu.par.enable = False
		elif self.targetTuplet is not None:
			if not scene:
				scene = self.targetTuplet[0].owner.parent()
			self.structureDropDownMenu.par.enable = True
		else:
			return
		pageNames = [page.name for page in scene.customPages]
		self.pageDropDownField.par.Menunames = ' '.join(pageNames)
		self.pageDropDownField.par.Value0 = pageNames[0] if pageNames else 'Scene'
		self.structureDropDownMenu.par.Value0 = 'same'
		self.sceneField.par.Value0 = scene.path if scene else ''
		self.prefixField.par.Value0 = ''
		self.window.par.winopen.pulse()

	def onOk(self):
		structure = self.structureDropDownMenu.par.Value0.eval()
		scene = self.sceneField.par.Value0.eval()  # type: COMP
		prefix = self.prefixField.par.Value0.eval()  # type: str
		pageName = self.pageDropDownField.par.Value0.eval()  # type: str
		if scene and (self.targetPar is not None or self.targetTuplet is not None):
			self._exposeParams(structure, scene, prefix, pageName)
		self.Close()

	def _exposeParams(
			self, structure: str, scene: 'COMP', prefix: str, pageName: str):
		if not scene:
			return
		if self.targetPar is not None:
			srcPars = [self.targetPar]
			par1 = self.targetPar
		elif self.targetTuplet is not None:
			srcPars = self.targetTuplet
			par1 = self.targetTuplet[0]
		else:
			return
		label = (prefix + ' ' if prefix else '') + par1.label
		prefix = prefix.replace(' ', '')
		ui.undo.startBlock(f'Expose parameter {par1.label}')
		scenePage = scene.appendCustomPage(pageName or 'Scene')
		if par1.isMenu:
			newPars = scenePage.appendMenu((prefix + par1.name).capitalize(), label=label)
			newPars[0].menuSource = scene.shortcutPath(par1.owner, toParName=par1.name)
		elif len(srcPars) == 1:
			newPars = scenePage.appendPar((prefix + par1.name).capitalize(), par=par1, label=label)
		elif structure == 'separate':
			newPars = []
			for i, srcPar in enumerate(srcPars):
				srcPar = srcPars[i]
				newName = (prefix + srcPar.name).capitalize()
				suffix = srcPar.name.replace(srcPar.tupletName, '').capitalize()
				if srcPar.isInt:
					newPar = scenePage.appendInt(newName, label=label + ' ' + suffix.upper())[0]
				else:
					newPar = scenePage.appendFloat(newName, label=label + ' ' + suffix.upper())[0]
				_copySettings(newPar, srcPar)
				newPars.append(newPar)
		else:
			newPars = scenePage.appendPar((prefix + par1.tupletName).capitalize(), par=par1, label=label)
		for i, newPar in enumerate(newPars):
			srcPar = srcPars[i]
			newPar.val = srcPar.eval()
			srcPar.bindExpr = srcPar.owner.shortcutPath(scene, toParName=newPar.name)
		ui.undo.endBlock()

	def onCancel(self):
		self.Close()

	def Close(self):
		self.window.par.winclose.pulse()

def _copySettings(newPar: 'Par', srcPar: 'Par'):
	newPar.default = srcPar.default
	newPar.min = srcPar.min
	newPar.max = srcPar.max
	newPar.normMin = srcPar.normMin
	newPar.normMax = srcPar.normMax
	newPar.clampMin = srcPar.clampMin
	newPar.clampMax = srcPar.clampMax
