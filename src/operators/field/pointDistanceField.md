A float field that provides the distance from a specific point in space.

## Parameters

* `Center`: The point from which distance is measured.
* `Coordtype`: The type of coordinates to use.
  * `float`
  * `vec2`
  * `vec3`
* `Contexttype`: The context type, which should usually be `Context`, except when used for materials.
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
  * `RayContext`