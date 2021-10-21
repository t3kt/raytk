// hash.glsl

// https://www.shadertoy.com/view/XlGcRh
// See the full paper at: http://www.jcgt.org/published/0009/03/02

// commonly used constants
#define hsh_c1 0xcc9e2d51u
#define hsh_c2 0x1b873593u

// Helper Functions
uint rotl(uint x, uint r)
{
	return (x << r) | (x >> (32u - r));
}

uint rotr(uint x, uint r)
{
	return (x >> r) | (x << (32u - r));
}

uint fmix(uint h)
{
	h ^= h >> 16;
	h *= 0x85ebca6bu;
	h ^= h >> 13;
	h *= 0xc2b2ae35u;
	h ^= h >> 16;
	return h;
}

uint mur(uint a, uint h) {
	// Helper from Murmur3 for combining two 32-bit values.
	a *= hsh_c1;
	a = rotr(a, 17u);
	a *= hsh_c2;
	h ^= a;
	h = rotr(h, 19u);
	return h * 5u + 0xe6546b64u;
}

uint bswap32(uint x) {
	return (((x & 0x000000ffu) << 24) |
	((x & 0x0000ff00u) <<  8) |
	((x & 0x00ff0000u) >>  8) |
	((x & 0xff000000u) >> 24));
}

uint taus(uint z, int s1, int s2, int s3, uint m)
{
	uint b = (((z << s1) ^ z) >> s2);
	return (((z & m) << s3) ^ b);
}



// convert 2D seed to 1D
// 2 imad
uint seed(uvec2 p) {
	return 19u * p.x + 47u * p.y + 101u;
}

// convert 3D seed to 1D
uint seed(uvec3 p) {
	return 19u * p.x + 47u * p.y + 101u * p.z + 131u;
}

// convert 4D seed to 1D
uint seed(uvec4 p) {
	return 19u * p.x + 47u * p.y + 101u * p.z + 131u * p.w + 173u;
}




/**********************************************************************
 * Hashes
 **********************************************************************/

// BBS-inspired hash
//  - Olano, Modified Noise for Evaluation on Graphics Hardware, GH 2005
uint bbs(uint v) {
	v = v % 65521u;
	v = (v * v) % 65521u;
	v = (v * v) % 65521u;
	return v;
}



// CityHash32, adapted from Hash32Len0to4 in https://github.com/google/cityhash
uint city(uint s)
{
	uint len = 4u;
	uint b = 0u;
	uint c = 9u;

	for (uint i = 0u; i < len; i++) {
		uint v = (s >> (i * 8u)) & 0xffu;
		b = b * hsh_c1 + v;
		c ^= b;
	}

	return fmix(mur(b, mur(len, c)));
}

// CityHash32, adapted from Hash32Len5to12 in https://github.com/google/cityhash
uint city(uvec2 s)
{
	uint len = 8u;
	uint a = len, b = len * 5u, c = 9u, d = b;

	a += bswap32(s.x);
	b += bswap32(s.y);
	c += bswap32(s.y);

	return fmix(mur(c, mur(b, mur(a, d))));
}

// CityHash32, adapted from Hash32Len5to12 in https://github.com/google/cityhash
uint city(uvec3 s)
{
	uint len = 12u;
	uint a = len, b = len * 5u, c = 9u, d = b;

	a += bswap32(s.x);
	b += bswap32(s.z);
	c += bswap32(s.y);

	return fmix(mur(c, mur(b, mur(a, d))));
}

// CityHash32, adapted from Hash32Len12to24 in https://github.com/google/cityhash
uint city(uvec4 s)
{
	uint len = 16u;
	uint a = bswap32(s.w);
	uint b = bswap32(s.y);
	uint c = bswap32(s.z);
	uint d = bswap32(s.z);
	uint e = bswap32(s.x);
	uint f = bswap32(s.w);
	uint h = len;

	return fmix(mur(f, mur(e, mur(d, mur(c, mur(b, mur(a, h)))))));
}



// Schechter and Bridson hash
// https://www.cs.ubc.ca/~rbridson/docs/schechter-sca08-turbulence.pdf
uint esgtsa(uint s)
{
	s = (s ^ 2747636419u) * 2654435769u;// % 4294967296u;
	s = (s ^ (s >> 16u)) * 2654435769u;// % 4294967296u;
	s = (s ^ (s >> 16u)) * 2654435769u;// % 4294967296u;
	return s;
}



