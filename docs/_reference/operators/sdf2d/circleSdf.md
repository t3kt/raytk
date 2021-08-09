---
layout: operator
title: circleSdf
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/circleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.circleSdf/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Radius Field
    name: radius_definition_in
    returnTypes:
    - float
  name: circleSdf
  opType: raytk.operators.sdf2d.circleSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Moves the center of the circle.
  - label: Radius
    name: Radius
    summary: Radius of the circle.
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Cartesian
      name: cartesian
    - label: Polar
      name: polar
    name: Uvmode
  summary: 2D circle SDF.

---


2D circle SDF.