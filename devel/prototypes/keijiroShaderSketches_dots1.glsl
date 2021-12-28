// https://href.li/?https://github.com/keijiro/ShaderSketches/blob/master/Dots1.glsl
// @Size {"default":1, "normMin":0, "normMax":2}
// @Swirlsize {"default":1, "normMin":0, "normMax":2}
// @Phase {"default":0}
// @Radius {"default":0.5}

float swirl(vec2 coord)
{
	float phase = THIS_Phase;
	float size = THIS_Swirlsize;
	float l = length(coord) / size;
	float phi = atan(coord.y, coord.x + 1e-6);
	return sin(l * 10 + phi - phase * 4) * 0.5 + 0.5;
}

float halftone(vec2 coord)
{
	float phase = THIS_Phase;
	float sz = THIS_Size;
	float radius = THIS_Radius;
//	coord -= sz * 0.5;
	float FOO = 60;
	float size = sz / (FOO + sin(phase * 0.5) * 50);
	vec2 uv = coord / size;
	vec2 ip = floor(uv); // column, row
	vec2 odd = vec2(0.5 * mod(ip.y, 2), 0); // odd line offset
	vec2 cp = floor(uv - odd) + odd; // dot center
	float d = length(uv - cp - 0.5) * size; // distance
	float r = swirl(cp * size) * (size - 2) * radius; // dot radius
	return step(1., d-r);
//	return clamp(d - r, 0, 1);
}

ReturnT thismap(CoordT p, Context ctx) {
	ReturnT res;
	res = vec4(vec3(1, 1, 0) * halftone(p), 1);
	return res;
}