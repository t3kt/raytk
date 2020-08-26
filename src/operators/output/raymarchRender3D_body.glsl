uniform vec3 camPos;
uniform vec3 camRot;
uniform float gridOffset;
uniform float FOV;
uniform int displayGrid;
uniform vec2 enableReflectRefract = vec2(1);


Sdf map(vec3 q)
{
	Sdf res = thismap(q);
	res.x *= 0.5;
	return res;
}

Sdf opU(Sdf d1, Sdf d2){
	return (d1.x<d2.x)? d1:d2;
}

vec3 forwardSF(float i, float n)
{
	float phi = 2.0*PI*fract(i/PHI);
	float zi = 1.0 - (2.0*i+1.0)/n;
	float sinTheta = sqrt(1.0 - zi*zi);
	return vec3(cos(phi)*sinTheta, sin(phi)*sinTheta, zi);
}

float calcAO(in vec3 pos, in vec3 nor, in vec2 pix)
{
	int N = 64;
	float ao = 0.0;
	for (int i=0; i<N; i++)
	{
		vec3 ap = forwardSF(float(i), N);
		ap *= sign(dot(ap, nor)) * hash1(float(i));
		ao += clamp(map(pos + nor*0.05 + ap*0.2).x*float(N), 0.0, 1.0);
	}
	ao /= float(N);

	return clamp(ao*ao, 0.0, 1.0);
}

float calcAO2(in vec3 pos, in vec3 nor, in vec2 pix)
{
	float ao = 0.0;
	for (int i=0; i<32; i++)
	{
		vec3 ap = forwardSF(float(i), 32.0);
		ap *= sign(dot(ap, nor)) * hash1(float(i));
		ao += clamp(map(pos + nor*0.05 + ap*0.2).x*100.0, 0.0, 1.0);
	}
	ao /= 32.0;

	return clamp(ao, 0.0, 1.0);
}



vec3 calcNormal(in vec3 pos)
{
	vec2 e = vec2(1.0, -1.0)*0.5773*0.005;
	return normalize(e.xyy*map(pos + e.xyy).x +
	e.yyx*map(pos + e.yyx).x +
	e.yxy*map(pos + e.yxy).x +
	e.xxx*map(pos + e.xxx).x);
}


// http://iquilezles.org/www/articles/checkerfiltering/checkerfiltering.htm
float checkersGradBox(in vec2 p)
{
	// filter kernel
	vec2 w = fwidth(p) + 0.001;
	// analytical integral (box filter)
	vec2 i = 2.0*(abs(fract((p-0.5*w)*0.5)-0.5)-abs(fract((p+0.5*w)*0.5)-0.5))/w;

	// xor pattern
	// return 0.5 - 0.5*i.x*i.y+smoothstep(fract(p.x), 0.0, 0.1)-smoothstep(fract(p.x), 0.2, 1);
	p*= 1.;
	float coarse = step(fract(p.x), 0.55)-step(fract(p.x), 0.5)+step(fract(p.y), 0.55)-step(fract(p.y), 0.5);
	p*= 3;
	float fine = step(fract(p.x), 0.55)-step(fract(p.x), 0.5)+step(fract(p.y), 0.55)-step(fract(p.y), 0.5);

	return coarse+fine*0.5;//step(fract(p.x), 0.55)-step(fract(p.x), 0.5)+step(fract(p.y), 0.55)-step(fract(p.y), 0.5);
}

float castShadow(vec3 ro, vec3 rd, Sdf thisRes){
	float res = 1;
	float t = 0.8;
	vec3 pos = vec3(0);
	Sdf ress;
	for (int i=0;i<50; i++){
		pos = ro + rd*t;
		ress = map(pos);
		float h = ress.x;
		res = min(res, 0.8*h/t);
		// if(t>0.01) break;
		h+=t;
		if (t>10) break;
		if (abs(pos.x)>limitBox.x||abs(pos.y)>limitBox.y||abs(pos.z)>limitBox.z)
		{
			break;
		}

	}
	// pseudo caustics===
	if (ress.refract && !thisRes.refract){
		vec3 n = calcNormal(pos);
		res+=smoothstep(0.3, 0.8, (dot(-rd, n)*0.5));
		res = 0.5-res;
	}

	return clamp(res, 0., 1.);
}

