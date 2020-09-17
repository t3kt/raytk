#ifdef THIS_RETURN_TYPE_Sdf
Sdf map(vec3 p) {
	Sdf res = thismap(p, createDefaultContext());
	res.x *= 0.5;
	return res;
}

vec4 getColor(Sdf res, vec3 p) {
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
	vec3 p = posAndExists.xyz;
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
#endif

#ifdef THIS_RETURN_TYPE_vec4
void main() {
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;
	vec4 posAndExists = texture(sTD2DInputs[0], fragCoord);

	if (posAndExists.a == 0) {
		#ifdef OUTPUT_VALUE
		valueOut = vec4(0);
		#endif
		return;
	}
	vec3 p = posAndExists.xyz;
	#ifdef OUTPUT_VALUE
	valueOut = thismap(p, createDefaultContext());
	#endif
}
#endif