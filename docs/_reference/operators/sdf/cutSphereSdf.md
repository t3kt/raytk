---
layout: operator
title: cutSphereSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/cutSphereSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.cutSphereSdf/
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
    label: Radius Field
    name: radiusField
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
    label: Offset Field
    name: offsetField
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
    label: Rotate Field
    name: rotateField
    returnTypes:
    - vec4
  name: cutSphereSdf
  opType: raytk.operators.sdf.cutSphereSdf
  parameters:
  - label: Shape
    menuOptions:
    - label: Solid
      name: solid
    - label: Hollow
      name: hollow
    name: Shape
  - label: Radius
    name: Radius
  - label: Cut Offset
    name: Offset
  - label: Thickness
    name: Thickness
  - label: Rotate
    name: Rotate
  status: beta
  thumb: assets/images/reference/operators/sdf/cutSphereSdf_thumb.png

---
