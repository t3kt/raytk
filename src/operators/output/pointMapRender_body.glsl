#if defined(THIS_RETURN_TYPE_Sdf)
Sdf map(THIS_CoordT p) {
	Sdf res = thismap(p, createDefaultContext());
	res.x *= 0.5;
	return res;
}

vec4 getColor(Sdf res, THIS_CoordT p) {
	int m = int(res.material);
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

void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;
	vec4 posAndExists = texture(sTD2DInputs[0], fragCoord);

	if (posAndExists.a == 0) {
		#ifdef OUTPUT_SDF
		sdfOut = vec4(0);
		#endif
		#ifdef OUTPUT_COLOR
		colorOut = vec4(0);
		#endif
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
		res.material,
		res.material2,
		res.interpolant);
	#endif
}
#elif defined(THIS_RETURN_TYPE_vec4) || defined(THIS_RETURN_TYPE_float)
void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;
	vec4 posAndExists = texture(sTD2DInputs[0], fragCoord);

	if (posAndExists.a == 0) {
		#ifdef OUTPUT_VALUE
		valueOut = vec4(0);
		#endif
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