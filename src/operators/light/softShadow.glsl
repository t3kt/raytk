// Soft shadow code from http://iquilezles.org/www/articles/rmshadows/rmshadows.htm
float thismap(vec3 p, MaterialContext ctx) {
//	float mint = uShadow.x;
//	float maxt = uShadow.y;
//	float k = uShadow.z;
	float mint = THIS_Mindist; // not sure if "t" actually means distance...
	float maxt = THIS_Maxdist;
	float k = THIS_Hardness;
	float res = 1.0;
//	float ph = 1e20;
	// Something about this is very broken
	for (float t=mint; t<maxt;)
	{
		float h = map(p + ctx.light.pos*t).x;
		if (h<0.001)
		return 0.0;
		res = min(res, k*h/t);
//		float y = h*h/(2.0*ph);
//		float d = sqrt(h*h-y*y);
//		res = min(res, k*d/max(0.0, t-y));
//		ph = h;
		t += h;
	}
	return res;
}

