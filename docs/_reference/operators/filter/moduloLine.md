---
layout: operator
title: moduloLine
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloLine
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloLine/
op:
  category: filter
  detail: Similar to `modulo1D`, this operator repeats space in a row of slices. But
    instead of being on an axis, it uses an arbitrary line defined by two points,
    with a fixed number of evenly spaced slices between them.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
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
    - Volume
    - Ray
    - Light
    supportedVariables:
    - cellcoord
    - normcoord
  name: moduloLine
  opType: raytk.operators.filter.moduloLine
  parameters:
  - label: Enable
    name: Enable
  - label: Point 1
    name: Point1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Divisions
    name: Divisions
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Number of slices.
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    name: Mirrortype
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Whether to flip alternating slices, which can be useful for ensuring
      that shapes line up with their neighbors if they get cut off.
  status: beta
  summary: Repeats space along a line, similar to `modulo1D`.
  variables:
  - label: Cell Index
    name: cellcoord
    summary: Cell index, 0, 1, 2, etc.
  - label: Normalized Cell Index
    name: normcoord
    summary: Cell index, scaled to a 0..1 range.

---


Repeats space along a line, similar to `modulo1D`.

Similar to `modulo1D`, this operator repeats space in a row of slices. But instead of being on an axis, it uses an arbitrary line defined by two points, with a fixed number of evenly spaced slices between them.