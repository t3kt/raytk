ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = vUV.st;
	vec4 val = texture(THIS_texture, uv);
	ReturnT res;
	#ifdef THIS_RETURN_TYPE_vec4
	res = val;
	#else
	switch (int(THIS_Channel)) {
		case 0: res = val.x; break;
		case 1: res = val.y; break;
		case 2: res = val.z; break;
		case 3: res = val.w; break;
	}
	#endif
	return res;
}