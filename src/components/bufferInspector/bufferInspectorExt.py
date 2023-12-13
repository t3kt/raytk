from typing import List, Tuple, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

	class ipar:
		class bufInsp:
			Showpointsampling: 'Union[bool, Par]'
			Samplepointu: 'Union[float, Par]'
			Samplepointv: 'Union[float, Par]'

class BufferInspector:
	def __init__(self, ownerComp: COMP):
		self.ownerComp = ownerComp

	def buildMaskChanSettings(self, dat: DAT):
		dat.clear()
		r = self.ownerComp.par.Showr
		g = self.ownerComp.par.Showg
		b = self.ownerComp.par.Showb
		a = self.ownerComp.par.Showa
		parts = ('r' if r else '') + ('g' if g else '') + ('b' if b else '') + ('a' if a else '')

		if parts == 'a':
			sourceR = sourceG = sourceB = 'one'
			sourceA = 'alpha'
		else:
			sourceR = 'red' if r else 'zero'
			sourceG = 'green' if r else 'zero'
			sourceB = 'blue' if r else 'zero'
			sourceA = 'alpha' if r else 'zero'

		if parts in ('r', 'ra'):
			mono = 1
			monoRgb = 'red'
		elif parts in ('g', 'ga'):
			mono = 1
			monoRgb = 'green'
		elif parts in ('b', 'ba'):
			mono = 1
			monoRgb = 'blue'
		else:
			mono = 0
			monoRgb = 'luminance'

		dat.appendRows([
			['r', sourceR],
			['g', sourceG],
			['b', sourceB],
			['a', sourceA],
			['mono', mono],
			['monorgb', monoRgb],
		])

	def onRightClickPreview(self, previewPanel: 'PanelCOMP'):
		u = previewPanel.panel.u
		v = previewPanel.panel.v
		self.Sample(u, v)

	def onCloseSampleClick(self):
		ipar.bufInsp.Showpointsampling = False
		self.Clear()

	def Sample(self, u, v):
		print(self.ownerComp, 'SAMPLE', u, v)
		ipar.bufInsp.Samplepointu = u
		ipar.bufInsp.Samplepointv = v
		ipar.bufInsp.Showpointsampling = True
		self.fillSampleTable()

	def Clear(self):
		dat = self.ownerComp.op('set_sample_table')
		dat.clear()
		renderSel = self.ownerComp.op('renderselect_sample')
		renderSel.par.top = ''

	def fillSampleTable(self):
		dat = self.ownerComp.op('set_sample_table')
		dat.clear()
		u, v = ipar.bufInsp.Samplepointu, ipar.bufInsp.Samplepointv
		buffers = self.ownerComp.op('output_table')
		dat.appendRow(['UV', u, v, '', ''])
		for i in range(1, buffers.numRows):
			top = op(buffers[i, 'path'] or '')  # type: TOP
			if not top:
				continue
			bufferIndex = buffers[i, 'buffer']
			if bufferIndex not in (None, ''):
				renderSel = self.ownerComp.op('renderselect_sample')
				renderSel.par.top = top.path
				renderSel.par.colorbufindex = bufferIndex
				top = renderSel
			label = buffers[i, 'label'].val
			value = top.sample(u=u, v=v) or ('', '', '', '')
			dat.appendRow([label] + list(value))
		if dat.numRows > 1:
			maxLength = max(len(cell.val) for cell in dat.col(0))
			for cell in dat.col(0):
				cell.val = cell.val.rjust(maxLength)
		for cell in dat.findCells('*', cols=[1, 2, 3, 4]):
			if cell.val:
				cell.val = f'{float(cell):8.2f}'
