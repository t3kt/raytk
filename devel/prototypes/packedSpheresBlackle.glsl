// @Density {"default":0.4, "normMin":0, "normMax":1}
// @Shapemix {"default":0, "normMin": -0.2, "normMax":0.2}

vec3 erot(vec3 p, vec3 ax, float ro) {
	return mix(dot(p, ax)*ax, p, cos(ro))+sin(ro)*cross(ax, p);
}

//the following functions assume that p is inside the cube of radius 1 centered at the origin
//closest vertex of the cube to p
vec3 vertex(vec3 p) {
	return max(sign(p), vec3(0))*2.-1.;
}
//closest face of the cube to p
vec3 face(vec3 p) {
	vec3 ap = abs(p);
	if (ap.x>=max(ap.z, ap.y)) return vec3(sign(p.x), 0., 0.);
	if (ap.y>=max(ap.z, ap.x)) return vec3(0., sign(p.y), 0.);
	if (ap.z>=max(ap.x, ap.y)) return vec3(0., 0., sign(p.z));
	return vec3(0);
}
//closest edge of the cube to p
vec3 edge(vec3 p) {
	vec3 mask = vec3(1)-abs(face(p));
	vec3 v = vertex(p);
	vec3 a = v*mask.zxy, b = v*mask.yzx;
	return distance(p, a)<distance(p, b)?a:b;
}

float hills(vec3 p) {
	return sin(2.*dot(sin(p.xy/16.), cos(p.xy/4.)))*3.;
}

float super(vec3 p) {
	return sqrt(length(p*p));
}

//rhombic dodecahedron SDF with rounded corners
float rho_dod(vec3 p)
{
	float offset = 0.1;
	float radius = .9;
	p = sqrt(p*p+offset*offset/2.);
	p = (p+p.yzx)-radius;
	return super(max(p, 0.))+min(0., max(p.x, max(p.y, p.z)))-offset;
}

float spheres(vec3 p, out vec3 id, out vec3 loc, float density, float shapeMix) {
	vec3 op = p;
	id = floor(p)+.5;
	vec3 d = face(p-id);
	vec3 m = sign(mod(id, 2.)-1.);
	if (m.x*m.y*m.z<0.) id += d;
	if (id.z + hills(id) > -5.) { //if this ball is absent, get the distance to its neighbour
		vec3 e = edge(p-id);
		id += e;
	}
	p -= id;
	float rad = 0.7;
	float sph = mix(rho_dod(p), length(p)-.7, smoothstep(-.2, .2, shapeMix));
	loc = p;
	return max((op.z+3.5+hills(op))/2., sph);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 id;
	vec3 loc;
	float density = THIS_Density;
	float shapeMix = THIS_Shapemix;

	float d = spheres(p, id, loc, density, shapeMix);

	return createSdf(d);
}