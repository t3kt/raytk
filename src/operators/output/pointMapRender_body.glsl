#if defined(THIS_RETURN_TYPE_Sdf)
Sdf map(THIS_CoordT p) {
	Sdf res = thismap(p, createDefaultContext());
	res.x *= 0.5;
	return res;
}

vec4 getColor(Sdf res, THIS_CoordT p) {
	int m = resultMaterial1(res);
	vec4 col;
	if (res.x > 0) {
		return vec4(0);
	}
	// #include <materialParagraph>
	else {
		return vec4(0);
	}
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

	#ifdef OUTPUT_COLOR
	colorOut = getColor(res, p);
	#endif

	#ifdef OUTPUT_SDF
	sdfOut = vec4(
		res.x,
		resultMaterial1(res),
		resultMaterial2(res),
		resultMaterialInterp(res));
	#endif
	#if defined(OUTPUT_NORMAL) && defined(THIS_COORD_TYPE_vec3)
	normalOut = vec4(calcNormal(p), 0.);
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