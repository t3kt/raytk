# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _stubs.TDCallbacksExt import CallbacksExt
	ext.Callbacks = CallbacksExt(None)

class Dialog:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp

	def ShowDialog(self):
		self.ownerComp.op('name_textfield').par.Value0 = ''
		self.ownerComp.op('window').par.winopen.pulse()

	def OnOk(self):
		name = self.ownerComp.op('name_textfield').par.Value0.eval()
		category = self.ownerComp.op('category_dropmenu').par.Value0.eval()
		if not name:
			return
		ext.Callbacks.DoCallback('onCreate', {'opName': name, 'opCategory': category})
		self.ownerComp.op('window').par.winclose.pulse()
