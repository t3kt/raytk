---
layout: operator
title: modularMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/modularMat
redirect_from:
  - /reference/opType/raytk.operators.material.modularMat/
op:
  category: material
  detail: 'The shading contribution operators are intended to be used with this material,

    including `diffuseContrib`, `specularContrib`, and `skyLightContrib`.

    However any float or vector field operator can be used as a lighting element as
    long

    as it''s set up to use `MaterialContext`.'
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 1
    name: contrib_definition_in_1
    returnTypes:
    - float
    - vec4
    summary: First shading element.
  - contextTypes:
    - Context
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 1
    name: contrib_definition_in_2
    returnTypes:
    - float
    - vec4
    summary: Second shading element.
  name: modularMat
  opType: raytk.operators.material.modularMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
  - label: Use Light Color
    name: Uselightcolor
  - label: Use Local Position
    name: Uselocalpos
  - label: Enable Ambient Occlusion
    name: Enableao
  - label: Enable Shadow
    name: Enableshadow
  status: beta
  summary: A material that is composed of one or more shading elements.

---


A material that is composed of one or more shading elements.

The shading contribution operators are intended to be used with this material,
including `diffuseContrib`, `specularContrib`, and `skyLightContrib`.
However any float or vector field operator can be used as a lighting element as long
as it's set up to use `MaterialContext`.