---
layout: operator
title: fieldMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/fieldMat
redirect_from:
  - /reference/opType/raytk.operators.material.fieldMat/
op:
  category: material
  detail: Essentially this is a conversion from a field to a material, with no other
    features.
  inputs:
  - contextTypes:
    - none
    - Context
    coordTypes:
    - vec3
    label: SDF Shape
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Field
    name: color_definition_in
    required: true
    returnTypes:
    - float
    - vec4
    summary: Vector field used to provide the color for each surface point.
  name: fieldMat
  opType: raytk.operators.material.fieldMat
  parameters:
  - label: Enable
    name: Enable
  - label: Use Local Position
    name: Uselocalpos
    summary: Whether to use the "local" position relative to the input shape when
      looking up colors using the `Color Field` input. If enabled, the coordinates
      used for the color field will be "before" any downstream transformations are
      applied. When disabled, the final global position where a point ends up in the
      render is used instead.
  - label: Use Light Color
    name: Uselightcolor
  summary: 'A material that uses a vector field input to determine

    the color.'

---


A material that uses a vector field input to determine
the color.

Essentially this is a conversion from a field to a material, with no other features.