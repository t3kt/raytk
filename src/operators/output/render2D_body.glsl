#if defined(THIS_COORD_TYPE_float)
float prepCoord(vec2 p) {
	return p.x;
}
#elif defined(THIS_COORD_TYPE_vec2)
vec2 prepCoord(vec2 p) {
	return p;
}
#else
#error invalidCoordType
#endif

#ifdef THIS_RETURN_TYPE_Sdf
Sdf map(vec2 p)
{
	Sdf res = thismap(prepCoord(p), createDefaultContext());
	res.x *= 0.5;
	return res;
}

vec3 getColorInner(vec2 p, MaterialContext matCtx, int m) {
	vec3 col = vec3(0.);
	if (false) {}
	// #include <materialParagraph>
	else {}
	return col;
}

vec3 getColor(vec2 p, MaterialContext matCtx) {
	if (matCtx.result.x > 0.) return vec3(0.);
	vec3 col = vec3(0.);
	float ratio = resultMaterialInterp(matCtx.result);
	int m1 = resultMaterial1(matCtx.result);
	int m2 = resultMaterial2(matCtx.result);
	#ifdef RAYTK_USE_MATERIAL_POS
	vec2 p1 = p;
	vec2 p2 = p;
	if (matCtx.result.materialPos.w > 0.) {
		p1 = matCtx.result.materialPos.xy;
	}
	if (matCtx.result.materialPos2.w > 0.) {
		p2 = matCtx.result.materialPos2.xy;
	}
	#endif
	#ifdef RAYTK_USE_UV
		vec4 uv1;
		vec4 uv2;
		resolveUV(matCtx, uv1, uv2);
	#endif
	int priorStage = pushStage(RAYTK_STAGE_MATERIAL);
	if (ratio <= 0 || m1 == m2) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = vec3(p1, 0.);
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv1;
		#endif
		col = getColorInner(p, matCtx, m1);
	} else if (ratio >= 1) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = vec3(p2, 0.);
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv2;
		#endif
		col = getColorInner(p, matCtx, m2);
	} else {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = vec3(p1, 0.);
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv1;
		#endif
		vec3 col1 = getColorInner(p, matCtx, m1);
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = vec3(p2, 0.);
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv2;
		#endif
		vec3 col2 = getColorInner(p, matCtx, m2);
		col = mix(col1, col2, ratio);
	}
	popStage(priorStage);
	return col;
}

#else
vec4 map(vec2 p) {
	#ifdef THIS_RETURN_TYPE_vec4
	return thismap(prepCoord(p), createDefaultContext());
	#else
	return vec4(thismap(prepCoord(p), createDefaultContext()));
	#endif
}
#endif

vec2 getCoord() {
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;//*resolution;
	vec2 p;

	#ifdef THIS_uvmap
	{
		p = texture(THIS_uvmap, fragCoord).rg;
	}
	#else
	{
		#if defined(THIS_Alignment_legacy)
		{
			fragCoord.x *= uTDOutputInfo.res.z/uTDOutputInfo.res.w;
			p = fragCoord*2. - vec2(1.);
		}
		#else
		{
			p = fragCoord;
			#if defined(THIS_Alignment_bottomleft)
			#elif defined(THIS_Alignment_center)
			p -= vec2(0.5);
			#else
			#error invalidAlignment
			#endif
			#if defined(THIS_Scaling_fill)
			#elif defined(THIS_Scaling_fitinside)
			{
				if (resolution.x > resolution.y) {
					p.x *= resolution.x / resolution.y;
				} else {
					p.y *= resolution.y / resolution.x;
				}
			}
			#elif defined(THIS_Scaling_fitoutside)
			{
				if (resolution.x > resolution.y) {
					p.y *= resolution.y / resolution.x;
				} else {
					p.x *= resolution.x / resolution.y;
				}
			}
			#endif
		}
		#endif
	}
	#endif
	return p;
}

void main()
{
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

vec2 p = getCoord();
#ifdef THIS_RETURN_TYPE_Sdf
	Sdf res = map(p);
	MaterialContext matCtx = createMaterialContext();
	float exists = isNonHitSdf(res) ? 0. : 1.;

	#ifdef OUTPUT_COLOR
	matCtx.result = res;
	vec3 col = getColor(p, matCtx);
	colorOut = vec4(col, exists);
	#endif
	#ifdef OUTPUT_SDF
	sdfOut = vec4(vec3(res.x), exists);
	#endif
	#ifdef OUTPUT_UV
	if (res.x < 0.)
	{
		vec4 uv1;
		vec4 uv2;
		resolveUV(matCtx, uv1, uv2);
		uvOut = mix(uv1, uv2, round(resultMaterialInterp(matCtx.result)));
	}
	#endif
#else
	#ifdef OUTPUT_COLOR
	colorOut = map(p);
	#endif
#endif
}
