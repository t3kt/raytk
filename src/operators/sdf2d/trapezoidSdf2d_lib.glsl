// https://www.shadertoy.com/view/MlycD3
// trapezoid / capped cone, specialized for Y alignment
// r1: bottom width, r2: top width, he: height
float sdTrapezoid(vec2 p, float r1, float r2, float he)
{
	vec2 k1 = vec2(r2,he);
	vec2 k2 = vec2(r2-r1,2.0*he);

	p.x = abs(p.x);
	vec2 ca = vec2(max(0.0,p.x-((p.y<0.0)?r1:r2)), abs(p.y)-he);
	vec2 cb = p - k1 + k2*clamp( dot(k1-p,k2)/dot2(k2), 0.0, 1.0 );

	float s = (cb.x < 0.0 && ca.y < 0.0) ? -1.0 : 1.0;

	return s*sqrt( min(dot2(ca),dot2(cb)) );
}

// trapezoid / capped cone
// a: ?, b: ?, ra: ?, rb: ?
float sdTrapezoid(vec2 p, vec2 a, vec2 b, float ra, float rb)
{
	float rba  = rb-ra;
	float baba = dot(b-a,b-a);
	float papa = dot(p-a,p-a);
	float paba = dot(p-a,b-a)/baba;
	float x = sqrt( papa - paba*paba*baba );
	float cax = max(0.0,x-((paba<0.5)?ra:rb));
	float cay = abs(paba-0.5)-0.5;
	float k = rba*rba + baba;
	float f = clamp( (rba*(x-ra)+paba*baba)/k, 0.0, 1.0 );
	float cbx = x-ra - f*rba;
	float cby = paba - f;
	float s = (cbx < 0.0 && cay < 0.0) ? -1.0 : 1.0;
	return s*sqrt( min(cax*cax + cay*cay*baba,
	cbx*cbx + cby*cby*baba) );
}
