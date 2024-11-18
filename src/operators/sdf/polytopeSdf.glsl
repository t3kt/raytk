// Regular 4D Polytopes by Syntopia
// https://www.shadertoy.com/view/XdfGW4

vec4 THIS_fold(vec4 pos) {
	int type = int(THIS_Type);
	if (type == 3) {
		for (int i=0;i<3;i++) {
			pos.xy=abs(pos.xy);
			float t=-2.*min(0.,dot(pos,THIS_nc)); pos+=t*THIS_nc;
			t=-2.*min(0.,dot(pos,THIS_nd)); pos+=t*THIS_nd;
		}
	} else if (type == 4) {
		for(int i=0;i<8;i++){
			pos.xy=abs(pos.xy);
			float t=-2.*min(0.,dot(pos,THIS_nc)); pos+=t*THIS_nc;
			t=-2.*min(0.,dot(pos,THIS_nd)); pos+=t*THIS_nd;
		}
	} else if (type == 5) {
		for(int i=0;i<15;i++){
			pos.xy=abs(pos.xy);
			float t=-2.*min(0.,dot(pos,THIS_nc)); pos+=t*THIS_nc;
			t=-2.*min(0.,dot(pos,THIS_nd)); pos+=t*THIS_nd;
		}
	}

	return pos;
}

float THIS_D2Vertex(vec4 z, float r, float size) {
	float ca=dot(z,THIS_p), sa=0.5*length(THIS_p-z)*length(THIS_p+z);//sqrt(1.-ca*ca);//
	return pto_DD(ca,sa,r)-size;
}
float THIS_D2Segment(vec4 z, vec4 n, float r, float size){
	//pmin is the orthogonal projection of z onto the plane defined by p and n
	//then pmin is projected onto the unit sphere
	float zn=dot(z,n),zp=dot(z,THIS_p),np=dot(n,THIS_p);
	float alpha=zp-zn*np, beta=zn-zp*np;
	vec4 pmin=normalize(alpha*THIS_p+min(0.,beta)*n);
	//ca and sa are the cosine and sine of the angle between z and pmin. This is the spherical distance.
	float ca=dot(z,pmin), sa=0.5*length(pmin-z)*length(pmin+z);//sqrt(1.-ca*ca);//
	return pto_DD(ca,sa,r)-size;
}

float THIS_D2Segments(vec4 z, float r, float size) {
	float da=THIS_D2Segment(z, vec4(1.,0.,0.,0.), r, size);
	float db=THIS_D2Segment(z, vec4(0.,1.,0.,0.), r, size);
	float dc=THIS_D2Segment(z, THIS_nc, r, size);
	float dd=THIS_D2Segment(z, THIS_nd, r, size);

	return min(min(da,db),min(dc,dd));
}

void THIS_combine(inout Sdf res1, in Sdf res2, in CoordT p, in ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	p.xyz = p.zyx;
	float r = length(p);
	vec4 z4 = vec4(2.*p, 1.-r*r)*1./(1.+r*r);// inverse steroegraphic projection
	float aa = 0.0; // not sure what this is for
	z4.xyw *= TDRotateOnAxis(aa, vec3(0.0,1.0,0.1));
	z4 = THIS_fold(z4);

	Sdf res1 = createSdf(RAYTK_MAX_DIST);

	if (IS_TRUE(THIS_Enablesegments)) {
		#ifdef THIS_HAS_INPUT_segmentSizeField
		float sSize = adaptAsFloat(inputOp_segmentSizeField(p0, ctx));
		#else
		float sSize = THIS_Segmentsize;
		#endif
		sSize *= 0.5;
		THIS_combine(res1, createSdf(THIS_D2Segments(z4, r, sSize)), p, ctx);
	}

	if (IS_TRUE(THIS_Enablevertices)) {
		#ifdef THIS_HAS_INPUT_vertexSizeField
		float vSize = adaptAsFloat(inputOp_vertexSizeField(p0, ctx));
		#else
		float vSize = THIS_Vertexsize;
		#endif
		THIS_combine(res1, createSdf(THIS_D2Vertex(z4, r, vSize)), p, ctx);
	}

	return res1;
}