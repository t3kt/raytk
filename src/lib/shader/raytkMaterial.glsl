// raytkMaterial.glsl

#ifdef RAYTK_USE_MATERIAL_POS
#define getPosForMaterial(p, mctx)  mctx.materialPos
#else
#define getPosForMaterial(p, mctx)  p
#endif

float getShadedLevel(MaterialContext ctx) {
	#if defined(RAYTK_USE_SHADOW)
	return ctx.shadedLevel;
	#else
	return 1.0;
	#endif
}

bool resultUsesShadow(Sdf res)
{
	#ifdef RAYTK_USE_SHADOW
	return res.useShadow;
	#else
	return false;
	#endif
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

// https://github.com/castano/qshaderedit/blob/d4cb6db3a966e129a3b35f1da5b99c0de1b0ec0f/data/shaders/gooch.glsl
vec3 goochShading(
	vec3 lightDirection,
	vec3 viewDirection,
	vec3 surfaceNormal,
	vec3 coolColor, vec3 warmColor, vec3 baseColor
) {
	vec3 reflectVec = normalize(reflect(-lightDirection, surfaceNormal));
	float NdotL = (dot(lightDirection, surfaceNormal) + 1.0) * 0.5;

	vec3 kcool = min(coolColor + baseColor, 1.0);
	vec3 kwarm = min(warmColor + baseColor, 1.0);
	vec3 kfinal = mix(kwarm, kcool, NdotL);
	float spec = max(dot(normalize(reflectVec), viewDirection), 0.0);
	spec = pow(spec, 32.0);

	vec3 col = min(kfinal + spec, 1.0);

	return col;
}

float attenuateLight(float attenScale, float attenBias, float attenRolloff, float lightDist)
{
	float lightAtten = lightDist * attenScale;
	lightAtten += attenBias;
	lightAtten = clamp(lightAtten, 0.0, 1.0) * 1.57079633;
	lightAtten = sin(lightAtten);
	float finalAtten = pow(lightAtten, attenRolloff);
	return finalAtten;
}
