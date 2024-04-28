vec2 hx_prepDualHelixCoords(vec3 p, float radius, float spread, float dualSpread) {
	float halfm = spread*.5,
	b = mod(p.y, PI*spread) - PI*halfm,
	a = abs(atan(p.x, p.z) * halfm - b);
	if (a > PI*halfm) a = PI*spread - a;
	//optimisation from Shane
	p.xy = vec2(length(p.xz) - radius, a);
	p.x = abs(p.x) - dualSpread;
	return p.xy;
}

// Helix Distance by tdhooper
// https://www.shadertoy.com/view/MstcWs


// Cartesian to polar coordinates
vec3 hx_cartToPolar(vec3 p) {
	float x = p.x; // distance from the plane it lies on
	float a = atan(p.y, p.z); // angle around center
	float r = length(p.zy); // distance from center
	return vec3(x, a, r);
}

// Polar to cartesian coordinates
vec3 hx_polarToCart(vec3 p) {
	return vec3(
		p.x,
		sin(p.y) * p.z,
		cos(p.y) * p.z
	);
}

vec2 hx_closestPointOnRepeatedLine(vec2 line, vec2 point){
	// Angle of the line
	float a = atan(line.x, line.y);

	// Rotate space so we can easily repeat along
	// one dimension
	pR(point, -a);

	// Repeat to create parallel lines at the corners
	// of the vec2(lead, radius) polar bounding area
	float repeatSize = sin(a) * line.y;
	float cell = pMod1(point.x, repeatSize);

	// Rotate space back to where it was
	pR(point, a);

	// Closest point on a line
	line = normalize(line);
	float d = dot(point, line);
	vec2 closest = line * d;

	// Part 2 of the repeat, move the line along it's
	// perpendicular by the repeat cell
	vec2 perpendicular = vec2(line.y, -line.x);
	closest += cell * repeatSize * perpendicular;

	return closest;
}

// Closest point on a helix
vec3 hx_closestHelix(vec3 p, float spread, float radius) {
	p = hx_cartToPolar(p);
	p.y *= radius;

	vec2 line = vec2(spread, radius * PI * 2.);
	vec2 closest = hx_closestPointOnRepeatedLine(line, p.xy);

	closest.y /= radius;
	vec3 closestCart = hx_polarToCart(vec3(closest, radius));

	return closestCart;
}

// Cartesian to helix coordinates
vec3 hx_helixCoords(vec3 p, vec3 closest, float spread, float radius) {
	float helixAngle = atan((2. * PI * radius) / spread);
	vec3 normal = normalize(closest - vec3(closest.x,0,0));
	vec3 tangent = vec3(1,0,0) * TDRotateOnAxis(helixAngle, normal);
	float x = (closest.x / spread) * radius * PI * 2.;
	float y = dot(p - closest, cross(tangent, normal));
	float z = dot(p - closest, normal);
	return vec3(x,y,z);
}