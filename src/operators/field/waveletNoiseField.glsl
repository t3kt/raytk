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
	#ifdef THIS_HAS_INPUT_1
	{
		#if defined(inputOp1_COORD_TYPE_vec2)
		{
			#ifdef THIS_COORD_TYPE_vec2
			z += inputOp1(p, ctx);
			#else
			#error mismatchedCoordType
			#endif
		}
		#elif defined(inputOp1_COORD_TYPE_vec3)
		{
			#ifdef THIS_COORD_TYPE_vec3
			z += inputOp1(p, ctx);
			#else
			#error mismatchedCoordType
			#endif
		}
		#else
		#error invalidCoordType
		#endif
	}
	#endif
	float d=0.,s=1.,m=0., a;
	#if defined(THIS_COORD_TYPE_vec2)
	p -= vec2(THIS_Translate1, THIS_Translate2);
	p /= vec2(THIS_Period1, THIS_Period2);

	for(int i=0; i<THIS_Iterations; i++) {
		vec2 q = p*s, g=fract(floor(q)*vec2(123.34,233.53));
		g += dot(g, g+23.234);
		a = fract(g.x*g.y)*1e3;
		#ifdef THIS_Enablevorticity
		a += z*(mod(g.x+g.y, 2.)-1.); // add vorticity
		#endif
		q = (fract(q)-.5)*mat2(cos(a),-sin(a),sin(a),cos(a));
		d += sin(q.x*10.+z)*smoothstep(.25, .0, dot(q,q))/s;
		p = p*mat2(.54,-.84, .84, .54)+i;
		m += 1./s;
		s *= k;
	}
	#elif defined(THIS_COORD_TYPE_vec3)
	p -= THIS_Translate;
	p /= THIS_Period;

	for(int i=0; i<THIS_Iterations; i++) {
		vec3 q = p*s, g=fract(floor(q)*vec3(123.34,233.53,314.15));
		g += dot(g, g+23.234);
		a = fract(g.x*g.y)*1e3;
		#ifdef THIS_Enablevorticity
		a += z*(mod(g.x+g.y, 2.)-1.); // add vorticity
		#endif
		q = (fract(q)-.5);
		//random rotation in 3d. the +.1 is to fix the rare case that g == vec3(0)
		//https://suricrasia.online/demoscene/functions/#rndrot
		q = THIS_erot(q, normalize(tan(g+.1)), a);
		d += sin(q.x*10.+z)*smoothstep(.25, .0, dot(q,q))/s;
		p = THIS_erot(p,normalize(vec3(-1,1,0)),atan(sqrt(2.)))+i; //rotate along the magic angle
		m += 1./s;
		s *= k;
	}
	#else
	#error invalidCoordType
	#endif

	float val = d/m;
	return (val * THIS_Amplitude) + THIS_Offset;
}