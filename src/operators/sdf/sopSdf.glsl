ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Voxelorigin;
	float dBound = fBox(p, THIS_Boundingboxsize);
//	if (dBound <= RAYTK_SURF_DIST) {
//		return createSdf(RAYTK_SURF_DIST);
//	}
	vec3 depthRes = vec3(THIS_normAndDist_info.res.zw, THIS_normAndDist_info.depth.y);
	ivec3 coord = ivec3((p / THIS_Boundingboxsize + vec3(0.5))*depthRes);
	vec4 data = texelFetch(THIS_normAndDist, coord, 0);
	//vec3 dir = data.xyz;
	float d = -data.w;
	return createSdf(d);
}