// @Density {"default":0.35, "normMin":0, "normMax":1}
// @Thickness {"default": 0.2, "normMin":0, "normMax":1}
// @Radius {"default": 1, "normMin":0, "normMax":2}
// @Scale {"default": 5, "normMax":8}

// Jungle Gym by blackle
// https://www.shadertoy.com/view/tsjfRw

//CC0 1.0 Universal https://creativecommons.org/publicdomain/zero/1.0/
//To the extent possible under law, Blackle Mori has waived all copyright and related or neighboring rights to this work.

//percentage of domains filled
//#define DENSITY 0.35

//returns a vector pointing in the direction of the closest neighbouring cell
vec3 quadrant(vec3 p) {
	vec3 ap = abs(p);
	if (ap.x >= max(ap.y, ap.z)) return vec3(sign(p.x),0.,0.);
	if (ap.y >= max(ap.x, ap.z)) return vec3(0.,sign(p.y),0.);
	if (ap.z >= max(ap.x, ap.y)) return vec3(0.,0.,sign(p.z));
	return vec3(0);
}

float hash(float a, float b) {
	return fract(sin(a*1.2664745 + b*.9560333 + 3.) * 14958.5453);
}

bool domain_enabled(vec3 id) {
	//repeat random number along z axis so every active cell has at least one active neighbour
	id.z = floor(id.z/2.);
	return hash(id.x, hash(id.y, id.z)) < THIS_Density;
}

float linedist(vec3 p, vec3 a, vec3 b) {
	float k = dot(p-a,b-a)/dot(b-a,b-a);
	return distance(p, mix(a,b,clamp(k,0.,1.)));
}

float ball;
float scene(vec3 p) {
	float scale = THIS_Scale;
	vec3 id = floor(p/scale);
	p = (fract(p/scale)-.5)*scale;
	if (!domain_enabled(id)) {
		//return distance to sphere in adjacent domain
		p = abs(p);
		if (p.x > p.y) p.xy = p.yx;
		if (p.y > p.z) p.yz = p.zy;
		if (p.x > p.y) p.xy = p.yx;
		p.z -= scale;
		return length(p)-THIS_Radius;
	}
	float dist = length(p)-THIS_Radius;
	ball = dist;
	vec3 quad = quadrant(p);
	if (domain_enabled(id+quad)) {
		//add pipe
		float pipe = linedist(p, vec3(0), quad*scale)-THIS_Thickness;
		dist = min(dist, pipe);
	}
	return dist;
}

/*
vec3 erot(vec3 p, vec3 ax, float ro) {
	return mix(dot(ax,p)*ax, p, cos(ro)) + sin(ro)*cross(ax,p);
}

vec3 srgb(float r, float g, float b) {
	return vec3(r*r,g*g,b*b);
}

float smoothstairs(float p, float scale) {
	p *= scale;
	p = smoothstep(0.9, 1., fract(p)) + floor(p);
	return p/scale;
}

const float PI = acos(-1.);
vec3 pixel_color(vec2 uv) {
	vec2 mouse = (iMouse.xy-0.5*iResolution.xy)/iResolution.y;
	vec3 cam = normalize(vec3(1,uv));
	vec3 init = vec3(iTime,0,0);

	float yrot = 0.;
	float zrot = 0.;
	if (iMouse.z > 0.) {
		yrot += smoothstep(-PI/2., PI/2., -4.*mouse.y)*PI-PI/2.;
		zrot += 4.*mouse.x;
	} else {
		yrot += cos(iTime*.2)*.6;
		zrot += sin(iTime*.2)*.6;
	}
	cam = erot(cam, vec3(0,1,0), yrot);
	cam = erot(cam, vec3(0,0,1), zrot);

	vec3 p = init;
	bool hit = false;
	bool triggered = false;
	bool outline = false;
	bool type = false;
	float dist;
	//ray marching
	for (int i = 0; i < 150 && !hit; i++) {
		dist = scene(p);
		float outline_radius = 0.1*sqrt(distance(p,init))/3.;
		if (dist < outline_radius*.9 && !triggered) {
			triggered = true;
			type = dist == ball;
		}
		if (triggered) {
			float line = (outline_radius-dist);
			outline = line < dist || type != (dist == ball);
			dist = min(line, dist);
		}
		hit = dist*dist < 1e-6;
		p+=dist*cam;
		if (distance(p,init)>90.) break;
	}
	if (!hit) return vec3(0.4);
	bool is_ball = dist == ball;
	vec3 n = norm(p);
	vec3 r = reflect(cam, n);

	//add outline to sharp edges
	outline = outline || scene(p+n*.1) < 0.09;
	float fog = smoothstep(80.,60., distance(p,init));

	//shading
	float ao = smoothstep(.0, .5, scene(p+n*.5));
	float fact = ao*length(sin(r*vec3(3.,-2.,2.))*.5+.5)/sqrt(3.);
	float lod = smoothstep(90.,50.,distance(p,init))*5.; //make the shading simpler in the distance
	fact = smoothstairs(fact, lod)+.1;
	vec3 ballcol = abs(erot(srgb(0.6,0.7,0.8), normalize(cos(p*.5)), .3));
	vec3 matcol = is_ball ? ballcol : srgb(0.6,0.65,0.7);
	vec3 col = matcol*fact + mix(vec3(1), matcol, .4)*pow(fact, 10.)*1.5;
	col *= smoothstep(0.,.25,abs(dot(cam, n)));
	col = mix(vec3(.6), outline ? vec3(0.) : col, fog);
	if (isnan(length(col))) return vec3(.6); //i have no idea where this nan is coming from
	return col;
}

vec2 weyl_2d(int n) {
	return fract(vec2(n*12664745, n*9560333)/exp2(24.));
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	vec2 uv = (fragCoord-.5*iResolution.xy)/iResolution.y;
	fragColor = vec4(0);
	for (int i = 0; i < AA_SAMPLES; i++) {
		vec2 uv2 = uv + weyl_2d(i)/iResolution.y*1.25;
		fragColor += vec4(pixel_color(uv2), 1.);
	}
	fragColor.xyz = sqrt(fragColor.xyz/fragColor.w);
}
*/

ReturnT thismap(CoordT p, Context ctx) {
	float d = scene(p);
	return createSdf(d);
}