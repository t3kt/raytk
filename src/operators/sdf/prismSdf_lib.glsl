float sdTriPrism( vec3 p, vec2 h )
{
	vec3 q = abs(p);
	return max(q.z-h.y,max(q.x*0.866025+p.y*0.5,-p.y)-h.x*0.5);
}

float sdHexPrism( vec3 p, vec2 h )
{
	const vec3 k = vec3(-0.8660254, 0.5, 0.57735);
	p = abs(p);
	p.xy -= 2.0*min(dot(k.xy, p.xy), 0.0)*k.xy;
	vec2 d = vec2(
	length(p.xy-vec2(clamp(p.x,-k.z*h.x,k.z*h.x), h.x))*sign(p.y-h.x),
	p.z-h.y );
	return min(max(d.x,d.y),0.0) + length(max(d,0.0));
}

float sdOctogonPrism( in vec3 p, in float r, float h )
{
	const vec3 k = vec3(-0.9238795325,  // sqrt(2+sqrt(2))/2
	0.3826834323,   // sqrt(2-sqrt(2))/2
	0.4142135623 ); // sqrt(2)-1
	// reflections
	p = abs(p);
	p.xy -= 2.0*min(dot(vec2( k.x,k.y),p.xy),0.0)*vec2( k.x,k.y);
	p.xy -= 2.0*min(dot(vec2(-k.x,k.y),p.xy),0.0)*vec2(-k.x,k.y);
	// polygon side
	p.xy -= vec2(clamp(p.x, -k.z*r, k.z*r), r);
	vec2 d = vec2( length(p.xy)*sign(p.y), p.z-h );
	return min(max(d.x,d.y),0.0) + length(max(d,0.0));
}

float sdSquarePrism(vec3 p, vec2 h) {
	return fBox(p, h.xxy);
}

float sdArbitraryPrism(vec3 p, float r, float h, float n) {
	pModPolar(p.xy, n);
	return max(p.x - r, abs(p.z)-h);
}

