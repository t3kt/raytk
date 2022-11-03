// @Thin {"default":0.1, "normMin":0, "normMax":1}
// @Glow {"default":0.01, "normMin":0, "normMax":1}
// @Size {"default":0.1, "normMin":0, "normMax":1}
// @Range {"style":"XY"}
// @Falloff {"default": 1.1}
// @Count {"default":6, "normMax":12}

// Funky Motherboard Carpet by leon
// https://www.shadertoy.com/view/7lGfWt

ReturnT thismap(CoordT p, ContextT ctx) {
	float thin = THIS_Thin;
	float glow = THIS_Glow;
	float size = THIS_Size;
	vec2 range = THIS_Range;
	float falloff = THIS_Falloff;
	float count = THIS_Count;

	vec3 color = vec3(0.);

	// kaleidoscope
	float a = 1.0;
	for (float index = 0.; index < count; ++index) {
		// transform
		p = abs(p) - range* a;
		pR(p, radians(45));

		// shape
		float dist = max(abs(p.x) + a*sin(TAU * index/count), p.y-size);

		// shade
		color += smoothstep(thin, 0.0, dist) * glow / dist;

		a /= falloff;
	}
	color = clamp(color, 0., 1.);

	// palette
	color *= .5 + .5 * cos(vec3(1,2,3)*5. + p.x * 10.);

	// glow
	float time = 0.;
	color += .04/abs(sin(p.y*12.+time*1.));
	return vec4(color, 1.);
}