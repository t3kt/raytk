// @Hexsize {"default":1, "normMin":0, "normMax":2}
// @Rotate {"default":0, "normMin":0, "normMax":360}

//vec2 closestHexCenter(vec2 p) {
//	vec2  f = fract(p);  p -= f;
//	float v = fract((p.x + p.y)/3.);
//	return  v<.6 ?   v<.3 ?  p  :  ++p  :  p + step(f.yx,f) ;
//}
// square root of 3 over 2



//const float hex_factor = 0.8660254037844386;
//
//#define HEX_FROM_CART(p) vec2(p.x / hex_factor, p.y)
//#define CART_FROM_HEX(g) vec2(g.x * hex_factor, g.y)
//
////////////////////////////////////////////////////////////////////////
//// Given a 2D position, find integer coordinates of center of nearest
//// hexagon in plane.
//
//vec2 closestHexCenter(in vec2 pos) {
//
//	// integer coords in hex center grid -- will need to be adjusted
//	vec2 gpos = HEX_FROM_CART(pos);
//	vec2 hex_int = floor(gpos);
//
//	// adjust integer coords
//	float sy = step(2.0, mod(hex_int.x+1.0, 4.0));
//	hex_int += mod(vec2(hex_int.x, hex_int.y + sy), 2.0);
//
//	// difference vector
//	vec2 gdiff = gpos - hex_int;
//
//	// figure out which side of line we are on and modify
//	// hex center if necessary
//	if (dot(abs(gdiff), vec2(hex_factor*hex_factor, 0.5)) > 1.0) {
//		vec2 delta = sign(gdiff) * vec2(2.0, 1.0);
//		hex_int += delta;
//	}
//
//	return hex_int;
//
//}


// https://www.shadertoy.com/view/Xljczw

// Helper vector. If you're doing anything that involves regular triangles or hexagons, the
// 30-60-90 triangle will be involved in some way, which has sides of 1, sqrt(3) and 2.
#ifdef FLAT_TOP_HEXAGON
const vec2 s = vec2(1.7320508, 1);
#else
const vec2 s = vec2(1, 1.7320508);
#endif

// This function returns the hexagonal grid coordinate for the grid cell, and the corresponding
// hexagon cell ID -- in the form of the central hexagonal point. That's basically all you need to
// produce a hexagonal grid.
//
// When working with 2D, I guess it's not that important to streamline this particular function.
// However, if you need to raymarch a hexagonal grid, the number of operations tend to matter.
// This one has minimal setup, one "floor" call, a couple of "dot" calls, a ternary operator, etc.
// To use it to raymarch, you'd have to double up on everything -- in order to deal with
// overlapping fields from neighboring cells, so the fewer operations the better.
vec4 getHex(vec2 p){

	// The hexagon centers: Two sets of repeat hexagons are required to fill in the space, and
	// the two sets are stored in a "vec4" in order to group some calculations together. The hexagon
	// center we'll eventually use will depend upon which is closest to the current point. Since
	// the central hexagon point is unique, it doubles as the unique hexagon ID.

	#ifdef FLAT_TOP_HEXAGON
	vec4 hC = floor(vec4(p, p - vec2(1, .5))/s.xyxy) + .5;
	#else
	vec4 hC = floor(vec4(p, p - vec2(.5, 1))/s.xyxy) + .5;
	#endif
	//vec4 hC = floor(vec4(p/s, p/s + .5));

	// Centering the coordinates with the hexagon centers above.
	vec4 h = vec4(p - hC.xy*s, p - (hC.zw + .5)*s);
	//vec4 h = p.xyxy - vec4(hC.xy + .5, hC.zw)*s.xyxy;


	// Nearest hexagon center (with respect to p) to the current point. In other words, when
	// "h.xy" is zero, we're at the center. We're also returning the corresponding hexagon ID --
	// in the form of the hexagonal central point. By the way, the unique ID (the .zw bit),
	// needs to be multiplied by "s" to give the correct quantized position back.
	// For example: float ns = noise2D(hID*s);
	//
	// On a side note, I sometimes compare hex distances, but I noticed that Iomateron compared
	// the squared Euclidian version, which seems neater, so I've adopted that.
	return dot(h.xy, h.xy)<dot(h.zw, h.zw) ? vec4(h.xy, hC.xy) : vec4(h.zw, hC.zw + .5);

}

ReturnT thismap(CoordT p, Context ctx) {
//	vec2 c = closestHexCenter(p / THIS_Hexsize);
//	c = CART_FROM_HEX(c);
	vec4 h = getHex(p / THIS_Hexsize);
	vec2 c = h.xy;
	pR(p, -radians(THIS_Rotate));
	p -= c;
	pR(p, radians(THIS_Rotate));
	p += c;
	return inputOp1(p, ctx);
}