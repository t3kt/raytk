---
layout: operator
title: getAttribute
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/getAttribute
redirect_from:
  - /reference/opType/raytk.operators.utility.getAttribute/
op:
  category: utility
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
    - vec4
    label: SDF
    name: sdf
    returnTypes:
    - Sdf
  name: getAttribute
  opType: raytk.operators.utility.getAttribute
  parameters:
  - label: Attribute Name
    name: Attributename
  - label: Data Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Datatype
  status: beta

---
