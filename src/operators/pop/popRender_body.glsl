Sdf map(THIS_CoordT p) {
	Sdf res = thismap(p, createDefaultContext());
	if (!isNonHitSdf(res)) {
		res.x *= 0.5;
	}
	return res;
}


void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();
	vec2 resolution = uTDOutputInfo.res.zw;
	vec4 posAndExists;

	#if defined(THIS_TEX_TYPE_texture2d)
	vec2 fragCoord = vUV.st;
	exposeDataPosition(resolution, fragCoord.xy);
	posAndExists = texture(sTD2DInputs[0], fragCoord);
	#elif defined(THIS_TEX_TYPE_texture3d)
	// The center of the first slice is not located at 0, but rather halfway between 0 (the start of the first slice)
	// and 1.0 / depth (the end of the first slice)
	float firstSlice = uTD3DInfos[0].depth.x * 0.5;

	// now add the offset
	firstSlice += uTD3DInfos[0].depth.z;

	vec3 pos = vec3(vUV.st, firstSlice);
	exposeDataPosition(resolution, pos.xy);
	posAndExists = texture(sTD3DInputs[0], pos);
	#else
	#error invalidOutputTextureType
	#endif

	if (posAndExists.a == 0) {
		return;
	}
	#if defined(THIS_COORD_TYPE_vec3)
	vec3 p = posAndExists.xyz;
	#elif defined(THIS_COORD_TYPE_vec2)
	vec2 p = posAndExists.xy;
	#else
	#error invalidCoordType
	#endif

	#if defined(THIS_RETURN_TYPE_Sdf)

		Sdf res = map(p);

		MaterialContext matCtx = createMaterialContext();
		#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
			matCtx.globalPos = adaptAsVec3(p);
		#endif
		matCtx.ray = getViewRay(vec2(0.));
		#if defined(OUTPUT_COLOR) || defined(OUTPUT_NORMAL) || defined(THIS_HAS_TAG_uselight)
			matCtx.normal = calcNormal(p);
		#endif
		#ifdef THIS_HAS_TAG_uselight
			LightContext lightCtx = createLightContext(res, matCtx.normal);
			#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
			lightCtx.globalPos = adaptAsVec3(p);
			#endif
			matCtx.light = getLight(p, lightCtx);
		#endif

		#ifdef OUTPUT_COLOR
			matCtx.result = res;
			float level = getLevel(adaptAsVec3(p), matCtx);
			if (level <= 0.) {
				colorOut = vec4(0.);
			} else {
				vec3 col = getColor(THIS_asCoordT(p), matCtx);
				colorOut = vec4(col * level, level);
			}
		#endif

		#ifdef OUTPUT_SDF
			if (isNonHitSdf(res)) {
				sdfOut = vec4(0.);
			} else {
				sdfOut = vec4(vec3(res.x), 1.0);
			}
		#endif
		#if defined(OUTPUT_NORMAL)
			normalOut = vec4(calcNormal(p), 0.);
		#endif
		#if defined(OUTPUT_OBJECTID) && defined(RAYTK_OBJECT_ID_IN_SDF)
			objectIdOut += res.objectId;
		#endif

	#elif defined(THIS_RETURN_TYPE_vec4) || defined(THIS_RETURN_TYPE_float)

		#ifdef OUTPUT_VALUE
		valueOut = vec4(thismap(p, createDefaultContext()));
		#endif

	#else
		#error invalidReturnType
	#endif
}
