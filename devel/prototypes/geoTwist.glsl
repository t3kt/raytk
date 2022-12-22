// @Mode {"default":0, "normMin":0, "normMax":4, "style": "Int"}
// @Subdivs {"default":1, "normMax":2, "style": "Int"}
// @Twist {"default": 0, "normMin": -180, "normMax": 180}

void pModIcosahedron(inout vec3 p) {
    p = abs(p);
    pReflect(p, geo_nc, 0.);
    p.xy = abs(p.xy);
    pReflect(p, geo_nc, 0.);
    p.xy = abs(p.xy);
    pReflect(p, geo_nc, 0.);
}


float indexSgn(float s) {
	return s / 2. + 0.5;
}

bool boolSgn(float s) {
	return bool(s / 2. + 0.5);
}

float pModIcosahedronIndexed(inout vec3 p, int subdivisions) {
	float x = indexSgn(sgn(p.x));
	float y = indexSgn(sgn(p.y));
	float z = indexSgn(sgn(p.z));
    p = abs(p);
	pReflect(p, geo_nc, 0.);

	float xai = sgn(p.x);
	float yai = sgn(p.y);
    p.xy = abs(p.xy);
	float sideBB = pReflect(p, geo_nc, 0.);

	float ybi = sgn(p.y);
	float xbi = sgn(p.x);
    p.xy = abs(p.xy);
	pReflect(p, geo_nc, 0.);

    float idx = 0.;

    float faceGroupAi = indexSgn(ybi * yai * -1.);
    float faceGroupBi = indexSgn(yai);
    float faceGroupCi = clamp((xai - ybi -1.), 0., 1.);
    float faceGroupDi = clamp(1. - faceGroupAi - faceGroupBi - faceGroupCi, 0., 1.);

    idx += faceGroupAi * (x + (2. * y) + (4. * z));
    idx += faceGroupBi * (8. + y + (2. * z));
    # ifndef SEAMLESS_LOOP
    	idx += faceGroupCi * (12. + x + (2. * z));
    # endif
    idx += faceGroupDi * (12. + x + (2. * y));

	return idx;
}

vec3 vMin(vec3 p, vec3 a, vec3 b, vec3 c) {
    float la = length(p - a);
    float lb = length(p - b);
    float lc = length(p - c);
    if (la < lb) {
        if (la < lc) {
            return a;
        } else {
            return c;
        }
    } else {
        if (lb < lc) {
            return b;
        } else {
            return c;
        }
    }
}

// Nearest icosahedron vertex
vec3 icosahedronVertex(vec3 p) {
    if (p.z > 0.) {
        if (p.x > 0.) {
            if (p.y > 0.) {
                return vMin(p, GDFVector13, GDFVector15, GDFVector17);
            } else {
                return vMin(p, GDFVector14, GDFVector15, GDFVector17b);
            }
        } else {
            if (p.y > 0.) {
                return vMin(p, GDFVector13, GDFVector16, GDFVector18);
            } else {
                return vMin(p, GDFVector14, GDFVector16, GDFVector18b);
            }
        }
    } else {
        if (p.x > 0.) {
            if (p.y > 0.) {
                return vMin(p, GDFVector13b, GDFVector15b, GDFVector17);
            } else {
                return vMin(p, GDFVector14b, GDFVector15b, GDFVector17b);
            }
        } else {
            if (p.y > 0.) {
                return vMin(p, GDFVector13b, GDFVector16b, GDFVector18);
            } else {
                return vMin(p, GDFVector14b, GDFVector16b, GDFVector18b);
            }
        }
    }
}

// Nearest vertex and distance.
// Distance is roughly to the boundry between the nearest and next
// nearest icosahedron vertices, ensuring there is always a smooth
// join at the edges, and normalised from 0 to 1
vec4 icosahedronAxisDistance(vec3 p) {
    vec3 iv = icosahedronVertex(p);
    vec3 originalIv = iv;

    vec3 pn = normalize(p);
    pModIcosahedron(pn);
    pModIcosahedron(iv);

    float boundryDist = dot(pn, vec3(1, 0, 0));
    float boundryMax = dot(iv, vec3(1, 0, 0));
    boundryDist /= boundryMax;

    float roundDist = length(iv - pn);
    float roundMax = length(iv - vec3(0, 0, 1.));
    roundDist /= roundMax;
    roundDist = -roundDist + 1.;

    float blend = 1. - boundryDist;
	blend = pow(blend, 6.);

    float dist = mix(roundDist, boundryDist, blend);

    return vec4(originalIv, dist);
}

// Twists p around the nearest icosahedron vertex
void pTwistIcosahedron(inout vec3 p, float amount) {
    vec4 a = icosahedronAxisDistance(p);
    vec3 axis = a.xyz;
    float dist = a.a;
    mat3 m = TDRotateOnAxis(dist * amount, axis);
    p *= m;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	int mode = int(THIS_Mode);
	int subdivs = int(THIS_Subdivs);
	float twist = radians(THIS_Twist);
	float idx;
	Sdf res;
	vec3 col = vec3(1.);
	switch (mode) {
		case 0:
			pModIcosahedron(p);
			break;
		case 1:
			idx = pModIcosahedronIndexed(p, subdivs);
			pTwistIcosahedron(p, twist);
			col = inputOp2(idx / 19., ctx).rgb*1.5;
//			col = vec3(map01(idx, 0., 19.));
			break;
	}
	res = inputOp1(p, ctx);
	assignColor(res, col);
	return res;
}