// UE4's RandFast function
// https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Shaders/Private/Random.ush
float fast(vec2 v)
{
	v = (1./4320.) * v + vec2(0.25,0.);
	float state = fract( dot( v * v, vec2(3571)));
	return fract( state * state * (3571. * 2.));
}




// Hash without Sine
// https://www.shadertoy.com/view/4djSRW
float hashwithoutsine11(float p)
{
	p = fract(p * .1031);
	p *= p + 33.33;
	p *= p + p;
	return fract(p);
}

float hashwithoutsine12(vec2 p)
{
	vec3 p3  = fract(vec3(p.xyx) * .1031);
	p3 += dot(p3, p3.yzx + 33.33);
	return fract((p3.x + p3.y) * p3.z);
}

float hashwithoutsine13(vec3 p3)
{
	p3  = fract(p3 * .1031);
	p3 += dot(p3, p3.yzx + 33.33);
	return fract((p3.x + p3.y) * p3.z);
}

vec2 hashwithoutsine21(float p)
{
	vec3 p3 = fract(vec3(p,p,p) * vec3(.1031, .1030, .0973));
	p3 += dot(p3, p3.yzx + 33.33);
	return fract((p3.xx+p3.yz)*p3.zy);
}

vec2 hashwithoutsine22(vec2 p)
{
	vec3 p3 = fract(vec3(p.xyx) * vec3(.1031, .1030, .0973));
	p3 += dot(p3, p3.yzx+33.33);
	return fract((p3.xx+p3.yz)*p3.zy);
}

vec2 hashwithoutsine23(vec3 p3)
{
	p3 = fract(p3 * vec3(.1031, .1030, .0973));
	p3 += dot(p3, p3.yzx+33.33);
	return fract((p3.xx+p3.yz)*p3.zy);
}

vec3 hashwithoutsine31(float p)
{
	vec3 p3 = fract(vec3(p,p,p) * vec3(.1031, .1030, .0973));
	p3 += dot(p3, p3.yzx+33.33);
	return fract((p3.xxy+p3.yzz)*p3.zyx);
}

vec3 hashwithoutsine32(vec2 p)
{
	vec3 p3 = fract(vec3(p.xyx) * vec3(.1031, .1030, .0973));
	p3 += dot(p3, p3.yxz+33.33);
	return fract((p3.xxy+p3.yzz)*p3.zyx);
}

vec3 hashwithoutsine33(vec3 p3)
{
	p3 = fract(p3 * vec3(.1031, .1030, .0973));
	p3 += dot(p3, p3.yxz+33.33);
	return fract((p3.xxy + p3.yxx)*p3.zyx);
}

vec4 hashwithoutsine41(float p)
{
	vec4 p4 = fract(vec4(p,p,p,p) * vec4(.1031, .1030, .0973, .1099));
	p4 += dot(p4, p4.wzxy+33.33);
	return fract((p4.xxyz+p4.yzzw)*p4.zywx);
}

vec4 hashwithoutsine42(vec2 p)
{
	vec4 p4 = fract(vec4(p.xyxy) * vec4(.1031, .1030, .0973, .1099));
	p4 += dot(p4, p4.wzxy+33.33);
	return fract((p4.xxyz+p4.yzzw)*p4.zywx);
}

vec4 hashwithoutsine43(vec3 p)
{
	vec4 p4 = fract(vec4(p.xyzx)  * vec4(.1031, .1030, .0973, .1099));
	p4 += dot(p4, p4.wzxy+33.33);
	return fract((p4.xxyz+p4.yzzw)*p4.zywx);
}

vec4 hashwithoutsine44(vec4 p4)
{
	p4 = fract(p4  * vec4(.1031, .1030, .0973, .1099));
	p4 += dot(p4, p4.wzxy+33.33);
	return fract((p4.xxyz+p4.yzzw)*p4.zywx);
}


