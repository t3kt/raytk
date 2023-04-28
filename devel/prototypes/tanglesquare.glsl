// @A {"default":16, "normMin":-30, "normMax":30}
// @B {"default":-25, "normMin":-30, "normMax":30}
// @C {"default":12, "normMin":-30, "normMax":30}

// https://www.shadertoy.com/view/st2SzK


// Implicit definition (my own modification of the tanglecube formula here:
// https://mathworld.wolfram.com/Tanglecube.html):
// (x^4 + y^4)a + (x^2 + y^2)b + c
float sdTanglesquare(in vec2 p, in float a, in float b, in float c) {
    p = abs(p); // Quadrant symmetry
    if (p.y > p.x) p = p.yx; // Diagonal symmetry

    // Upper-right critical point in the top right quadrant 
    vec2 crit = p - vec2(sqrt((-b + sqrt(2.0 * b * b - 4.0 * a * c)) / (2.0 * a)), sqrt(-b / (2.0 * a)));
    float d = max(abs(crit.x), abs(crit.y));

    // Lower critical point in the top right quadrant
    if (abs((b * b) / (a * c) - 3.0) < 1.0) {
        crit = p - vec2(sqrt(-b / (2.0 * a)), sqrt((-b - sqrt(2.0 * b * b - 4.0 * a * c)) / (2.0 * a)));
        d = min(d, max(abs(crit.x), abs(crit.y)));
    }

    else {
        crit = p - vec2(sqrt((-b + sqrt(b * b - 4.0 * a * c)) / (2.0 * a)), 0.0); // Rightmost middle critical point
        d = min(d, max(abs(crit.x), abs(crit.y)));

        float h = b * b - 4.0 * a * c;
        if (h > 0.0) {
            float x = (-b - sqrt(h)) / (2.0 * a);
            if (x > 0.0) {
                crit = p - vec2(sqrt(x), 0.0); // Next critical point to the left
                d = min(d, max(abs(crit.x), abs(crit.y)));
            }
        }
    }

    // Diagonal ray intersection
    vec2 p2 = p * p, p4 = p2 * p2;
    float sum1 = p.x + p.y, diff1 = p.x - p.y;
    float sum2 = p2.x + p2.y, sum4 = p4.x + p4.y;

    // (ux^2 + vx + w)^2 + t = 0 ---> ux^2 + vx + w = (+/-)sqrt(-t)
    float u = sqrt(2.0 * a);
    float v = sum1 * u;
    float w = ((3.0 * sum2 - sum1 * sum1) * a + b) / u;
    float t = sqrt(w * w - sum4 * a - sum2 * b - c);

    // ux^2 + vx + w = +sqrt(-t)
    float h = v * v - 4.0 * u * (w - t);
    float k = 2.0 * u;
    if (h > 0.0) {
        h = sqrt(h);
        d = min(d, min(abs(v - h), abs(v + h)) / k);
    }

    // ux^2 + vx + w = -sqrt(-t)
    h = v * v - 4.0 * u * (w + t);
    if (h > 0.0) {
        h = sqrt(h);
        d = min(d, min(abs(v - h), abs(v + h)) / k);
    }

    // Other diagonal ray intersection
    v = diff1 * u;
    w = ((3.0 * sum2 - diff1 * diff1) * a + b) / u;
    t = sqrt(w * w - sum4 * a - sum2 * b - c);

    // ux^2 + vx + w = +sqrt(-t)
    h = v * v - 4.0 * u * (w - t);
    if (h > 0.0) {
        h = sqrt(h);
        d = min(d, min(abs(v - h), abs(v + h)) / k);
    }

    // ux^2 + vx + w = -sqrt(-t)
    h = v * v - 4.0 * u * (w + t);
    if (h > 0.0) {
        h = sqrt(h);
        d = min(d, min(abs(v - h), abs(v + h)) / k);
    }

    return d * sign(sum4 * a + sum2 * b + c);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float a = THIS_A;
	float b = THIS_B;
	float c = THIS_C;
	
	float d = sdTanglesquare(p, a, b, c);
	return createSdf(d);

}