Sdf castRay(in vec3 ro, in vec3 rd, float renderDepth, float prec)
{
	float tmin = 0.1;
	float tmax = min(50.0, renderDepth);
	Sdf result;
	result.x = tmin;
	result.y = -2.0;
	result.material2 = 0;
	result.interpolant = 0;
	result.ior = 1;
	result.refract = false;
	result.reflect = false;
	vec3 pos = vec3(0);
	for (int i=0; i<pow(2, 8); i++)
	{
		float precis = prec*result.x;
		pos = (ro+rd*result.x);
		Sdf res = map(pos);
		if (displayGrid==1){
			res = opU(res, distGrid(pos, gridOffset));// draw distance grid plane
		}
		result.refract = res.refract;
		result.reflect = res.reflect;
		result.material2 = res.material2;
		result.interpolant = res.interpolant;
		result.ior = res.ior;

		if (res.x<precis || result.x>tmax) break;
		result.x += res.x;
		result.y = res.y;
		if (abs(pos.x)>limitBox.x||abs(pos.y)>limitBox.y||abs(pos.z)>limitBox.z)
		{
			result.y = -1;
			break;
		}
	}

	if (result.x>tmax) {
		result.y=-1.0;
		result.refract = false;
		result.reflect = false;
		result.interpolant = 0;
		result.ior = 1;
	}

	return result;
}

vec4 getMat2(float m, MatInputs matIn) {
	vec3 pos = matIn.pos;
	vec3 n = matIn.n;
	vec3 ref = matIn.ref;
	vec3 refraction = matIn.refraction;
	vec3 eye = matIn.eye;
	float occ = matIn.occ;
	float occ2 = matIn.occ2;
	float t = matIn.t;
	vec3 rd = matIn.rd;


	vec4 col = vec4(vec3(0.5), 1);
	vec3 lightPos = lights[0].xyz;
	vec3 sunDir = normalize(lightPos);
	// ======= overlapped 'material', so alpha = 0
	if (m==-2){

		col = vec4(0);
		return col;
	}

	// ========checkerboard material
	if (m==1)
	{

		float f = checkersGradBox((1.0*pos.xz + pos.xy*2)*0.5);
		col.rgb = 0.3 + f*vec3(0.7);//+ smoothstep(fract(f*3), 0.9,1.)*vec3(1);
		Sdf dummy;
		float sunShadow = smoothstep(castShadow(pos+n*0.001, 1*sunDir, dummy), 0.0, 0.05);
		col.rgb *= 0.5+sunShadow*0.5;
	}
	// ========Standard Gray material
	if (m==2){
		vec3 mate = vec3(0.38);
		vec3 sunColor = vec3(5.8, 4.0, 3.5);
		vec3 skyColor = vec3(0.5, 0.8, 0.9);
		float sunDiffuse = clamp(dot(n, sunDir), 0, 1.);
		Sdf dummy;
		float sunShadow = 1-step(castShadow(pos+n*0.001, 1*sunDir, dummy), 0.0);
		float skyDiffuse = clamp(0.5+0.5*dot(n, vec3(0, 1, 0)), 0, 1);
		float sunSpec = pow(max(dot(-rd, n), 0.), 5)*0.5;
		vec3 col = mate *sunColor*sunDiffuse*sunShadow;
		col += mate*skyColor*skyDiffuse;
		col += mate*sunColor*sunSpec;
		col *= mix(vec3(0.5, 0.5, 0.5), vec3(1.0, 1.0, 1.0)*1.5, occ*1.);

		// float distAtten = 1-clamp(length(lightPos-pos)/30, 0,1);
		// vec3 col = vec3 (0.3,0.3,0.3)+vec3(0.3,0.3,0.3)*dot(lightPos, n)*0.6;
		// col *= mix(vec3(0.5,0.5,0.5)*5, vec3(1.0,1.0,1.0), occ*1.);
		// col *= 1.0*mix( vec3(0.3,0.3,0.3), vec3(0.7, 0.7,0.7), occ2*occ2*occ2 );
		// col*=distAtten;
		// col.a = 1;
		return vec4(col, 1);

	}

	// ==========Grid Material
	if (m==10){
		float notGrid = map(pos).x;
		if (notGrid > 0.1){
			vec4 col = vec4(1, 1, 1, 1);
			vec3 lightPos = lights[0].xyz;//vec3(0,3,2);
			vec3 sunDir = normalize(lightPos);
			Sdf dummy;
			float sunShadow = 1-step(castShadow(pos+n*0.001, 1*sunDir, dummy), 0.0);
			col.rgb *= saturate(abs(fract(notGrid*0.5)*1-0.9)*10)*1.3;//vec4(0,1,0,1);
			col.rgb *= 0.5+sunShadow*0.5;
			return col;
		}

	}

	// ===========Additional Material is inserted here===================
	// #include <materialParagraph>
	// ==================================================================
	return col;
}
vec4 getMat(Sdf res, vec3 pos, vec3 n, vec3 ref, vec3 refraction, vec3 eye, float occ, float occ2, float t, vec3 rd){
	float m = res.y;
	MatInputs matIn;
	matIn.res = res;
	matIn.pos = pos;
	matIn.n = n;
	matIn.ref = ref;
	matIn.refraction = refraction;
	matIn.eye = eye;
	matIn.occ = occ;
	matIn.occ2 = occ2;
	matIn.t = t;
	matIn.rd = rd;
	if (res.interpolant==0){
		return getMat2(floor(m), matIn);
	}
	else {
		vec4 c1 = getMat2(m, matIn);
		vec4 c2 = getMat2(res.material2, matIn);
		float k = 1;

		vec4 col = mix(c1, c2, res.interpolant);// - k*res.interpolant*(1.0-res.interpolant);

		return col;
	}
}

