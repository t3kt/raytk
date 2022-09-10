from io import StringIO

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

planes = {'x': 'yz', 'y': 'zx', 'z': 'xy'}

def onCook(dat):
	dat.clear()
	out = StringIO()
	p = parent().par
	axis = p.Axis.eval()
	out.write('ReturnT thismap(CoordT p, ContextT ctx) {\n')
	out.write(f'#ifdef THIS_EXPOSE_axispos\nTHIS_axispos = p.{axis};\n#endif\n')
	iterType = p.Iterationtype.eval()
	if p.Infiniteheight:
		if iterType == 'ratio':
			out.write(f'setIterationIndex(ctx, p.{axis});\n')
		out.write(f'#ifdef THIS_EXPOSE_normoffset\nTHIS_normoffset = p.{axis};\n#endif\n')
		out.write(f'ReturnT res = inputOp_crossSection(p.{planes[axis]}, ctx);\n')
		if p.Uvmode == 'depth':
			out.write(f'#ifdef RAYTK_USE_UV\nres.uv.y = mix(res.uv.y, p.{axis}, res.uv.w);\n#endif\n')
	else:
		if op('height_definition').numRows > 1:
			out.write('float h = inputOp_heightField(p, ctx);\n')
		else:
			out.write('float h = THIS_Height;\n')
		if op('offset_definition').numRows > 1:
			out.write('float o = inputOp_offsetField(p, ctx);\n')
		else:
			out.write('float o = THIS_Offset;\n')
		out.write(f'float ratio = map01(p.{axis} - o, -h/2., h/2.);\n')
		if iterType == 'ratio':
			out.write(f'setIterationIndex(ctx, ratio);\n')
		out.write(f'#ifdef THIS_EXPOSE_normoffset\nTHIS_normoffset = ratio;\n#endif\n')
		out.write(f'ReturnT res = inputOp_crossSection(p.{planes[axis]}, ctx);\n')
		out.write(f'vec2 w = vec2(res.x, abs(p.{axis} - o) - h);\n')
		out.write('res.x = min(max(w.x,w.y), 0.0) + length(max(w, 0.0));\n')
		if p.Uvmode == 'depth':
			out.write('#ifdef RAYTK_USE_UV\nres.uv.y = mix(res.uv.y, w.y, ratio);\n#endif\n')
	out.write('return res;\n}\n')
	dat.write(out.getvalue())
