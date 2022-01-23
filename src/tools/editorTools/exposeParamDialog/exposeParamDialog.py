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
		self.structureDropDownMenu.par.Value0 = 'same'
		self.sceneField.par.Value0 = scene or ''
		self.prefixField.par.Value0 = ''
		self.window.par.winopen.pulse()
		pass

	def onOk(self):
		pass

	def onCancel(self):
		self.Close()

	def Close(self):
		self.window.par.winclose.pulse()
		pass
