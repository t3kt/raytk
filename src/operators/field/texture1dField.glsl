ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q = adaptAsVec3(p);
	#endif
	float u = getAxis(q, int(THIS_Axis));
	vec4 value;
	#if defined(THIS_Coordmode_position)
	u = (u - THIS_Translate) / THIS_Scale;
	#elif defined(THIS_Coordmode_scaledindex)
	u = map01(u, THIS_Indexrange.x, THIS_Indexrange.y);
	#endif

	#if defined(THIS_Extendmode_hold)
	u = clamp(u, 0, 1);
	#elif defined(THIS_Extendmode_repeat)
	u = fract(u);
	#elif defined(THIS_Extendmode_mirror)
	u = modZigZag(u);
	#elif defined(THIS_Extendmode_zero)
	if (u < 0 || u > 1) {
		return ReturnT(0.);
	}
	#endif

	value = textureLod(THIS_texture, vec2(u, 0.), 0);

	return THIS_asReturnT(value);
}