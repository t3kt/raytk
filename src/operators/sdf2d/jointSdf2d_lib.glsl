// https://www.shadertoy.com/view/WldGWM

vec3 sdJoint2DSphere( in vec2 p, in float l, in float a, float w)
{
    // if perfectly straight
    if( abs(a)<0.001 )
    {
        float v = p.y;
        p.y -= clamp(p.y,0.0,l);
		return vec3( length(p), p.x, v );
    }
    
    // parameters
    vec2  sc = vec2(sin(a),cos(a));
    float ra = 0.5*l/a;
    
    // recenter
    p.x -= ra;
    
    // reflect
    vec2 q = p - 2.0*sc*max(0.0,dot(sc,p));

	// distance
    float u = abs(ra)-length(q);
    float d = (q.y<0.0) ? length( q+vec2(ra,0.0) ) : abs(u);

    // parametrization (optional)
    float s = sign(a);
    float v = ra*atan(s*p.y,-s*p.x);
    u = u*s;
    if( v<0.0 )
    {
        if( s*p.x>0.0 ) { v = abs(ra)*6.283185 + v; }
        else { v = p.y; u = q.x + ra; }
    }
    
    return vec3( d-w, u, v );
}

vec3 sdJoint2DFlat( in vec2 p, in float l, in float a, float w)
{
    // if perfectly straight
    if( abs(a)<0.001 )
    {
        float v = p.y;
        p.y -= clamp(p.y,0.0,l);
        // TODO: this isn't quite right
		return vec3( fBox2(p-vec2(0, l*.5), vec2(w, l)), p.x, v );
    }
    
    // parameters
    vec2  sc = vec2(sin(a),cos(a));
    float ra = 0.5*l/a;
    
    // recenter
    p.x -= ra;
    
    // reflect
    vec2 q = p - 2.0*sc*max(0.0,dot(sc,p));

	// distance
    float u = abs(ra)-length(q);
    float d = max(length( vec2(q.x+ra-clamp(q.x+ra,-w,w), q.y) )*sign(-q.y),abs(u) - w);

    // parametrization (optional)
    float s = sign(a);
    float v = ra*atan(s*p.y,-s*p.x);
    u = u*s;
    
    return vec3( d, u, v );
}