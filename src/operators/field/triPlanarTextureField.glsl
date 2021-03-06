ReturnT thismap(CoordT p, MaterialContext ctx) {
	vec3 uv = p;
	vec3 valMult = vec3(1.0);
	uv = (uv - THIS_Translate) / THIS_Scale;
	#if defined(THIS_Extendmode_hold)
	uv = clamp(uv, -0.5, 0.5);
	#elif defined(THIS_Extendmode_repeat)
	uv = fract(uv+0.5)-0.5;
	#elif defined(THIS_Extendmode_mirror)
	uv = modZigZag(uv+0.5)-0.5;
	#elif defined(THIS_Extendmode_zero)
		bvec3 isOut = bvec3(
			uv.x < -0.5 || uv.x > 0.5,
			uv.y < -0.5 || uv.y > 0.5,
			uv.z < -0.5 || uv.z > 0.5
		);
		valMult = vec3(
			!(isOut.y || isOut.z),
			!(isOut.x || isOut.z),
			!(isOut.x || isOut.y)
		);
	#endif
	vec3 n = abs(ctx.normal);
	n *= n;
	#ifdef THIS_Useseparatetextures
	vec3 colXY = texture(THIS_textureX, uv.xy + 0.5).rgb;
	vec3 colYZ = texture(THIS_textureY, uv.yz + 0.5).rgb;
	vec3 colZX = texture(THIS_textureZ, uv.zx + 0.5).rgb;
	#else
	vec3 colXY = texture(THIS_texture, uv.xy + 0.5).rgb;
	vec3 colYZ = texture(THIS_texture, uv.yz + 0.5).rgb;
	vec3 colZX = texture(THIS_texture, uv.zx + 0.5).rgb;
	#endif

	vec3 col = colXY * n.z * valMult.z + colYZ * n.x * valMult.x + colZX * n.y * valMult.y;
	vec4 value = vec4(col, 1);
	#ifdef THIS_RETURN_TYPE_float
	return value.x;
	#else
	return value;
	#endif
}
