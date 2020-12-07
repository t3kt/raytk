# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class ParamHelpEditor:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.status = ''

	def addHelpColumn(self, dat: 'DAT'):
		if not dat.numRows:
			return
		host = self.ownerComp.par.Op.eval()
		if not host:
			dat.appendCol([])
		else:
			dat.appendCol([
				host.par[name].help
				for name in dat.col(0)
			])

	def Reload(self, _=None):
		if self.status == 'write':
			return
		self.status = 'read'
		try:
			self.ownerComp.op('editable_table').copy(self.ownerComp.op('built_table'))
		finally:
			self.status = ''

	def Writetopars(self, _=None):
		if self.status == 'read':
			return
		host = self.ownerComp.par.Op.eval()
		try:
			table = self.ownerComp.op('editable_table')
			invalid = []
			if not host:
				return
			ui.undo.startBlock(f'Update param help for {host}')
			for name in table.col(0):
				p = host.par[name]
				if p is None:
					invalid.append(name.val)
				else:
					p.help = table[name, 1].val
			if invalid:
				print(self.ownerComp, 'Params not found: ', invalid)
				parent().addScriptError('Params not found: ' + ', '.join(invalid))
			ui.undo.endBlock()
		finally:
			self.status = ''
		self.ownerComp.op('add_help_to_param_table').cook(force=True)
