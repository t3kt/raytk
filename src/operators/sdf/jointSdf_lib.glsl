vec4 sdJoint3DSphere( in vec3 p, in float l, in float a, in float w)
{
    
    // if perfectly straight
    if( abs(a)<0.001 ) return vec4( length(p-vec3(0,clamp(p.y,0.0,l),0))-w, p );
    
    // parameters
    vec2  sc = vec2(sin(a),cos(a));
    float ra = 0.5*l/a;
    
    // recenter
    p.x -= ra;
    
    // reflect
    vec2 q = p.xy - 2.0*sc*max(0.0,dot(sc,p.xy));

    float u = abs(ra)-length(q);
    float d2 = (q.y<0.0) ? dot2( q+vec2(ra,0.0) ) : u*u;
    float s = sign(a);
    return vec4( sqrt(d2+p.z*p.z)-w,
                 (p.y>0.0) ? s*u : s*sign(-p.x)*(q.x+ra),
                 (p.y>0.0) ? atan(s*p.y,-s*p.x)*ra : (s*p.x<0.0)?p.y:l-p.y,
                 p.z );
}

vec4 sdJoint3DFlat( in vec3 p, in float l, in float a, in float w)
{
    
    // if perfectly straight
    if( abs(a)<0.001 )
    {
        vec3 q = p; q.y -= 0.5*l;
        q = abs(q) - vec3(w,l*0.5,w);
        return vec4(min(max(q.x,max(q.y,q.z)),0.0) + length(max(q,0.0)),p);
    }
    
    // parameters
    vec2  sc = vec2(sin(a),cos(a));
    float ra = 0.5*l/a;
    
    // recenter
    p.x -= ra;
    
    // reflect
    vec2 q = p.xy - 2.0*sc*max(0.0,dot(sc,p.xy));

	// distance
    float u = abs(ra)-length(q);
    float d = max(length( vec2(q.x+ra-clamp(q.x+ra,-w,w), q.y) )*sign(-q.y),abs(u) - w);

    // parametrization (optional)
    float s = sign(a);
    float v = ra*atan(s*p.y,-s*p.x);
    u = u*s;
    
    // square profile
    q = vec2(d,abs(p.z)-w);
    
    d = min(max(q.x,q.y),0.0) + length(max(q,0.0));

    
    return vec4( d, u, v, p.z );
}