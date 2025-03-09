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

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
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
	return inputOp1(p, ctx);
}