---
layout: operator
title: sdfField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/sdfField
redirect_from:
  - /reference/opType/raytk.operators.field.sdfField/
op:
  category: field
  inputs:
  - contextTypes:
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
    - vec4
    - Sdf
    - Ray
    - Light
  name: sdfField
  opType: raytk.operators.field.sdfField
  parameters:
  - label: Field Type
    menuOptions:
    - label: Distance
      name: dist
    - label: Inside
      name: inside
    - label: Outside
      name: outside
    - label: Surface
      name: surface
    - label: Surface Inside
      name: surfaceinside
    - label: Surface Outside
      name: surfaceoutside
    name: Fieldtype
  - label: Offset
    name: Offset
  - label: Thickness
    name: Thickness
  - label: Blending
    name: Blending

---
