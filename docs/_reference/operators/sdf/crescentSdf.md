---
layout: operator
title: crescentSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/crescentSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.crescentSdf/
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
  name: crescentSdf
  opType: raytk.operators.sdf.crescentSdf
  parameters:
  - label: Radius
    name: Radius
  - label: Thickness
    name: Thickness
  - label: Rotate
    name: Rotate
  thumb: assets/images/reference/operators/sdf/crescentSdf_thumb.png

---
