---
layout: operator
title: prismSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/prismSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.prismSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: Height field
    name: height_field_definition_in
    returnTypes:
    - float
    summary: Float value field that controls the height of the prism.
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: Radius field
    name: radius_field_definition_in
    returnTypes:
    - float
    summary: Float value field that controls the radius of the prism.
  name: prismSdf
  opType: raytk.operators.sdf.prismSdf
  parameters:
  - label: Prism Type
    menuOptions:
    - label: Triangle
      name: tri
    - label: Square
      name: square
    - label: Hexagon
      name: hex
    - label: Octogon
      name: octogon
    name: Prismtype
    summary: The number of sides of the prism.
  - label: Translate
    name: Translate
    summary: Moves the center of the prism.
  - label: Radius
    name: Radius
    summary: The radius of the prism. If the radius field input is connected, this
      is not used.
  - label: Height
    name: Height
    summary: The height / length of the prism. If the height field input, this is
      not used.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  summary: A prism shape, like a cylinder but with flat sides, along the z axis.

---

# prismSdf

Category: sdf



A prism shape, like a cylinder but with flat sides, along the z axis.