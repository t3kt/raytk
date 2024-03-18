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
    - float
    - vec2
    - vec3
    - vec4
    label: SDF
    name: sdf
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Contribution 1
    name: shading1
    returnTypes:
    - float
    - vec4
    summary: First shading element.
    supportedVariables:
    - RTK_raytk_operators_material_modularMat_lightcolor
    - RTK_raytk_operators_material_modularMat_lightpos
    - RTK_raytk_operators_material_modularMat_surfacecolor
    - RTK_raytk_operators_material_modularMat_surfaceuv
    - RTK_raytk_operators_material_modularMat_ao
    - RTK_raytk_operators_material_modularMat_shadedlevel
    - RTK_raytk_operators_material_modularMat_normal
    - RTK_raytk_operators_material_modularMat_reflectcolor
    - RTK_raytk_operators_material_modularMat_sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Contribution 2
    name: shading2
    returnTypes:
    - float
    - vec4
    summary: Second shading element.
    supportedVariableInputs:
    - shading1
    supportedVariables:
    - RTK_raytk_operators_material_modularMat_lightcolor
    - RTK_raytk_operators_material_modularMat_lightpos
    - RTK_raytk_operators_material_modularMat_surfacecolor
    - RTK_raytk_operators_material_modularMat_surfaceuv
    - RTK_raytk_operators_material_modularMat_ao
    - RTK_raytk_operators_material_modularMat_shadedlevel
    - RTK_raytk_operators_material_modularMat_normal
    - RTK_raytk_operators_material_modularMat_reflectcolor
    - RTK_raytk_operators_material_modularMat_sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Contribution 3
    name: shading3
    returnTypes:
    - float
    - vec4
    summary: Third shading element.
    supportedVariableInputs:
    - shading[1-2]
    supportedVariables:
    - RTK_raytk_operators_material_modularMat_lightcolor
    - RTK_raytk_operators_material_modularMat_lightpos
    - RTK_raytk_operators_material_modularMat_surfacecolor
    - RTK_raytk_operators_material_modularMat_surfaceuv
    - RTK_raytk_operators_material_modularMat_ao
    - RTK_raytk_operators_material_modularMat_shadedlevel
    - RTK_raytk_operators_material_modularMat_normal
    - RTK_raytk_operators_material_modularMat_reflectcolor
    - RTK_raytk_operators_material_modularMat_sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Contribution 4
    name: shading4
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - shading[1-3]
    supportedVariables:
    - RTK_raytk_operators_material_modularMat_lightcolor
    - RTK_raytk_operators_material_modularMat_lightpos
    - RTK_raytk_operators_material_modularMat_surfacecolor
    - RTK_raytk_operators_material_modularMat_surfaceuv
    - RTK_raytk_operators_material_modularMat_ao
    - RTK_raytk_operators_material_modularMat_shadedlevel
    - RTK_raytk_operators_material_modularMat_normal
    - RTK_raytk_operators_material_modularMat_reflectcolor
    - RTK_raytk_operators_material_modularMat_sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Contribution 5
    name: shading5
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - shading[1-4]
    supportedVariables:
    - RTK_raytk_operators_material_modularMat_lightcolor
    - RTK_raytk_operators_material_modularMat_lightpos
    - RTK_raytk_operators_material_modularMat_surfacecolor
    - RTK_raytk_operators_material_modularMat_surfaceuv
    - RTK_raytk_operators_material_modularMat_ao
    - RTK_raytk_operators_material_modularMat_shadedlevel
    - RTK_raytk_operators_material_modularMat_normal
    - RTK_raytk_operators_material_modularMat_reflectcolor
    - RTK_raytk_operators_material_modularMat_sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Contribution 6
    name: shading6
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - shading[1-5]
    supportedVariables:
    - RTK_raytk_operators_material_modularMat_lightcolor
    - RTK_raytk_operators_material_modularMat_lightpos
    - RTK_raytk_operators_material_modularMat_surfacecolor
    - RTK_raytk_operators_material_modularMat_surfaceuv
    - RTK_raytk_operators_material_modularMat_ao
    - RTK_raytk_operators_material_modularMat_shadedlevel
    - RTK_raytk_operators_material_modularMat_normal
    - RTK_raytk_operators_material_modularMat_reflectcolor
    - RTK_raytk_operators_material_modularMat_sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Contribution 7
    name: shading7
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - shading[1-6]
    supportedVariables:
    - RTK_raytk_operators_material_modularMat_lightcolor
    - RTK_raytk_operators_material_modularMat_lightpos
    - RTK_raytk_operators_material_modularMat_surfacecolor
    - RTK_raytk_operators_material_modularMat_surfaceuv
    - RTK_raytk_operators_material_modularMat_ao
    - RTK_raytk_operators_material_modularMat_shadedlevel
    - RTK_raytk_operators_material_modularMat_normal
    - RTK_raytk_operators_material_modularMat_reflectcolor
    - RTK_raytk_operators_material_modularMat_sdf
  name: modularMat
  opType: raytk.operators.material.modularMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Use Light Color
    name: Uselightcolor
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to apply the light color to the base color. This does not affect
      whether the shading elements use the light color.
  - label: Use Local Position
    name: Uselocalpos
    readOnlyHandling: baked
    regularHandling: baked
  - label: Enable Ambient Occlusion
    name: Enableao
    readOnlyHandling: baked
    regularHandling: baked
  - label: Enable Reflection
    name: Enablereflection
    readOnlyHandling: baked
    regularHandling: baked
  - label: Apply When
    menuOptions:
    - label: Always
      name: always
    - label: Only If Unassigned
      name: missing
    name: Condition
    readOnlyHandling: baked
    regularHandling: runtime
  shortcuts:
  - mm
  summary: A material that is composed of one or more shading elements.
  variables:
  - label: RTK_raytk_operators_material_modularMat_lightcolor
    name: RTK_raytk_operators_material_modularMat_lightcolor
  - label: RTK_raytk_operators_material_modularMat_lightpos
    name: RTK_raytk_operators_material_modularMat_lightpos
  - label: RTK_raytk_operators_material_modularMat_surfacecolor
    name: RTK_raytk_operators_material_modularMat_surfacecolor
  - label: RTK_raytk_operators_material_modularMat_surfaceuv
    name: RTK_raytk_operators_material_modularMat_surfaceuv
  - label: RTK_raytk_operators_material_modularMat_ao
    name: RTK_raytk_operators_material_modularMat_ao
  - label: RTK_raytk_operators_material_modularMat_shadedlevel
    name: RTK_raytk_operators_material_modularMat_shadedlevel
  - label: RTK_raytk_operators_material_modularMat_normal
    name: RTK_raytk_operators_material_modularMat_normal
  - label: RTK_raytk_operators_material_modularMat_reflectcolor
    name: RTK_raytk_operators_material_modularMat_reflectcolor
  - label: RTK_raytk_operators_material_modularMat_sdf
    name: RTK_raytk_operators_material_modularMat_sdf

---


A material that is composed of one or more shading elements.

The shading contribution operators are intended to be used with this material,
including `diffuseContrib`, `specularContrib`, and `skyLightContrib`.
However any float or vector field operator can be used as a lighting element as long
as it's set up to use `MaterialContext`.