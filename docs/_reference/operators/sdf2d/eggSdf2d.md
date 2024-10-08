---
layout: operator
title: eggSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/eggSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.eggSdf2d/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
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
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Rounding Field
    name: roundingField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
  name: eggSdf2d
  opType: raytk.operators.sdf2d.eggSdf2d
  parameters:
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rounding
    name: Rounding
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/eggSdf2d_thumb.png

---
