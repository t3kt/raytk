---
layout: operator
title: cameraRemap
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/cameraRemap
redirect_from:
  - /reference/opType/raytk.operators.camera.cameraRemap/
op:
  category: camera
  detail: Insert this between a camera and a renderer. Typically the second input
    would be a dataTextureField that uses a TOP with a UV map.
  inputs:
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera In
    name: camera
    required: true
    returnTypes:
    - Ray
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Pixel Map In
    name: pixelMap
    required: true
    returnTypes:
    - vec4
  name: cameraRemap
  opType: raytk.operators.camera.cameraRemap
  parameters:
  - label: Enable
    name: Enable
  status: beta
  summary: Modifies a camera by replacing the pixel UV coordinates that are used when
    calculating ray origins and directions.

---


Modifies a camera by replacing the pixel UV coordinates that are used when calculating ray origins and directions.

Insert this between a camera and a renderer. Typically the second input would be a dataTextureField that uses a TOP with a UV map.