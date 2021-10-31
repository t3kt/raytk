// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 ab = THIS_Scale;
	CoordT p0 = p;
	#pragma r:if THIS_HAS_INPUT_scaleField
	ab *= fillToVec2(inputOp_scaleField(p, ctx));
	#pragma r:endif
	ReturnT res;
	if (ab.x == ab.y) {
		res = createSdf(length(p) - ab.x);
	} else {
		p = abs(p); if( p.x > p.y ) {p=p.yx;ab=ab.yx;}
		float l = ab.y*ab.y - ab.x*ab.x;
		float m = ab.x*p.x/l;      float m2 = m*m;
		float n = ab.y*p.y/l;      float n2 = n*n;
		float c = (m2+n2-1.0)/3.0; float c3 = c*c*c;
		float q = c3 + m2*n2*2.0;
		float d = c3 + m2*n2;
		float g = m + m*n2;
		float co;
		if( d<0.0 )
		{
			float h = acos(q/c3)/3.0;
			float s = cos(h);
			float t = sin(h)*sqrt(3.0);
			float rx = sqrt( -c*(s + t + 2.0) + m2 );
			float ry = sqrt( -c*(s - t + 2.0) + m2 );
			co = (ry+sign(l)*rx+abs(g)/(rx*ry)- m)/2.0;
		}
		else
		{
			float h = 2.0*m*n*sqrt( d );
			float s = sign(q+h)*pow(abs(q+h), 1.0/3.0);
			float u = sign(q-h)*pow(abs(q-h), 1.0/3.0);
			float rx = -s - u - c*4.0 + 2.0*m2;
			float ry = (s - u)*sqrt(3.0);
			float rm = sqrt( rx*rx + ry*ry );
			co = (ry/sqrt(rm-rx)+2.0*g/rm-m)/2.0;
		}
		vec2 r = ab * vec2(co, sqrt(1.0-co*co));
		res = createSdf(length(r-p) * sign(p.y-r.y));
	}
	#pragma r:if THIS_Uvmode_bounds
	{
		vec2 bnd = ab / 2.;
		assignUV(res, vec3(map01(p0, -bnd, bnd), 0.));
	}
	#pragma r:endif
	return res;
}