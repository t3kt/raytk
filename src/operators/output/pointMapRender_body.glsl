layout (location = 0) out vec4 sdfOut;

Sdf map(vec3 p) {
	Sdf res = thismap(p, createDefaultContext());
	res.x *= 0.5;
	return res;
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

	sdfOut = vec4(res.x, res.x, res.x, 1);
}
