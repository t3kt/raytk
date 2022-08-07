ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		float h = THIS_H;
		vec3 r = THIS_R;

		vec2 q;
		float ra;

		float s = sign(r.x);
		if (s*r.x<.001) r.x = .001;
		if (abs(r.y)<.001) r.y = .001;
		if (abs(r.z)<.001) r.z = .001;
		vec2 sc = vec2(sin(r.x),cos(r.x)); // could de precalculated
		mat2 rot2 = rotateMatrix2d(r.y);            // could de precalculated
		ra = .5*h/r.x;           // Distance
		p.xz *= rot2;          // Apply 2nd rotation
		p.x -= ra;             // Recenter
		q = p.xy - 2.*sc*max(0.,dot(sc,p.xy));  // Reflect
		vec3 uvw = vec3(ra-length(q)*s,         // New space coordinates
		ra*atan(s*p.y,-s*p.x),
		p.z);
		uvw.zx *= rotateMatrix2d(r.y+r.z*(uvw.y/h));        // Inverse 2nd rotation

		p = uvw;
	}
	return inputOp1(p, ctx);
}