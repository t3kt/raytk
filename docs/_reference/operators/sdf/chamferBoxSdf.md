---
layout: operator
title: chamferBoxSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/chamferBoxSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.chamferBoxSdf/
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
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Chamfer Field
    name: chamferField
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
    label: Rounding Field
    name: roundingField
    returnTypes:
    - float
  keywords:
  - box
  - chamfer
  - cube
  name: chamferBoxSdf
  opType: raytk.operators.sdf.chamferBoxSdf
  parameters:
  - label: Translate
    name: Translate
  - label: Scale
    name: Scale
  - label: Uniform Scale
    name: Uniformscale
  - label: Chamfer
    name: Chamfer
  - label: Round
    name: Round
  thumb: assets/images/reference/operators/sdf/chamferBoxSdf_thumb.png

---
