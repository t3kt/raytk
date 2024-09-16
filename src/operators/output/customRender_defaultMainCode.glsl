void customMain(CustomRenderInputs inputs, Context ctx) {
	ivec3 pixelPos = inputs.pixelPos;
	vec2 uv = inputs.uvPos.xy;

	// "position" is uv scaled to [-1, 1]
	vec2 p = uv * vec2(2.) - vec2(1.);
	
	// This is how you would get the value of a float parameter named `Stuff` from the docked "params" COMP:
	// float s = THIS_Stuff;
	// This gets a 3-part vector parameter named `Color`:
	// vec3 c = THIS_Color;
	// Or you could do this to just get the second part:
	// float g = THIS_Colorg;

	// Use an input operator named `valueField` to get a float value based on the position.
	// In this example, your custom render config should have an input with the name `valueField`.
	// Note the prefix `inputOp_` added to the function name.
	// When calling operator functions, in most cases, just pass `ctx` as the second argument.
	// The first argument is some sort of position value.
	// This needs to be of the coordinate type that the input operator expects. (e.g. vec2 for 2D inputs)
	// This function's return value will have the type that the input operator outputs.
	//float value1 = inputOp_valueField(p, ctx);

	// In this case we're using a vector input operator named `someVectorField`.
	// This operator produces a vector value. These are always vec4 (not vec2 or vec3).
	// The "position" that we pass to this operator doesn't have to actually be a coordinate and doesn't have to match
	// the coordinate types used by other input operators. In this case, this operator expects 3D coordinates.
	//vec4 value2 = inputOp_someVectorField(vec3(p.x, value1, sin(p.y)), ctx);

	// The ultimate goal of a renderer is to produce at least one image buffer output, possibly multiple.

	// In this example there's an output buffer named `color`.
	// To output a color to that buffer, assign a vec4 to the `colorOut` variable.
	// This variable is defined elsewhere, don't redefine it like `vec4 colorOut;`.
	// It is generally good practice to use the `TDOutputSwizzle` function to ensure that the output is in the correct
	// format for certain GPUs / OSes
	//colorOut = TDOutputSwizzle(value2);

	// If you have another output buffer named `whatever`, you can output to it like this:
	// The output must be a vec4, even if you only care about one channel of that.
	//whateverOut = TDOutputSwizzle(vec4(value1, 0, 0, 1));
}
