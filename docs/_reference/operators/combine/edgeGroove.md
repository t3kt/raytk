---
layout: operator
title: edgeGroove
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgeGroove
redirect_from:
  - /reference/opType/raytk.operators.combine.edgeGroove/
op:
  category: combine
  inputs:
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
    label: definition_in_1
    name: definition_in_1
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
    label: definition_in_2
    name: definition_in_2
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius of the blend region at
      different points in space, by *multiplying* the value of the `Radius` parameter.
  name: edgeGroove
  opType: raytk.operators.combine.edgeGroove
  parameters:
  - label: Enable
    name: Enable
  - label: Function
    menuOptions:
    - label: Groove
      name: groove
    - label: Tongue
      name: tongue
    name: Function
  - label: Swap Inputs
    name: Swapinputs
  - label: Depth
    name: Depth
    summary: The depth/height of the bar/groove.
  - label: Radius
    name: Radius
    summary: The width of the bar/groove.
  status: deprecated
  summary: Creates a raised bar or indented groove where the second input intersects
    with the first.

---


Creates a raised bar or indented groove where the second input intersects with the first.