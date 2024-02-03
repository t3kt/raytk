---
layout: operator
title: colorSwitchField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/colorSwitchField
redirect_from:
  - /reference/opType/raytk.operators.field.colorSwitchField/
op:
  category: field
  images:
  - assets/images/reference/operators/field/colorSwitchField_clamp_blend_positionField.png
  - assets/images/reference/operators/field/colorSwitchField_clamp_iterationField.png
  - assets/images/reference/operators/field/colorSwitchField_loop_blend_positionField.png
  - assets/images/reference/operators/field/colorSwitchField_loop_iterationField.png
  - assets/images/reference/operators/field/colorSwitchField_zigzag_blend_positionField.png
  - assets/images/reference/operators/field/colorSwitchField_zigzag_iterationField.png
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
    - float
    - vec2
    - vec3
    - vec4
    label: Index Field
    name: indexField
    required: true
    returnTypes:
    - float
  name: colorSwitchField
  opType: raytk.operators.field.colorSwitchField
  parameters:
  - label: Extend
    menuOptions:
    - label: Clamp
      name: clamp
    - label: Loop
      name: loop
    - label: Zig-Zag
      name: zigzag
    name: Extend
  - label: Blend Indices
    name: Blendindices
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Count
    name: Count
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color 1
    name: Color1
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color 2
    name: Color2
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color 3
    name: Color3
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color 4
    name: Color4
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color 5
    name: Color5
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color 6
    name: Color6
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color 7
    name: Color7
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Color 8
    name: Color8
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Index Mode
    menuOptions:
    - label: Index (0 .. N-1)
      name: zeroindex
    - label: Index (1 .. N)
      name: oneindex
    - label: Normalized (0 .. 1)
      name: norm
    name: Indexmode
  summary: Switches or fades between a list of colors based on an index field.

---


Switches or fades between a list of colors based on an index field.