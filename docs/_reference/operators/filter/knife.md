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
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - Sdf
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
  keywords:
  - crop
  - knife
  - slice
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
  - label: Direction
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  summary: Cuts off an SDF along a plane.
  thumb: assets/images/reference/operators/filter/knife_thumb.png

---


Cuts off an SDF along a plane.