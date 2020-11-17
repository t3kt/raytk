// Dodecahedron Distance Estimator (Syntopia 2010), from Fragmentarium examples

ReturnT thismap(CoordT p, ContextT ctx) {
    float Scale = 2.617;
    float Phi = 1.618;
    float Bailout = 9;
    float Angle1 = 0.;
    vec3 Rot1 = vec3(1., 1., 1.);
    float Angle2 = 0.;
    vec3 Rot2 = vec3(1., 1., 1.);
    int Iterations = 13;

    mat3 fracRotation1 = TDRotateOnAxis(Angle1, Rot1);
    mat3 fracRotation2 = TDRotateOnAxis(Angle2, Rot2);

    vec4 orbitTrap;


    float bailout2 = pow(10., Bailout);

vec3 n1 = normalize(vec3(-1.0,Phi-1.0,1.0/(Phi-1.0)));
vec3 n2 = normalize(vec3(Phi-1.0,1.0/(Phi-1.0),-1.0));
vec3 n3 = normalize(vec3(1.0/(Phi-1.0),-1.0,Phi-1.0));
vec3 offset = vec3(1.0,1.0,1.0);

    float r;
    // prefolds
    float t;
    // iterate to compute the distance estimator
    int n = 0;
    while (n < Iterations) {
        p *= fracRotation1;

        // t =dot(p,n1); if (t<0.0) { p-=2.0*t*n1; } <- this form is a bit slower   
        p-=2.0 * min(0.0, dot(p, n1)) * n1;
        p-= 2.0 * min(0.0, dot(p, n2)) * n2;
        p-= 2.0 * min(0.0, dot(p, n3)) * n3;
        p-=2.0 * min(0.0, dot(p, n1)) * n1;
        p-= 2.0 * min(0.0, dot(p, n2)) * n2;
        p-= 2.0 * min(0.0, dot(p, n3)) * n3;
        p-=2.0 * min(0.0, dot(p, n1)) * n1;
        p-= 2.0 * min(0.0, dot(p, n2)) * n2;
        p-= 2.0 * min(0.0, dot(p, n3)) * n3;

        p = p*Scale - offset*(Scale-1.0);
        p *= fracRotation2;
        r = dot(p, p);
        orbitTrap = min(orbitTrap, abs(vec4(0.0,0.0,0.0,r)));
        if (r > bailout2) break;

        n++;
    }
    // Works better when subtracting -1
    float d= (length(p) ) * pow(Scale,  float(-n-1));

	return createSdf(d);
}