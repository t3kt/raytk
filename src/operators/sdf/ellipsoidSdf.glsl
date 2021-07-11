// https://www.shadertoy.com/view/tdS3DG
// http://iquilezles.org/www/articles/ellipsoids/ellipsoids.htm
ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 r = THIS_Scale;
	float k0 = length(p/r);
	float k1 = length(p/(r*r));
	return createSdf(k0*(k0-1.0)/k1);
}