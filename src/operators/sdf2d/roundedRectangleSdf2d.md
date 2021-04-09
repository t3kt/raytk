SDF for a 2D rectangle with optionally rounded corners.

Each corner has a separate roundness setting, which can be used to make some corners round and others sharp.

See [ShaderToy](https://www.shadertoy.com/view/4llXD7) for example.

## Parameters

* `Scale`: The size of the rectangle along the X and Y axes.
* `Roundness`: The distance of rounding for each of the four corners. When the roundness exceeds half the `Scale`, the rectangle will have discontinuities along the axes.