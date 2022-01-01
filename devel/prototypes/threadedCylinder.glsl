// @H {"style":"Float"}
// @R {"style":"Float"}
// @Turns {"style":"Float"}
// @Turnoffset {"style":"Float"}
// @Threadthickness {"style":"Float"}


// https://www.shadertoy.com/view/WttyR2

float sdThreadedCylinder(
	in vec3 p,
	in float h,
	in float r,
	in float turns,
	in float turnOffset,
	in float threadThickness) {
	vec2 d = abs(vec2(length(p.xz), p.y)) - vec2(r, h);
	float cylinder = min(max(d.x, d.y), 0.0) + length(max(d, 0.0));

	float a = p.y * turns + turnOffset;
	float c = cos(a), s = sin(a);
	p.xz *= mat2(c, -s, s, c);
	p.z -= r;
	float threads = max(abs(p.x), abs(p.z)) - threadThickness;

	return max(cylinder, -threads);
}

ReturnT thismap(CoordT p, Context ctx) {
	return createSdf(
		sdThreadedCylinder(p, THIS_H, THIS_R, THIS_Turns, THIS_Turnoffset, THIS_Threadthickness)
	);
}