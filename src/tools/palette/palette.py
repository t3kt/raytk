from typing import Callable, Optional
from raytkUtil import RaytkContext, detachTox, focusFirstCustomParameterPage, ROPInfo, IconColors

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from components.opPicker.opPicker import OpPicker, PickerItem

	ext.opPicker = OpPicker(COMP())

	class _Par(ParCollection):
		Devel: 'BoolParamT'
		Defaultshowalpha: 'BoolParamT'
		Defaultshowbeta: 'BoolParamT'
		Defaultshowdeprecated: 'BoolParamT'
	class _COMP(panelCOMP):
		par: _Par

	class _UIStatePar(ParCollection):
		Showalpha: 'BoolParamT'
		Showbeta: 'BoolParamT'
		Showdeprecated: 'BoolParamT'
		Showhelp: 'BoolParamT'
		Pinopen: 'BoolParamT'

	ipar.uiState = _UIStatePar()

# columns:
#  name
#  status icon

class Palette:
	def __init__(self, ownerComp: 'COMP'):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.selItem = tdu.Dependency()  # value type _AnyItemT
		self.isOpen = tdu.Dependency(False)

	def Initialize(self):
		ext.opPicker.SetFilterToggles(
			alpha=self.ownerComp.par.Defaultshowalpha.eval(),
			beta=self.ownerComp.par.Defaultshowbeta.eval(),
			deprecated=self.ownerComp.par.Defaultshowdeprecated.eval(),
		)
		ext.opPicker.Resetstate()

	@property
	def _closeTimer(self) -> 'timerCHOP':
		# noinspection PyTypeChecker
		return self.ownerComp.op('closeTimer')

	@property
	def _develMode(self):
		return bool(self.ownerComp.par.Devel)

	@property
	def SelectedItem(self):
		return ext.opPicker.SelectedItem

	def Show(self, _=None):
		self.open()

	def open(self):
		self._resetCloseTimer()
		self.ownerComp.op('window').par.winopen.pulse()
		self._resetState()
		self.isOpen.val = True
		ipar.uiState.Pinopen = False
		ext.opPicker.Loaditems()
		ext.opPicker.FocusFilterField()
		image = RaytkContext().libraryImage()
		if image and image.par['Showshortcut'] is not None:
			image.par.Showshortcut = False

	def close(self):
		self._resetCloseTimer()
		self.ownerComp.op('window').par.winclose.pulse()
		self.isOpen.val = False
		ipar.uiState.Pinopen = False

	def resetState(self):
		self._resetCloseTimer()
		self._resetState()

	def onCloseTimerComplete(self):
		if ipar.uiState.Pinopen:
			self._resetCloseTimer()
			return
		self.close()

	def _resetCloseTimer(self):
		timer = self._closeTimer
		timer.par.initialize.pulse()
		timer.par.active = False

	def _startCloseTimer(self):
		timer = self._closeTimer
		timer.par.active = True
		timer.par.start.pulse()

	def onPanelInsideChange(self, val: bool):
		if val:
			self._resetCloseTimer()
		else:
			self._startCloseTimer()

	def _resetState(self):
		ext.opPicker.Resetstate()
		self.isOpen.val = False

	def onKeyboardShortcut(self, shortcutName: str):
		if shortcutName == 'esc':
			self.close()

	def CreateItem(self, templatePath: str, postSetup: 'Optional[Callable[[COMP], None]]' = None):
		template = self._getTemplate(templatePath)
		if not template:
			self._printAndStatus(f'Unable to find template for path: {templatePath}')
			return
		pane = RaytkContext().activeEditor()
		dest = pane.owner if pane else None
		if not dest:
			self._printAndStatus('Unable to find active network editor pane')
			return
		newOp = self._createROP(
			template=template,
			dest=dest,
			nodeX=pane.x,
			nodeY=pane.y,
			name=template.name + ('1' if tdu.digits(template.name) is None else ''),
			postSetup=postSetup,
		)
		ui.undo.startBlock(f'Create ROP {template.name}')
		ui.undo.addCallback(self._createItemDoHandler, {
			'template': template,
			'dest': dest,
			'nodeX': pane.x,
			'nodeY': pane.y,
			'name': newOp.name,
			'postSetup': postSetup,
		})
		ui.undo.endBlock()
		if not ipar.uiState.Pinopen:
			self.close()

	def _createROP(
			self,
			template: 'COMP', dest: 'COMP',
			nodeX: int, nodeY: int, name: str,
			postSetup: 'Optional[Callable[[COMP], None]]' = None,
	):
		newOp = dest.copy(
			template,
			name=name,
		)  # type: COMP
		newOp.nodeCenterX = nodeX
		newOp.nodeCenterY = nodeY
		detachTox(newOp)
		img = newOp.op('*Definition/opImage')
		if img:
			detachTox(img)
			enableCloning = img.par.enablecloning  # type: Par
			enableCloning.expr = ''
			enableCloning.val = self._develMode
			newOp.par.opviewer.val = img
			newOp.viewer = True
		enableCloning = newOp.par.enablecloning  # type: Par
		enableCloning.expr = ''
		enableCloning.val = self._develMode
		focusFirstCustomParameterPage(newOp)
		for par in newOp.customPars:
			if par.readOnly or par.isPulse or par.isMomentary or par.isDefault:
				continue
			if par.mode in (ParMode.EXPORT, ParMode.BIND):
				continue
			if par.defaultExpr and par.defaultExpr != par.default:
				par.expr = par.defaultExpr
			else:
				par.val = par.default
		newOp.allowCooking = True
		newOp.color = IconColors.defaultBgColor
		if postSetup:
			postSetup(newOp)
		ropInfo = ROPInfo(newOp)
		ropInfo.invokeCallback('onCreate', master=template)
		self._printAndStatus(f'Created OP: {newOp} from {template}')
		return newOp

	def _createItemDoHandler(self, isUndo: bool, info: dict):
		dest = info['dest']  # type: COMP
		name = info['name']
		if isUndo:
			print(self.ownerComp, f'undoing create OP: {info}')
			newOp = dest.op(name)
			if newOp and newOp.valid:
				try:
					newOp.destroy()
				except:
					pass
		else:
			print(self.ownerComp, f'redoing create OP: {info}')
			self._createROP(
				template=info['template'],
				dest=dest,
				nodeX=info['nodeX'],
				nodeY=info['nodeY'],
				name=name,
				postSetup=info['postSetup'],
			)

	def CreateVariableReference(
			self,
			fromOp: 'COMP', variable: str, dataType: str,
			postSetup: 'Optional[Callable[[COMP], None]]' = None):
		def initRef(refOp: 'COMP'):
			refOp.par.Source.val = fromOp
			refOp.par.Source.readOnly = True
			refOp.par.Variable = variable
			refOp.par.Variable.readOnly = True
			refOp.par.Datatype = dataType
			refOp.par.Datatype.readOnly = True
			if postSetup:
				postSetup(refOp)
		self.CreateItem(
			'/raytk/operators/utility/variableReference',
			postSetup=initRef
		)

	def CreateRenderSelect(self, fromOp: 'COMP', outputName: str):
		def initSel(refOp: 'COMP'):
			refOp.par.Outputop.val = fromOp
			refOp.par.Outputop.readOnly = True
			refOp.par.Outputbuffer.val = outputName
			refOp.par.Outputbuffer.readOnly = True
		self.CreateItem(
			'/raytk/operators/output/renderSelect',
			postSetup=initSel
		)

	def _printAndStatus(self, msg):
		print(self.ownerComp, msg)
		ui.status = msg

	@staticmethod
	def _getTemplate(path: str):
		if not path:
			return
		if path.startswith('raytk.operators.'):
			path = '/' + path.replace('.', '/')
		if not path.startswith('/raytk/'):
			return op(path)
		context = RaytkContext()
		toolkit = context.toolkit()
		if toolkit and toolkit.path == '/raytk':
			return op(path)
		if not toolkit:
			return op(path)
		return op(path.replace('/raytk/', f'/{toolkit.path}/', 1))

	def onPickItem(self, item: 'PickerItem'):
		if not item:
			return
		if item.isCategory:
			# TODO: maybe expand/collapse?
			return
		self.CreateItem(item.path)

	def onRolloverItem(self, item: 'Optional[PickerItem]'):
		self.ownerComp.op('thumbImage').cook(force=True)
