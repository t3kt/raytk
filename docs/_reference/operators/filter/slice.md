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
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp1
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp1
    - offsetField
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
    readOnlyHandling: constant
    regularHandling: runtime
    summary: The axis along which to take the slice.
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Shifts the center position of the slice along the axis.
  - label: Thickness
    name: Thickness
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Thickness of the slice.
  - label: Enable Smoothing
    name: Enablesmoothing
    readOnlyHandling: constant
    regularHandling: runtime
    summary: Whether to smooth the transition on each side of the slice down to a
      size of zero.
  - label: Smooth Radius
    name: Smoothradius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The amount of smoothing distance.
  - label: Enable Mirror
    name: Enablemirror
    readOnlyHandling: constant
    regularHandling: runtime
    summary: When enabled, a second slice is added, mirrored across the origin along
      the axis.
  - label: Operation
    menuOptions:
    - label: Intersect
      name: intersect
    - label: Difference
      name: diff
    name: Operation
    readOnlyHandling: constant
    regularHandling: constant
  summary: Removes all of an SDF except for a slice in space.

---


Removes all of an SDF except for a slice in space.