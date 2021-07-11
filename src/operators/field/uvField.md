Field that produces surface UV coordinates, if available.

This can be used within modular materials for texture lookups.

For surfaces that have assigned UV coordinates, the W part of the produced vector will be 1. For surfaces without UV coordinates, all parts of the vector will be 0.


## Parameters

* `Coordtype`
  * `float`
  * `vec2`
  * `vec3`