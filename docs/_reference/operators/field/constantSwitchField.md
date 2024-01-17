---
layout: operator
title: constantSwitchField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/constantSwitchField
redirect_from:
  - /reference/opType/raytk.operators.field.constantSwitchField/
op:
  category: field
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
  name: constantSwitchField
  opType: raytk.operators.field.constantSwitchField
  parameters:
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
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
  - label: Offset
    name: Offset
  - label: Count
    name: Count
  - label: Value 1
    name: Value1
  - label: Value 2
    name: Value2
  - label: Value 3
    name: Value3
  - label: Value 4
    name: Value4
  - label: Value 5
    name: Value5
  - label: Value 6
    name: Value6
  - label: Value 7
    name: Value7
  - label: Value 8
    name: Value8
  summary: Switches or blends between constant values based on an index field.

---


Switches or blends between constant values based on an index field.