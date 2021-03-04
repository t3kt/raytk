---
layout: operator
title: slice
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/slice
redirect_from:
  - /reference/opType/raytk.operators.filter.slice/
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
  name: slice
  opType: raytk.operators.filter.slice
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
    summary: The axis along which to take the slice.
  - label: Offset
    name: Offset
    summary: Shifts the center position of the slice along the axis.
  - label: Thickness
    name: Thickness
    summary: Thickness of the slice.
  - label: Enable Smoothing
    name: Enablesmoothing
    summary: Whether to smooth the transition on each side of the slice down to a
      size of zero.
  - label: Smooth Radius
    name: Smoothradius
    summary: The amount of smoothing distance.
  - label: Enable Mirror
    name: Enablemirror
    summary: When enabled, a second slice is added, mirrored across the origin along
      the axis.
  summary: Removes all of an SDF except for a slice in space.

---


Removes all of an SDF except for a slice in space.