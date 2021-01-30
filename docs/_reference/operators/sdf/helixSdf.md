---
layout: operator
title: helixSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/helixSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.helixSdf/
op:
  category: sdf
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
    label: Thickness Field
    name: thickness_field_definition_in
    returnTypes:
    - float
    summary: Field used to multiply the `Radius` parameter. If it uses 1D coordinates,
      it is provided the position along the axis. If it uses 3D coordinates, it uses
      the absolute position.
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec3
    label: Radius Field
    name: radius_field_definition_in
    returnTypes:
    - float
    summary: Field used to multiply the `Thickness` parameter. If it uses 1D coordinates,
      it is provided the position along the axis. If it uses 3D coordinates, it uses
      the absolute position.
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Cross Section Shape
    name: cross_section_definition_in
    returnTypes:
    - float
    - Sdf
  name: helixSdf
  opType: raytk.operators.sdf.helixSdf
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Translate
    name: Translate
  - label: Radius
    name: Radius
  - label: Thickness
    name: Thickness
  - label: Spread
    name: Spread
  - label: Dual Spread
    name: Dualspread

---

# helixSdf

Category: sdf

