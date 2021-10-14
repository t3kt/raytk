// hexagonal truchet by FabriceNeyret2
// https://www.shadertoy.com/view/Xdt3D8


vec2 THIS_closestHexCenters(vec2 p) {
	vec2  f = fract(p);  p -= f;
	float v = fract((p.x + p.y)/3.);
	return  v<.6 ?   v<.3 ?  p  :  ++p  :  p + step(f.yx,f) ;
}


ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

//	vec2 R = iResolution.xy;
//	vec2 R = vec2(1920., 1080.);
//	float Z = 10./R.y;

//	q = q*0.1;

	// NB: M^-1.H(M.p) converts back and forth to hex grid, which is mostly a tilted square grid
	vec2 h = THIS_closestHexCenters( q+ vec2(.58,.15)*q.y ); // closestHex( mat2(1,0, .58, 1.15)*q ); // 1/sqrt(3), 2/sqrt(3)
	q -=   h- vec2(.5, .13)*h.y;   // q -= mat2(1,0,-.5, .87) * h;          // -1/2, sqrt(3)/2

	float s;
	// s = sign( fract(1e5*cos(h.x+9.*h.y)) -.5 );
	s = sign( cos(1e5*cos(h.x+THIS_Seed*h.y)) );   // rnd (tile) = -1 or 1

	#define THIS_L(x,y)  length( q - s*vec2(x,y) )            // dist to neighbor 1,3,5 or 2,4,6
	//#define L(a)  length( q - s*sin(a+vec2(1.57,0)) )  // variant L(0), L(2.1), L(-2.1)
	float l = min(min(THIS_L(-1, 0  ),                    // closest neigthborh (even or odd set, dep. s)
	THIS_L(.5, .87)),                   // 1/2, sqrt(3)/2
	THIS_L(.5,-.87));
//return l;

//o -=o-- -.2 / abs(l-.5);

// o -=o- smoothstep(.1+Z, .1, abs(l-.5));              // precise anti-aliasing
	return ReturnT(.2 / abs(l-.5));
//return ReturnT(cos(l*25.1));                                  // nice variant 1 by Shane
//return vec4(sqrt(2.*cos(vec3(1, 3, 3)*l*6.28)), 1.); // nice variant 2 by Shane
}
