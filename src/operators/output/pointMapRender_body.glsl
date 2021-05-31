#if defined(THIS_RETURN_TYPE_Sdf)
Sdf map(THIS_CoordT p) {
	Sdf res = thismap(p, createDefaultContext());
	res.x *= 0.5;
	return res;
}

vec3 getColorInner(THIS_CoordT p, MaterialContext matCtx, int m) {
	vec3 col = vec3(0.);
	if (false) {}
	// #include <materialParagraph>
	else {}
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

#ifdef THIS_COORD_TYPE_vec3

vec3 calcNormal(in vec3 pos)
{
	vec2 e = vec2(1.0, -1.0)*0.5773*0.005;
	return normalize(
	e.xyy*map(pos + e.xyy).x +
	e.yyx*map(pos + e.yyx).x +
	e.yxy*map(pos + e.yxy).x +
	e.xxx*map(pos + e.xxx).x);
}

#endif

void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;
	vec4 posAndExists = texture(sTD2DInputs[0], fragCoord);

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
	Sdf res = map(p);

	MaterialContext matCtx = createMaterialContext();
	#if defined(OUTPUT_COLOR) || defined(OUTPUT_NORMAL)
	matCtx.normal = calcNormal(p);
	#endif

	#ifdef OUTPUT_COLOR
	matCtx.result = res;
	vec3 col = getColor(p, matCtx);
	colorOut = vec4(col, 1.);
	#endif

	#ifdef OUTPUT_SDF
	sdfOut = vec4(vec3(res.x), 1.0);
	#endif
	#if defined(OUTPUT_NORMAL) && defined(THIS_COORD_TYPE_vec3)
	normalOut = vec4(calcNormal(p), 0.);
	#endif
	#if defined(OUTPUT_OBJECTID) && defined(RAYTK_OBJECT_ID_IN_SDF)
	objectIdOut += res.objectId;
	#endif
}
#elif defined(THIS_RETURN_TYPE_vec4) || defined(THIS_RETURN_TYPE_float)
void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;
	vec4 posAndExists = texture(sTD2DInputs[0], fragCoord);

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
	#ifdef OUTPUT_VALUE
	valueOut = vec4(thismap(p, createDefaultContext()));
	#endif
}

#else
	#error invalidReturnType
#endif