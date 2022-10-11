// space frame by jt
// https://www.shadertoy.com/view/7tGBD3

/*

Copyright (c) 2022 Jakob Thomsen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

*/

// modulo3d with limits
vec3 THIS_opRepLim( in vec3 p, in vec3 lima, in vec3 limb )
{
	p += 0.5;
	return p - clamp(floor(p),lima,limb);
}

float THIS_part(vec3 p, float r, float size)
{
	vec2 dim = vec2(size, 0.);
	float d = RAYTK_MAX_DIST;
	// TODO: use symmetry instead of explicitly defining each line
	d = min(d, fCapsule(p.xyz, dim.yyy, dim.yyx, r));
	d = min(d, fCapsule(p.yzx, dim.yyy, dim.yyx, r));
	d = min(d, fCapsule(p.zxy, dim.yyy, dim.yyx, r));
	d = min(d, fCapsule(p.xyz, dim.yyx, dim.xyy, r));
	d = min(d, fCapsule(p.yzx, dim.yyx, dim.xyy, r));
	d = min(d, fCapsule(p.zxy, dim.yyx, dim.xyy, r));
	return d;
}

float THIS_element(vec3 p, float r, float size) // TODO: use symmetries to improve performance
{
	vec2 dim = vec2(size, 0.);
	float d = RAYTK_MAX_DIST;
	d = min(d, THIS_part(p, r, size));
	d = min(d, THIS_part(size-p, r, size));
	d = min(d, fCapsule(p, dim.xxy, dim.xyy, r));
	d = min(d, fCapsule(p, dim.xxy, dim.yxy, r));
	d = min(d, fCapsule(p, dim.yyx, dim.xyx, r));
	d = min(d, fCapsule(p, dim.yyx, dim.yxx, r));
	d = min(d, fCapsule(p, dim.xyy, dim.xyx, r));
	d = min(d, fCapsule(p, dim.yxy, dim.yxx, r));
	return d;
}

// more efficient & more symmetric fundamental cube (nodes form face centric cubic)
float THIS_element2(vec3 p, float r) {
	p = abs(p - 0.5) + 0.5;  // mirror symmetry
	p.xy = p.x > p.y ? p.xy : p.yx; // reflect
	p.yz = p.y > p.z ? p.yz : p.zy; // reflect

	return min(fCapsule(p, vec3(1,1,0), vec3(1,1,1), r), fCapsule(p, vec3(1,1,1), vec3(1,0,0), r));
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 limA = vec3(-1,0, 0);
	vec3 limB = vec3(1, 1, 0);
	float r = 0.04;
	float size = 1;
	vec3 q = THIS_opRepLim(p, limA * size, limB * size);
//	float d = THIS_element2(q, r);
	float d = THIS_element(q, r, size);
	return createSdf(d);
}