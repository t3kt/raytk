---
layout: operator
title: scale
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/scale
redirect_from:
  - /reference/opType/raytk.operators.filter.scale/
op:
  category: filter
  detail: Scaling works for either 3D or 2D inputs.
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
    label: Scale Field
    name: scale_field_definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    summary: If provided, this field is used to modify the scaling at different points
      in space. If the field returns float values, the value of all the `Scale` parameters
      are multiplied by that value. If it returns vec4 values, each part of the `Scale`
      parameter is multiplied by the corresponding value in the vec4.
  name: scale
  opType: raytk.operators.filter.scale
  parameters:
  - label: Enable
    name: Enable
  - label: Scale
    name: Scale
    summary: Scale to apply to each axis. If input is 2D only X and Y are used.
  - label: Scale Type
    menuOptions:
    - label: Separate XYZ
      name: separate
    - label: Uniform
      name: uniform
    name: Scaletype
  - label: Uniform Scale
    name: Uniformscale
  summary: Scales space.

---


Scales space.

Scaling works for either 3D or 2D inputs.