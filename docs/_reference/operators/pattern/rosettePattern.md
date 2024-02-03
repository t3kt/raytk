---
layout: operator
title: rosettePattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/rosettePattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.rosettePattern/
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
    label: Glow Field
    name: glowField
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - glowField
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
    label: Spread Field
    name: spreadField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - coordField
    - glowField
    - radiusField
  name: rosettePattern
  opType: raytk.operators.pattern.rosettePattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Glow
    name: Glow
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Spread
    name: Spread
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/pattern/rosettePattern_thumb.png

---
