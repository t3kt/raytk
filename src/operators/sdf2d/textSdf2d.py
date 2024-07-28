import numpy as np

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def generateCode():
	text = parent().par.Text.eval()
	if not text:
		return ''
	code = [f'THIS_align(p, w, float({len(text)}));']
	for c in text:
		i = ord(c)
		code.append(f'THIS_char(d, p, {i});')
		code.append('p.x -= w;')
	return '\n'.join(code)

def fillCharTex(top: scriptTOP):
	text = parent().par.Text.eval()
	if not text:
		top.copyNumpyArray(np.zeros((1, 1, 1), dtype='uint8'))
		return
	n = len(text)
	output = np.empty([1, n, 1], dtype='uint8')
	for i in range(n):
		output[0, i, 0] = ord(text[i])
	top.copyNumpyArray(output)
