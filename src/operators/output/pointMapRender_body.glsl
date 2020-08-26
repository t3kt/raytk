layout (location = 0) out vec4 sdfOut;
layout (location = 1) out vec4 colorOut;

Sdf map(vec3 p) {
	Sdf res = thismap(p, createDefaultContext());
	res.x *= 0.5;
	return res;
}


vec4 getColor(Sdf res, vec3 p) {
	int m = int(res.material);
	vec4 col;
	if (false) {
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
		sdfOut = vec4(0);
		return;
	}
	vec3 p = posAndExists.xyz;
	Sdf res = map(p);

	colorOut = getColor(res, p);

	sdfOut = vec4(
		res.x,
		res.material,
		res.material2,
		res.interpolant);
}
