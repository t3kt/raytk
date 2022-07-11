// Wythoff Uniform Tilings + Duals by fizzer
// https://www.shadertoy.com/view/3tyXWw

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;


	float vertex_dot_radius = .06; // TODO: parameter

	float w = 0.05; // TODO: this is originally using length(fwidth(uv)) * 2.
	ivec4 sym;  // Wythoff symbol
	SYMBOL_BODY();

	vec3 angles = vec3(PI) / vec3(sym.xyz);
	vec3 sins = sin(angles);

	// Law of sines (c is defined to be 1.0)
	float a = sins.x / sins.z;
	float b = sins.y / sins.z;

	// Triangle corners (ta is defined to be vec2(0))
	vec2 tb = vec2(1, 0);
	vec2 tc = vec2(cos(angles.x), sin(angles.x)) * b;

	float sinzx = sin(angles.z + angles.x);

	// Triangle edge planes
	vec3 dirs[3] = vec3[3](vec3(-sin(angles.x), cos(angles.x), 0.), vec3(0., -1., 0.),
	vec3(sinzx, -cos(angles.z + angles.x), sinzx));

	vec2 incenter = (tb * b + tc) / (a + b + 1.);
	vec2 sidecenter = (tb * b) / (a + b);

	int reflcount = 0;

	// This is not the fastest way, but it certainly is the simplest.
	for(int i = 0; i < 32; ++i)
	{
		int j = 0;
		while(j < 3)
		{
			vec2 dir = dirs[j].xy;
			float d = dot(q, dir) - dirs[j].z;
			if(d > 0.)
			{
				// Reflect
				q -= dir * d * 2.;
				++reflcount;
				break;
			}
			++j;
		}
		if(j == 3)
		break;
	}

	vec3 col = vec3(0.);

	// Fermat point in trilinear coordinates
	vec3 fermat_tril = vec3(1) / cos(angles - PI/6.);
	vec3 fermat_bary = fermat_tril * vec3(a, b, 1.);
	vec2 fermat_point = (fermat_bary.y * tb + fermat_bary.z * tc) / (fermat_bary.x + fermat_bary.y + fermat_bary.z);

	// Calculate the generator for snub tilings
	vec2 refppa = fermat_point - dirs[0].xy * (dot(fermat_point, dirs[0].xy) - dirs[0].z) * 2.;
	vec2 refppb = fermat_point - dirs[1].xy * (dot(fermat_point, dirs[1].xy) - dirs[1].z) * 2.;
	vec2 refppc = fermat_point - dirs[2].xy * (dot(fermat_point, dirs[2].xy) - dirs[2].z) * 2.;
	vec2 snubpoint = tile_triangleCircumcenter(refppa, refppb, refppc);

	int poly = 0;
	float outline = 0.;

	if(sym.w == 0)
	{
		// Snub tiling
		if((reflcount & 1) == 0)
		{
			float sides[6];
			float linedist = 1e4;

			for(int i = 0; i < 3; ++i)
			{
				vec2 pp2 = snubpoint;
				vec2 dir = dirs[i].xy;
				float d = dot(pp2, dir) - dirs[i].z;
				pp2 -= dir * d * 2.;
				for(int j = 0; j < 2;++j)
				{
					vec2 pp3 = pp2;
					vec2 dir2 = dirs[(1 + i + j) % 3].xy;
					float d2 = dot(pp3, dir2) - dirs[(1 + i + j) % 3].z;
					pp3 -= dir2 * d2 * 2.;
					sides[i * 2 + j] = dot(q - snubpoint, normalize((pp3 - snubpoint).yx * vec2(1, -1)));
					linedist = min(linedist, tile_segment(q, snubpoint, pp3));
				}

			}

			if(sides[0] > 0. && sides[3] < 0.)
			{
				poly = 0;
			}
			else if(sides[1] > 0. && sides[2] < 0.)
			{
				poly = 2;
			}
			else if(sides[0] < 0. && sides[5] < 0. && sides[2] > 0.)
			{
				poly = 1;
			}
			else
			{
				poly = 2;
			}

			outline = mix(outline, 1., 1. - smoothstep(0., w, linedist));
			outline = mix(outline, 1., 1. - smoothstep(0., w, length(q - snubpoint) - vertex_dot_radius));
		}
		else
		{
			float sides[3];
			float linedist = 1e4;

			for(int i = 0; i < 3; ++i)
			{
				vec2 pp2 = snubpoint;
				vec2 dir = dirs[i].xy;
				float d = dot(pp2, dir) - dirs[i].z;
				pp2 -= dir * d * 2.;

				vec2 pp3 = snubpoint;
				vec2 dir2 = dirs[(i + 1) % 3].xy;
				float d2 = dot(pp3, dir2) - dirs[(i + 1) % 3].z;
				pp3 -= dir2 * d2 * 2.;

				sides[i] = dot(q - pp2, normalize((pp3 - pp2).yx * vec2(1, -1)));
				linedist = min(linedist, abs(sides[i]));
			}

			if(sides[0] > 0.)
			{
				poly = 0;
			}
			else if(sides[0] < 0. && sides[1] < 0.)
			{
				poly = 2;
			}
			else
			{
				poly = 1;
			}

			outline = mix(outline, 1., 1. - smoothstep(0., w, linedist));
		}
	}
	else
	{
		vec2 pp = sym.w == 1 ? vec2(0) : sym.w == 2 ? sidecenter : incenter;

		float side[3];

		// Point classification and distance to edges
		for(int i = 0; i < 3; ++i)
		{
			side[i] = dot(q - pp, dirs[i].yx * vec2(-1, 1));
			if(dot(q - pp, dirs[i].xy) > 0.)
			outline = mix(outline, 1., 1. - smoothstep(0., w, abs(side[i])));
		}

		outline = mix(outline, 1., 1. - smoothstep(0., w, length(q - pp) - vertex_dot_radius));
		poly = (side[0] > 0. && side[1] < 0.) ? 0 : (side[1] > 0. && side[2] < 0.) ? 1 : 2;
	}

	vec3 polycol = (poly == 0) ? vec3(1, .25, .25) : (poly == 1) ? vec3(.25, 1, .25) : vec3(.25, .25, 1);

	polycol *= mix(.85, 1., float(reflcount & 1));

	col = mix(polycol, vec3(.05), outline);

	ReturnT res;
	res = vec4(col, 1.);
	return res;
}