// raytkCommon.glsl

struct Sdf
{
	float x; // distance
	float material; // material ID
	float material2; // in case of interpolating, the second material
	float interpolant; // in case of interpolating, the interpolation value
	float ior; // index of refraction in case of refraction
	bool reflect; // do reflection for this?
	bool refract; // do refraction for this?
};

Sdf createSdf(float dist) {
	Sdf res;
	res.x = dist;
	res.material = 2;
	res.reflect = false;
	res.refract = false;
	res.material2 = 0.;
	res.interpolant = 0.;
	return res;
}

struct Context {
	float dummy;
};

Context createDefaultContext() {
	Context ctx;
	ctx.dummy = 0;
	return ctx;
}

Sdf opSimpleUnion(Sdf res1, Sdf res2){
	return (res1.x<res2.x)? res1:res2;
}

Sdf opSimpleUnion(float res1, float res2) {
	return fOpSimpleUnion(res1, res2);
}

Sdf opSmoothUnionM(Sdf d1, Sdf d2, float k) {
	float h = clamp(0.5 + 0.5*(d2.x-d1.x)/k, 0.0, 1.0);
	float resx = mix(d2.x, d1.x, h) - k*h*(1.0-h);
	Sdf res;
	res.x = resx;
	res.material = d2.material;
	res.material2 = d1.material;
	res.interpolant = h;
	res.ior = d1.ior;
	res.refract = d1.refract || d2.refract;
	res.reflect = d1.reflect || d2.reflect;
	return res;//vec2(resx, resy); }
}

float opSmoothUnionM(float d1, float d2, float k) {
	float h = clamp(0.5 + 0.5*(d2-d1)/k, 0.0, 1.0);
	return mix(d2, d1, h) - k*h*(1.0-h);
}
