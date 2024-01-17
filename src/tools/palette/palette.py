from raytkUtil import RaytkContext, detachTox, focusFirstCustomParameterPage, ROPInfo, IconColors

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	from components.opPicker.opPicker import OpPicker, PickerItem

	ext.opPicker = OpPicker(COMP())

	class _Par(ParCollection):
		Devel: BoolParamT
		Defaultshowalpha: BoolParamT
		Defaultshowbeta: BoolParamT
		Defaultshowdeprecated: BoolParamT

	class _COMP(panelCOMP):
		par: _Par

	class _UIStatePar(ParCollection):
		Showalpha: BoolParamT
		Showbeta: BoolParamT
		Showdeprecated: BoolParamT
		Showhelp: BoolParamT
		Pinopen: BoolParamT

	ipar.uiState = _UIStatePar()


USE_PLACE_OPS = True

# columns:
#  name
#  status icon

class Palette:
	def __init__(self, ownerComp: COMP):
		# noinspection PyTypeChecker
		self.ownerComp = ownerComp  # type: _COMP
		self.selItem = tdu.Dependency()  # value type _AnyItemT
		self.isOpen = tdu.Dependency(False)
		self._closeTask = None  # type: Run | None

	def Initialize(self):
		ext.opPicker.SetFilterToggles(
			alpha=self.ownerComp.par.Defaultshowalpha.eval(),
			beta=self.ownerComp.par.Defaultshowbeta.eval(),
			deprecated=self.ownerComp.par.Defaultshowdeprecated.eval(),
		)
		ext.opPicker.SetViewOptions(
			statusChips=True,
			displayCategories=True,
		)
		ext.opPicker.Resetstate()

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

	def _onCloseTimerComplete(self):
		if ipar.uiState.Pinopen:
			self._resetCloseTimer()
			return
		self.close()

	def _resetCloseTimer(self):
		if self._closeTask:
			self._closeTask.kill()
			self._closeTask = None

	def _startCloseTimer(self):
		self._resetCloseTimer()
		self._closeTask = run(
			'args[0]()', self._onCloseTimerComplete,
			delayMilliSeconds=1000)

	def onPanelInsideChange(self, val: bool):
		if val:
			self._resetCloseTimer()
		else:
			self._startCloseTimer()

	def _resetState(self):
		for finder in self.ownerComp.ops('findOpTables', 'findOpHelpTables'):
			finder.par.cookpulse.pulse()
		ext.opPicker.Resetstate()
		self.isOpen.val = False

	def onKeyboardShortcut(self, shortcutName: str):
		if shortcutName == 'esc':
			self.close()

	def CreateItem(
			self, templatePath: str,
			postSetup: 'Callable[[COMP], None] | None' = None,
			undoSetup: 'Callable[[], None] | None' = None,
	):
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
			pane=pane,
			nodeX=pane.x,
			nodeY=pane.y,
			name=template.name + ('1' if tdu.digits(template.name) is None else ''),
			postSetup=postSetup,
		)
		ui.undo.startBlock(f'Create ROP {template.name}')
		ui.undo.addCallback(self._createItemDoHandler, {
			'template': template,
			'dest': dest,
			'pane': pane,
			'nodeX': pane.x,
			'nodeY': pane.y,
			'name': newOp.name,
			'postSetup': postSetup,
			'undoSetup': undoSetup,
		})
		ui.undo.endBlock()
		if not ipar.uiState.Pinopen:
			self.close()

	def _createROP(
			self,
			template: COMP, dest: COMP, pane: NetworkEditor,
			nodeX: int, nodeY: int, name: str,
			postSetup: 'Callable[[COMP], None] | None' = None,
	):
		# when using postSetup, placeOPs won't work so don't use it
		if not postSetup and op('/sys/quiet'):
			bufferArea = op('/sys/quiet').create(baseCOMP)
		else:
			bufferArea = dest
		newOp = bufferArea.copy(
			template,
			name=name,
		)  # type: COMP
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
		if ROPInfo(newOp).isOutput and newOp.par['Resx'] is not None:
			if _isNonCommercial():
				newOp.par.Resx = 1280
				newOp.par.Resy = 720
		if not postSetup:
			pane.placeOPs([newOp], delOP=bufferArea if bufferArea is not dest else None)
		else:
			newOp.nodeCenterX = nodeX
			newOp.nodeCenterY = nodeY
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
			undoSetup = info['undoSetup']
			if undoSetup:
				try:
					undoSetup()
				except:
					pass
		else:
			print(self.ownerComp, f'redoing create OP: {info}')
			self._createROP(
				template=info['template'],
				dest=dest,
				pane=info['pane'],
				nodeX=info['nodeX'],
				nodeY=info['nodeY'],
				name=name,
				postSetup=info['postSetup'],
			)

	def CreateVariableReference(
			self,
			fromOp: COMP, variable: str, dataType: str,
			postSetup: 'Callable[[COMP], None] | None' = None):
		def initRef(refOp: COMP):
			# assume that they're in the same parent
			refOp.par.Source.val = fromOp.name
			refOp.par.Source.readOnly = True
			refOp.par.Variable = variable
			refOp.par.Variable.readOnly = True
			refOp.par.Variabletype = dataType
			refOp.par.Variabletype.readOnly = True
			if refOp.par['Datatype'] is not None:
				refOp.par.Datatype.enable = False
			if refOp.par['Part'] is not None:
				refOp.par.Part.enable = False
			if postSetup:
				postSetup(refOp)
		self.CreateItem(
			'/raytk/operators/utility/variableReference',
			postSetup=initRef
		)

	def CreateRenderSelect(
			self, fromOp: COMP, outputName: str,
			postSetup: 'Callable[[COMP], None] | None' = None):
		def initSel(refOp: COMP):
			# assume that they're in the same parent
			refOp.par.Outputop.val = fromOp.name
			refOp.par.Outputop.readOnly = True
			refOp.par.Outputbuffer.val = outputName
			refOp.par.Outputbuffer.readOnly = True
			if postSetup:
				postSetup(refOp)
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

	def IsKnownType(self, pathOrOpType: str):
		return bool(self._getTemplate(pathOrOpType))

	def onPickItem(self, item: 'PickerItem'):
		if not item:
			return
		if item.isCategory:
			# TODO: maybe expand/collapse?
			return
		self.CreateItem(item.path)

	def onRolloverItem(self, item: 'PickerItem | None'):
		self.ownerComp.op('thumbImage').cook(force=True)

def _isNonCommercial():
	import td
	return td.licenses.isNonCommercial
