ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	CoordT c = THIS_Position;
	p -= c;
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: p = p.yxz; break;
		case THISTYPE_Axis_y: break;
		case THISTYPE_Axis_z: p = p.xzy; break;
	}
	float a = atan(p.z, p.x);
	float r = THIS_Radius;
	vec3 lp = vec3(
		r * cos(a),
		0.,
		r * sin(a));
	lp += c;
	vec3 col = THIS_Color * THIS_Intensity;
	Light light = createLight(lp, col);
	#ifdef THIS_EXPOSE_lightdir
	THIS_lightdir = normalize(light.pos - p);
	#endif
	light.supportShadow = IS_TRUE(THIS_Enableshadow);
	#ifdef THIS_HAS_INPUT_colorField
	light.color *= fillToVec3(inputOp_colorField(p0, ctx));
	#endif
	if (IS_TRUE(THIS_Enableattenuation)) {
		float d = length(p0 - light.pos);
		float start = THIS_Attenuationstart;
		float end = THIS_Attenuationend;
		float atten = smoothstep(end, start, d);
		#ifdef THIS_HAS_INPUT_attenuationField
		light.color *= fillToVec3(inputOp_attenuationField(atten, ctx));
		#else
		light.color *= atten;
		#endif
	}
	return light;
}