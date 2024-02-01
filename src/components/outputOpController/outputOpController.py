# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *

	class _Par:
		Hostop: OPParamT
		Glslop: OPParamT

	class _COMP(COMP):
		par: _Par

class OutputOp:
	def __init__(self, ownerComp: '_COMP'):
		self.ownerComp = ownerComp

	def onInit(self):
		self.updateParamSequences()

	def onUniformsChange(self):
		self.updateParamSequences()

	def updateParamSequences(self):
		targetOp = self.ownerComp.par.Glslop.eval()
		if not targetOp:
			return
		table = self.ownerComp.op('uniforms')
		if table.numRows < 2:
			return
		constCount = 0
		arrayCount = 0
		for i in range(1, table.numRows):
			if table[i, 'uniformType'] == 'constant':
				constCount += 1
			elif table[i, 'uniformType'] == 'uniformarray':
				arrayCount += 1
		if constCount > 0:
			if targetOp.isMAT:
				raise Exception('Specialization constants not yet supported in MATs!')
			sequence = targetOp.par.const0name.sequence  # type: Sequence
			if constCount > sequence.numBlocks:
				sequence.numBlocks = constCount
		sequence = targetOp.par.array0name.sequence
		if arrayCount > sequence.numBlocks:
			sequence.numBlocks = arrayCount
