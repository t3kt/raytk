---
layout: operator
title: chamferBoxSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/chamferBoxSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.chamferBoxSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec3
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
    - vec3
    label: Chamfer Field
    name: chamfer_definition_in
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec3
    label: Rounding Field
    name: rounding_definition_in
    returnTypes:
    - float
  keywords:
  - box
  - chamfer
  - cube
  name: chamferBoxSdf
  opType: raytk.operators.sdf.chamferBoxSdf
  parameters:
  - label: Enable
    name: Enable
  - label: Translate
    name: Translate
  - label: Uniform Scale
    name: Uniformscale
  - label: Chamfer
    name: Chamfer
  - label: Scale
    name: Scale
  - label: Round
    name: Round

---
