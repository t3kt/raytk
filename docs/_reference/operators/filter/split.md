---
layout: operator
title: split
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/split
redirect_from:
  - /reference/opType/raytk.operators.filter.split/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp1
    - offsetField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Rotate Field
    name: rotateAxisField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - inputOp1
    - offsetField
    - thicknessField
  keywords:
  - separate
  - slice
  name: split
  opType: raytk.operators.filter.split
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
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: The along which to split.
  - label: Rotate Axis
    name: Rotateaxis
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the center position of the split along the axis.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the split.
  - label: Enable Smoothing
    name: Enablesmoothing
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to smooth the transition on each side of the split.
  - label: Smooth Radius
    name: Smoothradius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The amount of smoothing distance.
  thumb: assets/images/reference/operators/filter/split_thumb.png

---
