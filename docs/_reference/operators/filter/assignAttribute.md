---
layout: operator
title: assignAttribute
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/assignAttribute
redirect_from:
  - /reference/opType/raytk.operators.filter.assignAttribute/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Value Field
    name: valueField
    returnTypes:
    - float
    supportedVariableInputs:
    - definition_in
  name: assignAttribute
  opType: raytk.operators.filter.assignAttribute
  parameters:
  - label: Enable
    name: Enable
  - label: Attribute Name
    name: Attributename
  - label: Data Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Datatype
  - label: Value
    name: Value
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  variables:
  - label: Previous Value
    name: previous
  - label: SDF Surface
    name: sdf

---
