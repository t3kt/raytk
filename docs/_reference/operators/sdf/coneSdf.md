---
layout: operator
title: coneSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/coneSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.coneSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: Height Field
    name: height_field_definition_in
    returnTypes:
    - float
    summary: Value field that can be used to vary the height of the cone.
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: Radius Field
    name: radius_field_definition_in
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius (both base and top) of
      the cone.
  name: coneSdf
  opType: raytk.operators.sdf.coneSdf
  parameters:
  - label: Enable
    name: Enable
  - label: Shape
    menuOptions:
    - label: Cone
      name: cone
    - label: Capped Cone
      name: cappedcone
    name: Shape
    summary: Choose between a regular cone and a capped cone without a tip.
  - label: Translate
    name: Translate
    summary: Move the center of the shape.
  - label: Height
    name: Height
    summary: The height of the cone.
  - label: Radius
    name: Radius
    summary: The radius of the base of the cone.
  - label: Radius 2
    name: Radius2
    summary: The radius of the top of the cone, if using a capped cone.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  summary: Defines a cone or capped cone shape.

---

# coneSdf

Category: sdf



Defines a cone or capped cone shape.