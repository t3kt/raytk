# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildPartTable(dat: DAT):
	for i in range(1, 5):
		src = int(parent().par[f'Source{i}'])
		part = str(parent().par[f'Part{i}'])
		if op(f'definition_{i}').numRows < 2 and part not in ['zero', 'one']:
			dat.appendRow([0, 'zero'])
		elif part in ['zero', 'one']:
			dat.appendRow([0, part])
		else:
			dat.appendRow([
				src,
				part,
			])

def buildMacros(dat: DAT, partTable: DAT):
	dat.clear()
	sources = [int(c) for c in partTable.col(0)]
	parts = [str(c) for c in partTable.col(1)]
	if len(set(sources)) == 1 and sources[0] > 0 and all([p in 'xyzw' for p in parts]):
		src = sources[0]
		dat.appendRow([
			'',
			'THIS_EXPR',
			f'inputOp{src}(p, ctx).' + ''.join(parts),
		])
	else:
		sourceIsFloat = [
			op(f'definition_{i}')[1, 'returnType'] == 'float'
			for i in range(1, 5)
		]
		for i in range(1, 5):
			if i not in sources or op(f'definition_{i}').numRows < 2:
				continue
			returnType = op(f'definition_{i}')[1, 'returnType']
			dat.appendRow([
				'',
				f'THIS_DECL_{i}',
				f'{returnType} val{i} = inputOp{i}(p, ctx)'
			])
		exprParts = []
		for i in range(4):
			src = sources[i]
			part = parts[i]
			if part == 'zero':
				exprParts.append('0')
			elif part == 'one':
				exprParts.append('1')
			else:
				if sourceIsFloat[src - 1]:
					exprParts.append(f'val{src}')
				else:
					exprParts.append(f'val{src}.{part}')
		dat.appendRow([
			'',
			'THIS_EXPR',
			'vec4(' + ','.join(exprParts) + ')',
		])
