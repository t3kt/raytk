from raytkTools import RaytkTools
from raytkUtil import RaytkModuleContext

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from ..ropEditor.ropEditor import ROPEditor
	iop.ropEditor = ROPEditor(COMP())

class CreateRopDialog:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	def _setMessageText(self, message):
		dat = self.ownerComp.op('set_messageText')
		dat.clear()
		dat.write(message or '')

	def Open(self, _=None):
		self.ownerComp.op('window').par.winopen.pulse()
		self.ownerComp.op('typeName_field').par.Value0 = ''
		self._setMessageText('')

	def Close(self, _=None):
		self.ownerComp.op('window').par.winclose.pulse()
		self._setMessageText('')

	def Create(self):
		self._setMessageText('')
		category = self.ownerComp.op('category_dropmenu').par.Value0.eval()
		name = self.ownerComp.op('typeName_field').par.Value0.eval()
		moduleName = self.ownerComp.op('module_dropmenu').par.Value0.eval()
		moduleRoot = op(self.ownerComp.op('moduleTable')[moduleName, 'moduleRoot'])
		if not moduleRoot:
			self._setMessageText(f'Invalid module: {moduleName}')
			return
		context = RaytkModuleContext(moduleRoot)
		try:
			rop = RaytkTools(context).createNewRopType(typeName=name, category=category)
		except Exception as err:
			self._setMessageText(str(err))
			return
		iop.ropEditor.LoadROP(rop)
		self.Close()
