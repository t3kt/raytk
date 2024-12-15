// https://www.shadertoy.com/view/7tVXRt

float sdCutSphere( in vec3 p, in float r, in float h )
{
	float w = sqrt(r*r-h*h); // constant for a given shape

	vec2 q = vec2( length(p.xz), p.y );

	float s = max( (h-r)*q.x*q.x+w*w*(h+r-2.0*q.y), h*q.x-w*q.y );

	return (s<0.0) ? length(q)-r : // sphere
				 (q.x<w) ? h - q.y     :  // segment line
									 length(q-vec2(w,h)); // segment corner
}

float sdCutHollowSphere( vec3 p, float r, float h, float t )
{
	float w = sqrt(r*r-h*h); // constant for a given shape

	vec2 q = vec2( length(p.xz), p.y );

	return ((h*q.x<w*q.y) ? length(q-vec2(w,h)) :
				abs(length(q)-r) ) - t;
}
// https://www.shadertoy.com/view/lfcyDM
float sdSegmentSphere( vec3 p, float m, float r, float h, float t )
{
	// Mirror in z for easier calculation
	p.z = abs(p.z);

	// Angle in y-z plane, clamped to max angle m
	float a = min(atan(p.z, -p.y), m);

	// Rotate in y-z so each p corresponds to the case in
	// sdCutHollowSphere() i.e. sphere-cap at bottom of sphere
	p.yz *= mat2(cos(a), -sin(a), sin(a), cos(a));

	// Return sphere-cap. Done!
	return sdCutHollowSphere(p, r, h, t);
}