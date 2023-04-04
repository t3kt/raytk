page = parent().appendCustomPage('SDF')

for i in range(1,9):
	pa = page.appendXYZ(f'Pointa{i}', label=f'Point A {i}')[0]
	pa.enableExpr = f"me.par.Source == 'params' and me.par.Count >= {i}"
	pa.startSection = True
	pb = page.appendXYZ(f'Pointb{i}', label=f'Point B {i}')[0]
	pb.enableExpr = pa.enableExpr
