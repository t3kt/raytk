Particle extractParticle(ivec2 dataPos) {
	Particle part = createParticle(
		texelFetch(posIn, dataPos, 0).xyz,
		texelFetch(dirIn, dataPos, 0).xyz
	);
	part.vel = texelFetch(velIn, dataPos, 0).xyz;
	part.angVel = texelFetch(angVelIn, dataPos, 0).xyz;
	vec4 state = texelFetch(lifeStateIn, dataPos, 0);
	part.age = state.x;
	part.life = state.y;
	part.state = int(round(state.z));
	part.id = uint(round(state.w));
	return part;
}
void writeParticle(ivec2 dataPos, Particle part) {
	imageStore(posOut, dataPos, vec4(part.pos, 0.));
	imageStore(dirOut, dataPos, vec4(part.dir, 0.));
	imageStore(velOut, dataPos, vec4(part.vel, 0.));
	imageStore(angVelOut, dataPos, vec4(part.angVel, 0.));
	imageStore(lifeStateOut, dataPos, vec4(part.age, part.life, float(part.state), float(part.id)));
}

layout (local_size_x = 8, local_size_y = 8) in;
void main()
{
	ivec2 dataPos = ivec2(gl_GlobalInvocationID.xy);
	Particle part = extractParticle(dataPos);
	ParticleContext ctx = createParticleContext(createDefaultContext(), part);
	ctx.particle = part;
	part = thismap(part.pos, ctx);
	writeParticle(dataPos, part);
}
