---
layout: operator
title: projectPlane
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/projectPlane
redirect_from:
  - /reference/opType/raytk.operators.convert.projectPlane/
op:
  category: convert
  images:
  - assets/images/reference/operators/convert/projectPlane_plane_xy.png
  - assets/images/reference/operators/convert/projectPlane_plane_xz.png
  - assets/images/reference/operators/convert/projectPlane_plane_yx.png
  - assets/images/reference/operators/convert/projectPlane_plane_yz.png
  - assets/images/reference/operators/convert/projectPlane_plane_zx.png
  - assets/images/reference/operators/convert/projectPlane_plane_zy.png
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: projectPlane
  opType: raytk.operators.convert.projectPlane
  parameters:
  - label: Plane
    menuOptions:
    - label: XY
      name: xy
    - label: YX
      name: yx
    - label: YZ
      name: yz
    - label: ZY
      name: zy
    - label: XZ
      name: xz
    - label: ZX
      name: zx
    name: Plane
  status: beta

---
