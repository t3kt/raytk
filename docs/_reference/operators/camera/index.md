---
layout: operatorCategory
title: Camera Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/camera/
cat:
  detail: 'These operators are generally specialized for use in the raymarching

    `CameraContext`, and may not support being fed through filters

    or other OPs.'
  name: camera
  operators:
  - name: basicCamera
    summary: Standard camera equivalent to a traditional Camera COMP with default
      settings.
  - name: cameraRemap
    status: beta
    summary: Modifies a camera by replacing the pixel UV coordinates that are used
      when calculating ray origins and directions.
  - name: fieldCamera
    status: beta
  - keywords:
    - '360'
    - cubemap
    - dome
    - equiangular
    - equirectangular
    - pinhole
    - stereographic
    name: fisheyeCamera
    summary: A 360 fisheye camera, that shows all directions from a specific point
      in space.
  - name: linkedCamera
    summary: A camera that is linked to an existing TD Camera COMP.
  - name: lookAtCamera
    shortcuts:
    - lac
    summary: A camera that focuses on a specific point in space.
  - name: orthoCamera
    status: beta
    summary: An orthographic (non-perspective) camera, which can be used for flattened
      front/side/etc views.
  - name: splitCamera
    summary: A camera that splits the viewport into several zones, each using a separate
      camera.
  summary: 'Operators that are used in raymarching to determine which

    direction rays should travel, effectively behaving as cameras.'

---

# Camera Operators

Operators that are used in raymarching to determine which
direction rays should travel, effectively behaving as cameras.

These operators are generally specialized for use in the raymarching
`CameraContext`, and may not support being fed through filters
or other OPs.
