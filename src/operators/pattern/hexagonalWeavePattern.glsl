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

float THIS_mask( vec2 p, float thickness) {
	float ia = floor( atan(p.y,p.x) *3./TAU) + .5;
	pR(p, ia * TAU / 3.);
	p.x -= 1.;
	float rad2 = .666;

	rad2 = mix(.85, .49, thickness);
	return length(p) - rad2;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_thicknessField
	float thickness = adaptAsFloat(inputOp_thicknessField(p, ctx));
	#else
	float thickness = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	vec2 R = vec2(100); // REPLACE THIS IT WAS RESOLUTION
	vec4 O = vec4(0.);
	vec4 hp = THIS_getHex(q);

	vec2 hp2 = hp.xy;
	pR(hp2, -TAU/6.);
	vec2 D = vec2( THIS_mask(hp.xy, thickness), THIS_mask(hp2, thickness) );      // axial distance of the 2 layers
	vec2 M = smoothstep(-5./R.y,5./R.y, D);                       // masks
	vec2 B = smoothstep(0.,.05, D);                               // border decoration
	// B = smoothstep(0., 1., (.65 + D*D*4.)*B);                     // shaded relief
	#ifdef THIS_Randomize
	float m = THIS_rnd(hp.zw) > .5 ? M.x : 1.-M.y;                     // layer-preserving random control
	#else
	float m = M.x;
	#endif

	// O += mix( B.y, B.x, m );                                      // simple display
	O += mix( B.y*.5, B.x, m );                                   // 2-tints display
	// --- for next ones uncomment original random control
	// O += mix( -4.*D.x*B.y, B.x, M.x);                             // shadows
	// O += mix( -D.x*B.y, (1.+D.y)*B.x, M.x);                       // pseudo-Z
	return O;
}

#else
	#error invalidPattern
#endif
