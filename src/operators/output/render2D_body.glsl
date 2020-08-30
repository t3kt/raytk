layout (location = 0) out vec4 colorOut;
layout (location = 1) out vec4 sdfOut;

Sdf map(vec2 q)
{
	Sdf res = thismap(q, createDefaultContext());
	res.x *= 0.5;
	return res;
}

void main()
{
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;//*resolution;
	fragCoord.x *= uTDOutputInfo.res.z/uTDOutputInfo.res.w;

	Sdf res = map(fragCoord*2.0 - vec2(1));

	colorOut = getColor(res);
	sdfOut = vec4(res.x);
}
