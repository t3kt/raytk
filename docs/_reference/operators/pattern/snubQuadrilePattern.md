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
    label: Tiling Shift Field
    name: tilingShiftField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - coordField
    - sizeField
  name: snubQuadrilePattern
  opType: raytk.operators.pattern.snubQuadrilePattern
  parameters:
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Tiling Shift
    name: Tilingshift
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 1
    name: Polycolor1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 2
    name: Polycolor2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 3
    name: Polycolor3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 4
    name: Polycolor4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Outline Color
    name: Outlinecolor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Dual Outline Color
    name: Dualoutlinecolor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Outline
    name: Enableoutline
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Outline Thickness
    name: Outlinethickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Outline Blending
    name: Outlineblending
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Dual Outline
    name: Enabledualoutline
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Dual Outline Thickness
    name: Dualoutlinethickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Dual Outline Blending
    name: Dualoutlineblending
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/pattern/snubQuadrilePattern_thumb.png

---
