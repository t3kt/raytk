// @Bigradius {"default":1, "normMin":0, "normMax":2}
// @Coils {"default":1, "normMin":0, "normMax":2}
// @Coilstep {"default":1, "normMin":0, "normMax":2}

// Coil Symmetry by DjinnKahn
// https://www.shadertoy.com/view/MlK3z3

float angleOf( vec2 v ) { return atan( v.y, v.x ); }

float round_( float x, float m ) { return floor( x/m + .5 ) * m; }


// map `pos` to a coiled space
// Think of a thick wire (the coil) wrapped around a torus
// Walking along the wire,
//   the returned y-coordinate: distance from the torus
//   the returned x-coordinate: left/right deviation from the coil
//   the returned z-coordinate: the progress of walking the entire wire (usually ignore this)
// * Lipschitz_continuity is NOT guaranteed *
// 		- DjinnKahn
vec3 opTorusCoil( vec3 pos, float bigRadius, float numCoils, float coilStep/*try 1.*/ )
{
    vec3 polarPos = vec3( length( pos.xy ), angleOf( pos.xy ), pos.z );
    vec3 polarC   = vec3( bigRadius      , polarPos.y       , 0. );
    float tiltRelativeToRing = angleOf( ( polarPos - polarC ).xz );
    float distToRing = length( ( polarPos - polarC ).xz );

    vec3 polarD = vec3( bigRadius, round_(polarPos.y-coilStep*tiltRelativeToRing/numCoils,2.*PI/numCoils) + coilStep*tiltRelativeToRing/numCoils, 0. );
    //float sheetDeltaX = polarC.y - polarD.y; // if you want x-coordinate to be an angle
    float sheetDeltaX = polarPos.x * sin( polarC.y - polarD.y );
    float sheetDeltaY = distToRing;
    return vec3( sheetDeltaX, sheetDeltaY, fract(polarD.y/(2.*PI)) );
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float bigRadius = THIS_Bigradius;
	float coils = THIS_Coils;
	float coilStep = THIS_Coilstep;
	p = opTorusCoil(p, bigRadius, coils, coilStep);
	return inputOp1(p, ctx);
}