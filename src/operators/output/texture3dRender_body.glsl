#if defined(THIS_RETURN_TYPE_Sdf)
Sdf map(THIS_CoordT p) {
	Sdf res = thismap(p, createDefaultContext());
	if (!isNonHitSdf(res)) {
		res.x *= 0.5;
	}
	return res;
}

vec3 getColorInner(THIS_CoordT p, MaterialContext matCtx, int m) {
	vec3 col = vec3(0.);
	if (false) {}
	// #include <materialParagraph>
	else {
		return getColor(matCtx.result);
	}
	return col;
}

vec3 getColor(THIS_CoordT p, MaterialContext matCtx) {
	if (isNonHitSdf(matCtx.result)) return vec3(0.);
	vec3 col = vec3(0);
	float ratio = resultMaterialInterp(matCtx.result);
	int m1 = resultMaterial1(matCtx.result);
	int m2 = resultMaterial2(matCtx.result);
	#ifdef RAYTK_USE_MATERIAL_POS
	vec3 p1 = p;
	vec3 p2 = p;
	if (matCtx.result.materialPos.w > 0.) {
		p1 = matCtx.result.materialPos.xyz;
	}
	if (matCtx.result.materialPos2.w > 0.) {
		p2 = matCtx.result.materialPos2.xyz;
	}
	#endif
	int priorStage = pushStage(RAYTK_STAGE_MATERIAL);
	if (ratio <= 0 || m1 == m2) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p1;
		#endif
		col = getColorInner(p, matCtx, m1);
	} else if (ratio >= 1) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p2;
		#endif
		col = getColorInner(p, matCtx, m2);
	} else {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p1;
		#endif
		vec3 col1 = getColorInner(p, matCtx, m1);
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p2;
		#endif
		vec3 col2 = getColorInner(p, matCtx, m2);
		col = mix(col1, col2, ratio);
	}
	popStage(priorStage);
	return col;
}

vec3 calcNormal(THIS_CoordT pos)
{
	int priorStage = pushStage(RAYTK_STAGE_NORMAL);
	#ifdef THIS_Enablenormalsmoothing
	vec2 e = vec2(1.0, -1.0) * (0.5773*0.005 + THIS_Normalsmoothing);
	#else
	const vec2 e = vec2(1.0, -1.0)*0.5773*0.005;
	#endif
	#ifdef THIS_COORD_TYPE_vec3
	vec3 n = normalize(
		e.xyy*map(pos + e.xyy).x +
		e.yyx*map(pos + e.yyx).x +
		e.yxy*map(pos + e.yxy).x +
		e.xxx*map(pos + e.xxx).x);
	#elif defined(THIS_COORD_TYPE_vec2)
	vec2 n = normalize(
		e.xy*map(pos + e.xy).x +
		e.yy*map(pos + e.yy).x +
		e.yx*map(pos + e.yx).x +
		e.xx*map(pos + e.xx).x);
	#endif
	popStage(priorStage);
	return adaptAsVec3(n);
}

#endif

//#define RES ivec3(uTDOutputInfo.res.zw,uTDOutputInfo.depth.y)

layout (local_size_x = 8, local_size_y = 8, local_size_z = 8) in;
void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
//	initOutputs();
	ivec3 resolution = ivec3(uTDOutputInfo.res.zw,uTDOutputInfo.depth.y);
	ivec3 pixel = ivec3(gl_GlobalInvocationID.xyz);

	vec3 pixelUV = vec3(pixel) / vec3(resolution);

	vec3 center = THIS_Center;
	vec3 scale = THIS_Scale;

	vec3 p = mapRange(pixelUV, vec3(0.), vec3(1.), center - scale, center + scale);

	#if defined(THIS_RETURN_TYPE_Sdf)

		Sdf res = map(p);
		float level = getLevel(res);

		#if defined(OUTPUT_DENSITY) && defined(RAYTK_USE_DENSITY)
			imageStore(densityOut, pixel, vec4(res.density * level));
		#endif

		MaterialContext matCtx = createMaterialContext();
		#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
			matCtx.globalPos = adaptAsVec3(p);
		#endif
		matCtx.ray = getViewRay(p);
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
			if (level <= 0.) {
				imageStore(colorOut, pixel, vec4(0.));
			} else {
				vec3 col = getColor(THIS_asCoordT(p), matCtx);
				imageStore(colorOut, pixel, vec4(col * level, level));
			}
		#endif

		#ifdef OUTPUT_SDF
			if (isNonHitSdf(res)) {
				imageStore(sdfOut, pixel, vec4(0.));
			} else {
				imageStore(sdfOut, pixel, vec4(vec3(res.x), 1.0));
			}
		#endif
		#ifdef OUTPUT_NORMAL
			imageStore(normalOut, pixel, vec4(calcNormal(p), 1.));
		#endif

	#elif defined(THIS_RETURN_TYPE_vec4) || defined(THIS_RETURN_TYPE_float)

		#ifdef OUTPUT_VALUE
		imageStore(valueOut, pixel, vec4(thismap(p, createDefaultContext())));
		#endif

	#else
		#error invalidReturnType
	#endif
}
