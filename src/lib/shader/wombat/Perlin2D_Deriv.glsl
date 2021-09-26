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
//  Perlin Noise 2D Deriv
//  Return value range of -1.0->1.0, with format vec3( value, xderiv, yderiv )
//
vec3 Perlin2D_Deriv( vec2 P )
{
    //  https://github.com/BrianSharpe/Wombat/blob/master/Perlin2D_Deriv.glsl

    // establish our grid cell and unit position
    vec2 Pi = floor(P);
    vec4 Pf_Pfmin1 = P.xyxy - vec4( Pi, Pi + 1.0 );

    // calculate the hash
    vec4 Pt = vec4( Pi.xy, Pi.xy + 1.0 );
    Pt = Pt - floor(Pt * ( 1.0 / 71.0 )) * 71.0;
    Pt += vec2( 26.0, 161.0 ).xyxy;
    Pt *= Pt;
    Pt = Pt.xzxz * Pt.yyww;
    vec4 hash_x = fract( Pt * ( 1.0 / 951.135664 ) );
    vec4 hash_y = fract( Pt * ( 1.0 / 642.949883 ) );

    // calculate the gradient results
    vec4 grad_x = hash_x - 0.49999;
    vec4 grad_y = hash_y - 0.49999;
    vec4 norm = inversesqrt( grad_x * grad_x + grad_y * grad_y );
    grad_x *= norm;
    grad_y *= norm;
    vec4 dotval = ( grad_x * Pf_Pfmin1.xzxz + grad_y * Pf_Pfmin1.yyww );

    //	C2 Interpolation
    vec4 blend = Pf_Pfmin1.xyxy * Pf_Pfmin1.xyxy * ( Pf_Pfmin1.xyxy * ( Pf_Pfmin1.xyxy * ( Pf_Pfmin1.xyxy * vec2( 6.0, 0.0 ).xxyy + vec2( -15.0, 30.0 ).xxyy ) + vec2( 10.0, -60.0 ).xxyy ) + vec2( 0.0, 30.0 ).xxyy );

    //	Convert our data to a more parallel format
    vec3 dotval0_grad0 = vec3( dotval.x, grad_x.x, grad_y.x );
    vec3 dotval1_grad1 = vec3( dotval.y, grad_x.y, grad_y.y );
    vec3 dotval2_grad2 = vec3( dotval.z, grad_x.z, grad_y.z );
    vec3 dotval3_grad3 = vec3( dotval.w, grad_x.w, grad_y.w );

    //	evaluate common constants
    vec3 k0_gk0 = dotval1_grad1 - dotval0_grad0;
    vec3 k1_gk1 = dotval2_grad2 - dotval0_grad0;
    vec3 k2_gk2 = dotval3_grad3 - dotval2_grad2 - k0_gk0;

    //	calculate final noise + deriv
    vec3 results = dotval0_grad0
                    + blend.x * k0_gk0
                    + blend.y * ( k1_gk1 + blend.x * k2_gk2 );
    results.yz += blend.zw * ( vec2( k0_gk0.x, k1_gk1.x ) + blend.yx * k2_gk2.xx );
    return results * 1.4142135623730950488016887242097;  // scale things to a strict -1.0->1.0 range  *= 1.0/sqrt(0.5)
}
