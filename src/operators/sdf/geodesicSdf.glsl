// https://www.shadertoy.com/view/4tG3zW

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_Faceoffsetfieldcoordmode_origpos
	CoordT foFieldP = p;
	#endif
	float s = THIS_Divisions;
	#if defined(THIS_Shape_dodecahedron)
	vec3 n = pDodecahedron(p, int(s));
	#elif defined(THIS_Shape_icosahedron)
	vec3 n = pIcosahedron(p, int(s));
	#else
	#error invalidShape
	#endif

	float d = RAYTK_MAX_DIST;
	#ifdef THIS_Enablespikes
	float spikeSize = .08 + (2. - s) * THIS_Spikeradius;
	d = min(d, fCone(p, spikeSize, THIS_Spikelength, n, THIS_Spikeoffset));
	#endif
	#ifdef THIS_Enablefaces
	#ifdef THIS_Faceoffsetfieldcoordmode_geopos
	CoordT foFieldP = p;
	#endif
	#ifdef THIS_HAS_INPUT_faceOffset
	float fo = inputOp_faceOffset(foFieldP, ctx);
	#else
	float fo = THIS_Faceoffset;
	#endif
	d = min(d, fPlane(p, n, -fo));
	#endif
	#ifdef THIS_HAS_INPUT_spikeSdf
	p -= n * (THIS_Spikeoffset + THIS_Spikelength);
	p = reflect(p, normalize(mix(vec3(0,1,0), -n, .5)));
	ReturnT res = inputOp_spikeSdf(p, ctx);
	res.x = min(res.x, d);
	return res;
	#else
	return createSdf(d);
	#endif
}