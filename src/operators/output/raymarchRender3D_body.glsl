uniform vec3 uCamPos;
uniform vec3 uCamRot;  // in radians
uniform float uCamFov;  // in radians
uniform vec3 uLightPos1;
uniform float uUseRenderDepth;

#define MAX_STEPS 100
#define MAX_DIST 100.0
#define SURF_DIST 0.01

Sdf map(vec3 q)
{
	Sdf res = thismap(q, createDefaultContext());
//	res.x *= 0.5;
	return res;
}

Sdf castRay(Ray ray, float maxDist) {
	float dist = 0;
	for (int i = 0; i < MAX_STEPS; i++) {
		vec3 p = ray.pos + ray.dir * dist;
		Sdf res = map(p);
		dist += res.x;
		if (dist < SURF_DIST) {
			return res;
		}
		if (dist > maxDist) {
			break;
		}
	}
	return createSdf(dist);
}

vec3 calcNormal(in vec3 pos)
{
	vec2 e = vec2(1.0, -1.0)*0.5773*0.005;
	return normalize(
		e.xyy*map(pos + e.xyy).x +
		e.yyx*map(pos + e.yyx).x +
		e.yxy*map(pos + e.yxy).x +
		e.xxx*map(pos + e.xxx).x);
}

float getLight(vec3 p) {
	vec3 lightPos = uLightPos1;
	vec3 lightVec = normalize(lightPos - p);
	vec3 n = calcNormal(p);

	#ifdef OUTPUT_NORMAL
	normalOut = vec4(n, 0);
	#endif

	float diffuse = clamp(dot(n, lightVec), 0., 1.);

	Ray shadowRay = Ray(p+n * SURF_DIST*2., lightVec);
	float shadowDist = castRay(shadowRay, MAX_DIST).x;
	if (shadowDist < length(lightPos - p)) {
		diffuse *= .1;
	}

	return diffuse;
}

Ray getViewRay() {
	vec3 pos = uCamPos;
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st*resolution;
	vec2 p = (-resolution+2.0*fragCoord.xy)/resolution.y;

	float aspect = resolution.x/resolution.y;
	float screenWidth = 2*(aspect);
	float distanceToScreen = (screenWidth/2)/tan(uCamFov/2)*1;

	vec3 ro = pos*1;
	ro.x +=0.0;
	ro.y +=0.;

	vec3 ta = pos+vec3(0, 0, -1);//camLookAt;

	// camera matrix
	vec3 ww = normalize(ta - ro);
	vec3 uu = normalize(cross(ww, vec3(0.0, 1, 0.0)));
	vec3 vv = normalize(cross(uu, ww));
	// create view ray
	vec3 rd = normalize(p.x*uu + p.y*vv + distanceToScreen*ww) *rotateMatrix(uCamRot);
	return Ray(pos, rd);
}

void main()
{
	//-----------------------------------------------------
	// camera
	//-----------------------------------------------------

	Ray ray = getViewRay();
	//-----------------------------------------------------
	// render
	//-----------------------------------------------------

	float renderDepth = uUseRenderDepth > 0 ? min(texture(sTD2DInputs[0], vUV.st).r, MAX_DIST) : MAX_DIST;

	vec3 col = vec3(0);
	// raymarch
	Sdf res = castRay(ray, renderDepth);
	float outDepth = min(res.x, renderDepth);
	#ifdef OUTPUT_DEPTH
	depthOut = TDOutputSwizzle(vec4(vec3(outDepth), 1));
	#endif

	if (res.x > 0.0 && res.x < renderDepth) {
		vec3 p = ray.pos + ray.dir * res.x;
		#ifdef OUTPUT_WORLDPOS
		worldPosOut = vec4(p, 1);
		#endif

		#ifdef OUTPUT_SDF
		sdfOut = TDOutputSwizzle(vec4(res.x, res.x, res.x, 1));
		#endif
//		#ifdef OUTPUT_DEPTH
	//	depthOut = TDOutputSwizzle(vec4(vec3(min(res.x, renderDepth)), 1));
		//depthOut = TDOutputSwizzle(vec4(vec3(res.x)))
//		#endif

		float diffuse = getLight(p);
		col = vec3(diffuse);

		#ifdef OUTPUT_COLOR
		colorOut = TDOutputSwizzle(vec4(col, 1));
		#endif
	} else {
		#ifdef OUTPUT_WORLDPOS
//		worldPosOut = vec4(ray.pos + ray.dir * outDepth, 0);
		worldPosOut = vec4(0);
		#endif
		#ifdef OUTPUT_SDF
		sdfOut = vec4(0);
		#endif
		#ifdef OUTPUT_COLOR
		colorOut = vec4(0);
		#endif
		#ifdef OUTPUT_NORMAL
		normalOut = vec4(0);
		#endif
	}

}
