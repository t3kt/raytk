---
layout: operator
title: restrictTypes
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/restrictTypes
redirect_from:
  - /reference/opType/raytk.operators.utility.restrictTypes/
op:
  category: utility
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  name: restrictTypes
  opType: raytk.operators.utility.restrictTypes
  parameters:
  - label: Enable
    name: Enable
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    - label: 4D
      name: vec4
    name: Coordtype
  - label: Context Type
    menuOptions:
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  - label: Return Type
    menuOptions:
    - label: Sdf
      name: Sdf
    - label: vec4
      name: vec4
    - label: float
      name: float
    - label: Ray
      name: Ray
    - label: Light
      name: Light
    name: Returntype
  status: beta

---
