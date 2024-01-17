// Example Vertex Shader

void main() 
{
    vec3 pos = TDPos();
    vec4 worldSpacePos = TDDeform(pos);
	gl_Position = TDWorldToProj(worldSpacePos);
#ifndef TD_PICKING_ACTIVE
#else // TD_PICKING_ACTIVE
	// This will automatically write out the nessessary values
	// for this shader to work with picking.
	// See the documentation if you want to write custom values for picking.
	TDWritePickingValues();
#endif // TD_PICKING_ACTIVE
}

