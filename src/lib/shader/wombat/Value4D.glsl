//
//  Wombat
//  An efficient texture-free GLSL procedural noise library
//  Source: https://github.com/BrianSharpe/Wombat
//  Derived from: https://github.com/BrianSharpe/GPU-Noise-Lib
//
//  I'm not one for copyrights.  Use the code however you wish.
//  All I ask is that credit be given back to the blog or myself when appropriate.
//  And also to let me know if you come up with any changes, improvements, thoughts or interesting uses for this stuff. :)
//  Thanks!
//
//  Brian Sharpe
//  brisharpe CIRCLE_A yahoo DOT com
//  http://briansharpe.wordpress.com
//  https://github.com/BrianSharpe
//

//
//	Value Noise 4D
//	Return value range of 0.0->1.0
//
float Value4D( vec4 P )
{
    //  https://github.com/BrianSharpe/Wombat/blob/master/Value4D.glsl

    // establish our grid cell and unit position
    vec4 Pi = floor(P);
    vec4 Pf = P - Pi;

    // clamp the domain
    Pi = Pi - floor(Pi * ( 1.0 / 69.0 )) * 69.0;
    vec4 Pi_inc1 = step( Pi, vec4( 69.0 - 1.5 ) ) * ( Pi + 1.0 );

    // calculate the hash
    const vec4 OFFSET = vec4( 16.841230, 18.774548, 16.873274, 13.664607 );
    const vec4 SCALE = vec4( 0.102007, 0.114473, 0.139651, 0.084550 );
    Pi = ( Pi * SCALE ) + OFFSET;
    Pi_inc1 = ( Pi_inc1 * SCALE ) + OFFSET;
    Pi *= Pi;
    Pi_inc1 *= Pi_inc1;
    vec4 x0y0_x1y0_x0y1_x1y1 = vec4( Pi.x, Pi_inc1.x, Pi.x, Pi_inc1.x ) * vec4( Pi.yy, Pi_inc1.yy );
    vec4 z0w0_z1w0_z0w1_z1w1 = vec4( Pi.z, Pi_inc1.z, Pi.z, Pi_inc1.z ) * vec4( Pi.ww, Pi_inc1.ww ) * vec4( 1.0 / 56974.746094 );
    vec4 z0w0_hash = fract( x0y0_x1y0_x0y1_x1y1 * z0w0_z1w0_z0w1_z1w1.xxxx );
    vec4 z1w0_hash = fract( x0y0_x1y0_x0y1_x1y1 * z0w0_z1w0_z0w1_z1w1.yyyy );
    vec4 z0w1_hash = fract( x0y0_x1y0_x0y1_x1y1 * z0w0_z1w0_z0w1_z1w1.zzzz );
    vec4 z1w1_hash = fract( x0y0_x1y0_x0y1_x1y1 * z0w0_z1w0_z0w1_z1w1.wwww );

    //	blend the results and return
    vec4 blend = Pf * Pf * Pf * (Pf * (Pf * 6.0 - 15.0) + 10.0);
    vec4 res0 = z0w0_hash + ( z0w1_hash - z0w0_hash ) * blend.wwww;
    vec4 res1 = z1w0_hash + ( z1w1_hash - z1w0_hash ) * blend.wwww;
    res0 = res0 + ( res1 - res0 ) * blend.zzzz;
    blend.zw = vec2( 1.0 - blend.xy );
    return dot( res0, blend.zxzx * blend.wwyy );
}
