---
layout: operator
title: roundedRectangleSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/roundedRectangleSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.roundedRectangleSdf2d/
op:
  category: sdf2d
  detail: 'Each corner has a separate roundness setting, which can be used to make
    some corners round and others sharp.


    See [ShaderToy](https://www.shadertoy.com/view/4llXD7) for example.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Scale Field
    name: scale_definition_in
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Roundness Field
    name: roundness_definition_in
    returnTypes:
    - float
    - vec4
  name: roundedRectangleSdf2d
  opType: raytk.operators.sdf2d.roundedRectangleSdf2d
  parameters:
  - label: Scale
    name: Scale
    summary: The size of the rectangle along the X and Y axes.
  - label: Roundness
    name: Roundness
    summary: The distance of rounding for each of the four corners. When the roundness
      exceeds half the `Scale`, the rectangle will have discontinuities along the
      axes.
  summary: SDF for a 2D rectangle with optionally rounded corners.

---


SDF for a 2D rectangle with optionally rounded corners.

Each corner has a separate roundness setting, which can be used to make some corners round and others sharp.

See [ShaderToy](https://www.shadertoy.com/view/4llXD7) for example.