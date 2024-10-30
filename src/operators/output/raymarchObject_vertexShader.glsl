out Vertex {
	vec3 worldSpacePos;
	flat int cameraIndex;
} oVert;

void main() 
{
	vec3 pos = TDPos();
	vec4 worldSpacePos = TDDeform(pos);
	vec3 uvUnwrapCoord = TDInstanceTexCoord(TDUVUnwrapCoord());
	gl_Position = TDWorldToProj(worldSpacePos, uvUnwrapCoord);
	#ifndef TD_PICKING_ACTIVE
	int cameraIndex = TDCameraIndex();
	oVert.cameraIndex = cameraIndex;
	oVert.worldSpacePos = worldSpacePos.xyz;
	#else // TD_PICKING_ACTIVE
	// This will automatically write out the nessessary values
	// for this shader to work with picking.
	// See the documentation if you want to write custom values for picking.
	TDWritePickingValues();
	#endif // TD_PICKING_ACTIVE
}

