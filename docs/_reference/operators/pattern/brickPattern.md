---
layout: operator
title: brickPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/brickPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.brickPattern/
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
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
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - thicknessField
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
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - thicknessField
    - shiftField
  name: brickPattern
  opType: raytk.operators.pattern.brickPattern
  parameters:
  - label: Shift
    name: Shift
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Thickness
    name: Thickness
  - label: Blending
    name: Blending
  thumb: assets/images/reference/operators/pattern/brickPattern_thumb.png

---
