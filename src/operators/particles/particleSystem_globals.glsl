layout(binding = 0) uniform atomic_uint acNextId;
layout(binding = 1) uniform atomic_uint acParticleCount;

uint nextParticleId() {
	return atomicCounterIncrement(acNextId);
}
