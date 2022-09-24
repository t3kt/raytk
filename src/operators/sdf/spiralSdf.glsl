// Based on Spiral Tiling by Knightly
// https://www.shadertoy.com/view/ls2GRz

ReturnT thismap(CoordT p, ContextT ctx) {
	switch (int(THIS_Axis)) {
		case 0: p = p.yzx; break;
		case 1: p = p.zxy; break;
		case 2: p = p.xyz; break;
	}
	vec2 c = vec2(THIS_Branches, THIS_Bend);
	float r=length(p.xy);
	vec2 f=vec2(log(r),atan(p.y,p.x))*0.5/PI;//Log-polar coordinates
	float d=f.y*c.x-f.x*c.y;//apply rotation and scaling.
	d=fract(d);//"fold" d to [0,1] interval
	d=(d-0.5)*2.*PI*r/length(c);//(0.5-abs(d-0.5))*2.*PI*r/length(c);
	
	vec2 pp=vec2(d,p.z);
	//float a=20.*sin(3.*iTime)*f.x;//twisting angle
	float a=THIS_Twist*f.x;
	mat2 m=mat2(vec2(cos(a),-sin(a)), vec2(sin(a),cos(a)));
	pp=m*pp;//apply twist
	pp=abs(pp);
	ReturnT res;
	#if defined(inputOp_crossSection_RETURN_TYPE_Sdf)
	res = inputOp_crossSection(pp.xy, ctx);
	#elif defined(inputOp_crossSection_RETURN_float)
	res = createSdf(0.9 * (inputOp_crossSection(pp.xy, ctx) - THIS_Thickness));
	#else
	float e = THIS_Exponent;//superquadric param
	float d1= 0.9*(pow(pow(pp.x,e)+pow(pp.y,e),1./e)-THIS_Thickness*r);//distance have to be scaled down because this is just an approximation.
	res = createSdf(d1);
	#endif
	return res;
}