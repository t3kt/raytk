// @Res {"default":0.5, "style":"XYZ"}

// https://www.shadertoy.com/view/ssjSRw

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 resolution = THIS_Res;

	vec3 q = floor(p / resolution) * resolution;
	vec3 uvw = (p - q) / resolution;

	    // Determine the vertices of the tetrahedron we're in
    vec3 v0 = dot(uvw, vec3( 1,  1,  1)) > 2.0 ? vec3(1, 1, 1) : vec3(0, 0, 0);
    vec3 v1 = dot(uvw, vec3(-1, -1,  1)) > 0.0 ? vec3(0, 0, 1) : vec3(1, 1, 0);
    vec3 v2 = dot(uvw, vec3(-1,  1, -1)) > 0.0 ? vec3(0, 1, 0) : vec3(1, 0, 1);
    vec3 v3 = dot(uvw, vec3( 1, -1, -1)) > 0.0 ? vec3(1, 0, 0) : vec3(0, 1, 1);

    // Solve for barycentric coordinates
    mat4 map = inverse(transpose(mat4(v0, 1, v1, 1, v2, 1, v3, 1)));
    vec4 bary = vec4(uvw, 1) * map;

	ReturnT res = inputOp1(q + v0 * resolution, ctx);
	vec4 isoVals = vec4(
		res.x,
		inputOp1(q + v1 * resolution, ctx).x,
		inputOp1(q + v2 * resolution, ctx).x,
		inputOp1(q + v3 * resolution, ctx).x
	);
	res.x = dot(isoVals, bary);

	return res;
}