from io import StringIO

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	dat.write(buildCode())

def buildCode():
	out = StringIO()
	out.write('ReturnT thismap(CoordT p, ContextT ctx) {\n')
	out.write('vec3 scale = THIS_Scale * THIS_Uniformscale;\n')
	if op('scale_definition').numRows > 1:
		out.write('scale *= fillToVec3(inputOp_scaleField(p, ctx));\n')
	out.write('p -= THIS_Translate;\n')
	p = parent().par
	axis = p.Infiniteaxis.eval()
	uvMode = p.Uvmode.eval()
	if axis == 'none':
		out.write(f'Sdf res = createSdf(fBox(p, scale));\n')
		if uvMode == 'bounds':
			out.write('assignUV(res, map01(p, -scale/2., scale/2.));\n')
		elif uvMode == 'faces':
			out.write('vec3 pNorm = p / scale;\n')
			out.write('vec3 boxFaces = nearestFace(pNorm);\n')
			out.write('if (boxFaces.x != 0.) assignUV(res, vec3(pNorm.y * boxFaces.x, pNorm.z, 0.));\n')
			out.write('else if (boxFaces.y != 0.) assignUV(res, vec3(pNorm.z * boxFaces.y, pNorm.x, 0.));\n')
			out.write('else if (boxFaces.z != 0.) assignUV(res, vec3(pNorm.x * boxFaces.z, pNorm.y, 0.));\n')
		out.write('#ifdef RAYTK_HAS_ATTR_edgedist\n')
		out.write('res.attrs.edgedist = min(distance(abs(p.xy), scale.xy), min(distance(abs(p.zx), scale.zx), distance(abs(p.yz), scale.yz)));\n')
		out.write('#endif\n')
	else:
		swiz = {'x': 'yz', 'y': 'zx', 'z': 'xy'}[axis]
		out.write(f'Sdf res = createSdf(fBox2(p.{swiz}, scale.{swiz}));\n')
		if uvMode == 'bounds':
			out.write('vec3 uv = map01(p, -scale/2., scale/2.);\n')
			out.write(f'uv.{axis} = p.{axis};\n')
			out.write('assignUV(res, uv);\n')
		elif uvMode == 'faces':
			out.write(f'vec3 uv = vec3(0., p.{axis}, 0.);\n')
			out.write(f'vec2 pNorm = p.{swiz} / scale.{swiz};\n')
			out.write('vec2 edge = nearestEdge(pNorm);\n')
			out.write(f'if (edge.x != 0.) uv.x = pNorm.y * edge.x;\n')
			out.write(f'else uv.x = pNorm.x * edge.y;\n')
			out.write('assignUV(res, uv);\n')
		out.write('#ifdef RAYTK_HAS_ATTR_edgedist\n')
		out.write(f'res.attrs.edgedist = distance(abs(p.{swiz}), scale.{swiz});\n')
		out.write('#endif\n')
	out.write('return res;\n')
	out.write('}\n')
	return out.getvalue()
