---
layout: operator
title: knife
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/knife
redirect_from:
  - /reference/opType/raytk.operators.filter.knife/
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
  name: knife
  opType: raytk.operators.filter.knife
  parameters:
  - label: Enable
    name: Enable
  - label: Keep Side
    menuOptions:
    - label: Above Plane
      name: above
    - label: Below Plane
      name: below
    name: Side
    summary: Which side of the cut to keep.
  - label: Offset
    name: Offset
    summary: Shifts the cut plane along the axis that it faces.
  - label: Rotate Plane
    name: Rotateplane
    summary: Rotate the cut plane in XYZ. When in 2D, only the Z rotation is used.
  summary: Cuts off an SDF along a plane.

---


Cuts off an SDF along a plane.