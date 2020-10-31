ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_float)
	vec4 posAndDist = opElongate(vec3(p, 0, 0), THIS_Sizex);
	p = posAndDist.x;
	#elif defined(THIS_COORD_TYPE_vec2)
	vec4 posAndDist = opElongate(vec3(p, 0), THIS_Size);
	p = posAndDist.xy;
	#elif defined(THIS_COORD_TYPE_vec3)
	vec4 posAndDist = opElongate(p, THIS_Size);
	p = posAndDist.xyz;
	#else
	#error invalidCoordType
	#endif
	ReturnT res = inputOp1(p, ctx);
//#ifdef THIS_RETURN_TYPE_Sdf
//	res.x += posAndDist.w;
//#endif
	return res;
}
