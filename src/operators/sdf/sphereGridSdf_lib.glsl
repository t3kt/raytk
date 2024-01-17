// latitudes and longitudes (jt)
// https://www.shadertoy.com/view/DlVBzy

float longitudes(vec3 p, float n, float r) // https://www.shadertoy.com/view/DlVBzy latitudes and longitudes (jt)
{
	n = 2.0*round(n); // n must be be integer for exact sdf!
	float slice = 2.0*PI/n;

	float mu = atan(p.x,p.y);
	float mu0 = floor(mu/slice)*slice;
	float mu1 =  ceil(mu/slice)*slice;
	mat3 m0 = mat3(sin(mu0),cos(mu0),0,cos(mu0),-sin(mu0),0,0,0,1);
	mat3 m1 = mat3(sin(mu1),cos(mu1),0,cos(mu1),-sin(mu1),0,0,0,1);

	vec3 q0 = m0 * p;
	vec3 q1 = m1 * p;

	return min(length(vec2(length(q0.xz)-r, q0.y)),length(vec2(length(q1.xz)-r, q1.y)));
}
float latitudes(vec2 p, float n, float r) // https://www.shadertoy.com/view/DlVBzy latitudes and longitudes (jt)
{
	n = 2.0*round(n); // tested for integers (use fractions at your own risk!)

	float slice = 2.0*PI/n;

	float mu = atan(p.x,p.y);
	float mu0 = floor(mu/slice)*slice;
	float mu1 =  ceil(mu/slice)*slice;
	vec2 c0 = vec2(sin(mu0),cos(mu0))*r;
	vec2 c1 = vec2(sin(mu1),cos(mu1))*r;

	return min(length(p-c0),length(p-c1));
}

float latitudes(vec3 p, float n, float r)
{
	return latitudes(vec2(length(p.xy),p.z), n, r);
}
