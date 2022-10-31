// 2D version by Martijn Steinrucken / BigWIngs
// https://www.shadertoy.com/view/wsBfzK
//
// 3D version by Blackle Mori
// https://www.shadertoy.com/view/tlBczy

vec3 THIS_erot(vec3 p, vec3 ax, float ro) {
	return mix(dot(p,ax)*ax,p,cos(ro))+sin(ro)*cross(ax,p);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float k = 1/ (THIS_Scalefactor==0.?0.00001:THIS_Scalefactor);
	float z = THIS_Phase * k;
	#ifdef THIS_HAS_INPUT_phaseField
	z += inputOp_phaseField(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_coordField
	p = THIS_asCoordT(inputOp_coordField(p, ctx));
	#endif
	float d=0.,s=1.,m=0., a;
	p -= THIS_asCoordT(THIS_Translate);
	p /= THIS_asCoordT(THIS_Period);
	CoordT seed = THIS_asCoordT(vec3(123.34,233.53,314.15));
	for(int i=0; i<THIS_Iterations; i++) {
		CoordT q = p*s, g=fract(floor(q)*seed);
		g += dot(g, g+23.234);
		a = fract(g.x*g.y)*1e3;
		if (IS_TRUE(THIS_Enablevorticity)) {
			a += z*(mod(g.x+g.y, 2.)-1.);// add vorticity
		}
		q = (fract(q)-.5);
	#if defined(THIS_COORD_TYPE_vec2)
		q *= rotateMatrix2d(a);
		d += sin(q.x*10.+z)*smoothstep(.25, .0, dot(q,q))/s;
		p = p*mat2(.54,-.84, .84, .54)+i;
	#elif defined(THIS_COORD_TYPE_vec3)
		//random rotation in 3d. the +.1 is to fix the rare case that g == vec3(0)
		//https://suricrasia.online/demoscene/functions/#rndrot
		q = THIS_erot(q, normalize(tan(g+.1)), a);
		d += sin(q.x*10.+z)*smoothstep(.25, .0, dot(q,q))/s;
		p = THIS_erot(p,normalize(vec3(-1,1,0)),atan(sqrt(2.)))+i; //rotate along the magic angle
	#else
	#error invalidCoordType
	#endif
		m += 1./s;
		s *= k;
	}

	float val = d/m;
	return (val * THIS_Amplitude) + THIS_Offset;
}