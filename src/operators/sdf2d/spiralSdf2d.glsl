// Based on https://www.shadertoy.com/view/3ss3W7#

ReturnT thismap(CoordT p, ContextT ctx) {
	float a = 1.0;  // not sure what this is for
	float b = THIS_Spread;

	//https://swiftcoder.wordpress.com/2010/06/21/logarithmic-spiral-distance-field/
	//# calculate the target radius and theta
	float r = length(p);
	float t = atan(p.y, p.x) + THIS_Rotate;

	//# early exit if the point requested is the origin itself
	//# to avoid taking the logarithm of zero in the next step
	if (r == 0.)
	{
		return createSdf(0.);
	}

	//# calculate the floating point approximation for n
	//# calculate n
	float n = floor((log(r / a) / b - t) / (2.0 * PI));

	//# find the two possible radii for the closest point
	float lower_r = a * exp(b * (t + 2.0 * PI * n));
	float upper_r = lower_r * exp(2.0 * PI * b);

	#ifdef THIS_Useradiuslimit
	float r2 = r - THIS_Radiuslimit;
	#else
	float r2 = -r;
	#endif

	//# return the minimum distance to the target point
	float d =
		max(
			r2,
			(min(abs(upper_r - r), abs(r - lower_r)) - THIS_Thickness)
	);

	return createSdf(d);
}