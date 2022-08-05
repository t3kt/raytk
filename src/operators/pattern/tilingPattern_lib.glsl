vec2 tile_triangleCircumcenter(vec2 A, vec2 B, vec2 C)
{
    float a = distance(C, B);
    float b = distance(C, A);
    float c = distance(A, B);
    vec3 bary = vec3(a * a * (b * b + c * c - a * a),
                     b * b * (c * c + a * a - b * b),
                     c * c * (a * a + b * b - c * c));
    bary /= bary.x + bary.y + bary.z;
    return A * bary.x + B * bary.y + C * bary.z;
}

float tile_segment(vec2 p, vec2 a, vec2 b)
{
    return distance(p, mix(a, b, clamp(dot(p - a, b - a) / dot(b - a, b - a), 0., 1.)));
}