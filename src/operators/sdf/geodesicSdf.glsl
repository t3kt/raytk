// https://www.shadertoy.com/view/4tG3zW

ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_Faceoffsetfieldcoordmode_origpos
	CoordT foFieldP = p;
	#pragma r:endif
	float s = THIS_Divisions;
	#pragma r:if THIS_Shape_dodecahedron
	vec3 n = pDodecahedron(p, int(s));
	#pragma r:elif THIS_Shape_icosahedron
	vec3 n = pIcosahedron(p, int(s));
	#pragma r:else
	#error invalidShape
	#pragma r:endif

	float d = RAYTK_MAX_DIST;
	#pragma r:if THIS_Enablespikes
	float spikeSize = .08 + (2. - s) * THIS_Spikeradius;
	d = min(d, fCone(p, spikeSize, THIS_Spikelength, n, THIS_Spikeoffset));
	#pragma r:endif
	#pragma r:if THIS_Enablefaces
	#pragma r:if THIS_Faceoffsetfieldcoordmode_geopos
	CoordT foFieldP = p;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_faceOffset
	float fo = inputOp_faceOffset(foFieldP, ctx);
	#pragma r:else
	float fo = THIS_Faceoffset;
	#pragma r:endif
	d = min(d, fPlane(p, n, -fo));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_spikeSdf
	p -= n * (THIS_Spikeoffset + THIS_Spikelength);
	p = reflect(p, normalize(mix(vec3(0,1,0), -n, .5)));
	ReturnT res = inputOp_spikeSdf(p, ctx);
	res.x = min(res.x, d);
	return res;
	#pragma r:else
	return createSdf(d);
	#pragma r:endif
}