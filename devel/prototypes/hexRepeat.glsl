// @Radius {"default":0.3, "normMin":0, "normMax":1}
// @Halfspacing {"default":0.3, "normMin":0, "normMax":1}
// @Cornerradius {"default":0.3, "normMin":0, "normMax":1}

vec2 hexagon(vec2 position, float radius, float halfSpacing, float cornerRadius) {
    vec2 s = vec2(sqrt(3.0), 3.0) * (radius + halfSpacing * 2.0 / sqrt(3.0));
    position /= s;    
    vec2 d1 = (fract(position) - 0.5) * s;
    vec2 d2 = (fract(position + 0.5) - 0.5) * s;
    position = dot(d1, d1) < dot(d2, d2) ? d1 : d2;
    position = abs(position);
    position *= 0.5;
    position += vec2(-position.y, position.x) * sqrt(3.0);
    position.x = abs(position.x);
    //position.y -= radius - cornerRadius;
//    position.y -= radius ;
    return position;

}

ReturnT thismap(CoordT p, ContextT ctx) {
	float radius = THIS_Radius;
	float halfSpacing = THIS_Halfspacing;
	float cornerRadius = THIS_Cornerradius;
	halfSpacing = radius * (1.0 - 0.5*sqrt(3.));
	
	p = hexagon(p, radius, halfSpacing, cornerRadius);
	return inputOp1(p, ctx);

}