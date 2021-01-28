---
layout: operator
title: flip
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/flip
redirect_from:
  - /reference/opType/raytk.operators.filter.flip/
op:
  category: filter
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  name: flip
  opType: raytk.operators.filter.flip
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Offset
    name: Offset
  - label: Shift
    name: Shift
  - label: Merge Type
    menuOptions:
    - label: None
      name: none
    - label: Union
      name: union
    - label: Smooth Union
      name: smoothUnion
    name: Mergetype
  - label: Merge Radius
    name: Mergeradius
  - label: Iterate On Sides
    name: Iterateonsides
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help

---

# flip

Category: filter

