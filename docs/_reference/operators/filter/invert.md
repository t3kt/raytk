---
layout: operator
title: invert
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/invert
redirect_from:
  - /reference/opType/raytk.operators.filter.invert/
op:
  category: filter
  detail: If used on a box, this can create an empty room with the shape filling all
    the space outside the room.
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
    - vec4
    - Sdf
  name: invert
  opType: raytk.operators.filter.invert
  parameters:
  - label: Enable
    name: Enable
  summary: Invert an SDF, so that the inside is the outside.

---

# invert

Category: filter



Invert an SDF, so that the inside is the outside.

If used on a box, this can create an empty room with the shape filling all the space outside the room.