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
  name: rosettePattern
  opType: raytk.operators.pattern.rosettePattern
  parameters:
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Glow
    name: Glow
  - label: Radius
    name: Radius
  - label: Spread
    name: Spread
  thumb: assets/images/reference/operators/pattern/rosettePattern_thumb.png

---
