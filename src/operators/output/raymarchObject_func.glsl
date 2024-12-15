ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_sdf
	return inputOp_sdf(p, ctx);
	#else
	return createNonHitSdf();
	#endif
}

#ifdef THIS_USE_LIMIT_BOX
bool checkLimit(vec3 p) {
	return p.x >= THIS_Limitboxmin.x &&
		p.x <= THIS_Limitboxmax.x &&
		p.y >= THIS_Limitboxmin.y &&
		p.y <= THIS_Limitboxmax.y &&
		p.z >= THIS_Limitboxmin.z &&
		p.z <= THIS_Limitboxmax.z;
}
#else
#define checkLimit(p) (true)
#endif
