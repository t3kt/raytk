---
layout: page
title: Camera Operators
---

Operators that are used in raymarching to determine which
direction rays should travel, effectively behaving as cameras.

These operators are generally specialized for use in the raymarching
`CameraContext`, and may not support being fed through filters
or other OPs.

* [`basicCamera`](basicCamera.md) - 
* [`fisheyeCamera`](fisheyeCamera.md) - A 360 fisheye camera, that shows all directions from a specific point in space.
* [`lookAtCamera`](lookAtCamera.md) - A camera that focuses on a specific point in space.
* [`orthoCamera`](orthoCamera.md) - An orthographic (non-perspective) camera, which can be used for flattened front/side/etc views.
* [`splitCamera`](splitCamera.md) - A camera that splits the viewport into several zones, each using a separate camera.
