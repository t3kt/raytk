// Snub Quadrile by mla
// https://www.shadertoy.com/view/XdtyRn

vec2 THIS_perp(vec2 r) { return vec2(-r.y,r.x); }
int THIS_imod(int n, int m) {
	int k = n - n/m*m;
	if (k < 0) return k+m;
	else return k;
}

vec3 THIS_getcol0(int i) {
	if (i == 0) return THIS_Polycolor1;
	if (i == 1) return THIS_Polycolor2;
	if (i == 2) return THIS_Polycolor3;
	if (i == 3) return THIS_Polycolor4;
	if (i == 4) return vec3(1,0,1);
	if (i == 5) return vec3(0,1,1);
	if (i == 6) return vec3(1,1,1);
	return vec3(1,1,1);
}

vec3 THIS_getcol(int i) {
	return 0.25+0.75*THIS_getcol0(i);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p;
	q /= THIS_Size;
	vec2 wythoffPoint = vec2(0.64, 0.36);
	wythoffPoint += THIS_Tilingshift;
	wythoffPoint = clamp(wythoffPoint, 0., 1.);
	q = mod(q,2.)-1.; // Fold down to ±1 square
	bool parity = (q.y < 0.0) != (q.x < 0.0); // Need reflection?
	int quad = 2*int(q.x < 0.0) + int(parity); // Quadrant
	q = abs(q);
	if (parity) q.xy = q.yx;

	// q0,q1,q2 are reflections of q in sides of fundamental region
	// ie. the vertices of the snub triangle.
	vec2 q0 = wythoffPoint.yx;
	vec2 q1 = vec2(2.0-wythoffPoint.x,wythoffPoint.y);
	vec2 q2 = vec2(wythoffPoint.x,-wythoffPoint.y);

	// q3,q4,q5 are further reflections
	vec2 q3 = vec2(-wythoffPoint.x,wythoffPoint.y);
	vec2 q4 = vec2(-wythoffPoint.y,2.0-wythoffPoint.x);
	vec2 q5 = vec2(wythoffPoint.x,2.0-wythoffPoint.y);

	// Work out what color the point should be
	bool l1 = dot(q-q0,THIS_perp(q1-q0)) <= 0.0;
	bool l2 = dot(q-q0,THIS_perp(q2-q0)) <= 0.0;
	bool l3 = dot(q-q0,THIS_perp(q3-q0)) <= 0.0;
	bool l4 = dot(q-q0,THIS_perp(q4-q0)) <= 0.0;
	bool l5 = dot(q-q0,THIS_perp(q5-q0)) <= 0.0;
	int colindex = 0;
	vec3 col = vec3(1);

	//if (l2 && !l3) colindex = 0;
	if (l3 && !l4) colindex = THIS_imod(quad-1,4)/2+2;
	if (l4 && !l5) colindex = THIS_imod(quad+1,4)/2+2;
	if (l5 && !l1) colindex = 1;
	if (l1 && !l2) colindex = quad/2+2;
	col = THIS_getcol(colindex);

	if (IS_TRUE(THIS_Enableoutline)) {
		float d = 1e8;
		d = min(fCapsule(q,q0,q1),fCapsule(q,q0,q2));
		d = min(d,fCapsule(q,q0,q3));
		d = min(d,fCapsule(q,q0,q4));
		d = min(d,fCapsule(q,q0,q5));
		d = min(d,fCapsule(q,q1,q2));
		float lwidth = THIS_Outlinethickness;
		float awidth = THIS_Outlineblending;
		col = mix(THIS_Outlinecolor,col,smoothstep(lwidth-awidth,lwidth+awidth,d));
	}

	if (IS_TRUE(THIS_Enabledualoutline)) {
		// Lines from square centre to triangle (bary)centre.
		vec2 c = (q0+q1+q2)/3.0;
		float d = 1e8;
		float lwidth = THIS_Dualoutlinethickness;
		float awidth = THIS_Dualoutlineblending;
		d = min(d,fCapsule(q,vec2(0,0),c));
		d = min(d,fCapsule(q,vec2(1,0),c));
		d = min(d,fCapsule(q,vec2(1,1),c));
		d = min(d,fCapsule(q,vec2(-c.y,c.x),vec2(c.y,-c.x)));
		d = min(d,fCapsule(q,vec2(-c.y,c.x),vec2(c.y,2.0-c.x)));
		d = min(d,fCapsule(q,vec2(2.0-c.y,c.x),vec2(c.y,2.0-c.x)));
		col = mix(THIS_Dualoutlinecolor,col,smoothstep(0.5*lwidth-awidth,0.5*lwidth+awidth,d));
	}

	return vec4(col, 1.);
}