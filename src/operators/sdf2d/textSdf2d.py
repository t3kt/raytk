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
