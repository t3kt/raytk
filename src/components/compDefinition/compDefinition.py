import re

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _stubs.PopDialogExt import PopDialogExt

def buildName(host):
	if not host:
		return ''
	pathParts = host.path[1:].split('/')
	for i in range(len(pathParts)):
		if pathParts[i].startswith('_'):
			pathParts[i] = 'U' + pathParts[i][1:]
	name = '_'.join(pathParts)
	name = re.sub('_+', '_', name)
	if name.startswith('_'):
		name = 'o_' + name
	return 'RTK_' + name

def _useLocalHelp():
	return hasattr(op, 'raytk') and bool(op.raytk.par['Devel'])

def _popDialog() -> 'PopDialogExt':
	# noinspection PyUnresolvedReferences
	return op.TDResources.op('popDialog')

def ensureExt(comp):
	if not getattr(comp.ext, 'compDefinition', None):
		comp.par.reinitextensions.pulse()

class CompDefinition:
	def __init__(self, opDefComp: COMP):
		self.opDefComp = opDefComp
		self.hostRop = opDefComp.par.Hostop.eval()

	def inspect(self):
		for o in self.opDefComp.par.Rops.evalOPs():
			par = o.par['Inspect']
			if par is not None:
				par.pulse()
				return

	def launchHelp(self):
		url = self.opDefComp.par.Helpurl.eval()
		if not url:
			return
		if _useLocalHelp():
			url = url.replace('https://t3kt.github.io/raytk/', 'http://localhost:4000/raytk/')
		if url:
			ui.viewFile(url)

	def updateOP(self):
		if not hasattr(op, 'raytk'):
			_popDialog().Open(
				title='Warning',
				text='Unable to update OP because RayTK toolkit is not available.',
				escOnClickAway=True,
			)
			return
		host = self.hostRop
		toolkit = op.raytk
		updater = toolkit.op('tools/updater')
		if updater and hasattr(updater, 'UpdateOP'):
			updater.UpdateOP(host)
			return
		if not host.par.clone:
			msg = 'Unable to update OP because master is not found in the loaded toolkit.'
			if self.opDefComp.par.Raytkopstatus == 'deprecated':
				msg += '\nNOTE: This OP has been marked as "Deprecated", so it may have been removed from the toolkit.'
			_popDialog().Open(
				title='Warning',
				text=msg,
				escOnClickAway=True,
			)
			return
		if host and host.par.clone:
			host.par.enablecloningpulse.pulse()
