// raytkParticles.glsl

struct Particle {
	vec3 pos;
	vec3 dir;
	vec3 vel;
	vec3 angVel;
	vec3 accel;
	vec3 angAccel;
	float age;
	float life;
	int state;
};

const int PARTICLE_STATE_DEAD = 0;
const int PARTICLE_STATE_ALIVE = 1;
const float LIFE_INFINITE = -1.0;

Particle createParticle(vec3 p, vec3 d) {
	return Particle(
		p, d, vec3(0.), vec3(0.), vec3(0.), vec3(0.), 0., 0., PARTICLE_STATE_DEAD
	);
}
Particle createParticle() { return createParticle(vec3(0.), vec3(0.)); }

void initDefVal(out Particle val) {
	val = createParticle(vec3(0.), vec3(0.));
}

struct ParticleContext {
	Context context;
	Particle initParticle;
};

ParticleContext createParticleContext(Context ctx) {
	return ParticleContext(ctx, createParticle());
}
