from raytkUtil import RaytkTags

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

class TestManager:
	def __init__(self, ownerComp: 'COMP'):
		self.ownerComp = ownerComp
		self.logTable = ownerComp.op('log')

	def RunTests(self):
		caseTable = self.ownerComp.op('testCaseTable')  # type: DAT
		for casePath in caseTable.col('path')[1:]:
			case = op(casePath)
			self.RunTestCase(case)

	def RunTestCase(self, testCase: 'COMP', thenRun: str = None, runArgs: list = None):
		self.log(f'Running test case {testCase}')
		outputs = testCase.findChildren(tags=[RaytkTags.raytkOutput.name], maxDepth=1)
		for output in outputs:
			shaderTop = output.par.Shadertop.eval()  # type: TOP
			if not shaderTop:
				continue
			shaderTop.cook(force=True)
			if shaderTop.warnings() or shaderTop.errors():
				self.log(f'FAILED test f{shaderTop}')
			else:
				self.log(f'PASSED test f{shaderTop}')
		if thenRun:
			self.queueMethodCall(thenRun, *(runArgs or []))

	def log(self, message: str):
		print(message)
		self.logTable.appendRow([message])

	def queueMethodCall(self, method: str, *args):
		if '.' in method:
			run(method, *args, delayFrames=5, delayRef=root)
		else:
			run(f'args[0].{method}(*(args[1:]))', self, *args, delayFrames=5, delayRef=root)