float castInside(vec3 ro, vec3 rd){
	float res = 0.1;
	float t = 0.5;
	for (int i=0;i<20; i++){
		vec3 pos = ro + rd*t;
		float h = map(pos).x*-1;

		// res = min(res,0.8*h/t);
		// if(t<0.01) break;
		t+=h;
		res = t;
		// if(t>50) break;
		if (res<0) break;
		if (abs(pos.x)>limitBox.x||abs(pos.y)>limitBox.y||abs(pos.z)>limitBox.z)
		{
			break;
		}

	}
	return res;
}

void main()
{
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st*resolution;
	vec2 p = (-resolution+2.0*fragCoord.xy)/resolution.y;

	vec2 q = vUV.st;
	float renderDepth = texture(sTD2DInputs[0], vUV.st).r;

	//-----------------------------------------------------
	// camera
	//-----------------------------------------------------
	float aspect = resolution.x/resolution.y;
	float screenWidth = 2*(aspect);
	float distanceToScreen = (screenWidth/2)/tan(FOV/2)*1;

	vec3 ro = camPos*1;
	ro.x +=0.0;
	ro.y +=0.;

	vec3 ta = camPos+vec3(0, 0, -1);//camLookAt;

	// camera matrix
	vec3 ww = normalize(ta - ro);
	vec3 uu = normalize(cross(ww, vec3(0.0, 1, 0.0)));
	vec3 vv = normalize(cross(uu, ww));
	// create view ray
	vec3 rd = normalize(p.x*uu + p.y*vv + distanceToScreen*ww) *rotateMatrix(camRot);

	//-----------------------------------------------------
	// render
	//-----------------------------------------------------

	vec3 col = vec3(0.07)*clamp(1.0-length(q-0.5), 0.0, 1.0);
	float alpha = 0;
	// raymarch
	Sdf res = castRay(ro, rd, renderDepth, 0.001);
	float outDepth = min(res.x, renderDepth);
	depthBuffer = TDOutputSwizzle(vec4(outDepth, outDepth, outDepth, 1));

	float t = res.x;
	float mat = res.y;
	if (t>0.0)
	{
		if (mat <= 0){
			vec3 col =  vec3(0);
			// fragColor = TDOutputSwizzle(vec4(col,1));
		}
		else {

			vec3 pos = ro + t*rd;
			vec3 nor = calcNormal(pos);
			vec3 sor = nor;

			float occ = calcAO(pos, nor, fragCoord);
			float occ2 = calcAO2(pos, nor, fragCoord);

			// =============reflections======================
			Sdf resRef = res;
			vec3 colRefl = vec3(0);
			if (enableReflectRefract.x > 0) {
				vec3 posRefl = pos;
				vec3 norRefl = nor;
				vec3 rdRefl = rd;
				// vec3 roRefl
				for (int k=0;k<Reflectionpasses;k++){
					if (res.reflect){
						rdRefl = reflect(rdRefl, norRefl);
						vec3 roRefl = posRefl+norRefl*0.0001;
						// rdRefl = ref;
						resRef = castRay(roRefl, rdRefl, 50, 0.001);
						float tRefl = resRef.x;
						posRefl = roRefl + tRefl*rdRefl;

						norRefl = calcNormal(posRefl);
						colRefl += getMat(resRef, posRefl, norRefl, colRefl, vec3(0), camPos, occ, occ2, tRefl, rdRefl).rgb;
					}
				}
			}
			// ==============================================

			//================Refractions============================
			vec3 refrCol = vec3(0);
			if (enableReflectRefract.y > 0) {
				vec3 firstRd = rd;
				vec3 firstNor = nor;
				vec3 firstPos = pos;
				Sdf resRefr = res;
				float ior = 1;
				for (int i= 0;i<Refractionpasses;i++){
					if (resRefr.refract){
						ior = resRefr.ior;
						vec3 insideRd = refract(firstRd, firstNor, ior);
						float insideDist = castInside(firstPos+firstRd*0.1, insideRd);
						vec3 posRefrOut = firstPos+insideRd*insideDist*1.;
						vec3 norOut = calcNormal(posRefrOut);
						vec3 outSideRd = refract(insideRd, -1*norOut, 1/ior);
						resRefr = castRay(posRefrOut+firstRd*0.05, outSideRd, 70, 0.01*2*i);
						float tRefr = resRefr.x;
						vec3 posFin = posRefrOut+outSideRd*tRefr;
						vec3 norRefr = calcNormal(posFin);
						float travelAtten = clamp(1-tRefr*0.05, 0, 1);
						refrCol += travelAtten*getMat(resRefr, posFin, norRefr, vec3(0), refrCol, camPos, occ, occ2, tRefr, outSideRd).rgb;
						firstPos = posFin;
						firstRd = outSideRd;
						firstNor = norRefr;
					}
				}
				refrCol = vec3(1, 0, 0);
			}
			//=======================================================



			vec4 colA = getMat(res, pos, nor, colRefl, refrCol, camPos, occ, occ2, t, rd);
			col = colA.rgb;
			// col += refrCol;//mix (refrCol, vec3(0.8, 0.1, 0.1), travelAmnt);
			// col.r += abs(insideDist*100);
			// col += posRefrOut;
			alpha = colA.a;
			// float ar = clamp(1.0-0.8*length(q-pos),0.0,1.0);
			// col = mix( col, vec3(2.1,2.0,1.2), ar);
			col  *= 0.3;


			//		=================Shadows============================
			vec3 lightPos = lights[0].xyz;
			vec3 lightDir = 1*normalize(lightPos-pos);
			float shadow = castShadow(pos, lightDir, res)*0.9+0.1;
			//		====================================================

			//        float ks= 0.1;
			// // // lighting
			// float sky = 0.5 + 0.5*nor.y;
			// float fre = clamp( 1.0 + dot(nor,rd), 0.0, 1.0 );
			// float spe = pow(max( dot(-rd,nor),0.0),8.0);
			// // lights
			// vec3 lin  = vec3(0.0);
			//      lin += 3.0*vec3(0.7,0.80,1.00)*sky*occ;
			//      lin += 1.0*fre*vec3(1.2,0.70,0.60)*(0.1+0.9*occ);

			// add shadows======================
			col*=  shadow*3;// something is wrong with this
			//==================================

			// col += 0.3*ks*4.0*vec3(0.7,0.8,1.00)*smoothstep(0.0,0.2,ref.y)*(0.05+0.95*pow(fre,5.0))*(0.5+0.5*nor.y)*occ;
			// col += 4.0*ks*1.5*spe*occ*col.x;
			// col += 2.0*ks*1.0*pow(spe,8.0)*occ*col.x;
			// col = col* lin;
			// dust
			// col = mix( col, 0.2*fre*fre*fre+0.6*vec3(0.6,0.55,0.5)*sky*(0.8+0.4*texCube( sTD2DInputs[0], pos*10.0, nor, 4.0 ).xyz), 0.6*smoothstep(0.3,0.7,nor.y)*sqrt(occ) );

			// col *= 2.6*exp(-0.2*t);
		} }

	col = pow(col, vec3(0.4545));

	col = pow(col, vec3(1.0, 1.0, 1.4)) + vec3(0.0, 0.02, 0.14);

	col += (1.0/255.0)*hash1(fragCoord);




	col *= clamp(alpha, 0, 1);
	// vec4 color = vec4(1.0);
	fragColor = TDOutputSwizzle(vec4(col, alpha));
}