// Hybrid Taus
// https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch37.html
uint hybridtaus(uvec4 z)
{
	z.x = taus(z.x, 13, 19, 12, 0xfffffffeu);
	z.y = taus(z.y, 2, 25, 4, 0xfffffff8u);
	z.z = taus(z.z, 3, 11, 17, 0xfffffff0u);
	z.w = z.w * 1664525u + 1013904223u;

	return z.x ^ z.y ^ z.z ^ z.w;
}

// Interleaved Gradient Noise
//  - Jimenez, Next Generation Post Processing in Call of Duty: Advanced Warfare
//    Advances in Real-time Rendering, SIGGRAPH 2014
float ign(vec2 v)
{
	vec3 magic = vec3(0.06711056, 0.00583715, 52.9829189);
	return fract(magic.z * fract(dot(v, magic.xy)));
}



// Integer Hash - md5_I
// - Inigo Quilez, Integer Hash - md5_I, 2017
//   https://www.shadertoy.com/view/llGSzw
uint iqint1(uint n)
{
	// integer hash copied from Hugo Elias
	n = (n << 13U) ^ n;
	n = n * (n * n * 15731U + 789221U) + 1376312589U;

	return n;
}

// Integer Hash - II
// - Inigo Quilez, Integer Hash - II, 2017
//   https://www.shadertoy.com/view/XlXcW4
uvec3 iqint2(uvec3 x)
{
	const uint k = 1103515245u;

	x = ((x>>8U)^x.yzx)*k;
	x = ((x>>8U)^x.yzx)*k;
	x = ((x>>8U)^x.yzx)*k;

	return x;
}

// Integer Hash - III
// - Inigo Quilez, Integer Hash - III, 2017
//   https://www.shadertoy.com/view/4tXyWN
uint iqint3(uvec2 x)
{
	uvec2 q = 1103515245U * ( (x>>1U) ^ (x.yx   ) );
	uint  n = 1103515245U * ( (q.x  ) ^ (q.y>>3U) );

	return n;
}



uint jkiss32(uvec2 p)
{
	uint x=p.x;//123456789;
	uint y=p.y;//234567891;

	uint z=345678912u,w=456789123u,c=0u;
	int t;
	y ^= (y<<5); y ^= (y>>7); y ^= (y<<22);
	t = int(z+w+c); z = w; c = uint(t < 0); w = uint(t&2147483647);
	x += 1411392427u;
	return x + y + w;
}



// linear congruential generator
uint lcg(uint p)
{
	return p * 1664525u + 1013904223u;
}



// MD5GPU
// https://www.microsoft.com/en-us/research/wp-content/uploads/2007/10/tr-2007-141.pdf
#define md5_A0 0x67452301u
#define md5_B0 0xefcdab89u
#define md5_C0 0x98badcfeu
#define md5_D0 0x10325476u

uint md5_F(uvec3 v) { return (v.x & v.y) | (~v.x & v.z); }
uint md5_G(uvec3 v) { return (v.x & v.z) | (v.y & ~v.z); }
uint md5_H(uvec3 v) { return v.x ^ v.y ^ v.z; }
uint md5_I(uvec3 v) { return v.y ^ (v.x | ~v.z); }

void md5_FF(inout uvec4 v, inout uvec4 rotate, uint x, uint ac)
{
	v.x = v.y + rotl(v.x + md5_F(v.yzw) + x + ac, rotate.x);

	rotate = rotate.yzwx;
	v = v.yzwx;
}

void md5_GG(inout uvec4 v, inout uvec4 rotate, uint x, uint ac)
{
	v.x = v.y + rotl(v.x + md5_G(v.yzw) + x + ac, rotate.x);

	rotate = rotate.yzwx;
	v = v.yzwx;
}

void md5_HH(inout uvec4 v, inout uvec4 rotate, uint x, uint ac)
{
	v.x = v.y + rotl(v.x + md5_H(v.yzw) + x + ac, rotate.x);

	rotate = rotate.yzwx;
	v = v.yzwx;
}

void md5_II(inout uvec4 v, inout uvec4 rotate, uint x, uint ac)
{
	v.x = v.y + rotl(v.x + md5_I(v.yzw) + x + ac, rotate.x);

	rotate = rotate.yzwx;
	v = v.yzwx;
}

