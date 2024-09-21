ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) return ReturnT(0.);

	float depth = ctx.result.x / RAYTK_MAX_DIST;
	vec3 n = ctx.normal;
	vec3 lightDir = normalize(p - ctx.light.pos);

	// TODO: option to use local normal based on camera position and up vector
	vec3 dx = dFdx(n);
	vec3 dy = dFdy(n);
	vec3 xneg = n - dx;
	vec3 xpos = n + dx;
	vec3 yneg = n - dy;
	vec3 ypos = n + dy;
	float curvature = (cross(xneg, xpos).y - cross(yneg, ypos).x) * 2.0 / (depth*5.);




	vec3 ambient = vec3(0.);
	vec3 diffuse = vec3(0.);
	vec3 specular = vec3(0.);
	float shininess = THIS_Shininess;

	shininess *= 60.0;

	// Curvature
	ambient = vec3(curvature + 0.5);
	diffuse = vec3(0.);
	specular = vec3(0.);
//	shininess = 0.;

	// Metal
	float corrosion = clamp(-curvature * 3.0, 0.0, 1.0);
	float shine = clamp(curvature * 5.0, 0.0, 1.0);
	ambient = vec3(0.15, 0.1, 0.1) * .5;
	diffuse = mix(mix(vec3(0.3, 0.25, 0.2), vec3(0.45, 0.5, 0.5), corrosion), vec3(0.5, 0.4, 0.3), shine) - ambient;
	specular = mix(vec3(0.), vec3(1.) - ambient - diffuse, shine);
//	shininess = 128.;

	// Red wax
	float dirt = clamp(0.25 - curvature * 4.0, 0., 1.);
	ambient = vec3(0.05, 0.015, 0.0);
	diffuse = mix(vec3(0.4, 0.15, 0.1), vec3(0.4, 0.3, 0.3), dirt) - ambient;
	specular = mix(vec3(0.15) - ambient, vec3(0.0), dirt);
//	shininess = 32.0;




	float cosAngle = dot(n, lightDir);
	vec3 col = ambient +
		diffuse * max(0., cosAngle) +
		specular * pow(max(0., cosAngle), shininess);
	col = pow(col * 1.5, vec3(.9));
	if (depth >.9) col = vec3(.125);

	ReturnT res = ReturnT(col, 1.);

	return res;
}