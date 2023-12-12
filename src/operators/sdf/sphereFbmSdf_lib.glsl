// Sphere FBM by iq
// https://www.shadertoy.com/view/Ws3XWl

float SPHERE_FBM_hash(vec3 p)// replace this by something better
{
	p  = 17.0*fract(p*0.3183099+vec3(.11, .17, .13));
	return fract(p.x*p.y*p.z*(p.x+p.y+p.z));
}

float SPHERE_FBM_rad(float r, float g2) {
	return (r)*(r)*g2;
}

float SPHERE_FBM_lattice(vec3 i, vec3 f, vec3 c, float g2) {
	return length(f-c) - SPHERE_FBM_rad(SPHERE_FBM_hash(i+c), g2);
}

float SPHERE_FBM_simplex(vec3 d, float r, float g2) {
	return length(d) - r*r*g2;
}