uint md5_K(uint i)
{
	return uint(abs(sin(float(i)+1.)) * float(0xffffffffu));
}

uvec4 md5(uvec4 u)
{
	uvec4 digest = uvec4(md5_A0, md5_B0, md5_C0, md5_D0);
	uvec4 r, v = digest;
	uint i = 0u;

	uint M[16];
	M[0] = u.x; M[1] = u.y;	M[2] = u.z;	M[3] = u.w;
	M[4] = 0u; M[5] = 0u; M[6] = 0u; M[7] = 0u; M[8] = 0u;
	M[9] = 0u; M[10] = 0u; M[11] = 0u; M[12] = 0u; M[13] = 0u;
	M[14] = 0u; M[15] = 0u;

	r = uvec4(7, 12, 17, 22);
	md5_FF(v, r, M[0], md5_K(i++));
	md5_FF(v, r, M[1], md5_K(i++));
	md5_FF(v, r, M[2], md5_K(i++));
	md5_FF(v, r, M[3], md5_K(i++));
	md5_FF(v, r, M[4], md5_K(i++));
	md5_FF(v, r, M[5], md5_K(i++));
	md5_FF(v, r, M[6], md5_K(i++));
	md5_FF(v, r, M[7], md5_K(i++));
	md5_FF(v, r, M[8], md5_K(i++));
	md5_FF(v, r, M[9], md5_K(i++));
	md5_FF(v, r, M[10], md5_K(i++));
	md5_FF(v, r, M[11], md5_K(i++));
	md5_FF(v, r, M[12], md5_K(i++));
	md5_FF(v, r, M[13], md5_K(i++));
	md5_FF(v, r, M[14], md5_K(i++));
	md5_FF(v, r, M[15], md5_K(i++));

	r = uvec4(5, 9, 14, 20);
	md5_GG(v, r, M[1], md5_K(i++));
	md5_GG(v, r, M[6], md5_K(i++));
	md5_GG(v, r, M[11], md5_K(i++));
	md5_GG(v, r, M[0], md5_K(i++));
	md5_GG(v, r, M[5], md5_K(i++));
	md5_GG(v, r, M[10], md5_K(i++));
	md5_GG(v, r, M[15], md5_K(i++));
	md5_GG(v, r, M[4], md5_K(i++));
	md5_GG(v, r, M[9], md5_K(i++));
	md5_GG(v, r, M[14], md5_K(i++));
	md5_GG(v, r, M[3], md5_K(i++));
	md5_GG(v, r, M[8], md5_K(i++));
	md5_GG(v, r, M[13], md5_K(i++));
	md5_GG(v, r, M[2], md5_K(i++));
	md5_GG(v, r, M[7], md5_K(i++));
	md5_GG(v, r, M[12], md5_K(i++));

	r = uvec4(4, 11, 16, 23);
	md5_HH(v, r, M[5], md5_K(i++));
	md5_HH(v, r, M[8], md5_K(i++));
	md5_HH(v, r, M[11], md5_K(i++));
	md5_HH(v, r, M[14], md5_K(i++));
	md5_HH(v, r, M[1], md5_K(i++));
	md5_HH(v, r, M[4], md5_K(i++));
	md5_HH(v, r, M[7], md5_K(i++));
	md5_HH(v, r, M[10], md5_K(i++));
	md5_HH(v, r, M[13], md5_K(i++));
	md5_HH(v, r, M[0], md5_K(i++));
	md5_HH(v, r, M[3], md5_K(i++));
	md5_HH(v, r, M[6], md5_K(i++));
	md5_HH(v, r, M[9], md5_K(i++));
	md5_HH(v, r, M[12], md5_K(i++));
	md5_HH(v, r, M[15], md5_K(i++));
	md5_HH(v, r, M[2], md5_K(i++));

	r = uvec4(6, 10, 15, 21);
	md5_II(v, r, M[0], md5_K(i++));
	md5_II(v, r, M[7], md5_K(i++));
	md5_II(v, r, M[14], md5_K(i++));
	md5_II(v, r, M[5], md5_K(i++));
	md5_II(v, r, M[12], md5_K(i++));
	md5_II(v, r, M[3], md5_K(i++));
	md5_II(v, r, M[10], md5_K(i++));
	md5_II(v, r, M[1], md5_K(i++));
	md5_II(v, r, M[8], md5_K(i++));
	md5_II(v, r, M[15], md5_K(i++));
	md5_II(v, r, M[6], md5_K(i++));
	md5_II(v, r, M[13], md5_K(i++));
	md5_II(v, r, M[4], md5_K(i++));
	md5_II(v, r, M[11], md5_K(i++));
	md5_II(v, r, M[2], md5_K(i++));
	md5_II(v, r, M[9], md5_K(i++));

	return digest + v;
}



