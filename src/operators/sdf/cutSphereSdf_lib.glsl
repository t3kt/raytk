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