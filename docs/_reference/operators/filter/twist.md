---
layout: operator
title: twist
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/twist
redirect_from:
  - /reference/opType/raytk.operators.filter.twist/
op:
  category: filter
  inputs:
  - contextTypes:
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
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: twist
  opType: raytk.operators.filter.twist
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
    summary: The axis around which to twist.
  - label: Amount
    name: Amount
    summary: The amount of twisting to apply.
  - label: Shift
    name: Shift
    summary: Offsets the twisting along the axis, effectively rotating everything
      equally around it.
  summary: Twists space around an axis.

---


Twists space around an axis.