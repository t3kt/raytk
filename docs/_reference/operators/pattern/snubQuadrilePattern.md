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
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Tiling Shift
    name: Tilingshift
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Poly Color 1
    name: Polycolor1
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Poly Color 2
    name: Polycolor2
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Poly Color 3
    name: Polycolor3
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Poly Color 4
    name: Polycolor4
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Outline Color
    name: Outlinecolor
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Dual Outline Color
    name: Dualoutlinecolor
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Enable Outline
    name: Enableoutline
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Outline Thickness
    name: Outlinethickness
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Outline Blending
    name: Outlineblending
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Enable Dual Outline
    name: Enabledualoutline
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Dual Outline Thickness
    name: Dualoutlinethickness
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Dual Outline Blending
    name: Dualoutlineblending
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/pattern/snubQuadrilePattern_thumb.png

---
