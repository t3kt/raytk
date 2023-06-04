#if defined(THIS_Pattern_twolayer)
// Hexagonal Interlacing - base by FabriceNeyret2
// https://www.shadertoy.com/view/tsyXRh

#define THIS_rnd(p)   fract(sin(dot(p, vec2(411.3, 2899.7+THIS_Seed)))*43758.5453)

const vec2 THIS_s = vec2( 3, sqrt(3.));

vec4 THIS_getHex(vec2 p){
	vec4 hC = floor( vec4( p, p - vec2(THIS_s.y, THIS_s.y/2.))/THIS_s.xyxy ) + .5;
	vec2 a = p -  hC.xy *THIS_s,
	b = p - (hC.zw + .5) *THIS_s;
	return dot(a,a) < dot(b,b)
	? vec4(a, hC.xy)
	: vec4(b, hC.zw+.5);
}

float THIS_getMask( vec2 p, float thickness) {
	float ia = floor( atan(p.y,p.x) *3./TAU) + .5;
	pR(p, ia * TAU / 3.);
	p.x -= 1.;
	float rad2 = mix(.85, .49, thickness);
	return length(p) - rad2;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float thickness = adaptAsFloat(inputOp_thicknessField(p, ctx));
	#else
	float thickness = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_blendingField
	float b = adaptAsFloat(inputOp_blendingField(p, ctx));
	#else
	float b = THIS_Blending;
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	vec2 R = vec2(100); // REPLACE THIS IT WAS RESOLUTION
	vec4 hp = THIS_getHex(q);

	vec2 hp2 = hp.xy;
	pR(hp2, -TAU/6.);
	vec2 D = vec2( THIS_getMask(hp.xy, thickness), THIS_getMask(hp2, thickness) );      // axial distance of the 2 layers
	#ifdef THIS_EXPOSE_axialdist
	THIS_axialdist = D;
	#endif
	vec2 M = smoothstep(-5./R.y,5./R.y, D);                       // masks
	vec2 B = smoothstep(0.,b, D);                               // border decoration
	// B = smoothstep(0., 1., (.65 + D*D*4.)*B);                     // shaded relief
	#ifdef THIS_Randomize
	float m = THIS_rnd(hp.zw) > .5 ? M.x : 1.-M.y;                     // layer-preserving random control
	#else
	float m = M.x;
	#endif
	#ifdef THIS_EXPOSE_mask
	THIS_mask = vec3(M, m);
	#endif

	#ifdef THIS_HAS_INPUT_color1Field
	vec4 col1 = fillToVec4(inputOp_color1Field(p, ctx));
	#else
	vec4 col1 = vec4(THIS_Color1, 1.);
	#endif
	#ifdef THIS_HAS_INPUT_color2Field
	vec3 col2 = fillToVec3(inputOp_color2Field(p, ctx));
	#else
	vec3 col2 = THIS_Color2;
	#endif
	#ifdef THIS_HAS_INPUT_bgColorField
	vec3 bgCol = fillToVec3(inputOp_bgColorField(p, ctx));
	#else
	vec3 bgCol = THIS_Bgcolor;
	#endif

	vec4 res = vec4(0.);
	#ifdef THIS_Format_customcolor
	res = col1;
	#else
	// res += mix( B.y, B.x, m );                                      // simple display
//	res += mix( B.y*.5, B.x, m );                                   // 2-tints display
	res.rgb += mix(col1.rgb*B.y, col2*B.x, m);
	res.rgb += bgCol * (1.0-max(M.x, M.y));
//	res.rgb += mix(bgCol, mix(col1.rgb*B.y, col2*B.x, m), max(M.x,M.y));
//	res.rgb += mix(
//		mix(bgCol, col1*B.y, M.y),
//		mix(bgCol, col2*B.x, M.x),
//		m);
//	res.rgb += mix(
//		bgCol,
//		mix(col1*B.y, col2*B.x, m),
//		max(M.x, M.y)
//	);
	// --- for next ones uncomment original random control
	// res += mix( -4.*D.x*B.y, B.x, M.x);                             // shadows
	// res += mix( -D.x*B.y, (1.+D.y)*B.x, M.x);                       // pseudo-Z
	#endif
	return res;
}

#else
	#error invalidPattern
#endif
