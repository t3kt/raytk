---
layout: operator
title: blobRingPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/blobRingPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.blobRingPattern/
op:
  category: pattern
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
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
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
    - vec3
    label: Phase Field
    name: phaseField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
  name: blobRingPattern
  opType: raytk.operators.pattern.blobRingPattern
  parameters:
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Phase
    name: Phase
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/pattern/blobRingPattern_thumb.png

---
