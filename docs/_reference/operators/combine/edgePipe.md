---
layout: operator
title: edgePipe
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgePipe
redirect_from:
  - /reference/opType/raytk.operators.combine.edgePipe/
op:
  category: combine
  detail: Creates an entirely new SDF result, removing any materials and other settings
    from the inputs.
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Radius Field
    name: radius_definition_in
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius of the blend region at
      different points in space, by *multiplying* the value of the `Radius` parameter.
  name: edgePipe
  opType: raytk.operators.combine.edgePipe
  parameters:
  - label: Enable
    name: Enable
  - label: Radius
    name: Radius
    summary: The width of the pipe.
  summary: Produces a cylindrical pipe along the blend region, replacing the input
    shapes entirely.

---


Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.

Creates an entirely new SDF result, removing any materials and other settings from the inputs.