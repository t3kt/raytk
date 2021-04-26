---
layout: operator
title: sphereSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/sphereSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.sphereSdf/
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
    label: Radius Field
    name: radius_definition_in
    returnTypes:
    - float
  name: sphereSdf
  opType: raytk.operators.sdf.sphereSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Moves the center of the sphere.
  - label: Radius
    name: Radius
    summary: The radius of the sphere.
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
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
  summary: SDF in 3D space for a uniform sphere.

---


SDF in 3D space for a uniform sphere.