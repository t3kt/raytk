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
    name: sdf
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
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
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 1
    name: contrib_definition_in_2
    returnTypes:
    - float
    - vec4
    summary: Second shading element.
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Color Contribution 1
    name: contrib_definition_in_3
    returnTypes:
    - float
    - vec4
    summary: Third shading element.
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
  - label: Light Color
    name: Createreflightcolor
    summary: 'Create reference to variable: Light Color'
  - label: Light Position
    name: Createreflightpos
    summary: 'Create reference to variable: Light Position'
  - label: Surface Color (r, g, b, is set)
    name: Createrefsurfacecolor
    summary: 'Create reference to variable: Surface Color (r, g, b, is set)'
  - label: Surface UV (u, v, w, is set)
    name: Createrefsurfaceuv
    summary: 'Create reference to variable: Surface UV (u, v, w, is set)'
  - label: Ambient Occlusion
    name: Createrefao
    summary: 'Create reference to variable: Ambient Occlusion'
  - label: 'Shaded Level (0: full shadow, 1: none)'
    name: Createrefshadedlevel
    summary: 'Create reference to variable: Shaded Level (0: full shadow, 1: none)'
  - label: Surface Normal
    name: Createrefnormal
    summary: 'Create reference to variable: Surface Normal'
  - label: Reflection Color
    name: Createrefreflectcolor
    summary: 'Create reference to variable: Reflection Color'
  shortcuts:
  - mm
  summary: A material that is composed of one or more shading elements.

---


A material that is composed of one or more shading elements.

The shading contribution operators are intended to be used with this material,
including `diffuseContrib`, `specularContrib`, and `skyLightContrib`.
However any float or vector field operator can be used as a lighting element as long
as it's set up to use `MaterialContext`.