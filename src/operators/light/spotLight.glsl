// https://www.shadertoy.com/view/wlcyzf
// https://learnopengl.com/Lighting/Light-casters

Light thismap(CoordT p, LightContext ctx) {
	Light light;
	light.pos = THIS_Position;
	vec3 spotDir = normalize(THIS_Direction);
	float innerCutoffCos = cos(radians(THIS_Coneangle));
	float outerCutoffCos = cos(radians(THIS_Coneangle + THIS_Conedelta));
	vec3 lightDir = light.pos - p;
	float d = length(lightDir);
	lightDir /= d;
	float theta = dot(-lightDir, spotDir);
	float att = clamp((theta - outerCutoffCos) / (innerCutoffCos - outerCutoffCos), 0.0, 1.0);
	light.color = THIS_Color * THIS_Intensity * att;
	return light;
}