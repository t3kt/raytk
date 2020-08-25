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
