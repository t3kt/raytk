o = parent()

order = 0
cmbTable = op('combiner/codeSwitcher/table')
cmbNames = [c.val for c in cmbTable.col('name')[1:]]
cmbLabels = [c.val for c in cmbTable.col('label')[1:]]
inputNames = ['input'+str(i) for i in range(1, 9)]
inputLabels = ['Input '+str(i) for i in range(1, 9)]

for i in range(1, 9):
	if i < 5:
		page = o.appendCustomPage('Combine')
	else:
		page = o.appendCustomPage('Combine 5-8')
	p = page.appendToggle(f'Enable{i}', label=f'Enable {i}')[0]
	p.default = i == 1
	p.startSection = True
	enableExpr = f'me.par.Enable{i}'
	p.order = order
	order += 1
	p = page.appendMenu(f'Input{i}', label=f'Input {i}')[0]
	p.enableExpr = enableExpr
	p.menuNames = inputNames
	p.menuLabels = inputLabels
	p.default = f'input{i}'
	p.order = order
	order += 1
	p = page.appendXYZ(f'Translate{i}', label=f'Translate {i}')[0]
	p.enableExpr = enableExpr
	p.order = order
	order += 1
	p = page.appendMenu(f'Combine{i}', label=f'Combine {i}')[0]
	p.enableExpr = enableExpr
	p.menuNames = cmbNames
	p.menuLabels = cmbLabels
	p.order = order
	order += 1
	p = page.appendFloat(f'Blendradius{i}', label=f'Radius {i}')[0]
	p.default = 0.1
	p.enableExpr = enableExpr + f" and me.par.Combine{i} in ('smoothUnion', 'smoothIntersect', 'smoothDiff', 'roundUnion', 'roundIntersect', 'roundDiff', 'chamferUnion', 'chamferIntersect', 'chamferDiff', 'stairUnion', 'stairIntersect', 'stairDiff', 'columnUnion', 'columnIntersect', 'columnDiff')"
	p.order = order
	order += 1
	p = page.appendFloat(f'Blendnumber{i}', label=f'Number {i}')[0]
	p.default = 3
	p.normMax = 5
	p.enableExpr = enableExpr + f" and me.par.Combine{i} in ('stairUnion', 'stairIntersect', 'stairDiff', 'columnUnion', 'columnIntersect', 'columnDiff')"
	p.order = order
	order += 1
	p = page.appendFloat(f'Blendoffset{i}', label=f'Offset {i}')[0]
	p.enableExpr = enableExpr
	p.enableExpr = enableExpr + f" and me.par.Combine{i} in ('stairUnion', 'stairIntersect', 'stairDiff', 'columnUnion', 'columnIntersect', 'columnDiff')"
	p.order = order
	order += 1
	p = page.appendFloat(f'Blendgutter{i}', label=f'Gutter {i}')[0]
	p.enableExpr = enableExpr + f" and me.par.Combine{i} in ('smoothAvoid',)"
	p.order = order
	order += 1

