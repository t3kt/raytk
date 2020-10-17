from typing import Callable

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class BuildContext:
	def __init__(self, log: Callable[[str], None]):
		self.log = log

	def detachTox(self, comp: 'COMP'):
		if not comp or comp.par['externaltox'] is None:
			return
		if not comp.par.externaltox and comp.par.externaltox.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching tox from {comp}')
		comp.par.reloadtoxonstart.expr = ''
		comp.par.reloadtoxonstart.val = False
		comp.par.externaltox.expr = ''
		comp.par.externaltox.val = ''

	def reclone(self, comp: 'COMP'):
		if not comp or not comp.par['enablecloningpulse'] or not comp.par['clone']:
			return
		self.log(f'Recloning {comp}')
		comp.par.enablecloningpulse.pulse()

	def disableCloning(self, comp: 'COMP'):
		if not comp or comp.par['enablecloning'] is None:
			return
		self.log(f'Disabling cloning on {comp}')
		comp.par.enablecloning.expr = ''
		comp.par.enablecloning = False

	def detachDat(self, dat: 'DAT'):
		if not dat or dat.par['file'] is None:
			return
		if not dat.par.file and dat.par.file.mode == ParMode.CONSTANT:
			return
		self.log(f'Detaching DAT {dat}')
		for par in dat.pars('syncfile', 'loadonstart', 'loadonstartpulse', 'write', 'writepulse'):
			par.expr = ''
			par.val = False
		dat.par.file.expr = ''
		dat.par.file.val = ''

	def resetCustomPars(self, o: 'OP'):
		if not o:
			return
		self.log(f'Resetting pars on {o}')
		for par in o.customPars:
			if par.readOnly or not par.enable:
				continue
			par.val = par.default

	def reloadTox(self, comp: 'COMP'):
		if not comp or not comp.par['reinitnet'] or not comp.par['externaltox']:
			return
		self.log(f'Reloading {comp.par.externaltox} for {comp}')
		comp.par.reinitnet.pulse()

	@staticmethod
	def queueAction(action: Callable, *args):
		run(f'args[0](*(args[1:]))', action, *args, delayFrames=5, delayRef=root)

	def runBuildScript(self, dat: 'DAT', thenRun: Callable, runArgs: list):
		self.log(f'Running build script: {dat}')

		def finishTask():
			self.log(f'Finished running build script: {dat}')
			self.queueAction(thenRun, *runArgs)
		subContext = BuildTaskContext(finishTask, self.log)
		dat.run(subContext)

class BuildTaskContext(BuildContext):
	"""
	Context passed to build scripts, in order to provide common tools, and to support asynchronously triggering the rest
	of the build process to continue.

	`
	context = args[0]  # type: BuildTaskContext
	doStuff()
	context.detachTox(foo)
	# This part is required:
	context.finishTask()
	`
	"""
	def __init__(
			self,
			finish: Callable[[], None],
			log: Callable[[str], None]):
		self.finish = finish
		super().__init__(log)

	def finishTask(self):
		self.finish()
