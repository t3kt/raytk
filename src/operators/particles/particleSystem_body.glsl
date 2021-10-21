Particle extractParticle(ivec2 dataPos) {
	Particle part = createParticle(
		texelFetch(posIn, dataPos, 0).xyz,
		texelFetch(dirIn, dataPos, 0).xyz
	);
	part.vel = texelFetch(velIn, dataPos, 0).xyz;
	part.angVel = texelFetch(angVelIn, dataPos, 0).xyz;
	setParticleStateVec(part, texelFetch(lifeStateIn, dataPos, 0));
	return part;
}
void writeParticle(ivec2 dataPos, Particle part) {
	imageStore(posOut, dataPos, vec4(part.pos, 0.));
	imageStore(dirOut, dataPos, vec4(part.dir, 0.));
	imageStore(velOut, dataPos, vec4(part.vel, 0.));
	imageStore(angVelOut, dataPos, vec4(part.angVel, 0.));
	imageStore(lifeStateOut, dataPos, getParticleStateVec(part));
}

layout (local_size_x = 8, local_size_y = 8) in;
void main()
{
	ivec2 dataPos = ivec2(gl_GlobalInvocationID.xy);
	Particle part = extractParticle(dataPos);
	ParticleContext ctx = createParticleContext(createDefaultContext(), part, dataPos);
	ctx.particle = part;
	part = thismap(part.pos, ctx);
	writeParticle(dataPos, part);
}
