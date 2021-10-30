vec3 THIS_fold(vec3 pos) {
	for(int i=0;i<5 /*Type*/;i++){
		pos.xy=abs(pos.xy);//fold about xz and yz planes
		pos-=2.*min(0.,dot(pos,THIS_nc))*THIS_nc;//fold about nc plane
	}
	return pos;
}

float THIS_D2Planes(vec3 pos) {//distance to the 3 faces
	pos-=THIS_p;
	float d0=dot(pos,THIS_pab);
	float d1=dot(pos,THIS_pbc);
	float d2=dot(pos,THIS_pca);
	return max(max(d0,d1),d2);
}

float THIS_D2Segments(vec3 pos) {
	pos-=THIS_p;
	float dla=dot2(pos-min(0.,pos.x)*vec3(1.,0.,0.));
	float dlb=dot2(pos-min(0.,pos.y)*vec3(0.,1.,0.));
	float dlc=dot2(pos-min(0.,dot(pos,THIS_nc))*THIS_nc);
	return sqrt(min(min(dla,dlb),dlc))-THIS_Segmentradius;
}

float THIS_D2Vertices(vec3 pos) {
	return length(pos-THIS_p)-THIS_Vertexradius;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	p = THIS_fold(p);
	float d = RAYTK_MAX_DIST;
	if (THIS_Enablefaces > 0.5) {
		d = min(d, THIS_D2Planes(p));
	}
	if (THIS_Enablesegments > 0.5) {
		d = min(d, THIS_D2Segments(p));
	}
	if (THIS_Enablevertices > 0.5) {
		d = min(d, THIS_D2Vertices(p));
	}

	return createSdf(d);
}