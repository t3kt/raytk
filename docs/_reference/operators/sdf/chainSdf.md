---
layout: operator
title: chainSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/chainSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.chainSdf/
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
  name: chainSdf
  opType: raytk.operators.sdf.chainSdf
  parameters:
  - label: Length
    name: Length
  - label: Radius
    name: Radius
  - label: Thickness
    name: Thickness
  thumb: assets/images/reference/operators/sdf/chainSdf_thumb.png

---
