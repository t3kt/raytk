from raytkUtil import ROPInfo, showMessageDialog

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class Updater:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	# This MUST remain publicly available since OPs reference it for the `Updateop` par handler.
	def UpdateOP(self, o: COMP):
		self._log(f'Updating {o}')
		info = ROPInfo(o)
		if not info:
			self._showError(f'Unable to update {o}, it must be a ROP or RComp')
			return
		master = o.par.clone.eval()
		if not master and o.par.clone.val.startswith('/raytk/'):
			path = o.par.clone.val  # type: str
			if path.startswith('/raytk/'):
				path = path.replace('/raytk/', '')
			master = parent.raytk.op(path)
			if not master:
				self._showError(f'Unable to update {o}, no clone master found')
				return
			o.par.clone = master
		self._log(f'Updating {o} using master {master}')
		postAction = self._getPostUpdateAction(info)
		o.par.enablecloningpulse.pulse()
		if postAction:
			run('args[0](args[1])', postAction, o, delayFrames=2)
		img = o.op('*Definition/opImage')
		if img:
			o.par.opviewer.val = img
			o.viewer = True
		o.par.clone = master.par.clone.val

	def _getPostUpdateAction(self, info: 'ROPInfo'):
		if info.opType == 'raytk.operators.utility.variableReference':
			if info.rop.par['Variabletype'] is not None:
				origType = info.rop.par.Variabletype.eval()
				origField = info.rop.par.Field.eval()
				def _action(rop: COMP):
					self._log(f'Restoring params for variableReference {info.rop} (origType: {origType}, origField: {origField})')
					rop.par.Variabletype = origType
					rop.par.Field = origField
					def _after():
						self._log(f'Afterwards... {info.rop} (newType: {rop.par.Variabletype}, newField: {rop.par.Field})')
					run('args[0]()', _after, delayFrames=3)
				return _action
			elif info.rop.par['Datatype'] is not None:
				originalType = info.rop.par.Datatype.eval()
				originalPart = info.rop.par.Part.eval()
				def _action(rop: COMP):
					self._log(f'Converting params for variableReference {info.rop} (origType: {originalType}, origPart: {originalPart})')
					rop.par.Variabletype = originalType
					if originalPart == 'vec':
						rop.par.Field = ''
					else:
						rop.par.Field = originalPart
					rop.par.Variabletype.readOnly = True
					rop.par.Datatype.readOnly = False
					rop.par.Datatype.enable = False
					rop.par.Part.enable = False
				return _action

	def _showError(self, msg: str):
		self._log(msg)
		showMessageDialog(
			title='Warning',
			text=msg,
			escOnClickAway=True,
		)

	def _log(self, msg: str):
		print(self.ownerComp, msg)
		ui.status = msg
