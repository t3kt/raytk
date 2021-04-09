// Based on ChamferBox Super Primitive by TLC123
// https://www.shadertoy.com/view/3lBGzt

ReturnT thismap(CoordT p, ContextT ctx) {
	p = abs(p - THIS_Translate) + vec3(THIS_Chamfer) + vec3(THIS_Round);
	return createSdf(sdOctahedron(max(vec3(0), p-THIS_Scale * THIS_Uniformscale), THIS_Chamfer) - THIS_Round);
}