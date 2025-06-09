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

void main() {
	const uint id = TDIndex();
	if(id >= TDNumElements()) return;

	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

	CoordT pos = getPos();

	Sdf res = map(p);

	MaterialContext matCtx = createMaterialContext();
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
		matCtx.globalPos = adaptAsVec3(p);
	#endif
	matCtx.ray = getViewRay(vec2(0.));
	#if defined(OUTPUT_ATTR_COLOR) || defined(OUTPUT_ATTR_NORMAL) || defined(THIS_HAS_TAG_uselight)
		matCtx.normal = calcNormal(p);
	#endif
	#ifdef THIS_HAS_TAG_uselight
		LightContext lightCtx = createLightContext(res, matCtx.normal);
		#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
		lightCtx.globalPos = adaptAsVec3(p);
		#endif
		matCtx.light = getLight(p, lightCtx);
	#endif

	#ifdef OUTPUT_ATTR_COLOR
		matCtx.result = res;
		float level = getLevel(adaptAsVec3(p), matCtx);
		if (level <= 0.) {
			OUTPUT_ATTR_COLOR[id] = vec4(0.);
		} else {
			vec3 col = getColor(THIS_asCoordT(p), matCtx);
			OUTPUT_ATTR_COLOR[id] = vec4(col * level, level);
		}
	#endif

	#ifdef OUTPUT_ATTR_DIST
		if (isNonHitSdf(res)) {
			OUTPUT_ATTR_DIST[id] = 0.;
		} else {
			OUTPUT_ATTR_DIST[id] = res.x;
		}
	#endif
	#if defined(OUTPUT_NORMAL)
		normalOut = vec4(calcNormal(p), 0.);
	#endif
	#if defined(OUTPUT_OBJECTID) && defined(RAYTK_OBJECT_ID_IN_SDF)
		objectIdOut += res.objectId;
	#endif
}
