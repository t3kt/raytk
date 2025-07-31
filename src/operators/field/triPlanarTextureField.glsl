vec3 THIS_sampleTexture(sampler2D tex, vec2 uv, ContextT ctx) {
	#if defined(RAYTK_LOD_IN_MATERIAL_CONTEXT)
	return textureLod(tex, uv + 0.5, ctx.lod).rgb;
	#else
	return textureLod(tex, uv + 0.5, 0).rgb;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_uvField)
	vec3 uv = inputOp_uvField(p, ctx).xyz;
	#elif defined(RAYTK_USE_UV)
	vec3 uv = mix(p, ctx.uv.xyz, ctx.uv.w);
	#else
	vec3 uv = p;
	#endif
	vec3 valMult = vec3(1.0);
	uv = (uv - THIS_Translate) / THIS_Scale;
	switch (int(THIS_Extendmode)) {
		case THISTYPE_Extendmode_hold:
			uv = clamp(uv, -0.5, 0.5);
			break;
		case THISTYPE_Extendmode_repeat:
			uv = fract(uv+0.5)-0.5;
			break;
		case THISTYPE_Extendmode_mirror:
			uv = modZigZag(uv+0.5)-0.5;
			break;
		case THISTYPE_Extendmode_zero:
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
			break;
	}
	vec3 n = abs(ctx.normal);
	n *= n;
	#ifdef THIS_Useseparatetextures
	vec3 colXY = THIS_sampleTexture(THIS_textureX, uv.xy, ctx).rgb;
	vec3 colYZ = THIS_sampleTexture(THIS_textureY, uv.yz, ctx).rgb;
	vec3 colZX = THIS_sampleTexture(THIS_textureZ, uv.zx, ctx).rgb;
	#else
	vec3 colXY = THIS_sampleTexture(THIS_texture, uv.xy, ctx).rgb;
	vec3 colYZ = THIS_sampleTexture(THIS_texture, uv.yz, ctx).rgb;
	vec3 colZX = THIS_sampleTexture(THIS_texture, uv.zx, ctx).rgb;
	#endif

	vec3 col;
	switch (int(THIS_Blendmode)) {
		case THISTYPE_Blendmode_normals:
			col = colXY * n.z * valMult.z + colYZ * n.x * valMult.x + colZX * n.y * valMult.y;
			break;
		case THISTYPE_Blendmode_add:
			col = colXY + colYZ + colZX;
			break;
		case THISTYPE_Blendmode_max:
			col = max(max(colXY, colYZ), colZX);
			break;
		case THISTYPE_Blendmode_avg:
			col = (colXY + colYZ + colZX) / 3.0;
			break;
	}

	#ifdef THIS_RETURN_TYPE_float
	return col.x;
	#else
	return vec4(col, 1);
	#endif
}
