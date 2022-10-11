vec3 THIS_fold(vec3 pos) {
	for(int i=0;i<5 /*Type*/;i++){
		pos.xy=abs(pos.xy);//fold about xz and yz planes
		pos-=2.*min(0.,dot(pos,THIS_nc))*THIS_nc;//fold about nc plane
	}
	return pos;
}

float THIS_D2Planes(vec3 pos, float rad) {//distance to the 3 faces
	pos-=THIS_p * rad;
	float d0=dot(pos,THIS_pab);
	float d1=dot(pos,THIS_pbc);
	float d2=dot(pos,THIS_pca);
	return max(max(d0,d1),d2);
}

float THIS_D2Segments(vec3 pos, float rad, float size) {
	pos-=THIS_p * rad;
	float dla=dot2(pos-min(0.,pos.x)*vec3(1.,0.,0.));
	float dlb=dot2(pos-min(0.,pos.y)*vec3(0.,1.,0.));
	float dlc=dot2(pos-min(0.,dot(pos,THIS_nc))*THIS_nc);
	return sqrt(min(min(dla,dlb),dlc))-size;
}

Sdf THIS_D2Vertices(vec3 pos, ContextT ctx, float rad, float size) {
	Sdf res;
	#ifdef THIS_HAS_INPUT_vertexShape
	res = inputOp_vertexShape(pos - THIS_p * rad, ctx);
	#else
	res = createSdf(length(pos - THIS_p * rad)-size);
	#endif
	return res;
}

void THIS_combine(inout Sdf res1, in Sdf res2, in CoordT p, in ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	#ifdef THIS_HAS_INPUT_radiusField
	float rad = adaptAsFloat(inputOp_radiusField(p0, ctx));
	#else
	float rad = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_uvwField
	vec3 uvw = inputOp_uvwField(p, ctx).xyz;
	THIS_p=normalize((uvw.x*THIS_pab+uvw.y*THIS_pbc+uvw.z*THIS_pca));//U,V and W are the 'barycentric' coordinates (coted barycentric word because I'm not sure if they are really barycentric... have to check)
	#endif
	p = THIS_fold(p);
	Sdf res1 = createSdf(RAYTK_MAX_DIST);
	if (IS_TRUE(THIS_Enablefaces)) {
		#ifdef THIS_HAS_INPUT_faceRadiusField
		float fRad = adaptAsFloat(inputOp_faceRadiusField(p0, ctx));
		#else
		float fRad = THIS_Faceradius;
		#endif
		THIS_combine(res1, createSdf(THIS_D2Planes(p, fRad * rad)), p, ctx);
	}
	if (IS_TRUE(THIS_Enablesegments)) {
		#ifdef THIS_HAS_INPUT_segmentRadiusField
		float sRad = adaptAsFloat(inputOp_segmentRadiusField(p0, ctx));
		#else
		float sRad = THIS_Segmentradius;
		#endif
		#ifdef THIS_HAS_INPUT_segmentSizeField
		float sSize = adaptAsFloat(inputOp_segmentSizeField(p0, ctx));
		#else
		float sSize = THIS_Segmentsize;
		#endif
		THIS_combine(res1, createSdf(THIS_D2Segments(p, sRad * rad, sSize)), p, ctx);
	}
	if (IS_TRUE(THIS_Enablevertices)) {
		#ifdef THIS_HAS_INPUT_vertexRadiusField
		float vRad = adaptAsFloat(inputOp_vertexRadiusField(p0, ctx));
		#else
		float vRad = THIS_Vertexradius;
		#endif
		#if defined(THIS_HAS_INPUT_vertexSizeField) && !defined(THIS_HAS_INPUT_vertexShape)
		float vSize = adaptAsFloat(inputOp_vertexSizeField(p0, ctx));
		#else
		float vSize = THIS_Vertexsize;
		#endif
		THIS_combine(res1, THIS_D2Vertices(p, ctx, vRad * rad, vSize), p, ctx);
	}

	return res1;
}