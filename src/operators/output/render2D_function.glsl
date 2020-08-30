#define thismap inputOp1

vec4 getColor(Sdf res) {
	vec4 color = THIS_Backgroundcolor;
	if (THIS_Enableedge > 0) {
		// TODO: fully implement edge blending / thickness
		color = mix(color, THIS_Edgecolor, 1.0-smoothstep(0.0, THIS_Edgethickness/2.0, abs(res.x)));
	}
	return color;
}