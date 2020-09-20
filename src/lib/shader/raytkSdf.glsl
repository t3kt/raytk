// raytkSdf.glsl

Sdf opSimpleUnion(Sdf res1, Sdf res2){
	return (res1.x<res2.x)? res1:res2;
}

float opSimpleUnion(float res1, float res2) {
	return min(res1, res2);
}

Sdf opSimpleIntersect(Sdf res1, Sdf res2) {
	return (res1.x>res2.x) ? res1 : res2;
}

float opSimpleIntersect(float res1, float res2) {
	return max(res1, res2);
}

Sdf opSimpleDiff(Sdf res1, Sdf res2) {
	Sdf res = res1;
	res.x = max(-res1.x, res2.x);
	return res;
}

float opSimpleDiff(float res1, float res2) {
	return max(-res1, res2);
}

Sdf opSmoothUnionM(Sdf d1, Sdf d2, float k) {
	float h = clamp(0.5 + 0.5*(d2.x-d1.x)/k, 0.0, 1.0);
	float resx = mix(d2.x, d1.x, h) - k*h*(1.0-h);
	Sdf res = d1;
	res.x = resx;
	res.material = d2.material;
	res.material2 = d1.material;
	res.interpolant = h;
	res.refract = d1.refract || d2.refract;
	res.reflect = d1.reflect || d2.reflect;
	return res;
}

float opSmoothUnionM(float d1, float d2, float k) {
	float h = clamp(0.5 + 0.5*(d2-d1)/k, 0.0, 1.0);
	return mix(d2, d1, h) - k*h*(1.0-h);
}

float sdBoundingBox( vec3 p, vec3 b, float e )
{
	p = abs(p)-b;
	vec3 q = abs(p+e)-e;
	return min(min(
		length(max(vec3(p.x,q.y,q.z),0.0))+min(max(p.x,max(q.y,q.z)),0.0),
		length(max(vec3(q.x,p.y,q.z),0.0))+min(max(q.x,max(p.y,q.z)),0.0)),
		length(max(vec3(q.x,q.y,p.z),0.0))+min(max(q.x,max(q.y,p.z)),0.0));
}

#ifdef RAYTK_USE_APOLLONIAN
// https://www.shadertoy.com/view/4ds3zn
float sdApollonian(vec3 p, float s, float scale, out vec4 orb) {
	orb = vec4(1000.0);

	for (int i=0; i<8; i++)
	{
		p = -1.0 + 2.0*fract(0.5*p+0.5);

		float r2 = dot(p, p);

		orb = min(orb, vec4(abs(p), r2));

		float k = s/r2;
		p *= k;
		scale *= k;
	}

	return 0.25*abs(p.y)/scale;
}
#endif// RTK_USE_APOLLONIAN
