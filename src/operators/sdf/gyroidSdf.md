Gyroid shape, which is an infinitely connected periodic surface.

The Gyroid is constructed using overlapping sine and cosine waves.
See [wikipedia](https://en.wikipedia.org/wiki/Gyroid) for more information.

## Parameters

* `Coordtype`: Switches between 2D and 3D gyroids.
  * `vec2`
  * `vec3`
* `Contexttype`: Advanced parameter that should usually just be set to `Context`.
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
* `Translate`: Moves the shape as a whole.
* `Scale`: Spacing of the shape in each dimension.
* `Enableperiod`: Whether to specify periods for the waves.
* `Period1`: Period of the first waves on each axis.
* `Period2`: Period of the second waves on each axis.
* `Enablephase`: Whether to specify phase shift for the waves.
* `Phase1`: Phase shift of the first waves on each axis.
* `Phase2`: Phase shift of the second waves on each axis.
* `Bias`
* `Thickness`: Expands the surfaces producing thicker shapes.
* `Inspect`