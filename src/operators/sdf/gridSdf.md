An infinite grid shape, along two axes.

## Parameters

* `Coordtype`: allows the shape to be used in a 2D context.
  * `vec2`
  * `vec3`
* `Crosssectionshape`: choose the shape of the bars of the grid. Not available in 2D mode.
  * `circle`
  * `diamond`
* `Axis`: choose which axis the grid should face.
  * `x`
  * `y`
  * `z`
* `Spacing`: spacing between the bars of the grid. If this value is very small and the `Thickness` is high enough, the bars can merge into a solid surface. But if it is set to zero the grid will disappear due to a calculation error.
* `Axisoffset`: shifts the grid forwards or backwards along the `Axis` that it is facing. Not available in 2D mode.
* `Offset`: shifts the grid along its plane.
* `Thickness`: the thickness of the bars.
* `Contexttype`: advanced parameter that should usually just be set to `Context`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
* `Inspect`