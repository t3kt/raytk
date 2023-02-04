---
layout: operator
title: jointSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/jointSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.jointSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Length Field
    name: lengthField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Angle Field
    name: angleField
    returnTypes:
    - float
  name: jointSdf
  opType: raytk.operators.sdf.jointSdf
  parameters:
  - label: Shape
    menuOptions:
    - label: Square
      name: square
    - label: Round
      name: round
    name: Shape
  - label: Direction
    menuOptions:
    - label: Along X Toward Y
      name: xy
    - label: Along X Toward Z
      name: xz
    - label: Along Y Toward X
      name: yx
    - label: Along Y Toward Z
      name: yz
    - label: Along Z Toward X
      name: zx
    - label: Along Z Toward Y
      name: zy
    name: Direction
  - label: Length
    name: Length
  - label: Thickness
    name: Thickness
  - label: Angle
    name: Angle
  status: beta
  thumb: assets/images/reference/operators/sdf/jointSdf_thumb.png

---
