uniform vec4 uDiffuseColor;
uniform vec4 uAmbientColor;
uniform vec3 uSpecularColor;
uniform float uShininess;
uniform vec3 uConstant;
uniform float uShadowStrength;
uniform vec3 uShadowColor;

uniform vec3 uVoxelOrigin;
uniform int uDepth;
uniform vec3 uBoxSize;

uniform ivec2 uSaveRes;

in Vertex
{
	vec4 color;
	vec3 worldSpacePos;
	vec3 worldSpaceNorm;
	flat int cameraIndex;
} iVert;

// Output variable for the color
layout(location = 0) out vec4 oFragColor[TD_NUM_COLOR_BUFFERS];

void main()
{
	// This allows things such as order independent transparency
	// and Dual-Paraboloid rendering to work properly
	TDCheckDiscard();

	vec4 outcol = vec4(0.0, 0.0, 0.0, 0.0);
	vec3 diffuseSum = vec3(0.0, 0.0, 0.0);
	vec3 specularSum = vec3(0.0, 0.0, 0.0);

	vec3 worldSpaceNorm = normalize(iVert.worldSpaceNorm.xyz);
	vec3 normal = normalize(worldSpaceNorm.xyz);

	vec3 viewVec = normalize(uTDMats[iVert.cameraIndex].camInverse[3].xyz - iVert.worldSpacePos.xyz );

	// Flip the normals on backfaces
	// On most GPUs this function just return gl_FrontFacing.
	// However, some Intel GPUs on macOS have broken gl_FrontFacing behavior.
	// When one of those GPUs is detected, an alternative way
	// of determing front-facing is done using the position
	// and normal for this pixel.
	if (!TDFrontFacing(iVert.worldSpacePos.xyz, worldSpaceNorm.xyz))
	{
		normal = -normal;
	}

	// Your shader will be recompiled based on the number
	// of lights in your scene, so this continues to work
	// even if you change your lighting setup after the shader
	// has been exported from the Phong MAT
	for (int i = 0; i < TD_NUM_LIGHTS; i++)
	{
		vec3 diffuseContrib = vec3(0);
		vec3 specularContrib = vec3(0);
		TDLighting(diffuseContrib,
			specularContrib,
			i,
			iVert.worldSpacePos.xyz,
			normal,
			uShadowStrength, uShadowColor,
			viewVec,
			uShininess);
		diffuseSum += diffuseContrib;
		specularSum += specularContrib;
	}

	// Final Diffuse Contribution
	diffuseSum *= uDiffuseColor.rgb * iVert.color.rgb;
	vec3 finalDiffuse = diffuseSum;
	outcol.rgb += finalDiffuse;

	// Final Specular Contribution
	vec3 finalSpecular = vec3(0.0);
	specularSum *= uSpecularColor;
	finalSpecular += specularSum;

	outcol.rgb += finalSpecular;

	// Ambient Light Contribution
	outcol.rgb += vec3(uTDGeneral.ambientColor.rgb * uAmbientColor.rgb * iVert.color.rgb);

	// Constant Light Contribution
	outcol.rgb += uConstant * iVert.color.rgb;


	// Apply fog, this does nothing if fog is disabled
	outcol = TDFog(outcol, iVert.worldSpacePos.xyz, iVert.cameraIndex);

	// Alpha Calculation
	float alpha = uDiffuseColor.a * iVert.color.a ;

	// Dithering, does nothing if dithering is disabled
	outcol = TDDither(outcol);

	outcol.rgb *= alpha;

	// Modern GL removed the implicit alpha test, so we need to apply
	// it manually here. This function does nothing if alpha test is disabled.
	TDAlphaTest(alpha);

	outcol.a = alpha;
	oFragColor[0] = TDOutputSwizzle(outcol);


	// TD_NUM_COLOR_BUFFERS will be set to the number of color buffers
	// active in the render. By default we want to output zero to every
	// buffer except the first one.
	for (int i = 1; i < TD_NUM_COLOR_BUFFERS; i++)
	{
		oFragColor[i] = vec4(0.0);
	}
	
	vec3 worldSpacePos = iVert.worldSpacePos.xyz;
	
	//ivec3 voxelPos = ivec3(uDepth/2+floor((worldSpacePos-uVoxelOrigin)*uVoxelSize));
	ivec3 voxelPos = ivec3(floor((vec3(.5)+(worldSpacePos-uVoxelOrigin)/uBoxSize)*uDepth));
	
	int voxID = voxelPos.x + voxelPos.y*uDepth + voxelPos.z*uDepth*uDepth;
	
	voxID *= 4;
	
	ivec2 outCoord = ivec2(voxID%uSaveRes.x,voxID/uSaveRes.x);
	
	imageAtomicAdd(mTD2DImageOutputs[0], outCoord, 1.);
	voxID += 1;
	outCoord = ivec2(voxID%uSaveRes.x,voxID/uSaveRes.x);
	imageAtomicAdd(mTD2DImageOutputs[0], outCoord, worldSpaceNorm.x);
	voxID += 1;
	outCoord = ivec2(voxID%uSaveRes.x,voxID/uSaveRes.x);
	imageAtomicAdd(mTD2DImageOutputs[0], outCoord, worldSpaceNorm.y);
	voxID += 1;
	outCoord = ivec2(voxID%uSaveRes.x,voxID/uSaveRes.x);
	imageAtomicAdd(mTD2DImageOutputs[0], outCoord, worldSpaceNorm.z);
	
}
