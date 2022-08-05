// @T {"default":0,"normMax":5}

// https://www.shadertoy.com/view/MtBGDG


float cc,ss;

vec4 formula (vec4 p) {
    float t = THIS_T;
    p.y-=t*.25;
    p.y=abs(3.-mod(p.y-t,6.));
    for (int i=0; i<6; i++) {
        p.xyz = abs(p.xyz)-vec3(.0,2.,.0);
        p=p*2./clamp(dot(p.xyz,p.xyz),.3,1.)-vec4(0.5,1.5,0.5,0.);
        p.xz*=mat2(cc,ss,-ss,cc);
    }
    return p;
}
float getDist(vec3 pos)
{
    float t = THIS_T;
    float aa=smoothstep(0.,1.,clamp(cos(t-pos.y*.4)*1.5,0.,1.))*3.14159;
    cc=cos(aa);ss=sin(aa);
    float hid=0.;
    vec3 tpos=pos;
    //tpos.xz=abs(1.5-mod(tpos.xz,3.))-1.5;
    vec4 p=vec4(tpos,1.);
    float y=max(0.,.3-abs(pos.y-3.3))/.3;
    p=formula(p);
    float floor=pos.y-3.7-length(sin(pos.xz*60.))*.01;
    float fr=max(abs(p.z/p.w)-.01,length(p.zx)/p.w-.002);
    float bl=max(abs(p.x/p.w)-.01,length(p.zy)/p.w-.0005);
    fr=smin(bl,fr,.02);
    fr*=.9;
    //float fr=length(p.xyz)/p.w;
    floor-=(length(p.xz)*.005+length(sin(pos*3.+t*5.))*.15);
    floor*=.9;
    float d=smin(floor,fr,.7);
    if (abs(d-floor)<.2) {
        hid=1.;
    }
    vec2 res = vec2(d,hid);
    return res.x;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float d = getDist(p);
	return createSdf(d);
}