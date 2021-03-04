Renders a 2D image by evaluating the input field for each pixel.

The input field can return either vec4 which is used as RGBA, or a float, which is copied to all 4 channels.
The input field can use either 2D coordinates, or 1D, in which case it only uses the X axis and renders the
same result for each vertical line of pixels.

## Parameters

* `Res`
* `Format`
  * `useinput`
  * `rgba8fixed`
  * `srgba8fixed`
  * `rgba16float`
  * `rgba32float`
  * `_separator_`
  * `rgb10a2fixed`
  * `rgba16fixed`
  * `rgba11float`
  * `rgb16float`
  * `rgb32float`
  * `mono8fixed`
  * `mono16fixed`
  * `mono16float`
  * `mono32float`
  * `rg8fixed`
  * `rg16fixed`
  * `rg16float`
  * `rg32float`
  * `a8fixed`
  * `a16fixed`
  * `a16float`
  * `a32float`
  * `monoalpha8fixed`
  * `monoalpha16fixed`
  * `monoalpha16float`
  * `monoalpha32float`
* `Alignment`: How coordinates are positioned within the render frame.
  * `center`: Places 0,0 in the center of the frame.
  * `bottomleft`: Places 0,0 at the bottom left of the frame.
  * `legacy`: Old default behavior. Note that when used, `Scaling` is ignored. When in doubt, don't use this.
* `Scaling`: How coordinates are scaled within the render frame.
  * `fill`: Stretches coordinates so both axes are -0.5 on one side and 0.5 on the other.
  * `fitinside`: Uses the smaller of the two dimensions of the frame resolution to put -0.5..0.5 on that axis, and whatever the equivalent is on the other axis so that the scaling remains uniform.
  * `fitoutside`: Equivalent to `Fit Inside` but uses the larger of the two dimensions.
* `Uvmap`: UV Map that is used to pick the uV coordinates used for each pixel. If this is provided, the `Alignment` and `Scaling` not used.
* `Timerefop`
* `Shaderbuilderconfig`

## Inputs

* `definition_in`: 