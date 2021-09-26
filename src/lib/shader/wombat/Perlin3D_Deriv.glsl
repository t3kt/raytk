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
//  Perlin Noise 3D Deriv
//  Return value range of -1.0->1.0, with format vec4( value, xderiv, yderiv, zderiv )
//
vec4 Perlin3D_Deriv( vec3 P )
{
    //  https://github.com/BrianSharpe/Wombat/blob/master/Perlin3D_Deriv.glsl

    // establish our grid cell and unit position
    vec3 Pi = floor(P);
    vec3 Pf = P - Pi;
    vec3 Pf_min1 = Pf - 1.0;

    // clamp the domain
    Pi.xyz = Pi.xyz - floor(Pi.xyz * ( 1.0 / 69.0 )) * 69.0;
    vec3 Pi_inc1 = step( Pi, vec3( 69.0 - 1.5 ) ) * ( Pi + 1.0 );

    // calculate the hash
    vec4 Pt = vec4( Pi.xy, Pi_inc1.xy ) + vec2( 50.0, 161.0 ).xyxy;
    Pt *= Pt;
    Pt = Pt.xzxz * Pt.yyww;
    const vec3 SOMELARGEFLOATS = vec3( 635.298681, 682.357502, 668.926525 );
    const vec3 ZINC = vec3( 48.500388, 65.294118, 63.934599 );
    vec3 lowz_mod = vec3( 1.0 / ( SOMELARGEFLOATS + Pi.zzz * ZINC ) );
    vec3 highz_mod = vec3( 1.0 / ( SOMELARGEFLOATS + Pi_inc1.zzz * ZINC ) );
    vec4 hashx0 = fract( Pt * lowz_mod.xxxx );
    vec4 hashx1 = fract( Pt * highz_mod.xxxx );
    vec4 hashy0 = fract( Pt * lowz_mod.yyyy );
    vec4 hashy1 = fract( Pt * highz_mod.yyyy );
    vec4 hashz0 = fract( Pt * lowz_mod.zzzz );
    vec4 hashz1 = fract( Pt * highz_mod.zzzz );

    //	calculate the gradients
    vec4 grad_x0 = hashx0 - 0.49999;
    vec4 grad_y0 = hashy0 - 0.49999;
    vec4 grad_z0 = hashz0 - 0.49999;
    vec4 grad_x1 = hashx1 - 0.49999;
    vec4 grad_y1 = hashy1 - 0.49999;
    vec4 grad_z1 = hashz1 - 0.49999;
    vec4 norm_0 = inversesqrt( grad_x0 * grad_x0 + grad_y0 * grad_y0 + grad_z0 * grad_z0 );
    vec4 norm_1 = inversesqrt( grad_x1 * grad_x1 + grad_y1 * grad_y1 + grad_z1 * grad_z1 );
    grad_x0 *= norm_0;
    grad_y0 *= norm_0;
    grad_z0 *= norm_0;
    grad_x1 *= norm_1;
    grad_y1 *= norm_1;
    grad_z1 *= norm_1;

    //	calculate the dot products
    vec4 dotval_0 = vec2( Pf.x, Pf_min1.x ).xyxy * grad_x0 + vec2( Pf.y, Pf_min1.y ).xxyy * grad_y0 + Pf.zzzz * grad_z0;
    vec4 dotval_1 = vec2( Pf.x, Pf_min1.x ).xyxy * grad_x1 + vec2( Pf.y, Pf_min1.y ).xxyy * grad_y1 + Pf_min1.zzzz * grad_z1;

    //	C2 Interpolation
    vec3 blend = Pf * Pf * Pf * (Pf * (Pf * 6.0 - 15.0) + 10.0);
    vec3 blendDeriv = Pf * Pf * (Pf * (Pf * 30.0 - 60.0) + 30.0);

    //  the following is based off Milo Yips derivation, but modified for parallel execution
    //  http://stackoverflow.com/a/14141774

    //	Convert our data to a more parallel format
    vec4 dotval0_grad0 = vec4( dotval_0.x, grad_x0.x, grad_y0.x, grad_z0.x );
    vec4 dotval1_grad1 = vec4( dotval_0.y, grad_x0.y, grad_y0.y, grad_z0.y );
    vec4 dotval2_grad2 = vec4( dotval_0.z, grad_x0.z, grad_y0.z, grad_z0.z );
    vec4 dotval3_grad3 = vec4( dotval_0.w, grad_x0.w, grad_y0.w, grad_z0.w );
    vec4 dotval4_grad4 = vec4( dotval_1.x, grad_x1.x, grad_y1.x, grad_z1.x );
    vec4 dotval5_grad5 = vec4( dotval_1.y, grad_x1.y, grad_y1.y, grad_z1.y );
    vec4 dotval6_grad6 = vec4( dotval_1.z, grad_x1.z, grad_y1.z, grad_z1.z );
    vec4 dotval7_grad7 = vec4( dotval_1.w, grad_x1.w, grad_y1.w, grad_z1.w );

    //	evaluate common constants
    vec4 k0_gk0 = dotval1_grad1 - dotval0_grad0;
    vec4 k1_gk1 = dotval2_grad2 - dotval0_grad0;
    vec4 k2_gk2 = dotval4_grad4 - dotval0_grad0;
    vec4 k3_gk3 = dotval3_grad3 - dotval2_grad2 - k0_gk0;
    vec4 k4_gk4 = dotval5_grad5 - dotval4_grad4 - k0_gk0;
    vec4 k5_gk5 = dotval6_grad6 - dotval4_grad4 - k1_gk1;
    vec4 k6_gk6 = (dotval7_grad7 - dotval6_grad6) - (dotval5_grad5 - dotval4_grad4) - k3_gk3;

    //	calculate final noise + deriv
    float u = blend.x;
    float v = blend.y;
    float w = blend.z;
    vec4 result = dotval0_grad0
        + u * ( k0_gk0 + v * k3_gk3 )
        + v * ( k1_gk1 + w * k5_gk5 )
        + w * ( k2_gk2 + u * ( k4_gk4 + v * k6_gk6 ) );
    result.y += dot( vec4( k0_gk0.x, k3_gk3.x * v, vec2( k4_gk4.x, k6_gk6.x * v ) * w ), vec4( blendDeriv.x ) );
    result.z += dot( vec4( k1_gk1.x, k3_gk3.x * u, vec2( k5_gk5.x, k6_gk6.x * u ) * w ), vec4( blendDeriv.y ) );
    result.w += dot( vec4( k2_gk2.x, k4_gk4.x * u, vec2( k5_gk5.x, k6_gk6.x * u ) * v ), vec4( blendDeriv.z ) );
    return result * 1.1547005383792515290182975610039;  // scale things to a strict -1.0->1.0 range  *= 1.0/sqrt(0.75)
}
