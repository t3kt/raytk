---
layout: operator
title: extend
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/extend
redirect_from:
  - /reference/opType/raytk.operators.filter.extend/
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
  name: extend
  opType: raytk.operators.filter.extend
  parameters:
  - label: Enable
    name: Enable
  - label: Center
    name: Center
    summary: The center position around which the coordinates are clamped.
  - label: Size
    name: Size
    summary: The size of the region outside which the coordinates are clamped. Within
      this area, the SDF will behave as it normally does.
  summary: Clamps coordinates around an SDF result, which causes their edges to be
    extended infinitely along each axis.

---


Clamps coordinates around an SDF result, which causes their edges to be extended infinitely along each axis.