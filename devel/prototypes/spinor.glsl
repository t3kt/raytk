// @Angle {"default":0,"normMax":360}

// https://shaderoo.org/?shader=A3X0e7



float getDist(vec3 p)
{
    float d=10000.;
    //float falloff=clamp(1./(1.+.025*max(0.,dot(p,p))),0.,1.);
    float falloff=1.-(smoothstep(1.,15.,length(p)));
    //float falloff=exp(-dot(p,p)/10./10.);
    
    //float ang=(iMouse.xy/iResolution.xy*PI2).x;
    float ang=radians(THIS_Angle);
    
    // those 3 lines are the core part
    // ...remove them and you'll just have 3 boring sticks and a cube ;-)
    pR(p.xy, -ang);             // globally rotate around z
    pR(p.yz, TAU*.5*falloff);   // locally rotate around x by 180 degrees
    pR(p.xy, ang);              // globally rotate back around z 

    d=min(d,fBox(p,vec3(1)));
    d=min(d,fBox(p,vec3(.1,.8,100)));
    d=min(d,fBox(p,vec3(100,.1,.8)));
    d=min(d,fBox(p,vec3(.8,100,.1)));
    return d;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float d = getDist(p);
	return createSdf(d);
}