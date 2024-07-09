// supershape - gradient by valvw
// https://www.shadertoy.com/view/lXGSRy

ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 a = THIS_A;
	float m1 = a.x;
	float n11 = a.y;
	float n12 = a.z;
	float n13 = a.w;
	vec4 b = THIS_B;
	float m2 = b.x;
	float n21 = b.y;
	float n22 = b.z;
	float n23 = b.w;

	float d = distanceToSupershape(p, m1, n11, n12, n13, m2, n21, n22, n23)*.1;
	return createSdf(d);
}