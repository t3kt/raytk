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
    - VertexContext
    - PixelContext
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp1
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
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Which side of the cut to keep.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the cut plane along the axis that it faces.
  - label: Rotate Plane
    name: Rotateplane
    readOnlyHandling: baked
    regularHandling: runtime
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
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Enable Smoothing
    name: Enablesmoothing
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to smooth the transition on each side of the slice down to a
      size of zero.
  - label: Smooth Radius
    name: Smoothradius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The amount of smoothing distance.
  summary: Cuts off an SDF along a plane.
  thumb: assets/images/reference/operators/filter/knife_thumb.png

---


Cuts off an SDF along a plane.