// Adapted from MurmurHash3_x86_32 from https://github.com/aappleby/smhasher
uint murmur3(uint seed)
{
	uint h = 0u;
	uint k = seed;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	h ^= 4u;

	return fmix(h);
}

// Adapted from MurmurHash3_x86_32 from https://github.com/aappleby/smhasher
uint murmur3(uvec2 seed)
{
	uint h = 0u;
	uint k = seed.x;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	k = seed.y;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	h ^= 8u;

	return fmix(h);
}

// Adapted from MurmurHash3_x86_32 from https://github.com/aappleby/smhasher
uint murmur3(uvec3 seed)
{
	uint h = 0u;
	uint k = seed.x;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	k = seed.y;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	k = seed.z;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	h ^= 12u;

	return fmix(h);
}

// Adapted from MurmurHash3_x86_32 from https://github.com/aappleby/smhasher
uint murmur3(uvec4 seed)
{
	uint h = 0u;
	uint k = seed.x;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	k = seed.y;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	k = seed.z;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	k = seed.w;

	k *= hsh_c1;
	k = rotl(k,15u);
	k *= hsh_c2;

	h ^= k;
	h = rotl(h,13u);
	h = h*5u+0xe6546b64u;

	h ^= 16u;

	return fmix(h);
}

// https://www.pcg-random.org/
uint pcg(uint v)
{
	uint state = v * 747796405u + 2891336453u;
	uint word = ((state >> ((state >> 28u) + 4u)) ^ state) * 277803737u;
	return (word >> 22u) ^ word;
}



uvec2 pcg2d(uvec2 v)
{
	v = v * 1664525u + 1013904223u;

	v.x += v.y * 1664525u;
	v.y += v.x * 1664525u;

	v = v ^ (v>>16u);

	v.x += v.y * 1664525u;
	v.y += v.x * 1664525u;

	v = v ^ (v>>16u);

	return v;
}

// http://www.jcgt.org/published/0009/03/02/
uvec3 pcg3d(uvec3 v) {

	v = v * 1664525u + 1013904223u;

	v.x += v.y*v.z;
	v.y += v.z*v.x;
	v.z += v.x*v.y;

	v ^= v >> 16u;

	v.x += v.y*v.z;
	v.y += v.z*v.x;
	v.z += v.x*v.y;

	return v;
}

// http://www.jcgt.org/published/0009/03/02/
uvec3 pcg3d16(uvec3 v)
{
	v = v * 12829u + 47989u;

	v.x += v.y*v.z;
	v.y += v.z*v.x;
	v.z += v.x*v.y;

	v.x += v.y*v.z;
	v.y += v.z*v.x;
	v.z += v.x*v.y;

	v >>= 16u;

	return v;
}

// http://www.jcgt.org/published/0009/03/02/
uvec4 pcg4d(uvec4 v)
{
	v = v * 1664525u + 1013904223u;

	v.x += v.y*v.w;
	v.y += v.z*v.x;
	v.z += v.x*v.y;
	v.w += v.y*v.z;

	v ^= v >> 16u;

	v.x += v.y*v.w;
	v.y += v.z*v.x;
	v.z += v.x*v.y;
	v.w += v.y*v.z;

	return v;
}



// UE4's PseudoRandom function
// https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Shaders/Private/Random.ush
float pseudo(vec2 v) {
	v = fract(v/128.)*128. + vec2(-64.340622, -72.465622);
	return fract(dot(v.xyx * v.xyy, vec3(20.390625, 60.703125, 2.4281209)));
}



