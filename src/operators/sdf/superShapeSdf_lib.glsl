// supershape - gradient by valvw
// https://www.shadertoy.com/view/lXGSRy

// Supershape formula
float supershape(float theta, float m, float n1, float n2, float n3) {
const float a = 1.3;
const float b = 1.0;
    float t1 = abs(cos(m * theta / 4.0) / a);
    t1 = pow(t1, n2);
    float t2 = abs(sin(m * theta / 4.0) / b);
    t2 = pow(t2, n3);
    float r = pow(t1 + t2, -1.0 / n1);
    return r;
}

// Distance to the supershape surface
float distanceToSupershape(vec3 p, float m1, float n11, float n12, float n13, float m2, float n21, float n22, float n23) {
    float phi = atan(p.z, p.x);
    float r1 = supershape(phi, m1, n11, n12, n13);

    float theta = atan(p.y, length(vec2(p.x, p.z)));
    float r2 = supershape(theta, m2, n21, n22, n23);

    float r = r1 * r2;
    vec3 ss = vec3(r * cos(theta) * cos(phi), r * sin(theta), r * cos(theta) * sin(phi));

    return length(p - ss);
}
