// @Teeth {"default":8, "normMin":0, "normMax":16,"style":"Int"}
// @W {"default":0.5}
#define GEAR_W .27

// https://shaderoo.org/?shader=c7N0Lh

float gear(vec3 p, int numTeeth, float w)
{
    float lpxy=length(p.xy);
    float d=10000.;
    float ang=atan(p.y,p.x);
    d=min(d,length(p+vec3(p.xy/lpxy,0)*.1*sin(ang*float(numTeeth)))-1.);
    d=max(d,abs(p.z)-GEAR_W*w);
    d=max(d,.75-lpxy);
    return d;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float d = gear(p, int(THIS_Teeth), THIS_W);
	return createSdf(d);
}