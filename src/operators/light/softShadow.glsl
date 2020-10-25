// Soft shadow code from http://iquilezles.org/www/articles/rmshadows/rmshadows.htm
float thismap(vec3 p, MaterialContext ctx) {
	float mint = THIS_MIN_DIST;
	float maxt = THIS_MAX_DIST;
	float k = THIS_Hardness;
	Ray ray = Ray(p + ctx.normal + RAYTK_SURF_DIST*2., normalize(ctx.light.pos - p));
	float res = 1.0;
	float ph = 1e20;
	for (float t=mint; t<maxt;)
	{
		float h = map(ray.pos + ray.dir *t).x;
		if (h<0.001)
		return 0.0;
		float y = h*h/(2.0*ph);
		float d = sqrt(h*h-y*y);
		res = min(res, k*d/max(0.0, t-y));
		ph = h;
		t += h;
	}
	return res;
}

