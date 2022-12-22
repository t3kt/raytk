// Generalized Hexagonal Tiling SDF by TheTurk
// https://www.shadertoy.com/view/NltcWj

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p;
	#ifdef THIS_HAS_INPUT_radiusField
	float radius = inputOp_radiusField(p, ctx);
	#else
	float radius = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_spacingField
	float halfSpacing = inputOp_spacingField(p, ctx) / 2.;
	#else
	float halfSpacing = THIS_Spacing / 2.;
	#endif
	#ifdef THIS_HAS_INPUT_roundingField
	float cornerRadius = inputOp_roundingField(p, ctx);
	#else
	float cornerRadius = THIS_Rounding;
	#endif
	cornerRadius *= radius;
	vec2 s = vec2(sqrt(3.0), 3.0) * (radius + halfSpacing * 2.0 / sqrt(3.0));
	q /= s;
	vec2 d1 = (fract(q) - 0.5) * s;
	vec2 d2 = (fract(q + 0.5) - 0.5) * s;
	q = dot(d1, d1) < dot(d2, d2) ? d1 : d2;
	q = abs(q);
	q *= 0.5;
	q += vec2(-q.y, q.x) * sqrt(3.0);
	q.x = abs(q.x);
	q.y -= radius - cornerRadius;
	vec2 n = vec2(sqrt(3.0) * 0.5, -0.5);
	float h = clamp(dot(q, n), 0.0, radius - cornerRadius);
	vec2 d0 = q - n * h;
	float d = length(d0) * sign(d0.x) - cornerRadius;
	return createSdf(d);
}