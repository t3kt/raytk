uniform vec3 uCamPos;
uniform vec3 uCamRot;  // in radians
uniform float uCamFov;  // in radians
uniform vec3 uLightPos1;
uniform float uUseRenderDepth;


Sdf map(vec3 q)
{
	Sdf res = thismap(q, createDefaultContext());
//	res.x *= 0.5;
	return res;
}

Sdf castRay(Ray ray, float maxDist) {
	float dist = 0;
	Sdf res;
	for (int i = 0; i < MAX_STEPS; i++) {
		vec3 p = ray.pos + ray.dir * dist;
		res = map(p);
		dist += res.x;
		if (dist < SURF_DIST) {
			return res;
		}
		if (dist > maxDist) {
			break;
		}
	}
	res.x = dist;
	return res;
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

// Soft shadow code from http://iquilezles.org/www/articles/rmshadows/rmshadows.htm
float softShadow(vec3 p, MaterialContext matCtx)
{
//	float mint = uShadow.x;
//	float maxt = uShadow.y;
//	float k = uShadow.z;
	float mint = 0.1;
	float maxt = 2.0;
	float k = 0.5;  // hardness
	float res = 1.0;
	float ph = 1e20;
	for (float t=mint; t<maxt;)
	{
		float h = map(p + matCtx.ray.pos*t).x;
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

float calcShadow(in vec3 p, MaterialContext matCtx) {
	vec3 lightVec = normalize(matCtx.lightPos1 - p);
	Ray shadowRay = Ray(p+matCtx.normal * SURF_DIST*2., lightVec);
	float shadowDist = castRay(shadowRay, MAX_DIST).x;
	if (shadowDist < length(matCtx.lightPos1 - p)) {
		return 0.1;
	}
	return 1.0;
}

// compute ambient occlusion value at given position/normal
// Source - https://www.shadertoy.com/view/lsKcDD
float calcAO( in vec3 pos, in vec3 nor )
{
//	float occ = uAO.x;
//	float sca = uAO.y;
	float occ = 0.0;
	float sca = 1.0;
	// int n = int(uAO.z);
	int n = 4;
	for( int i=0; i<n; i++ )
	{
		float hr = 0.01 + 0.12*float(i)/4.0;
		vec3 aopos =  nor * hr + pos;
		Sdf res = map(aopos);
		float dd = res.x;
		occ += -(dd-hr)*sca;
		sca *= 0.95;
	}
	return clamp( 1.0 - 3.0*occ, 0.0, 1.0 );
}

vec3 getColorDefault(vec3 p, MaterialContext matCtx) {
	vec3 color = vec3(0.5);  // ambient color
	color += phongContribForLight(
		vec3(0.5), // diff
		vec3(0.7), // spec
		1.,
		p,
		matCtx.ray.pos,
		matCtx.lightPos1,
		vec3(1),  // light color
		matCtx.normal,
		0  // occlusion
	);
	vec3 lightVec = normalize(matCtx.lightPos1 - p);
	float diffuse = clamp(dot(matCtx.normal, lightVec), 0., 1.);
	color = vec3(diffuse);
//	color *= calcShadow(p, matCtx);
	color *= softShadow(p, matCtx);
	return color;
}

vec3 getColor(vec3 p, MaterialContext matCtx) {
	vec3 col = vec3(0);
	int m = int(matCtx.result.material);
	#ifdef OUTPUT_DEBUG
	debugOut.x = m;
	#endif
	// TODO: material blending

	if (false) {}
	// #include <materialParagraph>

	else {
		col = getColorDefault(p, matCtx);
	}
	return col;
}

#ifndef THIS_USE_CAM_FUNC

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

#endif

void main()
{
	#ifdef OUTPUT_DEBUG
	debugOut = vec4(0);
	#endif
	//-----------------------------------------------------
	// camera
	//-----------------------------------------------------

	Ray ray = getViewRay();
	#ifdef OUTPUT_RAYDIR
	rayDirOut = vec4(ray.dir, 0);
	#endif
	#ifdef OUTPUT_RAYORIGIN
	rayOriginOut = vec4(ray.pos, 0);
	#endif
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

	MaterialContext matCtx;
	matCtx.result = res;
	matCtx.context = createDefaultContext();
	matCtx.lightPos1 = uLightPos1;
	matCtx.ray= ray;

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

		matCtx.normal = calcNormal(p);
		col = getColor(p, matCtx);

		#ifdef OUTPUT_NORMAL
		normalOut = vec4(matCtx.normal, 0);
		#endif
		#ifdef OUTPUT_COLOR
		colorOut = TDOutputSwizzle(vec4(col, 1));
		#endif
		#ifdef OUTPUT_ORBIT
		orbitOut = res.orbit;
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
		#ifdef OUTPUT_ORBIT
		orbitOut = vec4(0);
		#endif
	}
}
