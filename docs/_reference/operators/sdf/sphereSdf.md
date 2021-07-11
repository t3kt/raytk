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
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Bounds XYZ
      name: bounds
    - label: Spherical Polar
      name: spherical
    name: Uvmode
  summary: SDF in 3D space for a uniform sphere.

---


SDF in 3D space for a uniform sphere.