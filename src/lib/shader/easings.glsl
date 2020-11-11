// https://github.com/glslify/glsl-easings
// http://robertpenner.com/easing/

#ifndef PI
#define PI 3.141592653589793
#endif

#ifndef HALF_PI
#define HALF_PI 1.5707963267948966
#endif

float ease_backInOut(float t) {
	float f = t < 0.5
	? 2.0 * t
	: 1.0 - (2.0 * t - 1.0);

	float g = pow(f, 3.0) - f * sin(f * PI);

	return t < 0.5
	? 0.5 * g
	: 0.5 * (1.0 - g) + 0.5;
}

float ease_backIn(float t) {
	return pow(t, 3.0) - t * sin(t * PI);
}

float ease_backOut(float t) {
	float f = 1.0 - t;
	return 1.0 - (pow(f, 3.0) - f * sin(f * PI));
}

float ease_bounceOut(float t) {
	const float a = 4.0 / 11.0;
	const float b = 8.0 / 11.0;
	const float c = 9.0 / 10.0;

	const float ca = 4356.0 / 361.0;
	const float cb = 35442.0 / 1805.0;
	const float cc = 16061.0 / 1805.0;

	float t2 = t * t;

	return t < a
	? 7.5625 * t2
	: t < b
	? 9.075 * t2 - 9.9 * t + 3.4
	: t < c
	? ca * t2 - cb * t + cc
	: 10.8 * t * t - 20.52 * t + 10.72;
}

float ease_bounceIn(float t) {
	return 1.0 - ease_bounceOut(1.0 - t);
}

float ease_bounceInOut(float t) {
	return t < 0.5
	? 0.5 * (1.0 - ease_bounceOut(1.0 - t * 2.0))
	: 0.5 * ease_bounceOut(t * 2.0 - 1.0) + 0.5;
}

float ease_circularInOut(float t) {
	return t < 0.5
	? 0.5 * (1.0 - sqrt(1.0 - 4.0 * t * t))
	: 0.5 * (sqrt((3.0 - 2.0 * t) * (2.0 * t - 1.0)) + 1.0);
}

float ease_circularIn(float t) {
	return 1.0 - sqrt(1.0 - t * t);
}

float ease_circularOut(float t) {
	return sqrt((2.0 - t) * t);
}

float ease_cubicInOut(float t) {
	return t < 0.5
	? 4.0 * t * t * t
	: 0.5 * pow(2.0 * t - 2.0, 3.0) + 1.0;
}

float ease_cubicIn(float t) {
	return t * t * t;
}

float ease_cubicOut(float t) {
	float f = t - 1.0;
	return f * f * f + 1.0;
}

float ease_elasticInOut(float t) {
	return t < 0.5
	? 0.5 * sin(+13.0 * HALF_PI * 2.0 * t) * pow(2.0, 10.0 * (2.0 * t - 1.0))
	: 0.5 * sin(-13.0 * HALF_PI * ((2.0 * t - 1.0) + 1.0)) * pow(2.0, -10.0 * (2.0 * t - 1.0)) + 1.0;
}

float ease_elasticIn(float t) {
	return sin(13.0 * t * HALF_PI) * pow(2.0, 10.0 * (t - 1.0));
}

float ease_elasticOut(float t) {
	return sin(-13.0 * (t + 1.0) * HALF_PI) * pow(2.0, -10.0 * t) + 1.0;
}
float ease_exponentialInOut(float t) {
	return t == 0.0 || t == 1.0
	? t
	: t < 0.5
	? +0.5 * pow(2.0, (20.0 * t) - 10.0)
	: -0.5 * pow(2.0, 10.0 - (t * 20.0)) + 1.0;
}

float ease_exponentialIn(float t) {
	return t == 0.0 ? t : pow(2.0, 10.0 * (t - 1.0));
}

float ease_exponentialOut(float t) {
	return t == 1.0 ? t : 1.0 - pow(2.0, -10.0 * t);
}

#define ease_linear(t) t

float ease_quadraticInOut(float t) {
	float p = 2.0 * t * t;
	return t < 0.5 ? p : -p + (4.0 * t) - 1.0;
}

float ease_quadraticIn(float t) {
	return t * t;
}

float ease_quadraticOut(float t) {
	return -t * (t - 2.0);
}

float ease_quarticInOut(float t) {
	return t < 0.5
	? +8.0 * pow(t, 4.0)
	: -8.0 * pow(t - 1.0, 4.0) + 1.0;
}

float ease_quarticIn(float t) {
	return pow(t, 4.0);
}

float ease_quarticOut(float t) {
	return pow(t - 1.0, 3.0) * (1.0 - t) + 1.0;
}

float ease_qinticInOut(float t) {
	return t < 0.5
	? +16.0 * pow(t, 5.0)
	: -0.5 * pow(2.0 * t - 2.0, 5.0) + 1.0;
}

float ease_qinticIn(float t) {
	return pow(t, 5.0);
}

float ease_qinticOut(float t) {
	return 1.0 - (pow(t - 1.0, 5.0));
}

float ease_sineInOut(float t) {
	return -0.5 * (cos(PI * t) - 1.0);
}

float ease_sineIn(float t) {
	return sin((t - 1.0) * HALF_PI) + 1.0;
}

float ease_sineOut(float t) {
	return sin(t * HALF_PI);
}
