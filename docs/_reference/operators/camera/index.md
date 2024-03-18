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
  - name: cameraRemap
    status: beta
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
  - name: linkedCamera
  - name: lookAtCamera
    shortcuts:
    - lac
  - name: orthoCamera
    status: beta
  - name: splitCamera
  summary: 'Operators that are used in raymarching to determine which

    direction rays should travel, effectively behaving as cameras.'

---

# Camera Operators

Operators that are used in raymarching to determine which
direction rays should travel, effectively behaving as cameras.

These operators are generally specialized for use in the raymarching
`CameraContext`, and may not support being fed through filters
or other OPs.
