// https://github.com/keijiro/ShaderSketches/blob/master/Fragment/Circles.glsl
// @Size {"default":1, "normMin":0, "normMax":2}
// @Phase {"default": 0}
// @Thickness {"default":0.1}

float circle(vec2 coord, vec2 offs)
{
	float reso = THIS_Size;
	float phase = THIS_Phase;
	// float cw = iResolution.x / reso;
	float cw = reso;

	vec2 p = mod(coord, cw) + offs * cw;
	float d = distance(p, vec2(cw / 2.0));

	vec2 p2 = floor(coord / cw) - offs;
	vec2 gr = vec2(0.443, 0.312);
	float t = phase * 2.0 + dot(p2, gr);

	float l = cw * (sin(t) + 1.2) * 0.4;
	float lw = 1.5;
	lw = THIS_Thickness;
	return max(0.0, 1.0 - abs(l - d) / lw);
}

ReturnT thismap(CoordT p, Context ctx) {

	float c = 0.0;
	for (int i = 0; i < 9; i++)
	{
		float dx = mod(float(i), 3.0) - 1.0;
		float dy = float(i / 3) - 1.0;
		dx *= 0.2;
		dy *= 0.1;
		c += circle(p, vec2(dx, dy));
	}

	c = circle(p, vec2(0.));

	vec4 res;
	res.rgb = vec3(c);
	res.a = 1.;
	return res;
}