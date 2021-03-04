Curl noise field.

Note that this operator can be very resource intensive, especially when used in a 3D raymarching scene.
Based on https://github.com/cabbibo/glsl-curl-noise

## Parameters

* `Coordtype`
  * `vec2`
  * `vec3`
* `Contexttype`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
* `Translate`: Coordinate translation.
* `Scale`: Coordinate scale.
* `Amplitude`: Noise value amplitude.
* `Offset`: Noise value offset.