// Numerical Recipies 3rd Edition
uint ranlim32(uint j){
	uint u, v, w1, w2, x, y;

	v = 2244614371U;
	w1 = 521288629U;
	w2 = 362436069U;

	u = j ^ v;

	u = u * 2891336453U + 1640531513U;
	v ^= v >> 13; v ^= v << 17; v ^= v >> 5;
	w1 = 33378u * (w1 & 0xffffu) + (w1 >> 16);
	w2 = 57225u * (w2 & 0xffffu) + (w2 >> 16);

	v = u;

	u = u * 2891336453U + 1640531513U;
	v ^= v >> 13; v ^= v << 17; v ^= v >> 5;
	w1 = 33378u * (w1 & 0xffffu) + (w1 >> 16);
	w2 = 57225u * (w2 & 0xffffu) + (w2 >> 16);

	x = u ^ (u << 9); x ^= x >> 17; x ^= x << 6;
	y = w1 ^ (w1 << 17); y ^= y >> 15; y ^= y << 5;

	return (x + v) ^ (y + w2);
}



// SuperFastHash, adapated from http://www.azillionmonkeys.com/qed/hash.html
uint superfast(uint data)
{
	uint hash = 4u, tmp;

	hash += data & 0xffffu;
	tmp = (((data >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	/* Force "avalanching" of final 127 bits */
	hash ^= hash << 3;
	hash += hash >> 5;
	hash ^= hash << 4;
	hash += hash >> 17;
	hash ^= hash << 25;
	hash += hash >> 6;

	return hash;
}


// SuperFastHash, adapated from http://www.azillionmonkeys.com/qed/hash.html
uint superfast(uvec2 data)
{
	uint hash = 8u, tmp;

	hash += data.x & 0xffffu;
	tmp = (((data.x >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	hash += data.y & 0xffffu;
	tmp = (((data.y >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	/* Force "avalanching" of final 127 bits */
	hash ^= hash << 3;
	hash += hash >> 5;
	hash ^= hash << 4;
	hash += hash >> 17;
	hash ^= hash << 25;
	hash += hash >> 6;

	return hash;
}

// SuperFastHash, adapated from http://www.azillionmonkeys.com/qed/hash.html
uint superfast(uvec3 data)
{
	uint hash = 8u, tmp;

	hash += data.x & 0xffffu;
	tmp = (((data.x >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	hash += data.y & 0xffffu;
	tmp = (((data.y >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	hash += data.z & 0xffffu;
	tmp = (((data.z >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	/* Force "avalanching" of final 127 bits */
	hash ^= hash << 3;
	hash += hash >> 5;
	hash ^= hash << 4;
	hash += hash >> 17;
	hash ^= hash << 25;
	hash += hash >> 6;

	return hash;
}

// SuperFastHash, adapated from http://www.azillionmonkeys.com/qed/hash.html
uint superfast(uvec4 data)
{
	uint hash = 8u, tmp;

	hash += data.x & 0xffffu;
	tmp = (((data.x >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	hash += data.y & 0xffffu;
	tmp = (((data.y >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	hash += data.z & 0xffffu;
	tmp = (((data.z >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	hash += data.w & 0xffffu;
	tmp = (((data.w >> 16) & 0xffffu) << 11) ^ hash;
	hash = (hash << 16) ^ tmp;
	hash += hash >> 11;

	/* Force "avalanching" of final 127 bits */
	hash ^= hash << 3;
	hash += hash >> 5;
	hash ^= hash << 4;
	hash += hash >> 17;
	hash ^= hash << 25;
	hash += hash >> 6;

	return hash;
}



// Tiny Encryption Algorithm
//  - Zafar et al., GPU random numbers via the tiny encryption algorithm, HPG 2010
uvec2 tea(int tea, uvec2 p) {
	uint s = 0u;

	for( int i = 0; i < tea; i++) {
		s += 0x9E3779B9u;
		p.x += (p.y<<4u)^(p.y+s)^(p.y>>5u);
		p.y += (p.x<<4u)^(p.x+s)^(p.x>>5u);
	}
	return p.xy;
}



// common GLSL hash
//  - Rey, On generating random numbers, with help of y= [(a+x)sin(bx)] mod 1,
//    22nd European Meeting of Statisticians and the 7th Vilnius Conference on
//    Probability Theory and Mathematical Statistics, August 1998
/*
uvec2 trig(uvec2 p) {
    return uvec2(float(0xffffff)*fract(43757.5453*sin(dot(vec2(p),vec2(12.9898,78.233)))));
}
*/
float trig(vec2 p)
{
	return fract(43757.5453*sin(dot(p, vec2(12.9898,78.233))));
}



// Wang hash, described on http://burtleburtle.net/bob/hash/integer.html
// original page by Thomas Wang 404
uint wang(uint v)
{
	v = (v ^ 61u) ^ (v >> 16u);
	v *= 9u;
	v ^= v >> 4u;
	v *= 0x27d4eb2du;
	v ^= v >> 15u;
	return v;
}



// 128-bit xorshift
//  - Marsaglia, Xorshift RNGs, Journal of Statistical Software, v8n14, 2003
uint xorshift128(uvec4 v)
{
	v.w ^= v.w << 11u;
	v.w ^= v.w >> 8u;
	v = v.wxyz;
	v.x ^= v.y;
	v.x ^= v.y >> 19u;
	return v.x;
}



// 32-bit xorshift
//  - Marsaglia, Xorshift RNGs, Journal of Statistical Software, v8n14, 2003
uint xorshift32(uint v)
{
	v ^= v << 13u;
	v ^= v >> 17u;
	v ^= v << 5u;
	return v;
}



// xxhash (https://github.com/Cyan4973/xxHash)
//   From https://www.shadertoy.com/view/Xt3cDn
uint xxhash32(uint p)
{
	const uint PRIME32_2 = 2246822519U, PRIME32_3 = 3266489917U;
	const uint PRIME32_4 = 668265263U, PRIME32_5 = 374761393U;
	uint h32 = p + PRIME32_5;
	h32 = PRIME32_4*((h32 << 17) | (h32 >> (32 - 17)));
	h32 = PRIME32_2*(h32^(h32 >> 15));
	h32 = PRIME32_3*(h32^(h32 >> 13));
	return h32^(h32 >> 16);
}

uint xxhash32(uvec2 p)
{
	const uint PRIME32_2 = 2246822519U, PRIME32_3 = 3266489917U;
	const uint PRIME32_4 = 668265263U, PRIME32_5 = 374761393U;
	uint h32 = p.y + PRIME32_5 + p.x*PRIME32_3;
	h32 = PRIME32_4*((h32 << 17) | (h32 >> (32 - 17)));
	h32 = PRIME32_2*(h32^(h32 >> 15));
	h32 = PRIME32_3*(h32^(h32 >> 13));
	return h32^(h32 >> 16);
}

uint xxhash32(uvec3 p)
{
	const uint PRIME32_2 = 2246822519U, PRIME32_3 = 3266489917U;
	const uint PRIME32_4 = 668265263U, PRIME32_5 = 374761393U;
	uint h32 =  p.z + PRIME32_5 + p.x*PRIME32_3;
	h32 = PRIME32_4*((h32 << 17) | (h32 >> (32 - 17)));
	h32 += p.y * PRIME32_3;
	h32 = PRIME32_4*((h32 << 17) | (h32 >> (32 - 17)));
	h32 = PRIME32_2*(h32^(h32 >> 15));
	h32 = PRIME32_3*(h32^(h32 >> 13));
	return h32^(h32 >> 16);
}

uint xxhash32(uvec4 p)
{
	const uint PRIME32_2 = 2246822519U, PRIME32_3 = 3266489917U;
	const uint PRIME32_4 = 668265263U, PRIME32_5 = 374761393U;
	uint h32 =  p.w + PRIME32_5 + p.x*PRIME32_3;
	h32 = PRIME32_4*((h32 << 17) | (h32 >> (32 - 17)));
	h32 += p.y * PRIME32_3;
	h32 = PRIME32_4*((h32 << 17) | (h32 >> (32 - 17)));
	h32 += p.z * PRIME32_3;
	h32 = PRIME32_4*((h32 << 17) | (h32 >> (32 - 17)));
	h32 = PRIME32_2*(h32^(h32 >> 15));
	h32 = PRIME32_3*(h32^(h32 >> 13));
	return h32^(h32 >> 16);
}
