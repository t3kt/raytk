// @Param1 {"default":1, "normMin":0, "normMax":2}

// https://github.com/patriciogonzalezvivo/lygia/blob/main/space/triTile.glsl
vec4 triTile(vec2 st) {
  st *= mat2(1., -1. / 1.7320508, 0., 2. / 1.7320508);
  vec4 f = vec4(st, -st);
  vec4 i = floor(f);
  f = fract(f);
  return dot(f.xy, f.xy) < dot(f.zw, f.zw)
             ? vec4(f.xy, vec2(2., 1.) * i.xy)
             : vec4(f.zw, -(vec2(2., 1.) * i.zw + 1.));
}

vec4 triTile(vec2 st, float scale) { return triTile(st * scale); }

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.xy;
	vec4 tiled = triTile(q);

	p.xy = tiled.xy;

	return inputOp1(p, ctx);
}