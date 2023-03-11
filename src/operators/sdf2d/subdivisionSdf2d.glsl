// https://www.shadertoy.com/view/stdGz4
// Fully Animated Subdivision

float THIS_h11 (float a) { return fract(sin((a)*12.9898)*43758.5453123); }

ReturnT thismap(CoordT p, ContextT ctx) {
	float ITERS = THIS_Iterations;
	vec2 dMin = vec2(-0.5);
	vec2 dMax = vec2(0.5);
	dMax = THIS_Size * 0.5;
	dMin = -dMax;
//	dMin.x*=R.x/R.y;
//	dMax.x*=R.x/R.y;
	vec2 dim = dMax - dMin;
	float id = 0.;
	float seed = 0.4;
	float MIN_SIZE = 0.01;
	float MIN_ITERS = 1.;

	float t = THIS_Patternshift;

	//BIG THANKS to @0b5vr for letting me use his cleaner subdiv implementation
	//https://www.shadertoy.com/view/NsKGDy
	vec2 diff2 = vec2(1);
	for(float i = 0.;i<ITERS;i++){

		// divide the box into quads
		//Big thanks to @SnoopethDuckDuck for telling me about tanh(sin(x)*a)
		vec2 divHash=tanh(vec2(sin(t*PI/3.+id+i*t*0.05),cos(t*PI/3.+THIS_h11(id)*100.+i*t*0.05))*7.)*0.35+0.5;

		//Less agressive animation
		//divHash=vec2(sin(t*PI/3.+id),cos(t*PI/3.+THIS_h11(id)*100.))*0.5+0.5;

//		if(iMouse.z>0.5){
//			divHash = mix(divHash,M,0.3);
//		}

		vec2 divide = divHash * dim + dMin;

		//Clamp division line
		divide = clamp(divide, dMin + MIN_SIZE+0.01, dMax - MIN_SIZE-0.01);

		//Find the minimum dimension size
		vec2 minAxis = min(abs(dMin - divide), abs(dMax - divide));
		float minSize = min( minAxis.x, minAxis.y);

		//if minimum dimension is too small break out
		bool smallEnough = minSize < MIN_SIZE;
		if (smallEnough && i + 1. > MIN_ITERS) { break; }

		// update the box domain
		dMax = mix( dMax, divide, step( p, divide ));
		dMin = mix( divide, dMin, step( p, divide ));

		//Deterministic seeding for future divisions
		diff2 =step( p, divide)-
		vec2(THIS_h11(diff2.x)*10.,THIS_h11(diff2.y)*10.);

		// id will be used for coloring
		id = length(diff2)*100.0;

		// recalculate the dimension
		dim = dMax - dMin;
	}

	vec2 center = (dMin + dMax)/2.0;

	#ifdef THIS_EXPOSE_cellsize
	THIS_cellsize = dim;
	#endif
	#ifdef THIS_EXPOSE_cellid
	THIS_cellid = id/100.;
	#endif

	Sdf res;
	#ifdef THIS_HAS_INPUT_shape
	res = inputOp_shape(p-center, ctx);
	#else
	float d = fBox2(p-center,dim*0.5);
	//d = length(p-center)-min(dim.x,dim.y)*0.5;
	res = createSdf(d);
	#endif

	return res;
}