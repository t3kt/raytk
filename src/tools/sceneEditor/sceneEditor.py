from raytkUtil import RaytkContext, ROPInfo
from typing import Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _StatePar:
		Selectedsceneroot: CompParamT
		Networkpane: PythonParamT[NetworkEditor]

	ipar.state = _StatePar()

class SceneEditor:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	@property
	def sceneRoot(self) -> Optional['COMP']:
		return ipar.state.Selectedsceneroot.eval()

	@property
	def networkPane(self) -> Optional['NetworkEditor']:
		pane = ipar.state.Networkpane.eval()
		if pane:
			return pane
		scene = self.sceneRoot
		if not scene:
			return
		for pane in ui.panes:
			if isinstance(pane, NetworkEditor):
				if pane.owner == scene:
					return pane

	def buildSceneInfo(self, dat: 'scriptDAT'):
		dat.clear()
		dat.appendCol([
			'path',
			'paneName', 'paneX', 'paneY', 'paneZoom',
			'paneL', 'paneR', 'paneT', 'paneB', 'paneW', 'paneH',
		])
		dat.appendCol([])
		scene = self.sceneRoot
		pane = self.networkPane
		if scene:
			dat['path', 1] = scene.path
		if pane:
			dat['paneName', 1] = pane.name
			dat['paneX', 1] = pane.x
			dat['paneY', 1] = pane.y
			dat['paneZoom', 1] = pane.zoom
			tr = pane.topRight
			bl = pane.bottomLeft
			dat['paneL', 1] = bl.x
			dat['paneR', 1] = tr.x
			dat['paneT', 1] = tr.y
			dat['paneB', 1] = bl.y
			dat['paneW', 1] = tr.x - bl.x
			dat['paneH', 1] = tr.y - bl.y

	def buildRopTable(self, dat: 'scriptDAT'):
		dat.clear()
		dat.appendRow([
			'name',
			'kind',
			'opType',
			'nodeX',
			'nodeY',
			'nodeW',
			'nodeH',
			'path',
			'colorr', 'colorg', 'colorb',
		])
		scene = self.sceneRoot
		if not scene:
			return
		context = RaytkContext()
		rops = context.ropChildrenOf(scene, maxDepth=1)
		for rop in rops:
			ropInfo = ROPInfo(rop)
			opDef = ropInfo.opDef
			compImg = opDef.op('opImage/compImage')
			if compImg:
				color = [compImg.par.Bgcolorr, compImg.par.Bgcolorg, compImg.par.Bgcolorb]
			else:
				color = [0.5, 0.5, 0.5]
			dat.appendRow([
				rop.name,
				ropInfo.ropKind or '',
				ropInfo.opType or '',
				rop.nodeX,
				rop.nodeY,
				rop.nodeWidth,
				rop.nodeHeight,
				rop.path,
			] + color)
