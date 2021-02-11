---
layout: operator
title: colorRampField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/colorRampField
redirect_from:
  - /reference/opType/raytk.operators.field.colorRampField/
op:
  category: field
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
  name: colorRampField
  opType: raytk.operators.field.colorRampField
  parameters:
  - label: Enable
    name: Enable
  - label: Color 1
    name: Color1
  - label: Color 2
    name: Color2
  - label: Alpha 1
    name: Alpha1
  - label: Alpha 2
    name: Alpha2
  - label: Clamp Range
    name: Clamprange
  summary: A vector field that maps an input field to values from a range of colors.

---

# colorRampField

Category: field



A vector field that maps an input field to values from a range of colors.