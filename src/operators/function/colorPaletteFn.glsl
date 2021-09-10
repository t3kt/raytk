// https://iquilezles.org/www/articles/palettes/palettes.htm
// https://github.com/Erkaman/glsl-cos-palette
ReturnT thismap(CoordT p, ContextT ctx) {
	float t = (p - THIS_Phase) / THIS_Period;
	vec3 a = THIS_Color1;
	vec3 b = THIS_Color2;
	vec3 c = THIS_Color3;
	vec3 d = THIS_Color4;
	return vec4(a + b*cos( 6.28318*(c*t+d) ), 1.0);
}