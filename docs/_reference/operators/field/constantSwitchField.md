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
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Blend Indices
    name: Blendindices
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Count
    name: Count
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value 1
    name: Value1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value 2
    name: Value2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value 3
    name: Value3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value 4
    name: Value4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value 5
    name: Value5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value 6
    name: Value6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value 7
    name: Value7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value 8
    name: Value8
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Switches or blends between constant values based on an index field.

---


Switches or blends between constant values based on an index field.