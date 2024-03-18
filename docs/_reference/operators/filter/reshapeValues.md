---
layout: operator
title: reshapeValues
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/reshapeValues
redirect_from:
  - /reference/opType/raytk.operators.filter.reshapeValues/
op:
  category: filter
  detail: 'If the source field produces float values, the function is just applied
    to those values, returning whatever type the function returns.

    If the source field produces vector values, the function is applied individually
    to each channel in the produced values.

    If the source is an SDF, the function is applied to the distance value in the
    SDF result.'
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
    - float
    - vec2
    - vec3
    - vec4
    label: Source
    name: source_definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    summary: The field or SDF whose results will be reshaped.
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
    label: Function
    name: function_definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    summary: The function that is applied to the results of the source field. In cases
      where the source field produces vectors but the function only works of single
      values, the function will be called 4 times. That can end up costly if the function
      is complex, though most function ops are relatively cheap.
  name: reshapeValues
  opType: raytk.operators.filter.reshapeValues
  parameters:
  - label: Enable
    name: Enable
  summary: Reshapes the values produced by a field by applying a function.

---


Reshapes the values produced by a field by applying a function.

If the source field produces float values, the function is just applied to those values, returning whatever type the function returns.
If the source field produces vector values, the function is applied individually to each channel in the produced values.
If the source is an SDF, the function is applied to the distance value in the SDF result.