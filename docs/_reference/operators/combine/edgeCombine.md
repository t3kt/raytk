---
layout: operator
title: edgeCombine
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgeCombine
redirect_from:
  - /reference/opType/raytk.operators.combine.edgeCombine/
op:
  category: combine
  inputs:
  - contextTypes:
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
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
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
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Depth Field
    name: depth_definition_in
    returnTypes:
    - float
  name: edgeCombine
  opType: raytk.operators.combine.edgeCombine
  parameters:
  - label: Enable
    name: Enable
  - label: Combine
    menuOptions:
    - label: Engrave
      name: engrave
    - label: Groove
      name: groove
    - label: Tongue
      name: tongue
    - label: Pipe
      name: pipe
    name: Combine
  - label: Swap Inputs
    name: Swapinputs
  - label: Radius
    name: Radius
  - label: Depth
    name: Depth

---
