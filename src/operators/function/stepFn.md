A function that changes from zero to one at a cutoff point.

## Parameters

* `Function`
  * `step`: A hard transition at the edge.
  * `smoothstep`: A smooth transition at the end.
* `Edge`: Below this the result will be 0 and above it will produce 1. When using blending, the bottom edge will be `Blend/2` lower than this and the upper edge will be `Blend/2` higher.
* `Blend`: The amount of smoothing to apply on the edge.
* `Contexttype`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`