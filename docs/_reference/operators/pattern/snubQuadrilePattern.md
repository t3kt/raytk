---
layout: operator
title: snubQuadrilePattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/snubQuadrilePattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.snubQuadrilePattern/
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
    label: Size Field
    name: sizeField
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
    label: Tiling Shift Field
    name: tilingShiftField
    returnTypes:
    - vec4
  name: snubQuadrilePattern
  opType: raytk.operators.pattern.snubQuadrilePattern
  parameters:
  - label: Size
    name: Size
  - label: Tiling Shift
    name: Tilingshift
  - label: Poly Color 1
    name: Polycolor1
  - label: Poly Color 2
    name: Polycolor2
  - label: Poly Color 3
    name: Polycolor3
  - label: Poly Color 4
    name: Polycolor4
  - label: Outline Color
    name: Outlinecolor
  - label: Dual Outline Color
    name: Dualoutlinecolor
  - label: Enable Outline
    name: Enableoutline
  - label: Outline Thickness
    name: Outlinethickness
  - label: Outline Blending
    name: Outlineblending
  - label: Enable Dual Outline
    name: Enabledualoutline
  - label: Dual Outline Thickness
    name: Dualoutlinethickness
  - label: Dual Outline Blending
    name: Dualoutlineblending
  status: beta
  thumb: assets/images/reference/operators/pattern/snubQuadrilePattern_thumb.png

---
