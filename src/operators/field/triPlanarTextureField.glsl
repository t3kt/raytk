ReturnT thismap(CoordT p, MaterialContext ctx) {
	vec3 uv = p - 0.5;
	uv = (uv - THIS_Translate) / THIS_Scale;
	#if defined(THIS_Extendmode_hold)
	uv = clamp(uv, 0, 1);
	#elif defined(THIS_Extendmode_repeat)
	uv = fract(uv);
	#elif defined(THIS_Extendmode_mirror)
	uv = modZigZag(uv);
	#elif defined(THIS_Extendmode_zero)
		if (uv.x < 0 || uv.x > 1 || uv.y < 0 || uv.y > 1 || uv.z < 0 || uv.z > 1) {
			#if defined(THIS_RETURN_TYPE_float)
			return 0;
			#else
			return vec4(0);
			#endif
		}
	#endif
	vec3 n = abs(ctx.normal);
	n *= n;
	#ifdef THIS_Useseparatetextures
	vec3 colXY = texture(THIS_textureX, uv.xy).rgb;
	vec3 colYZ = texture(THIS_textureY, uv.yz).rgb;
	vec3 colZX = texture(THIS_textureZ, uv.zx).rgb;
	#else
	vec3 colXY = texture(THIS_texture, uv.xy).rgb;
	vec3 colYZ = texture(THIS_texture, uv.yz).rgb;
	vec3 colZX = texture(THIS_texture, uv.zx).rgb;
	#endif

	vec3 col = colXY * n.z + colYZ * n.x + colZX * n.y;
	vec4 value = vec4(col, 1);
	#ifdef THIS_RETURN_TYPE_float
	return value.x;
	#else
	return value;
	#endif
}
