vec3 THIS_fold(vec3 pos) {
	for(int i=0;i<5 /*Type*/;i++){
		pos.xy=abs(pos.xy);//fold about xz and yz planes
		pos-=2.*min(0.,dot(pos,THIS_nc))*THIS_nc;//fold about nc plane
	}
	return pos;
}

float THIS_D2Planes(vec3 pos) {//distance to the 3 faces
	pos-=THIS_p * THIS_Faceradius * THIS_Radius;
	float d0=dot(pos,THIS_pab);
	float d1=dot(pos,THIS_pbc);
	float d2=dot(pos,THIS_pca);
	return max(max(d0,d1),d2);
}

float THIS_D2Segments(vec3 pos) {
	pos-=THIS_p * THIS_Segmentradius * THIS_Radius;
	float dla=dot2(pos-min(0.,pos.x)*vec3(1.,0.,0.));
	float dlb=dot2(pos-min(0.,pos.y)*vec3(0.,1.,0.));
	float dlc=dot2(pos-min(0.,dot(pos,THIS_nc))*THIS_nc);
	return sqrt(min(min(dla,dlb),dlc))-THIS_Segmentsize;
}

Sdf THIS_D2Vertices(vec3 pos, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_vertexShape
	return inputOp_vertexShape(pos - THIS_p * THIS_Vertexradius * THIS_Radius, ctx);
	#pragma r:else
	return createSdf(length(pos - THIS_p * THIS_Vertexradius * THIS_Radius)-THIS_Vertexsize);
	#pragma r:endif
}

void THIS_combine(inout Sdf res1, Sdf res2) {
	#pragma r:if THIS_HAS_BLEND_RADIUS
	float r = THIS_Blendradius;
	float h = smoothBlendRatio(res1.x, res2.x, r);
	#else
	#pragma r:endif
	#pragma r:if THIS_HAS_BLEND_NUMBER
	float n = THIS_Blendnumber;
	#pragma r:endif
	#pragma r:if THIS_HAS_BLEND_OFFSET
	float o = THIS_Blendoffset;
	#pragma r:endif
	COMBINE();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	p = THIS_fold(p);
	Sdf res1 = createSdf(RAYTK_MAX_DIST);
	if (THIS_Enablefaces > 0.5) {
		THIS_combine(res1, createSdf(THIS_D2Planes(p)));
	}
	if (THIS_Enablesegments > 0.5) {
		THIS_combine(res1, createSdf(THIS_D2Segments(p)));
	}
	if (THIS_Enablevertices > 0.5) {
		THIS_combine(res1, THIS_D2Vertices(p, ctx));
	}

	return res1;
}