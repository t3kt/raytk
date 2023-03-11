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
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
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
  thumb: assets/images/reference/operators/filter/invert_thumb.png

---


Invert an SDF, so that the inside is the outside.

If used on a box, this can create an empty room with the shape filling all the space outside the room.