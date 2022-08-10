from io import StringIO

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildCode():
	p = parent().par
	out = StringIO()
	out.write('ReturnT thismap(CoordT p, ContextT ctx) {\n')
	if p.Usepivot:
		if op('pivot_field_definition').numRows > 2:
			out.write('CoordT pivot = THIS_asCoordT(inputOp_pivotField(p, ctx));\n')
		else:
			out.write(f'CoordT pivot = THIS_asCoordT(vec3({parCode(p.Pivotx)}, {parCode(p.Pivoty)}, {parCode(p.Pivotz)}));\n')

	if p.Usepivot:
		out.write('p -= pivot;\n')
	out.write('vec3 q = adaptAsVec3(p);\n')

	mode = p.Rotatemode.eval()
	if mode == 'euler':
		out.write(f'vec3 r = vec3({parCode(p.Rotx)}, {parCode(p.Roty)}, {parCode(p.Rotz)});\n')
		if op('rotate_field_definition').numRows > 2:
			if 'vec4' not in op('rotate_field_definition')[1, 'returnType'].val:
				out.write('r *= adaptAsFloat(inputOp_rotateField(p, ctx));\n')
			else:
				out.write('r += inputOp_rotateField(p, ctx).xyz;\n')
		out.write('r = radians(r);\n')
		if op('definition_1')[1, 'coordType'] == 'vec2':
			out.write('pR(q.xy, r.z);\n')
		else:
			order = p.Rord.eval()  # type: str
			# planes = {'x': 'yz', 'y': 'xz', 'z': 'xy'}
			axisVecs = {'x': 'vec3(1.,0., 0.)', 'y': 'vec3(0.,1.,0.)', 'z': 'vec3(0.,0.,1.)'}
			for part in order:
				# out.write(f'pR(q.{planes[part]}, r.{part});\n')
				out.write(f'q *= TDRotateOnAxis(r.{part}, {axisVecs[part]});\n')
	elif mode == 'axis':
		out.write(f'float r = {parCode(p.Rotate)};\n')
		if op('rotate_field_definition').numRows > 2:
			out.write('r += adaptAsFloat(inputOp_rotateField(p, ctx));\n')
		out.write('r = radians(r);\n')
		axis = p.Axisx, p.Axisy, p.Axisz
		if op('definition_1')[1, 'coordType'] == 'vec2':
			out.write('pR(q.xy, r);\n')
		elif not _isConst(axis[0]) or not _isConst(axis[1]) or not _isConst(axis[2]):
			out.write(f'q *= TDRotateOnAxis(r, normalize(vec3({parCode(axis[0])}, {parCode(axis[1])}, {parCode(axis[2])})));\n')
		elif axis == (1., 0., 0.):
			out.write('pR(q.yz, r);\n')
		elif axis == (0., 1., 0.):
			out.write('pR(q.zx, r);\n')
		elif axis == (0., 0., 1.):
			out.write('pR(q.xy, r);\n')
		else:
			out.write(f'q *= TDRotateOnAxis(r, normalize(vec3({axis[0]}, {axis[1]}, {axis[2]})));\n')

	out.write('p = THIS_asCoordT(q);\n')
	if p.Usepivot:
		out.write('p += pivot;\n')
	if op('definition_1').numRows < 2:
		out.write('return adaptAsVec4(p);\n')
	else:
		out.write('return inputOp1(p, ctx);\n')
	out.write('}\n')
	return out.getvalue()

def getParams():
	p = parent().par
	params = []
	if p.Usepivot:
		if op('pivot_field_definition').numRows < 2:
			params += [p.Pivotx, p.Pivoty, p.Pivotz]
	mode = p.Rotatemode.eval()
	if mode == 'euler':
		params += [p.Rotx, p.Roty, p.Rotz]
	elif mode == 'axis':
		params.append(p.Rotate)
		axis = p.Axisx, p.Axisy, p.Axisz
		if op('definition_1')[1, 'coordType'] != 'vec2':
			if not _isConst(axis[0]) or not _isConst(axis[1]) or not _isConst(axis[2]):
				params += axis
			elif axis != (1., 0., 0.) and axis != (0., 1., 0.) and axis != (0., 0., 1.):
				params += axis
	return params

def _isConst(par: 'Par'):
	return par.mode == ParMode.CONSTANT

def parCode(par: 'Par'):
	if _isConst(par):
		return str(par.eval())
	return 'THIS_' + par.name
