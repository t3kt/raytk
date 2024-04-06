
Sdf cmb_simpleUnion(Sdf res1, Sdf res2) { return (res1.x<res2.x)? res1:res2; }

Sdf cmb_simpleIntersect(Sdf res1, Sdf res2) { return (res1.x>res2.x) ? res1 : res2; }

Sdf cmb_simpleDiff(Sdf res1, Sdf res2) {
	res1.x = max(-res2.x, res1.x);
	return res1;
}

Sdf cmb_smoothUnion(Sdf res1, Sdf res2, float r) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = mix(res2.x, res1.x, h) - r*h*(1.0-h);
	blendInSdf(res1, res2, 1. - h);
	return res1;
}

float cmb_smoothUnion(float d1, float d2, float r) {
	float h = smoothBlendRatio(d1, d2, r);
	return mix(d2, d1, h) - r*h*(1.0-h);
}

Sdf cmb_smoothIntersect(Sdf res1, Sdf res2, float r) {
	Sdf res = res1;
	float h = clamp(0.5 - 0.5*(res2.x-res1.x)/r, 0., 1.);
	res.x = mix(res2.x, res1.x, h) + r*h*(1.0-h);
	blendInSdf(res1, res2, h);
	return res;
}

Sdf cmb_smoothDiff(Sdf res1, Sdf res2, float r) {
	res2.x *= -1.;
	return cmb_smoothIntersect(res1, res2, r);
}

Sdf cmb_roundUnion(Sdf res1, Sdf res2, float r) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = fOpUnionRound(res1.x, res2.x, r);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

Sdf cmb_roundIntersect(Sdf res1, Sdf res2, float r) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = fOpIntersectionRound(res1.x, res2.x, r);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

Sdf cmb_roundDiff(Sdf res1, Sdf res2, float r) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = fOpDifferenceRound(res1.x, res2.x, r);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

Sdf cmb_chamferUnion(Sdf res1, Sdf res2, float r) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = fOpUnionChamfer(res1.x, res2.x, r);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

Sdf cmb_chamferIntersect(Sdf res1, Sdf res2, float r) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = fOpIntersectionChamfer(res1.x, res2.x, r);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

Sdf cmb_chamferDiff(Sdf res1, Sdf res2, float r) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = fOpDifferenceChamfer(res1.x, res2.x, r);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

float cmb_stairUnion(float res1, float res2, float r, float n, float o) {
	float s = r/n;
	float u = res2-r;
	return min(min(res1,res2), 0.5 * (u + res1 + abs ((mod (u - res1 + s + o, 2 * s)) - s)));
}
Sdf cmb_stairUnion(Sdf res1, Sdf res2, float r, float n, float o) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = cmb_stairUnion(res1.x, res2.x, r, n, o);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

Sdf cmb_stairIntersect(Sdf res1, Sdf res2, float r, float n, float o) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = -cmb_stairUnion(-res1.x, -res2.x, r, n, o);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

Sdf cmb_stairDiff(Sdf res1, Sdf res2, float r, float n, float o) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	float s = r/n;
	float u = res2.x-r;
	res1.x = -min(min(-res1.x,res2.x), 0.5 * (u - res1.x + abs ((mod (u + res1.x + s + o, 2 * s)) - s)));
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

float cmb_columnUnion(float res1, float res2, float r, float n, float o) {
	if ((res1 < r) && (res2 < r)) {
		vec2 p = vec2(res1, res2);
		float columnradius = r*sqrt(2)/((n-1)*2+sqrt(2));
		pR45(p);
		p.x -= sqrt(2)/2*r;
		p.x += columnradius*sqrt(2);
		if (mod(n,2) == 1) {
			p.y += columnradius;
		}
		// At this point, we have turned 45 degrees and moved at a point on the
		// diagonal that we want to place the columns on.
		// Now, repeat the domain along this direction and place a circle.
		p.y += o;
		pMod1(p.y, columnradius*2);
		float result = length(p) - columnradius;
		result = min(result, p.x);
		result = min(result, res1);
		return min(result, res2);
	} else {
		return min(res1, res2);
	}
}

Sdf cmb_columnUnion(Sdf res1, Sdf res2, float r, float n, float o) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = cmb_columnUnion(res1.x, res2.x, r, n, o);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

float cmb_columnDiff(float res1, float res2, float r, float n, float o) {
	res1 = -res1;
	float m = min(res1, res2);
	//avoid the expensive computation where not needed (produces discontinuity though)
	if ((res1 < r) && (res2 < r)) {
		vec2 p = vec2(res1, res2);
		float columnradius = r*sqrt(2)/n/2.0;
		columnradius = r*sqrt(2)/((n-1)*2+sqrt(2));

		pR45(p);
		p.y += columnradius;
		p.x -= sqrt(2)/2*r;
		p.x += -columnradius*sqrt(2)/2;

		if (mod(n,2) == 1) {
			p.y += columnradius;
		}
		p.y += o;
		pMod1(p.y,columnradius*2);

		float result = -length(p) + columnradius;
		result = max(result, p.x);
		result = min(result, res1);
		return -min(result, res2);
	} else {
		return -m;
	}
}
Sdf cmb_columnDiff(Sdf res1, Sdf res2, float r, float n, float o) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = cmb_columnDiff(res1.x, res2.x, r, n, o);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

Sdf cmb_columnIntersect(Sdf res1, Sdf res2, float r, float n, float o) {
	float h = smoothBlendRatio(res1.x, res2.x, r);
	res1.x = cmb_columnDiff(res1.x, -res2.x, r, n, o);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}

// https://www.shadertoy.com/view/ssG3WK XOR SDF by jt
// https://iquilezles.org/articles/sdfxor/ by Inigo Quilez.
float cmb_simpleXor(float res1, float res2) {
	return max(min(res1, res2), -max(res1, res2));
}

Sdf cmb_simpleXor(Sdf res1, Sdf res2) {
	res1.x = cmb_simpleXor(res1.x, res2.x);
	return res1;
}
