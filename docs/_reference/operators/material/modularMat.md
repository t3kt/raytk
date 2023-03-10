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
    label: SDF
    name: sdf
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 1
    name: shading1
    returnTypes:
    - float
    - vec4
    summary: First shading element.
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 2
    name: shading2
    returnTypes:
    - float
    - vec4
    summary: Second shading element.
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 3
    name: shading3
    returnTypes:
    - float
    - vec4
    summary: Third shading element.
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 4
    name: shading4
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 5
    name: shading5
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 6
    name: shading6
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 7
    name: shading7
    returnTypes:
    - float
    - vec4
  name: modularMat
  opType: raytk.operators.material.modularMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
  - label: Use Light Color
    name: Uselightcolor
    summary: Whether to apply the light color to the base color. This does not affect
      whether the shading elements use the light color.
  - label: Use Local Position
    name: Uselocalpos
  - label: Enable Ambient Occlusion
    name: Enableao
  - label: Enable Reflection
    name: Enablereflection
  shortcuts:
  - mm
  summary: A material that is composed of one or more shading elements.
  variables:
  - label: lightcolor
    name: lightcolor
  - label: lightpos
    name: lightpos
  - label: surfacecolor
    name: surfacecolor
  - label: surfaceuv
    name: surfaceuv
  - label: ao
    name: ao
  - label: shadedlevel
    name: shadedlevel
  - label: normal
    name: normal
  - label: reflectcolor
    name: reflectcolor

---


A material that is composed of one or more shading elements.

The shading contribution operators are intended to be used with this material,
including `diffuseContrib`, `specularContrib`, and `skyLightContrib`.
However any float or vector field operator can be used as a lighting element as long
as it's set up to use `MaterialContext`.