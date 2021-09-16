layout (local_size_x = 8, local_size_y = 8) in;
void main()
{
	vec4 color;
	//color = texelFetch(sTD2DInputs[0], ivec2(gl_GlobalInvocationID.xy), 0);
	color = vec4(1.0);
	imageStore(mTDComputeOutputs[0], ivec2(gl_GlobalInvocationID.xy), TDOutputSwizzle(color));
}
